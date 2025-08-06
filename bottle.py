import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class Bottle:
    id: int
    name: Optional[str]
    volume: Optional[str]
    date: Optional[datetime.date]
    quality: Optional[str]
    price: Optional[float]
    notes: Optional[str]

    @classmethod
    def from_row(cls, row) -> "Bottle":
        return cls(
            id=row[0],
            name=row[1],
            volume=row[2],
            date=datetime.datetime.strptime(row[3], "%Y-%m-%d").date() if isinstance(row[3], str) else row[3],
            quality=row[4],
            price=row[5],
            notes=row[6]
        )

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Namn: {self.name or '-'}\n"
            f"Volym: {self.volume or '-'}\n"
            f"Inköpsdatum: {self.date or '-'}\n"
            f"Kvalitet: {self.quality or '-'}\n"
            f"Pris: {f'{self.price} kr' if self.price is not None else '-'}\n"
            f"Övrigt: {self.notes or '-'}\n"
            f"{'-' * 20}\n"
        )

