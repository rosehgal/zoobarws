from zoodb import *
from debug import *

import time

def transfer(sender, recipient, zoobars):
    persondb = person_setup()
    senderp = persondb.query(Person).get(sender)
    recipientp = persondb.query(Person).get(recipient)

    # there will be balance mismatch if sender nd reciver are same!!
    if zoobars<0 or sender==recipient:
        raise ValueError("Kya Kar Diya")

    sender_balance = senderp.zoobars - zoobars
    recipient_balance = recipientp.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()

    senderp.zoobars = sender_balance
    recipientp.zoobars = recipient_balance
    persondb.commit()

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    db = person_setup()
    person = db.query(Person).get(username)

    transferdb = transfer_setup()
    transfer_table = db.query(Transfer).all()
    sender_balance = 10
    
    for t in transfer_table:
        if getattr(t,'sender') == username:
            sender_balance=sender_balance-getattr(t,'amount')
        elif getattr(t,'recipient')==username:
            sender_balance=sender_balance+getattr(t,'amount')
    
    if person.zoobars != sender_balance :
        raise ValueError("SomeBody tried Thefting!!")
        
    return person.zoobars

def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))

