
import airsim

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True,"Drone1")
API_control=client.isApiControlEnabled()
if API_control == True:
	print("API controll enabled")
else:
	print("API controll not established")
client.armDisarm(True,"Drone1")
def state():
	return(client.getMultirotorState("Drone1"))
def x_position(state):
	return(state.kinematics_estimated.position.x_val)
def y_position(state):
	return(state.kinematics_estimated.position.y_val)
def z_position(state):
	return(state.kinematics_estimated.position.z_val)
def x_velocity(state):
	return(state.kinematics_estimated.linear_velocity.x_val)
def y_velocity(state):
	return(state.kinematics_estimated.linear_velocity.y_val)
def z_velocity(state):
	return(state.kinematics_estimated.linear_velocity.z_val)
def position(x_position,y_position,z_position):
	return (f"current x position:{x_position(state())}, current y position:{y_position(state())}")
	


client.takeoffAsync().join()
client.moveToPositionAsync(-10, 0, -3, 2).join()
print(position(x_position,y_position,z_position))
client.moveToPositionAsync(-10, 2, -3, 2).join()
print(position(x_position,y_position,z_position))
client.moveToPositionAsync(10, 2, -3, 2).join()
print(position(x_position,y_position,z_position))
client.moveToPositionAsync(10, 4, -3, 2).join()
print(position(x_position,y_position,z_position))
client.moveToPositionAsync(-10, 4, -3, 2).join()
print(position(x_position,y_position,z_position))
client.moveToPositionAsync(-10, 6, -3, 2).join()
print(position(x_position,y_position,z_position))
client.moveToPositionAsync(10, 6, -3, 2).join()
print(position(x_position,y_position,z_position))
client.moveToPositionAsync(10, 8, -3, 2).join()
print(position(x_position,y_position,z_position))
client.moveToPositionAsync(-10, 8, -3, 2).join()
print(position(x_position,y_position,z_position))
client.moveToPositionAsync(-10, 10, -3, 2).join()
print(position(x_position,y_position,z_position))
client.moveToPositionAsync(10, 10, -3, 2).join()
print(position(x_position,y_position,z_position))

print("Returning to start position")
client.moveToPositionAsync(0,0,-3,2).join()
client.moveToPositionAsync(0,0,1,0.5).join()
client.armDisarm(False,"Drone1")
print("Motors OFF")
client.enableApiControl(False,"Drone1")