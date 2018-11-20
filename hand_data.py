import time
import collections
from lib_leap import Leap
from Leap import Bone

def get_hand_position(controller, blocking=False):
    frame = controller.frame()
    if not blocking and len(frame.fingers) == 0:
        return None

    while len(frame.fingers) == 0:
        frame = controller.frame()

    fingers = controller.frame().fingers
    finger_bones = []
    for finger in fingers:
        finger_bones.append(finger.bone(Bone.TYPE_METACARPAL).next_joint)
        finger_bones.append(finger.bone(Bone.TYPE_PROXIMAL).next_joint)
        finger_bones.append(finger.bone(Bone.TYPE_INTERMEDIATE).next_joint)
        finger_bones.append(finger.bone(Bone.TYPE_DISTAL).next_joint)

    hands = controller.frame().hands
    hand_center = 0
    for hand in hands:
        hand_center = hand.palm_position

    calibrated_finger_bones = collections.OrderedDict()
    for i in range(len(finger_bones)):
        normalized_joint = (finger_bones[i] - hand_center).to_tuple()
        for j in range(3):
            calibrated_finger_bones[
                "attr" + str(i * 3 + j)] = normalized_joint[j]

    return calibrated_finger_bones