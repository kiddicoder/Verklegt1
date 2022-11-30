class NameLengthException(Exception):
    pass

def name_validator(name):
    if len(name) >= 50:
        raise NameLengthException()

def id_validator(id):
    if len(id) > 10 and id.isdigit() == False:
        return ""

def address_validator(address):
    if len(address) >= 25:
        raise NameLengthException()

def phone_validator(phone): #á líka við gsm
    if len(phone) > 7 and phone.isdigit() == False:
        pass 

def email_validator(email):
    pass

def role_validator(role):
    pass
