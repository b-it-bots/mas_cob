# mas_cob_move_arm_action

A Care-O-bot-specific configuration package for `mdr_move_arm_action`.

## Directory structure

```
mas_cob_move_arm_action
|    CMakeLists.txt
|    package.xml
|    README.md
|____ros
     |____launch
          |_____move_arm.launch
```

## Dependencies

* ``mdr_move_arm_action``

## Example usage

1. Run the robot simulation: ``roslaunch mas_cob_bringup_sim robot.launch``
2. Run the action server: ``roslaunch mas_cob_move_arm_action move_arm.launch``
3. Run the client example:
    1. with a named target motion goal: ``rosrun mdr_move_arm_action move_arm_action_client_test 1 folded``
    2. with a pose motion goal: ``rosrun mdr_move_arm_action move_arm_action_client_test 2 "['base_link', <x, y, z>, <x, y, z, w>]"``
    3. with a goal for the joint values: ``rosrun mdr_move_arm_action move_arm_action_client_test 3 "[<joint values>]"``
