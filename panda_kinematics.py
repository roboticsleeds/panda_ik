from abc import ABC
from abc import abstractmethod
import math
import numpy as np
import panda_ik_pump
import panda_ik_hand


class PandaKinematics(ABC):
    @abstractmethod
    def solver(self, initial_joint_positions, position, orientation_quat, q7):
        pass

    def ik(self, initial_joint_positions, position, orientation_quat):
        angles = np.linspace(-2.89, 2.89, 50)

        for angle in angles:
            q7 = angle
            initial_joint_positions[-1] = q7
            solutions = self.solver(position, orientation_quat, q7, initial_joint_positions)

            for solution in solutions:
                if all([not math.isnan(solution[i]) for i in range(7)]):
                    return solution


class PandaWithHandKinematics(PandaKinematics):
    def solver(self, position, orientation_quat, q7, initial_joint_positions):
        return panda_ik_hand.franka_IK(position, orientation_quat, q7, initial_joint_positions)


class PandaWithPumpKinematics(PandaKinematics):
    def solver(self, position, orientation_quat, q7, initial_joint_positions):
        return panda_ik_pump.franka_IK(position, orientation_quat, q7, initial_joint_positions)

    def ik(self, initial_joint_positions, position, orientation_quat):
        solution = super().ik(initial_joint_positions, position, orientation_quat)

        if solution is not None:
            # When not using the hand, we need to remove 45 degrees from the
            # last joint. See discussion in README of the kinematics repo.
            solution[-1] -= 0.785398

        return solution
