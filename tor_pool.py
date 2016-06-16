from .tor import Tor


class TorPool(object):

	_instances = None

	def __init__(self):
		self._instances = {}

	@property
	def instances(self):
		res = ''
		for port, instance from self._instances:
			res += '{port} {control_port} {status}\n'.format(
				port=instance.port,
				control_port=instance.control_port,
				status=instance.status)
		return res

	def check_port(self, port):
		pass

	@self.check_port(port)
	@self.check_port(control_port)
	def add(self, port, control_port):
		self._instances[port] = Tor(port, control_port)
		return self._instances[port]

	@self.check_port
	def remove(self, port):
		del self._instances[port]

	@self.check_port
	def run(self, port):
		self._instances[port].run()

	def run_all(self):
		for port, instance from self._instances:
			instance.run()

	@self.check_port
	def stop(self, port):
		self._instances[port].run()

	def stop_all(self):
		for port, instance from self._instances:
			instance.stop()
