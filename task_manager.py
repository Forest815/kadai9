import re
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox, QMessageBox

class TaskManager(QWidget):
    def __init__(self):
        super(TaskManager, self).__init__()
        self.initUI()
    def initUI(self):
        self.tasks = []

        self.layout = QVBoxLayout()

        # Subject ComboBox
        self.subjectComboBox = QComboBox(self)
        self.subjectComboBox.addItems(['微分積分', 'ベクトル', '物理', '化学', '生物', '英語', '英語表現', '社会', '国語', '専門科目', 'その他'])  # ここに教科名を追加

        # Input and Add Task Button
        self.taskInput = QLineEdit(self)
        self.addButton = QPushButton('決定', self)
        self.addButton.clicked.connect(self.addTask)
        
        # Reset Button
        self.resetButton = QPushButton('リセット', self)
        self.resetButton.clicked.connect(self.resetTasks)

        inputLayout = QHBoxLayout()
        inputLayout.addWidget(self.subjectComboBox)
        inputLayout.addWidget(self.taskInput)
        inputLayout.addWidget(self.addButton)
        inputLayout.addWidget(self.resetButton)

        self.layout.addLayout(inputLayout)

        # Task List and Checkboxes
        self.tasksLayout = QVBoxLayout()
        self.layout.addLayout(self.tasksLayout)

        # Completed Tasks Label
        self.completedLabel = QLabel('完了した課題数: 0 個中の 0 個')
        self.layout.addWidget(self.completedLabel)

        self.setLayout(self.layout)
        self.setWindowTitle('課題管理アプリ')
        
        # Set the geometry of the main window
        self.setGeometry(100, 50, 320, 240)  # Updated geometry

    def addTask(self):
        subject_text = self.subjectComboBox.currentText()  # 選択された教科名を取得
        task_text = self.taskInput.text().strip()  # 入力されたテキストから空白を削除
        
        # 入力が空かどうかを正規表現でチェック
        if not re.search(r'\S', task_text):  # \S は非空白文字にマッチする
            QMessageBox.warning(self, '入力エラー', '未入力です')
            return

        full_task_text = f'{subject_text}: {task_text}'  # 教科名とタスク内容を結合
        taskLayout = QHBoxLayout()
        taskLabel = QLabel(full_task_text)
        taskCheckBox = QCheckBox('完了')
        taskCheckBox.toggled.connect(self.updateCompletedTasks)

        taskLayout.addWidget(taskLabel)
        taskLayout.addWidget(taskCheckBox)

        self.tasks.append((taskLabel, taskCheckBox))
        self.tasksLayout.addLayout(taskLayout)

        self.taskInput.clear()
        self.updateCompletedTasks()

    def updateCompletedTasks(self):
        completed_tasks = sum(1 for _, checkBox in self.tasks if checkBox.isChecked())
        total_tasks = len(self.tasks)
        self.completedLabel.setText(f'完了した課題数: {completed_tasks} 個中の {total_tasks} 個')

    def resetTasks(self):
        # Remove all tasks and reset the completed tasks counter
        for taskLabel, checkBox in self.tasks:
            checkBox.setParent(None)
            checkBox.deleteLater()  # GUIからチェックボックスを削除
            taskLabel.setParent(None)
            taskLabel.deleteLater()  # GUIからタスクラベルを削除
        self.tasks.clear()  # タスクリストをクリア
        self.updateCompletedTasks()  # 完了した課題数を更新
