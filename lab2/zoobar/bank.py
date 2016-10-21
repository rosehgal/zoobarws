from zoodb import *
from debug import *

import time


def register(username):
    db = bank_setup()
    person_for_bank = db.query(Bank).get(username)
    
    if person_for_bank:
        raise ValueError("Person Already Exist")

    person_for_bank = Bank()    
    person_for_bank.username=username
    person_for_bank.zoobars=10
    db.add(person_for_bank)
    db.commit();
    return None

def transfer(sender, recipient, zoobars):
    # persondb = person_setup()
    bankdb = bank_setup()

    # senderp = persondb.query(Person).get(sender)
    # recipientp = persondb.query(Person).get(recipient)

    #sender_zoobar = bankdb.query(Bank).get(sender).zoobars
    #recipient_zoobar = bankdb.query(Bank).get(recipient).zoobars

    # sender_balance = sender_zoobars - zoobars
    # recipient_balance = recipient_zoobars + zoobars

    # if sender_balance < 0 or recipient_balance < 0:
    #     raise ValueError()

    # sender_zoobars = sender_balance
    # recipient_zoobars = recipient_balance
    # persondb.commit()

    sender= bankdb.query(Bank).get(sender)
    recipient= bankdb.query(Bank).get(recipient)

    if not recipient:
        raise ValueError("recipient Not Found")

    sender_balance = sender.zoobars - zoobars
    recipient_balance = recipient.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError("Not Sufficient balance")


    sender.zoobars = sender_balance
    recipient.zoobars = recipient_balance
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender.username
    transfer.recipient = recipient.username
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    # db = person_setup()
    #person = db.query(Person).get(username)
    #return person.zoobars
    db = bank_setup()
    user_bank_row = db.query(Bank).get(username)
    return user_bank_row.zoobars

def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))

