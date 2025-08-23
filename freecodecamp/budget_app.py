# Freecodecamp - Scientific Calc. Python - Project No. 3

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    res = "Percentage spent by category\n"

    withdrawals = []
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                total += -item['amount']
        withdrawals.append(total)

    total_spent = sum(withdrawals)
    percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in withdrawals]


    for i in range(100, -1, -10):
        res += str(i).rjust(3) + "|"
        for perc in percentages:
            res += " o " if perc >= i else "   "
        res += " \n"


    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"


    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        res += "     "
        for cat in categories:
            if i < len(cat.name):
                res += cat.name[i] + "  "
            else:
                res += "   "
        if i != max_len - 1:
            res += "\n"

    return res

