class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin= pin

    def checkbalance(self):
        print("Rupees 200000")

    def withdrawal(self):
        print("withdrew")

card= Atm(234098,988456)

card.checkbalance()
card.withdrawal()