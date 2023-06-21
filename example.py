import numpy as np
from panda_kinematics import PandaWithHandKinematics
from panda_kinematics import PandaWithPumpKinematics


if __name__ == '__main__':
    print('Example using kinematics with Panda + Hand')
    kinematics = PandaWithHandKinematics()
    position = np.array([0.53, 0.07, 0.31])
    orientation_quat = np.array([ 0.0, 0.0, 0.0, 1.0]) # xyzw
    initial_joint_positions = np.array([0, 0, 0, 0, 0, 0, 0])
    solution = kinematics.ik(initial_joint_positions, position, orientation_quat)
    print(solution)

    print('Example using kinematics with Panda + Pump')
    kinematics = PandaWithPumpKinematics()
    position = np.array([0.53, 0.07, 0.31])
    orientation_quat = np.array([ 0.0, 0.0, 0.0, 1.0]) # xyzw
    initial_joint_positions = np.array([0, 0, 0, 0, 0, 0, 0])
    solution = kinematics.ik(initial_joint_positions, position, orientation_quat)
    print(solution)
