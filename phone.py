from typing import Any

class Phone:
    def __init__(self, brand: str, model: str, price: float, color: str, storage_gb: int, is_in_stock: bool) -> None:
        self.brand: str = brand
        self.model: str = model
        self.price: float = price
        self.color: str = color
        self.storage_gb: int = storage_gb
        self.is_in_stock: bool = is_in_stock

    def get_full_name(self) -> str:
        return f"{self.brand} {self.model}"

    def apply_discount(self, discount_percent: float) -> None:
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount percent must be between 0 and 100.")
        self.price -= self.price * (discount_percent / 100)

    def check_availability(self) -> str:
        return "В наличии" if self.is_in_stock else "Нет в наличии"

    def __str__(self) -> str:
        return (f"Телефон: {self.get_full_name()}\n"
                f"Цвет: {self.color}\n"
                f"Память: {self.storage_gb} ГБ\n"
                f"Цена: {self.price:.2f} руб.\n"
                f"Статус: {self.check_availability()}")

if __name__ == "__main__":
    phone1 = Phone("Apple", "iPhone 14", 89999.0, "черный", 128, True)
    phone2 = Phone("Samsung", "Galaxy S23", 79999.0, "белый", 256, False)
    phone3 = Phone("Xiaomi", "Redmi Note 12", 24999.0, "синий", 128, True)
    phone4 = Phone("Google", "Pixel 8", 69999.0, "зеленый", 128, True)

    phones = [phone1, phone2, phone3, phone4]

    for phone in phones:
        print(phone)
        print("Полное имя:", phone.get_full_name())
        print("Статус:", phone.check_availability())
        phone.apply_discount(10)
        print("Цена после скидки 10%:", f"{phone.price:.2f} руб.")
        print("-")
