import zmq

if __name__ == '__main__':
	context = zmq.Context.instance()
	server = context.socket(zmq.PUSH)
	server.connect("tcp://127.0.0.1:5488")
	send = context.socket(zmq.PUSH)
	send.connect("tcp://127.0.0.1:5489")
	started = False
	while True:
		if started:
			input("Press Enter to Stop...")
			send.send_string("false")
			started = False
		else:
			input("Press Enter to Start...")
			server.send_string("true")
			started = True