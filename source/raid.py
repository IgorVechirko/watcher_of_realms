from item import Item

class Raid:
    def __init__(self, name, stamina, items_default_drop_rate):
        self._name = name
        self._stamina = stamina
        self._items_default_drop_rate = items_default_drop_rate

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
        if self._visit_times > 10:
            pass
        else:
            pass


if __name__ == '__main__':
    raid = Raid("Exp", 36, {
                            Item("hero", "common"): 0.01,
                            Item("hero", "magic"): 0.01,
                            Item("hero", "rare"): 0.01,
                            Item("gold"): 0.01,
                            Item("exp"): 0.01})

    raid.add_stat(16, {Item("hero", "rare"): 1, Item("hero", "magic"): 11, Item("hero", "common"): 7, Item("gold"): 12000})