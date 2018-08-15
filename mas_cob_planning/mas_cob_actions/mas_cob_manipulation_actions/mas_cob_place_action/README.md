# mas_cob_place_action

A Care-O-bot-specific configuration package for `mdr_place_action`.

## Directory structure

```
mas_cob_place_action
|    CMakeLists.txt
|    package.xml
|    README.md
|____ros
     |____launch
          |_____place_action.launch
```

## Dependencies

* ``mdr_place_action``

## Example usage

1. Run the robot simulation: ``roslaunch mas_cob_bringup_sim robot.launch``
2. Run the ``move_arm`` action server: ``roslaunch mas_cob_move_arm_action move_arm.launch``
3. Run the ``move_base`` action server: ``roslaunch mas_cob_move_base_action move_base_action.launch``
4. Run the action server: ``roslaunch mas_cob_place_action place_action.launch``
5. Run the client example: ``rosrun mdr_place_action place_action_client_test``; the client example uses a predefined placing pose
