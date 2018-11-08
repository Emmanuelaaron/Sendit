users = {
    "Emma":{
        "email": "emmanuelisabirye9@gamil.com",
        "password": "isabirye",
        "userId": 1
    }
}

orders = {
    "Emma": {
        "parcel 1":{
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
            if dict_product is self.name:
                return "Name already taken"
            else:
                users[self.name] = {"email":self.email, "password": self.password, "userId":(len(users)+1)}
                return f"{self.name}, congrats! You have sucessfully signed up"
    
    def login(self, name, password):
        for dict_product in users:
            if dict_product is not name:
                return "Not registered user, please signup" 
            else:
                if dict_product is name and users[dict_product]["password"] is password:
                    return "sucessfully logged in"
                else:
                    return "Incorrect password"

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

        