#!/usr/bin/python

import rpclib
import sys
import bank
import auth_client
from debug import *

class BankRpcServer(rpclib.RpcServer):
	def rpc_balance(self,username):
		return bank.balance(username=username)

	def rpc_transfer(self,sender,recipient,zoobars,token):
		if not auth_client.check_token(sender,token):
			raise ValueError("Invalid token")
		return bank.transfer(sender,recipient,zoobars)

	def rpc_register(self,username):
		return bank.register(username)

	def rpc_get_log(self,username):
		return bank.get_log(username)

(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
