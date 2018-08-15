# mas_cob_move_base_action

A Care-O-bot-specific configuration package for `mdr_move_base_action`.

## Directory structure

```
mas_cob_move_base_action
|    CMakeLists.txt
|    package.xml
|    README.md
|____ros
     |____launch
          |_____move_base.launch
```

## Dependencies

* ``mdr_move_base_action``
* ``mas_cob_move_arm_action``

## Example usage

1. Run the robot simulation: ``roslaunch mas_cob_bringup_sim robot.launch``
2. Run the moveit interface for the robot: ``roslaunch mas_cob_moveit move_group.launch``
3. Run the ``move_arm`` action server: ``roslaunch mas_cob_move_arm_action move_arm.launch``
4. Run the action server: ``roslaunch mas_cob_move_base_action move_base.launch``
5. Run the client example: ``rosrun mdr_move_base_action move_base_action_client_test <NAMED_TARGET>``; the client example only allows using the action with a named target
