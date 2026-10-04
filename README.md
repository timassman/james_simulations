# james_simulations
Gazebo simulation for the James robot

> **Status: work in progress — not functional yet.** See [Known issues](#known-issues).

| Package | Contents |
|---|---|
| `james_gazebo` | Gazebo models of objects in the environment, worlds and launch files |

How this repo fits in with the other James repositories is described in the README of
[james_robot](https://github.com/timassman/james_robot).

**Laptop only.** Gazebo is not installed in the Docker image on the Jetson. Do not sync this
repo to the Jetson or build it there.

## Contents of james_gazebo

| Path | Contents |
|---|---|
| `models/beer_bottle/` | Gazebo model (SDF) of a single beer bottle, plus a URDF variant |
| `launch/spawn_bottle.launch.py` | Starts Gazebo, spawns one bottle and opens RViz |
| `rviz/beer_bottle.rviz` | RViz configuration |

Only environment objects belong here. The crate is part of the robot (bolted to the
Roomba, arm mounted on it), so its geometry belongs in `james_description` in james_robot.

## Build (laptop)

```bash
cd ~/Git-Workspace/james_simulations
colcon build --symlink-install
source install/local_setup.bash
ros2 launch james_gazebo spawn_bottle.launch.py
```

## Known issues

Likely reasons the bottle does not show up (not yet verified):

- **Gazebo cannot resolve `model://beer_bottle/...`**: the `models/` directory of this
  package is not on the Gazebo model path. `package.xml` needs an export such as
  `<gazebo_ros gazebo_model_path="${prefix}/models"/>`.
- **RViz shows nothing**: the RViz config contains a RobotModel display, but the launch
  file starts no `robot_state_publisher`, so there is no `robot_description`. The URDF also
  uses `model://` URIs, which RViz cannot resolve (`package://james_gazebo/...` is needed).
- **Gazebo Classic**: `gazebo_ros` (Gazebo Classic 11) reached end-of-life in January 2025.
  For new work on ROS 2 Humble, consider Gazebo Fortress with `ros_gz`.
- **Unused mesh variants**: only `beerbottle.obj` is used; `beerbottle2.obj`,
  `beerbottle3.obj` and `beerbottle.obj.old` are experiments.

## Credits

- Bottle mesh: "Low Poly Beer Bottle" by kenny_pizza, licensed under
  [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)
  (see `james_gazebo/models/beer_bottle/meshes/beerbottle.LICENSE`)
