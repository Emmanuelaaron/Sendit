users = []

orders = []


class Users:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def signup(self):
                user = {
                    "username": self.name,
                    "email": self.email,
                    "password": self.password,
                    "user_id": len(users) + 1
                }
                users.append(user)
                return user
        
    @staticmethod
    def all_users():
        return users


class Orders:
    def __init__(self, item, pickup_location, destination):
        self.item = item
        self.pickup_location = pickup_location
        self.destination = destination

    @staticmethod
    def get_all_orders():
        return orders

    def create_parcel_delivery_order(self, user_id):
        for user in users:
            if user["user_id"] is user_id:
                new_order = {
                    "item": self.item,
                    "pickup_location": self.pickup_location,
                    "destination": self.destination,
                    "parcel_id": len(orders) + 1,
                    "status": "pending",
                    "user_id": user_id
                }
                orders.append(new_order)
                return new_order

