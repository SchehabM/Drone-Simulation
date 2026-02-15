
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


client.takeoffAsync().join()
client.moveToPositionAsync(-10, 0, -3, 2).join()
#velocity_z=state.kinematics_estimated.linear_velocity.z_val
#position_z=state.kinematics_estimated.position.z_val

client.moveToPositionAsync(0,0,-3,2).join()
client.moveToPositionAsync(0,0,1,0.5).join()
client.landAsync("Drone1").join()
#state=client.getMultirotorState("Drone1")
#velocity_x=state.kinematics_estimated.linear_velocity.x_val
#position_x=state.kinematics_estimated.position.x_val
client.armDisarm(False,"Drone1")
print("Motors OFF")
client.enableApiControl(False,"Drone1")
