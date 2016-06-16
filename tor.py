class Tor(object):

	CONFIG_PATH = '/tmp/tor.config.{}'
	DATA_PATH = '/tmp/tor.data.{}'

	port = None
	control_port = None

	def __init__(self, port, control_port):
		self.port = port
		self.control_port = control_port

	def run(self):
		pass

	def stop(self):
		pass
