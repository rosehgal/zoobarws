#!/usr/bin/python

import rpclib
import sys
import auth
from debug import *

class AuthRpcServer(rpclib.RpcServer):
	def rpc_getToken(self,username):
		return auth.getToken(username)
		
	def rpc_login(self, user, passd):
		#return 'You said: %s' % s
		return auth.login(user, passd)

	def rpc_register(self, user, passd):
		#return 'You said: %s' % s
		print "before registration"
		return auth.register(user, passd)

	def rpc_check_token(self, user, token):
		#return 'You said: %s' % s
		return auth.check_token(user, token)

## Fill in RPC methods here.
#pass

(_, dummy_zookld_fd, sockpath) = sys.argv

s = AuthRpcServer()
s.run_sockpath_fork(sockpath)
