import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QContextMenuEvent
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QListWidget, QPushButton,
    QDialog, QLineEdit, QFormLayout, QMessageBox, QMenu
)

class setStatusDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Изменение статуса")

        statusList = ["Планируется", "В работе", "Завершен"]

        self.statusEdit = QComboBox()
        self.statusEdit.addItems(statusList)

        layout = QFormLayout()
        layout.addRow("Новый статус:", self.statusEdit)

        button_box = QHBoxLayout()
        ok_button = QPushButton("ОК")
        cancel_button = QPushButton("Отмена")
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        button_box.addWidget(ok_button)
        button_box.addWidget(cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(button_box)
        self.setLayout(main_layout)

    def get_data(self):
        return self.statusEdit.currentText()

class projectManagerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер проектов")
        self.resize(500, 400)

        self.projects = {
            "Планируется": [
                ("Планируемый проект 1", "Дедлайн отсутствует"),
                ("Планируемый проект 2", "Дедлайн отсутствует"),
                ("Планируемый проект 3", "20.12.2027")
            ],
            "В работе": [
                ("Проект в работе 1", "19.02.26"),
                ("Проект в работе 2", "20.02.26"),
                ("Проект в работе 3", "21.02.26")
            ],
            "Завершен": [
                ("Завершенный проект 1", "17.02.26"),
                ("Завершенный проект 2", "18.02.26"),
                ("Завершенный проект 3", "19.02.26")
            ]
        }

        #Список проектов
        self.statusCombo = QComboBox()
        self.statusCombo.addItems(self.projects.keys())
        self.statusCombo.currentTextChanged.connect(self.updateProjectList)
        # Список проектов

        #Двойной клик
        self.projectList = QListWidget()
        self.projectList.itemDoubleClicked.connect(self.showProjectInfo)
        # Двойной клик

        #Контекстное меню
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        self.menu = QtWidgets.QMenu(self)
        action = self.menu.addAction('Изменить статус проекта...')
        action.triggered.connect(self.setStatus)
        # Контекстное меню


        layout = QVBoxLayout()
        layout.addWidget(QLabel("Статус:"))
        layout.addWidget(self.statusCombo)

        layout.addWidget(QLabel("Проекты:"))
        layout.addWidget(self.projectList)

        self.setLayout(layout)

        self.updateProjectList()



    def updateProjectList(self):
        status = self.statusCombo.currentText()
        self.projectList.clear()
        for projectName, deadline in self.projects.get(status, []):
            self.projectList.addItem(projectName)


    def showProjectInfo(self, item):
        status = self.statusCombo.currentText()
        title = item.text()
        for t, deadline in self.projects[status]:
            if t == title:
                info = f"Название: {title}\nДедлайн: {deadline}\nСтатус: {status}"
                QMessageBox.information(self, "Информация о проекте", info)
                break

    def setStatus(self):
        prevStatus = self.statusCombo.currentText()
        title = self.getSelectedItem().text()

        dialog = setStatusDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            status = dialog.get_data()
            if not status:
                QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
                return
            if prevStatus == status:
                return
            for t, deadline in self.projects[prevStatus]:
                if t == title:
                    self.projects[status].append((t, deadline))
                    self.projects[prevStatus].remove((t, deadline))

        self.updateProjectList()

    def show_context_menu(self, point):
        self.menu.exec(self.mapToGlobal(point))

    def getSelectedItem(self):
        if not self.projectList.hasFocus(): return
        for selectedItem in self.projectList.selectedItems():
            if not selectedItem: continue
            if selectedItem.isHidden(): continue
            return selectedItem


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = projectManagerApp()
    window.show()
    sys.exit(app.exec_())