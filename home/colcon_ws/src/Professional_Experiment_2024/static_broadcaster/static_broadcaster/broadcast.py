import math
import sys

from geometry_msgs.msg import TransformStamped

import numpy as np

import rclpy
from rclpy.node import Node

from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster


def quaternion_from_euler(ai, aj, ak):
    ai /= 2.0
    aj /= 2.0
    ak /= 2.0
    ci = math.cos(ai)
    si = math.sin(ai)
    cj = math.cos(aj)
    sj = math.sin(aj)
    ck = math.cos(ak)
    sk = math.sin(ak)
    cc = ci*ck
    cs = ci*sk
    sc = si*ck
    ss = si*sk

    q = np.empty((4, ))
    q[0] = cj*sc - sj*cs
    q[1] = cj*ss + sj*cc
    q[2] = cj*cs - sj*sc
    q[3] = cj*cc + sj*ss

    return q


class StaticFramePublisher(Node):
    """
    Broadcast transforms that never change.

    This example publishes transforms from `world` to a static turtle frame.
    The transforms are only published once at startup, and are constant for all
    time.
    """

    def __init__(self):
        super().__init__('static_turtle_tf2_broadcaster')

        self.tf_static_broadcaster = StaticTransformBroadcaster(self)

        # Publish static transforms once at startup
        self.make_transforms()

    def make_transforms(self):
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'world'
        t.child_frame_id = 'default_cam'

        t.transform.translation.x = float(0.12)
        t.transform.translation.y = float(0.0)
        t.transform.translation.z = float(0.4525)
        t.transform.rotation.x = -0.70711
        t.transform.rotation.y = 0.70711
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 0.0

        self.tf_static_broadcaster.sendTransform(t)

        self.get_logger().info(f'Creation of {t.child_frame_id} frame is completed')


def main():
    rclpy.init()
    node = StaticFramePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
