users = {
    1:{
        "name": "Emma",
        "email": "emmanuelisabirye9@gamil.com",
        "password": "isabirye",
    }
}



orders = {
    1: {
        1:{
            "item": "blanket",
            "pickup_location": "Kansaga",
            "destination": "muyenga",
            # "parcelId": 1 
        }
    }
}

admins = {
    "Isabirye":{
        "email": "isabirye@gmail.com",
        "password": "emmanuel",
        "userId": 1, 
        "usertype": "admin"
    }
}

class Users:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        # self.userId = userId

    def signup(self):
        for dict_product in users:
            if users[dict_product]["name"] is self.name:
               return "Username already in use! Please use another name"
            else:
                users[dict_product] = {}
                users[dict_product][len(users) + 1] = {}
                users[dict_product][len(users) + 1]["name"] = {}
                users[dict_product][len(users) + 1]["name"] = self.name
                users[dict_product][len(users) + 1]["email"] = self.email
                users[dict_product][len(users) + 1]["password"] = self.password
                return "You have sucessfully signed up."


            
    def login(self, name, password):
        for dict_product in users:
            if users[dict_product]["name"] is not name:
                return "Not registered user, please signup" 
            if users[dict_product]["password"] is not password:
                return "Incorrect password"
            else:
                return "sucessfully logged in"


class Admin(Users):
    def __init__(self, name, email, password, user_type):
        super().__init__(name, email, password, user_type)
        self.user_type = user_type

    def login(self, name, password):
        for dict_product in admins:
            if dict_product is not name:
                return "Not registered user, please signup" 
            else:
                if dict_product is name and users[dict_product]["password"] is password:
                    return "sucessfully logged in"
                else:
                    return "Incorrect password"

class Order:
    def __init__(self, item, pickup_location, destination):
        self.item = item
        self.pickup_location = pickup_location
        self.destination = destination
        # self.parcelId = parcelId

    def get_all_orders(self):
        return orders

    def get_specific_order(self, parcelId):
        for order_dict in orders:
            for parcel_number in orders[order_dict]:
                if parcel_number is parcelId:
                    return orders[order_dict][parcel_number]
                else:
                    return "Invalid parcel id"
            
    def get_all_orders_specific_user(self, userId):
        for user in users:
            if user is userId:
                for order_dict in orders:
                    if user is order_dict:
                        return orders[order_dict]
                    else:
                        return "user has not yet made orders with us"
            else:
                return "Invalid Id user"
            
    def delete_order(self, parcelId):
        for order_dict in orders:
            del orders[order_dict][parcelId]
        return "sucessfully deleted"

    def create_parcel_delivery_order(self, userId):
        for user in users:
            if user is userId:
                for order in orders:
                    orders[order][len(orders) + 1] = {}
                    orders[order][len(orders) + 1]["item"] = self.item
                    orders[order][len(orders) + 1]["pickup_location"] = self.pickup_location
                    orders[order][len(orders) + 1]["destination"] = self.destination
                    return "You've sucessfully created a parcel delivery order"
            else:
                return "user does not exist or check your user id please signup and make delivery orders"

