class User:
    def __init__(self, name, email, age, gender, phone):
        self.name = name
        self.email = email
        self.age = age
        self.gender = gender
        self.phone = phone
    
    def update(self, field_name, new_value):
        if field_name == "phone":
            return "Cant update phone number"
        else:
            exec("self."+field_name +"="+new_value)
        pass