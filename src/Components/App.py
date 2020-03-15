import re

def Conn():
	return {
		'clientX': 0,
		'clientY': 0,
		# 'brush': {
		# 	'hue': 100,
		# 	'size': 1,
		# 	'brush': 'default',
		# }
	}

conns = op('conns')

def format(client):
	return re.sub("[.:]", "_", client)

class App:
	def __init__(self, owner):
		self.owner = owner
		return
	def AddConn(self, client):
		c = self.owner.copy(self.owner.op('conn_artist0'), name=format(client))
		geo = c.op('geo')
		geo.display = True
		geo.render = True
	def DelConn(self, client):
		self.owner.op(format(client)).destroy()
	def WipeConns(self):
		self.owner.unstore('*')
	def UpdateConn(self, client, data):
		c = self.owner.op(format(client))
		c.panel.u = data[0]
		c.panel.v = data[1]
		return
		# op(client.ClientX.val = data['clientX']
		# op(conns[client, 1],)
	def BindConnOp(self, client, op):
		return
	# 	print(client)
	# 	conn = self.owner.fetch(client)
	# 	conn['op'] = op
	# 	self.owner.store(client, conn)