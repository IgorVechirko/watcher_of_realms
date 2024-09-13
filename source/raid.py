from item import Item

class Raid:
    def __init__(self, name, stamina, posible_items):
        self._name = name
        self._stamina = stamina
        self._posible_items = posible_items

        self._visit_times = 0
        self._items_droped = {}

    def add_stat(self, tries, drops):
        self._visit_times += tries

        for item, amount in drops.items():
            if item in list(self._items_droped):
                self._items_droped[item] += amount
            else:
                self._items_droped[item] = amount

    def calc_avg_outcome(tries):
        pass


if __name__ == '__main__':
    raid = Raid("Exp", 36, (
                            Item("hero", "common"),
                            Item("hero", "magic"),
                            Item("hero", "rare"),
                            Item("gold"),
                            Item("exp")))

    raid.add_stat(16, {Item("hero", "rare"): 1, Item("hero", "magic"): 11, Item("hero", "common"): 7, Item("gold"): 12000})