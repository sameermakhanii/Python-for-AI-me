def fetch_menu():
    return menu

def validate_order(order_id):
    for order in order:
        if order["order_id"] == order_id:
            return True
    return False


tools = [
    {
        "type": "function",
        "function": {
                "name": "fetch_menu",
                "description": "Get the restaurant menu",
                # no inputs
                "parameters": {"type": "object", "properties": {}},
        },
    }

     {
            "type": "function",
            "function": {
                    "name": "validate_order",
                    "description": "Validate an order",
                    # no inputs
                    "parameters": {"type": "object", "properties": {}},
            },
        }


]