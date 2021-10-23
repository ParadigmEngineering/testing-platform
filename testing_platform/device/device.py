import json
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
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


class DeviceType(Enum):
    STREAMING = "streaming"

    @staticmethod
    def get_device_type(type: str):
        if type == DeviceType.STREAMING.value:
            return DeviceType.STREAMING


class Device(ABC):
    def __init__(self, id: str, comms_type: CommsType):
        self.id = id
        self.comms_type = comms_type

    @abstractmethod
    def on_setup(self):
        pass

    @abstractmethod
    def on_update(self, time_delta: float):
        pass

    @abstractmethod
    def on_destroy(self):
        pass


@dataclass
class StreamingDeviceSettings:
    DEVICE_TYPE: DeviceType = DeviceType.STREAMING
    comms_type: CommsType = CommsType.SERIAL
    data: str = ''.encode()
    interval_ms: int = 1000

    @classmethod
    def create_from_config(cls, config: dict):
        return cls(DeviceType.STREAMING,
                   CommsType.get_comms_type(config['comms_type']),
                   config['data'].encode(),
                   config['interval_ms'])


class StreamingDevice(Device):
    def __init__(self, config: dict):
        super().__init__(config['id'], DeviceType.STREAMING)
        self.settings = StreamingDeviceSettings.create_from_config(config)
        self.comms_object = create_comms_object(self.settings.comms_type, config)
        self.time_since_last_send: float = 0

    def on_setup(self):
        """@override"""
        self.comms_object.open()

    def on_update(self, time_delta: float):
        """@override"""
        self.time_since_last_send += time_delta
        if self.time_since_last_send > self.settings.interval_ms:
            self.time_since_last_send = 0
            self.comms_object.write(self.settings.data)

    def on_destroy(self):
        """@override"""
        self.comms_object.close()


def create_comms_object(comms_type: CommsType, config: dict) -> comms.Comms:
    if comms_type == CommsType.SERIAL:
        return comms.SerialComms(comms.SerialSettings.create_from_config(config))
    # Add other comms interfaces here once implemented
    else:
        raise NotImplementedError


def create_device_from_config(device_config: dict) -> Device:
    if device_config['type'] == "streaming":
        return StreamingDevice(device_config)


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
    device_config_s = '{"devices": {"device1": {"id": "device1", "comms_type": "serial","port": "COM7","baud_rate": 9600,"type": "streaming","data": "Hello","interval_ms": 1000}}}'
    device_config = json.loads(device_config_s)
    device = Process(target=create_device_and_run, args=(device_config['devices']['device1'], receive_end))
    device.start()
    time.sleep(5)
    send_end.send(True)
    device.join()
