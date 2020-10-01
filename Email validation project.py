# this program checks the validity of a list of email IDs

def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."
    
    for i in string:
         if i not in valid:
           return True
    return False
    

def is_valid(email):
    if email.count("@")!=1:
        return False
        
    prefix, domain = email.split("@")
        
    if len(prefix) == 0:
        return False
        
    if domain.count(".")!=1:
        return False
        
    domain_name, extension = domain.split(".")
    
    if len(domain_name)== 0  or  len(extension) == 0:
        return False
       
    if has_invalid_characters(prefix):
        return False
        
    if has_invalid_characters(domain):
        return False 
    
    
    return True

emails = [
    "love@yahoo.com",
    "marvelian@gmail.com",
    "gamerno007@gmail",
    "invalid",
    "not an email",
    "invalid@email",
    "!@/",
    "metrorider@@example.com",
    "gta@.com",
    "trustt@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@yahoo!.com"
]   

for i in emails:
    if is_valid(i):
        print(i + " is valid")
    else:
        print(i + " is invalid")
    