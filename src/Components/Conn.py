from TDStoreTools import StorageManager # deeply dependable collections/storage
TDF = op.TDModules.mod.TDFunctions # utility functions

class Conn:
	def __init__(self, owner):
		self.owner = owner
		TDF.createProperty(
			self,
			'ClientX',
			value=0,
			dependable=True,
			readOnly=False
		)
		return
	def update(self, data):
		op('update').cook()