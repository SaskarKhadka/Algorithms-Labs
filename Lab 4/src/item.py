class Item:
    def __init__(self, name, weight, value) -> None:
        self.name = name
        self.weight = weight
        self.value = value


def get_items():
    items = []
    items.append(Item("Table", 40, 300))
    items.append(Item("Chair", 25, 130))
    items.append(Item("Door", 30, 200))
    items.append(Item("Basket", 15, 70))

    return items
