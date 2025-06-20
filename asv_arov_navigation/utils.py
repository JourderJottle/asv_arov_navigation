import rclpy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Quaternion
from scipy.spatial.transform import Rotation
import numpy as np

def build_pose_stamped(time, frame_id, pose, orientation=None) :
    pose_stamped = PoseStamped()
    pose_stamped.header.stamp = time.to_msg()
    pose_stamped.header.frame_id = frame_id
    if orientation is None :
        pose_stamped.pose.position.x = float(pose[0])
        pose_stamped.pose.position.y = float(pose[1])
        pose_stamped.pose.position.z = float(pose[2])
        pose_stamped.pose.orientation = quaternion_from_euler(pose[3:6])
    else :
        pose_stamped.pose.position.x = float(pose[0])
        pose_stamped.pose.position.y = float(pose[1])
        pose_stamped.pose.position.z = float(pose[2])
        pose_stamped.pose.orientation = orientation
    return pose_stamped

def quaternion_from_euler(rpy) :
    quat = Rotation.from_euler("xyz", rpy, degrees=False).as_quat()
    out = Quaternion()
    out.x = float(quat[0])
    out.y = float(quat[1])
    out.z = float(quat[2])
    out.w = float(quat[3])
    return out

def euler_from_quaternion(quat) :
    return Rotation.from_quat([quat.x, quat.y, quat.z, quat.w]).as_euler("xyz", degrees=False)