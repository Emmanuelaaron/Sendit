users = {
    "Emma":{
        "email": "emmanuelisabirye9@gamil.com",
        "password": "isabirye"
    }
}

order = {
    "Emma":{
        "Item": "blanket",
        "pickup location": "Kansaga",
        "destination": "muyenga"

    }
}

class Users:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def signup(self):
        for dict_product in users:
            if dict_product is self.name:
                return "Name already taken"
            else:
                users[self.name] = {"email":self.email, "password": self.password}
                return f"{self.name}, congrats! You have sucessfully signed up"
    



            

