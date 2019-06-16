import hashlib

def encryption_password(userid, password) -> str:
    target = userid + password
    bin_string = target.encode()
    encryption_string = hashlib.sha256(bin_string).hexdigest() 
    return encryption_string
