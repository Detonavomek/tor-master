from jinja2 import Template


#tor -f /tmp/tor.config.9070
class Tor(object):

	CONFIG_PATH = '/tmp/tor.config.{}'
	DATA_PATH = '/tmp/tor.data.{}'
	RUN_TOR_CMD = 'tor -f {}'
	TEMPLATE_CONFIG_PATH = 'torrc.template'

	STATUSES = {
		1: 'STOP',
		2: 'RUN'
	}

	port = None
	control_port = None
	_status = None

	@property
	def status(self):
		return Tor.STATUSES[self._status]

	def __init__(self, port, control_port):

		self.CONFIG_PATH = Tor.CONFIG_PATH.format(port)
		self.DATA_PATH = Tor.DATA_PATH.format(port)
		self.RUN_TOR_CMD = Tor.RUN_TOR_CMD.format(self.CONFIG_PATH)
		
		self.port = port
		self.control_port = control_port
		self._status = 1
		
		self._create()

	def _create(self):
		with open(Tor.TEMPLATE_CONFIG_PATH) as template_file:
			template = Template(template_file.read())
		config = template.render(port=self.port, control_port=self.control_port)
		with open(self.CONFIG_PATH, 'w') as config_file:
			config_file.write(config)

	def run(self):
		pass

	def stop(self):
		pass

	def flush_all(self):
		pass
