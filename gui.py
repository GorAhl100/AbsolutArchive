from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QDialog
from bottle_manager import BottleManager
from typing import List
from bottle import Bottle
from addBottleGui import AddBottleDialog

class BottleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flaskarkiv")
        self.manager = BottleManager()

        self.layout = QVBoxLayout()
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.btn_list: QPushButton  = QPushButton("Lista flaskor")
        self.btn_list.clicked.connect(self.list_bottles)

        self.btn_add: QPushButton = QPushButton("Lägg till flaska")
        self.btn_add.clicked.connect(self.add_bottle)

        self.layout.addWidget(self.output)
        self.layout.addWidget(self.btn_list)
        self.layout.addWidget(self.btn_add)

        self.setLayout(self.layout)

    def list_bottles(self) -> None:
        try:
            bottles: List[Bottle] = self.manager.get_all_bottles()
            print(f"Antal flaskor: {len(bottles)}")
            if bottles:
                text = "\n\n".join(str(b) for b in bottles)
                self.output.setText(text)
            else:
                self.output.setText("Inga flaskor hittades.")
        except Exception as e:
            print("Fel vid listning:", e)
            self.output.setText(f"Fel: {e}")

    def add_bottle(self) -> None:
        dialog = AddBottleDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            bottle = dialog.get_bottle()
            self.manager.add_bottle(bottle)
            self.output.setText(f"Flaskan '{bottle.name}' har lagts till.")
