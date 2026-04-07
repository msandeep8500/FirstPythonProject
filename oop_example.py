from Robot import Robot, PackagingSolution
from Robot import RoboticArm
from Robot import PackagingSolution
# print("test")
# my_robot= Robot("R2D2",2 )
# my_robot.say_hi()
# my_robot.init_hardware()
# my_robot.print_info()
#
# print(my_robot.name)
# print(my_robot.version_number)

robotic_arm_left = RoboticArm("Bob2",4,300)

robotic_arm_left.pick_object(3,4)
robotic_arm_left.place_object(4,5)
robotic_arm_right = RoboticArm("Bob_Right",5,500)
robotic_arm_left.pick_object(7,8)
robotic_arm_left.place_object(14,9)

packaging_solution = PackagingSolution(robotic_arm_left,robotic_arm_right)
