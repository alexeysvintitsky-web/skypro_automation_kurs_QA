from address import Address
from mailing import Mailing

to_address = Address(
    index="101000",
    city="Москва",
    street="Тверская",
    house="15",
    apartment="47"
)

from_address = Address(
    index="190000",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="25",
    apartment="12"
)

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350.50,
    track="TRK123456789"
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f" {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index},"
      f" {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}."
      f" Стоимость {mailing.cost} рублей.")