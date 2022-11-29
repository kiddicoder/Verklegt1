class Player():
   def __init__(self, name="", id=0, address="", email="", gsm=0, phone=0, role="", team=""):
       self.name = name
       self.id = id
       self.address = address
       self.email = email
       self.gsm = gsm
       self.phone = phone
       self.role = role
       self.team = Team().id()
  
   def __str__(self):
       return f"{self.name}, {self.id}, {self.address}, {self.email}, {self.gsm}, {self.phone}, {self.role}, {self.team}"

