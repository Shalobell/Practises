from abc import ABC, abstractmethod

class deposit(ABC):
    def __init__(self, amount: float, months: int, percent: float):
        self.amount = amount
        self.months = months
        self.percent = percent

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getAmount(self) -> float:
        pass

class urgentDeposit(deposit):
    def getName(self) -> str:
        return 'Срочный вклад'

    def getAmount(self) -> float:
        years = self.months / 12
        return self.amount * (1 + self.percent / 100 * years)

class bonusDeposit(deposit):
    def __init__(self, amount: float, months: int, percent: float, minBonusAmount: float,
                 bonusPercent: float = None, bonusFixed: float = None):
        super().__init__(amount, months, percent)
        self.minBonusAmount = minBonusAmount
        self.bonusPercent = bonusPercent
        self.bonusFixed = bonusFixed

    def getName(self) -> str:
        return 'Бонусный вклад'

    def getAmount(self) -> float:
        years = self.months / 12
        baseAmount = self.amount * (1 + self.percent / 100 * years)

        bonus = 0.0

        if self.amount >= self.minBonusAmount:
            if self.bonusPercent is not None:
                bonus = self.amount * (self.bonusPercent / 100)
            elif self.bonusFixed is not None:
                bonus = self.bonusFixed

        return baseAmount + bonus

class capitalizedDeposit(deposit):
    def getName(self) -> str:
        return 'Вклад с капитализацией'

    def getAmount(self) -> float:
        montlyRate = self.percent / 100 / 12
        amount = self.amount

        for i in range(self.months):
            amount += amount * montlyRate
        return amount

class depositSelector:
    def __init__(self, deposits: list[deposit]):
        self.deposits = deposits

    def selectBestDeposit(self) -> deposit:
        bestDeposit = max(self.deposits, key=lambda deposit: deposit.getAmount())

        return bestDeposit

    def showComparsion(self):
        for deposit in self.deposits:
            final = deposit.getAmount()
            print(f"{deposit.getName()}: {final:.2f} RUB")

    def recommend(self):
        best = self.selectBestDeposit()
        print(f"Рекомендуемый вклад: {best.getName()}")
        print(f"Итоговая сумма: {best.getAmount():.2f} RUB")

def main():

    amount = float(input("Сумма вклада: "))
    term = int(input("Срок вклада (месяцев): "))
    rate = float(input("Процентная ставка (%): "))

    deposits = [
        urgentDeposit(amount, term, rate),
        capitalizedDeposit(amount, term, rate),
        bonusDeposit(
            amount=amount,
            months=term,
            percent=rate,
            minBonusAmount=200_000,
            bonusPercent=1.0
        )
    ]

    selector = depositSelector(deposits)
    selector.showComparsion()
    selector.recommend()

if __name__ == "__main__":
    main()