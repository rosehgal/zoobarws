from zoodb import *
from debug import *
from base64 import b64encode

import hashlib
import random
import pbkdf2


def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return cred.token

# def login(username, password):
#     db = person_setup()
#     person = db.query(Person).get(username)
#     if not person:
#         return None
#     if person.password == password:
#         return newtoken(db, person)
#     else:
#         return None

def login(username, password):
    db = cred_setup()
    person = db.query(Cred).get(username)
    
    if not person:
        return None

    salt=person.salt
    password=pbkdf2.PBKDF2(password,salt).hexread(32)

    if person.password == password:
        return newtoken(db, person)
    else:
        return None

# def register(username, password):
#     print "registring "
#     db = person_setup()
#     person = db.query(Person).get(username)
#     if person:
#         return None
#     newperson = Person()
#     newperson.username = username
#     newperson.password = password
#     db.add(newperson)
#     db.commit()
#     return newtoken(db, newperson)

def register(username, password):
    db = person_setup()
    db2 = cred_setup()

    #db3 = bank_setup()
    
    person = db.query(Person).get(username)

    print "check_token 1"
    if person:
        return None

    #generates 64 bit salt
    salt = b64encode(os.urandom(8)).decode('utf-8')
    
    person = Person()
    person_for_cred = Cred()
    #person_for_bank = Bank()
    

    #print "check_token 2"

    #salt=unicode(salt)
    person_for_cred.salt=salt
    
    person.username = username
    person_for_cred.username = username
    #person_for_bank.username = username

    #print "check_token 3"

    password=pbkdf2.PBKDF2(password,salt).hexread(32)
    person_for_cred.password = password

    #print "check_token 4"

    db.add(person)
    db2.add(person_for_cred)
    #db3.add(person_for_bank)

    #print "before db commit"
    db.commit()
    db2.commit()
    #db3.commit()
    #print "after db commit"
    return newtoken(db2, person_for_cred)

# def check_token(username, token):
#     db = person_setup()
#     person = db.query(Person).get(username)
#     if person and person.token == token:
#         return True
#     else:
#         return False

def check_token(username, token):
    db = cred_setup()
    person = db.query(Cred).get(username)
    if person and person.token == token:
        return True
    else:
        return False


def getToken(username):
    credDb=cred_setup()
    user = credDb.query(Cred).get(username)
    if not user:
        raise ValueError("Invalid user")
    return user.token