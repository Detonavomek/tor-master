from .tor_pool import TorPool


tors = TorPool()

print tors.instances

tors.add(port=9070, control_port=9071)
tors.add(port=9080, control_port=9081)
tors.add(port=9090, control_port=9091)

tors.run(9070)

print tors.instances

tors.run_all()

print tors.instances

tors.stop(9070)

print tors.instances

tors.stop_all()

print tors.instances