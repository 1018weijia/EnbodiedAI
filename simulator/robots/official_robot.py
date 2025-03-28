from simulator.core.robot_base import BaseRobot
from simulator.core.register import register
from lazyimport import lazyimport
lazyimport.lazyattr(
    globals(), 
    """
    from omni.isaac.wheeled_robots.robots import WheeledRobot
    """
)

@register.registry_robot("wheeled_robot")
class Wheeled_Robot(BaseRobot, WheeledRobot):
    def __init__(WheeledRobotConfig):
        pass