
posible_items_rarity = {
    "gear": ("rare", "epic", "legend", "mythic", "ancient_legend", "ancient_mythic"),
    "artifact": ("epic", "legend", "mythic", "gleming"),
    "gold": None,
    "exp": None,
    "hero": ("common", "magic", "rare", "epic", "legend"),
    "mythril": None,
    "extract": ("legend", "mythic"),
    "insignia_marksman": ("I", "II", "III"),
    "insignia_mage": ("I", "II", "III"),
    "insignia_endurance": ("I", "II", "III"),
    "insignia_fight": ("I", "II", "III")
}

class Item:
    def __init__(self, item_type, rarity = None):
        if item_type in list(posible_items_rarity):
            if (posible_items_rarity[item_type] is not None) and (rarity is None):
                raise Exception(f"No sush item: {item_type} {rarity}")
            if (rarity is not None) and (posible_items_rarity[item_type] is None):
                raise Exception(f"No sush item: {item_type} {rarity}")
            if (rarity is not None) and (posible_items_rarity[item_type] is not None) and (rarity not in posible_items_rarity[item_type]):
                raise Exception(f"No sush item: {item_type} {rarity}")


if __name__ == '__main__':
    #item = Item("hero")
    #item = Item("gold", "gold")
    #item = Item("hero", "gold")
    item = Item("gold")
    item = Item("hero", "epic")
