users = {
    1:{
        "name": "Emma",
        "email": "emmanuelisabirye9@gamil.com",
        "password": "isabirye",
    }
}



orders = {
    2: {
        1:{
            "item": "blanket",
            "pickup_location": "Kansaga",
            "destination": "muyenga",
            "parcelId": 1 
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
                users[len(users)]["name"] = self.name
                users[len(users)]["email"] = self.email
                users[len(users)]["password"] = self.password
                return "You have sucessfully signed up"


            
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
    def __init__(self, item, pickup_location, destination, parcelId):
        self.item = item
        self.pickup_location = pickup_location
        self.destination = destination
        self.parcelId = parcelId

    def get_all_orders(self):
        return orders

    def get_specific_order(self, parcelId):
        for order_dict in orders:
            for parcel_number in orders[order_dict]:
                if parcel_number is parcelId:
                    return orders[order_dict][parcel_number]
            

