import json
import time
from abc import ABC, abstractmethod
from enum import Enum
from multiprocessing import Pipe, Process

import comms

class CommsType(Enum):
    TCP_CLIENT = "tcp_client"
    TCP_SERVER = "tcp_server"
    UDP_CLIENT = "udp_client"
    UDP_SERVER = "udp_server"
    SERIAL = "serial"
    CAN = "can"

    @staticmethod
    def get_comms_type(type: str):
        if type == CommsType.TCP_CLIENT.value:
            return CommsType.TCP_CLIENT
        elif type == CommsType.TCP_SERVER.value:
            return CommsType.TCP_SERVER
        elif type == CommsType.UDP_CLIENT.value:
            return CommsType.UDP_CLIENT
        elif type == CommsType.UDP_SERVER.value:
            return CommsType.UDP_SERVER
        elif type == CommsType.SERIAL.value:
            return CommsType.SERIAL
        elif type == CommsType.CAN.value:
            return CommsType.CAN


class Device(ABC):
    def __init__(self, comms_type: CommsType, config: dict):
        self.comms_type = comms_type
        self.comms_object = create_comms_object(self.comms_type, config)
        self.config = config

    @abstractmethod
    def on_setup(self):
        self.comms_object.open()

    @abstractmethod
    def on_update(self, time_delta: float):
        pass

    @abstractmethod
    def on_destroy(self):
        self.comms_object.close()


class StreamingDevice(Device):
    def __init__(self, comms_type: CommsType, config: dict):
        super().__init__(comms_type, config)
        self.data = config['data'].encode()
        self.interval_ms = config['interval_ms']
        self.time_since_last_send: float = 0

    def on_setup(self):
        super().on_setup()

    def on_update(self, time_delta: float):
        self.time_since_last_send += time_delta
        if self.time_since_last_send > self.interval_ms:
            self.time_since_last_send = 0
            self.comms_object.write(self.data)

    def on_destroy(self):
        super().on_destroy()


def create_comms_object(comms_type: CommsType, config: dict) -> comms.Comms:
    if comms_type == CommsType.SERIAL:
        return comms.SerialComms(comms.SerialSettings.create_from_config(config))
    # Add other comms interfaces here once implemented
    else:
        raise NotImplementedError


def create_device_from_config(device_config: dict) -> Device:
    comms_type: CommsType = CommsType.get_comms_type(device_config['comms_type'])
    if device_config['type'] == "streaming":
        return StreamingDevice(comms_type, device_config)


def create_device_and_run(device_configuration: dict, pipe: Pipe):
    """ Creates device based off of configuration, and runs the device """
    current_time_ms: float = time.time() * 1000.0
    device: Device = create_device_from_config(device_configuration)
    device.on_setup()
    while True:
        # Send true to the manager to indicate device is still running,
        # and expect bool back to indicate whether or not the process should
        # continue to run
        pipe.send(True)

        #TODO make the poll timeout configurable
        if pipe.poll(0.1):
            kill_signal: bool = pipe.recv()
            if kill_signal:
                break
        next_time_ms: float = time.time() * 1000.0
        time_delta_ms: float = next_time_ms - current_time_ms
        current_time_ms = next_time_ms
        device.on_update(time_delta_ms)
    device.on_destroy()
    return 0


if __name__ == '__main__':
    send_end, receive_end = Pipe()
    device_config_s = '{"devices": {"device1": {"comms_type": "serial","port": "COM1","baud_rate": 9600,"type": "streaming","data": "Hello","interval_ms": 1000}}}'
    device_config = json.loads(device_config_s)
    device = Process(target=create_device_and_run, args=(device_config['devices']['device1'], receive_end))
    device.start()
    time.sleep(5)
    send_end.send(True)
    device.join()
