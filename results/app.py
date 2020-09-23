
import anvil.server

anvil.server.connect("3W7A4JNMTUBLSEIZO2WZIZ22-ZUI6HCYXCAQSQSYP")

@anvil.server.callable
def say_hello(name):
  print("Hello from the uplink, %s!" % name)

anvil.server.wait_forever()
