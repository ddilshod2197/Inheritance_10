# 10. Telefon tariflari
class PhonePlan:
    def __init__(self, name, minutes, sms, minute_rate, sms_rate):
        self.name = name
        self.minutes = minutes         
        self.sms = sms                  
        self.minute_rate = minute_rate  
        self.sms_rate = sms_rate       

    def total_cost(self):
        """Umumiy xarajat = (daqiqalar × daqiqa narxi) + (SMS × SMS narxi)"""
        return (self.minutes * self.minute_rate) + (self.sms * self.sms_rate)

    def __str__(self):
        cost = self.total_cost()
        return (f"{self.name:12} | {self.minutes:4} daq | {self.sms:4} SMS | "
                f"{self.minute_rate:5.3f}$/daq | {self.sms_rate:5.3f}$/SMS | {cost:6.2f}$")


class StandardPlan(PhonePlan):
    def __str__(self):
        cost = self.total_cost()
        return f"📱 Standart   | {self.minutes:4} daq | {self.sms:4} SMS → {cost:5.2f}$"


class PremiumPlan(PhonePlan):
    def __str__(self):
        cost = self.total_cost()
        return f"🌟 Premium    | {self.minutes:4} daq | {self.sms:4} SMS → {cost:5.2f}$"



def show_phone_plans(plans):
    print("\n" + "═" * 70)
    print("  TELEFON TARIFLARI — OYLIK XARAJAT HISOBI  ".center(70))
    print("═" * 70)
    print("Tarif nomi   | Daqiqalar | SMS lar | Daq.narxi | SMS.narxi | Jami ($)")
    print("─" * 70)

    total_all = 0

    for plan in plans:
        print(plan)
        total_all += plan.total_cost()

    print("─" * 70)
    print(f"UMUMIY XARAJAT (barcha tariflar):           {total_all:8.2f}$")
    print("═" * 70 + "\n")


tariflar = [
    StandardPlan("Standart", 120, 65, 0.10, 0.05),
    PremiumPlan("Premium", 180, 90, 0.08, 0.04),
    StandardPlan("Standart+", 95, 120, 0.09, 0.06),
    PremiumPlan("Premium Family", 250, 150, 0.075, 0.035),
]

show_phone_plans(tariflar)


print("\nSizning misol tariflaringiz:\n")
misol_tariflar = [
    StandardPlan("Standart", 100, 50, 0.1, 0.05),
    PremiumPlan("Premium", 200, 100, 0.08, 0.04),
]

show_phone_plans(misol_tariflar)
