import time

from tor_pool import TorPool
from tor import TorIpUpdateException


tors = TorPool()

tors.add(port=9070, control_port=9071)
tors.add(port=9080, control_port=9081)
tors.add(port=9090, control_port=9091)

print "START"
print tors.instances

print "RUN 9070"
tors.run(9070)

print tors.instances

print "FAST UPDATE IP 9070"
try:
	tors.update_ip(9070)
	raise Exception('IP Update Error. Need wait 10 seconds')
except TorIpUpdateException as e:
	pass

print tors.instances

print "NORMAL UPDATE IP 9070"
time.sleep(10)
tors.update_ip(9070)

print tors.instances

print "RUN ALL"
tors.run_all()

print tors.instances

print "STOP 9070"
tors.stop(9070)

print tors.instances

print "STOP ALL"
tors.stop_all()

print tors.instances
