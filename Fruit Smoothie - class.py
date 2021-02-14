prices = {
    "Strawberries": "$1.50",
    "Banana": "$0.50",
    "Mango": "$2.50",
    "Blueberries": "$1.00",
    "Raspberries": "$1.00",
    "Apple": "$1.75",
    "Pineapple": "$3.50"
}

class Smoothie:
    # Write code here!
    count = 0
    def __init__(self, *arg):
        self.ingredients = arg

    def get_cost(self):
        ls = self.ingredients
        ls1 = ls[0]
        a = 0
        for i in prices:
            for j in ls1:
                if i == j:
                    a += float(prices[i].replace("$",""))
        a = str(a)
        return "$" + a

    def get_price(self):
        ls = self.ingredients
        ls1 = ls[0]
        a = 0
        for i in prices:
            for j in ls1:
                if i == j:
                    a += float(prices[i].replace("$", ""))
        a = a + a * 1.5
        a = str(a)
        return "$" + a

    def get_name(self):
        ls = self.ingredients
        ls1= ls[0]
        ls1.sort()
        if len(ls1)>1:
            return " ".join(ls1) + " Fusion"
        else:
            return " ".join(ls1) + " Smoothie"

s1 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())
