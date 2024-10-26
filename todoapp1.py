import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListView
from PySide6.QtCore import QStringListModel

class TodoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo List App")
        self.setGeometry(100, 100, 400, 300)

        self.tasks = []
        self.task_input = QLineEdit()
        self.task_list = QListView()
        self.task_list.setEditTriggers(QListView.NoEditTriggers)
        
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.task_list)
        layout.addWidget(self.task_input)
        
        layout.addWidget(self.create_button("Add", self.add_task))
        layout.addWidget(self.create_button("Remove", self.remove_task))
        
        self.setCentralWidget(central_widget)
        self.update_task_list()

    def create_button(self, text, callback):
        button = QPushButton(text)
        button.clicked.connect(callback)
        return button

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.tasks.append(task)
            self.task_input.clear()
            self.update_task_list()
