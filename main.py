import sys
from PySide6.QtWidgets import QApplication
from task_manager import TaskManager

if __name__ == '__main__':
    app = QApplication(sys.argv)
    taskManager = TaskManager()
    taskManager.show()
    sys.exit(app.exec())
