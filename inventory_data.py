inventory = {}

def add_item(name, cp, sp, qty):
    if name in inventory:
        return False

    inventory[name] = {
        "name": name,
        "cp": cp,
        "sp": sp,
        "qty": qty,
        "total_profit": 0.0
    }
    return True

def upd_item(name, new_cp=None, new_sp=None, new_qty=None):
    if name not in inventory:
        return False

    item = inventory[name]

    if new_cp is not None:
        item["cp"] = new_cp
    if new_sp is not None:
        item["sp"] = new_sp
    if new_qty is not None:
        item["qty"] = new_qty

    return True

def get_item(name):
    if name in inventory:
        return inventory[name]
    else:
        return None

def all_items():
    return inventory
