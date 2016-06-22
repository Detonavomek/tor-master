from tor import Tor


class TorPool(object):

	_instances = None

	def __init__(self):
		self._instances = {}

	@property
	def instances(self):
		res = 'Tor instances:\n'
		for port, instance in self._instances.items():
			res += '{port} {control_port} {status}\n'.format(
				port=instance.port,
				control_port=instance.control_port,
				status=instance.status)
		return res

	def check_port(self, port):
		pass

	# @self.check_port(port)
	# @self.check_port(control_port)
	def add(self, port, control_port):
		self._instances[port] = Tor(port, control_port)
		return self._instances[port]

	# @self.check_port
	def remove(self, port):
		del self._instances[port]

	# @self.check_port
	def run(self, port):
		self._instances[port].run()

	def run_all(self):
		for port, instance in self._instances.items():
			instance.run()

	# @self.check_port
	def update_ip(self, port):
		return self._instances[port].update_ip()

	# @self.check_port
	def stop(self, port):
		self._instances[port].stop()

	def stop_all(self):
		for port, instance in self._instances.items():
			instance.stop()

	def flush_all(self):
		pass
