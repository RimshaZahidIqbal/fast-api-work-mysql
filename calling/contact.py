class Contact:

    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
   
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

    def __repr__(self):
        return f"Contact(id={self.id}, name={self.name}, email={self.email}, phone={self.phone})"
