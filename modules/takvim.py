import calendar
from application.ultraconsole import UltraConsole as UC

def takvim(**kwargs):
    for i in range(1,13):
        # print(calendar.month(2023,i))
        UC.create_frame("Takvim", calendar.month(2025,i), "info")
    # UC.create_frame("Takvim", type(calendar.month(2023,i)), "info")
    # print(type(calendar.month(2023,i)))
    # input("Devam etmek için bir tuşa basın.")