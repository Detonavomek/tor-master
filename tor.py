from threading import Thread
import subprocess
import time
import os

from jinja2 import Template


class Tor(object):

	CONFIG_PATH = '/tmp/tor.config.{}'
	DATA_PATH = '/tmp/tor.data.{}'
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

		def run_thread(CONFIG_PATH):
			self._status = 2
			subprocess.call(["tor", "-f", CONFIG_PATH])
			self._status = 1

		if self._status == 1:
			thread = Thread(target = run_thread, args = (self.CONFIG_PATH, ))
			thread.start()
			time.sleep(10)

	def stop(self):
		cmd = "kill $(ps -a | grep tor | grep " + str(self.port) + " | awk '{print $1}')"
		os.system(cmd)
		time.sleep(1)

	def flush_all(self):
		pass
