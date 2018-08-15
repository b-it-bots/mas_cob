import rospy
import simple_script_server

from mdr_gripper_controller.gripper_controller_base import GripperControllerBase

class GripperController(GripperControllerBase):
    def __init__(self):
        self.cob_script_server = simple_script_server.simple_script_server()

    def open(self):
        rospy.loginfo('[OPEN_GRIPPER] Opening the gripper')
        sdh_handle = self.cob_script_server.move('gripper', 'cylopen', blocking=False)
        rospy.loginfo('[OPEN_GRIPPER] Gripper opened')

    def close(self):
        rospy.loginfo('[CLOSE_GRIPPER] Closing the gripper')
        sdh_handle = self.cob_script_server.move('gripper', 'cylclosed', blocking=False)
        rospy.loginfo('[CLOSE_GRIPPER] Gripper closed')
