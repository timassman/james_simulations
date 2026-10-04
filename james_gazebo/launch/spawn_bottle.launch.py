from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # Path to the beer bottle model
    bottle_model_path = PathJoinSubstitution(
        [
            FindPackageShare("james_gazebo"),
            "models",
            "beer_bottle",
        ]
    )

    # Path to the SDF file
    sdf_file_path = PathJoinSubstitution([bottle_model_path, "model.sdf"])

    # Spawn the beer bottle model in Gazebo
    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-entity",
            "beer_bottle",
            "-file",
            sdf_file_path,
            "-x",
            "0.0",
            "-y",
            "0.0",
            "-z",
            "0.5",
        ],
        output="screen",
    )

    # Launch Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [FindPackageShare("gazebo_ros"), "launch", "gazebo.launch.py"]
            )
        )
    )

    # Launch RViz
    rviz_config_path = PathJoinSubstitution(
        [
            FindPackageShare("james_gazebo"),
            "rviz",
            "beer_bottle.rviz",
        ]
    )
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", rviz_config_path],
        output="screen",
    )

    return LaunchDescription([gazebo, spawn_entity, rviz])
