from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
)

# Qt design pattern is to subclass the main window
class Window(QMainWindow):
    def __init__(self, width: int, height: int):
        super().__init__()
        icon_path = "E:\\dev\\testing-platform\\examples\\qt\\resources\\pdm-logo.png"
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle("Paratwin")
  
        # Position window at center of screen with desired resolution
        app = QApplication.instance()
        screen = app.primaryScreen()
        screen_geometry = screen.availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        self.setGeometry(screen_width/2 - width/2, screen_height/2 - height/2, width, height)

if __name__ == "__main__":
    
    # Every qt app requires exactly one instance of QApplication
    # The [] are command line args
    app = QApplication([])

    # QWidget is just a container widget 
    main_window = Window(1920, 1080)
    main_window.show()
    
    app.exec()
    print("App closed")
    