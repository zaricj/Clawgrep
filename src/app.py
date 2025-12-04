from pathlib import Path
from typing import List, Optional, Dict, Any, TYPE_CHECKING
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QDialog)

from PySide6.QtGui import QIcon, QCloseEvent, QGuiApplication, QAction
from PySide6.QtCore import (
    Qt,
    QFile,
    QTextStream,
    QIODevice,
    QSettings,
    QThreadPool
)

from gui.ui_files.main_ui.ui_LobsterGeneralLogViewer import Ui_MainWindow
from gui.models.treeViewModel import DirectoryViewer

# ----------------------------
# Constants
# ----------------------------
CURRENT_DIR = Path(__file__).parent
GUI_CONFIG_DIRECTORY: Path = CURRENT_DIR / "config"
GUI_CONFIG_FILE_PATH: Path = GUI_CONFIG_DIRECTORY / "config.json"

# Application versioning and metadata
APP_VERSION: str = "v0.0.1"
APP_NAME: str = "LobsterLogReportViewer"
AUTHOR: str = "Jovan"

# ----------------------------
# Helpers for window state
# ----------------------------
def save_window_state(window: QMainWindow, settings: QSettings):
    settings.setValue("geometry", window.saveGeometry())
    settings.setValue("windowState", window.saveState())


def restore_window_state(window: QMainWindow, settings: QSettings):
    geometry = settings.value("geometry")
    if geometry:
        window.restoreGeometry(geometry)
    state = settings.value("windowState")
    if state:
        window.restoreState(state)

    # Clamp window into current screen space
    screen = QGuiApplication.primaryScreen()
    available = screen.availableGeometry()
    win_geom = window.frameGeometry()

    if not available.contains(win_geom, proper=False):
        window.resize(
            min(win_geom.width(), available.width()),
            min(win_geom.height(), available.height())
        )
        window.move(
            max(available.left(), min(win_geom.left(), available.right() - window.width())),
            max(available.top(), min(win_geom.top(), available.bottom() - window.height()))
        )

# ----------------------------
# Entrypoint
# ----------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dir_viewer = DirectoryViewer(main_window=self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())