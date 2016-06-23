from threading import Thread
from datetime import datetime
import subprocess
import time
import os

from stem import Signal
from stem.control import Controller
from jinja2 import Template


TEMPLATE_CONFIG = """
SocksPort {{ port }}
ControlPort {{ control_port }}
DataDirectory /tmp/tor.datadir.{{ port }}
"""

class TorIpUpdateException(Exception):
	message_template = "Cannot update Tor IP. You can do it in {0} seconds"
	pass

class TorRunException(Exception):
	message_template = "Cannot run Tor"
	pass

class Tor(object):

	CONFIG_PATH = '/tmp/tor.config.{}'
	DATA_PATH = '/tmp/tor.data.{}'

	STATUSES = {
		1: 'STOP',
		2: 'RUN'
	}

	port = None
	control_port = None
	_status = None
	_ip_updated_time = None

	@property
	def status(self):
		return Tor.STATUSES[self._status]

	def __init__(self, port, control_port):

		self.CONFIG_PATH = Tor.CONFIG_PATH.format(port)
		self.DATA_PATH = Tor.DATA_PATH.format(port)
		
		self.port = port
		self.control_port = control_port
		self._status = 1
		self._ip_updated_time = None
		
		self._create()

	def _create(self):
		template = Template(TEMPLATE_CONFIG)
		config = template.render(port=self.port, control_port=self.control_port)
		with open(self.CONFIG_PATH, 'w') as config_file:
			config_file.write(config)

	def run(self):
		if self._status == 1:
			self.stop()
			proc = subprocess.Popen(["tor", "-f", self.CONFIG_PATH],stdout=subprocess.PIPE)
			while True:
				line = proc.stdout.readline()
				if 'Bootstrapped 100%' in line:
					self._status = 2
					self._ip_updated_time = datetime.now()
					break
				if not line:
					raise TorRunException(TorRunException.message_template)


	def stop(self):
		cmd = "kill $(ps -a | grep tor | grep " + str(self.port) + " | awk '{print $1}')"
		os.system(cmd)
		self._status = 1

	def update_ip(self):
		seconds = (datetime.now() - self._ip_updated_time).seconds
		if seconds < 10:
		    raise TorIpUpdateException(TorIpUpdateException.message_template.format(seconds), seconds)
		with Controller.from_port(port=self.control_port) as controller:
			controller.authenticate()
			controller.signal(Signal.NEWNYM)
			self._ip_updated_time = datetime.now()
		return 0

	def flush_all(self):
		pass
