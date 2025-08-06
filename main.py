from PyQt5.QtWidgets import QApplication
from gui import BottleApp
import db
import sys

if __name__ == "__main__":
    db.creat_table()
    app = QApplication(sys.argv)
    window = BottleApp()
    window.show()
    sys.exit(app.exec_())