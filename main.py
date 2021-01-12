import sys

from PyQt5 import uic
from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication, QMainWindow


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.db')
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('Coffee')
        model.select()

        self.view.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Espresso()
    wnd.show()
    sys.exit(app.exec())