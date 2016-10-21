from debug import *
from zoodb import *
import rpclib

def balance(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('balance',username=username)
        return ret

def transfer(sender,recipient,zoobars,token):
    try:
        with rpclib.client_connect('/banksvc/sock') as c:
            ret = c.call('transfer',sender=sender,recipient=recipient,zoobars=zoobars,token=token)
            return ret
    except Exception:
        return ValueError("Error")

def register(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('register',username=username)
        return ret


def get_log(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('get_log',username=username)
        return ret



# def login(username, password):
#     ## Fill in code here.
#     with rpclib.client_connect('/authsvc/sock') as c:
#         ret = c.call('login',user = username,passd = password)
#         return ret

# def register(username, password):
#     ## Fill in code here.
#     with rpclib.client_connect('/authsvc/sock') as c:
#         ret = c.call('register', user = username,passd = password)
#         return ret

# def check_token(username, token):
#     ## Fill in code here.
#     with rpclib.client_connect('/authsvc/sock') as c:
#         ret = c.call('check_token',user = username,token = token)
#         return ret
