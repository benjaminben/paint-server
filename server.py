import json
import struct
import re
# me - this DAT.
# webServerDAT - the connected Web Server DAT
# request - A dictionary of the request fields. The dictionary will always contain the below entries, plus any additional entries dependent on the contents of the request
# 		'method' - The HTTP method of the request (ie. 'GET', 'PUT').
# 		'uri' - The client's requested URI path. If there are parameters in the URI then they will be located under the 'pars' key in the request dictionary.
#		'pars' - The query parameters.
# 		'clientAddress' - The client's address.
# 		'serverAddress' - The server's address.
# 		'data' - The data of the HTTP request.
# response - A dictionary defining the response, to be filled in during the request method. Additional fields not specified below can be added (eg. response['content-type'] = 'application/json').
# 		'statusCode' - A valid HTTP status code integer (ie. 200, 401, 404). Default is 404.
# 		'statusReason' - The reason for the above status code being returned (ie. 'Not Found.').
# 		'data' - The data to send back to the client. If displaying a web-page, any HTML would be put here.

# return the response dictionary

connections = op("connections")

def updateConn(client, data):
	# for p in data:
	# o = op("conn"+str(connections[client,0].row))
	# o.op('clientX').panel.u = data['u']
	# o.op('clientY').panel.v = data['v']
	# op('examine1').cook()
	# for key in data:
		# print(key, data[key])
		# conns[client][key] = data[key]
		# o.Update()
	parent().UpdateConn(client, data)
	# print(op(re.sub("[.:]", "_", client)))
	# op(client).panel.u = data[0]
	# op(clinet).panel.v = data[1]
	return

def onHTTPRequest(webServerDAT, request, response):
	print("incoming")
	response['statusCode'] = 200 # OK
	response['statusReason'] = 'OK'
	# response['data'] = '<b>TouchDesigner: </b>' + webServerDAT.name
	response['data'] = "404 (try client)"
	return response

def onWebSocketOpen(webServerDAT, client):
	print("socket opened", client, webServerDAT.webSocketConnections)
	parent().AddConn(client)
	return

def onWebSocketClose(webServerDAT, client):
	print("socket closed", client)
	parent().DelConn(client)
	return

def onWebSocketReceiveText(webServerDAT, client, data):
	webServerDAT.webSocketSendText(client, data)
	return

def onWebSocketReceiveBinary(webServerDAT, client, data):
	# print("socket binary received", float(data))
	# updateConn(client, json.loads(data.decode()))
	updateConn(client, struct.unpack('ff', data))
	# webServerDAT.webSocketSendBinary(client, data)
	return

def onWebSocketReceivePing(webServerDAT, client, data):
	print("receive ping")
	return

def onWebSocketReceivePong(webServerDAT, client, data):
	print("receive pong")
	return

def onServerStart(webServerDAT):
	print("server alive")
	parent().WipeConns()
	return

def onServerStop(webServerDAT):
	print("server dun")
	parent().WipeConns()
	return
	