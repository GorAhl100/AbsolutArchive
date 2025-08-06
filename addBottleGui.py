from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox
from bottle import Bottle
from datetime import datetime
from typing import Optional

class AddBottleDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Lägg till flaska")

        self.layout = QFormLayout()

        self.name_input = QLineEdit()
        self.volume_input = QLineEdit()
        self.date_input = QLineEdit()
        self.quality_input = QLineEdit()
        self.price_input = QLineEdit()
        self.notes_input = QLineEdit()

        self.layout.addRow("Namn:", self.name_input)
        self.layout.addRow("Volym:", self.volume_input)
        self.layout.addRow("Inköpsdatum (ÅÅÅÅ-MM-DD):", self.date_input)
        self.layout.addRow("Kvalitet:", self.quality_input)
        self.layout.addRow("Pris:", self.price_input)
        self.layout.addRow("Övrigt:", self.notes_input)

        self.buttons: QDialogButtonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        self.layout.addWidget(self.buttons)
        self.setLayout(self.layout)

    def get_bottle(self) -> Optional[Bottle]:
        try:
            date_str = self.date_input.text().strip()
            date: Optional[datetime.date] = (
                datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
            )
        except ValueError:
            date = None

        try:
            price_str = self.price_input.text().strip()
            price: Optional[float] = float(price_str) if price_str else None
        except ValueError:
            price = None

        return Bottle(
            id=None,
            name=self.name_input.text(),
            volume=self.volume_input.text(),
            date=date,
            quality=self.quality_input.text(),
            price=price,
            notes=self.notes_input.text()
        )
