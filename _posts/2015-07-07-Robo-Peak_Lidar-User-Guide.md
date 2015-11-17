---
layout: post
comments: true
title: Robo Peak Lidar User Guide
comments: true
excerpt: "The rplidar is a 360 degree laser scanning device equipped with a rotary motor that spins when connected to any USB 2.0/3.0 device. It spins at 5.5 Hz and I uderstand it can be configured at a  user-specified scan-rate ..."
date: 2015-07-07 16:00:00
tags: Lidars, Sensing, Robots
permalink: Robo Peak Lidar
---

<div style="text-align:center;"></div>

###Introduction

Here is a simple guide for using the robo peak lidar for simultaneous localization and mapping in ROS.

I struggled a little bit between yesterday and now when I tried to get the robopeak lidar working in order to sense a human head and report 6D tracking information for my current project, more so because the documentation for the robot is sparse and you have to glean countless internet pages to understand how the sensor works. I am putting together this short user guide to aid someone who might be facing a asimilar challenge as I did. 

**First things first**: The rplidar is a 360 degree laser scanning device equipped with a rotary motor that spins when connected to any USB 2.0/3.0 device. It spins at 5.5 Hz and I uderstand it can be configured at a user-specified scan-rate (I have not tried this yet). It has a typical distance range of 0.2m to 6m and a distance resolution of `<0.5mm` when `<1.5m` from an object.

Thankfully, the team at robopeak have a [git repo](https://github.com/robopeak/rplidar_ros) that allows you do to a quick scan and view of the lidar output frames in [rviz](http://wiki.ros.org/rviz/Tutorials). Clone this master and build it with `catkin_make`. If you follow the [Readme](https://github.com/robopeak/rplidar_ros), this will catch you up to speed, provided you have ros set-up on your device (I used ros indigo but it works across groovy and hydro).

###Building a map of the environment.
Next, head over to your linux terminal and install `hector_slam` as follows:

<pre class="terminal"> <code>$ sudo apt-install ros-indigo-hector-slam</code></pre>

That should get you up fired and running by installing [hector-slam](http://wiki.ros.org/hector_slam/Tutorials/SettingUpForYourRobot) for the rplidar robot.

Now, navigate to your `catkin_ws` and edit the file `hector_mapping.launch` as in 

```xml
    <launch>
  <node pkg="hector_mapping" type="hector_mapping" name="hector_height_mapping" output="screen">
    <!--Source here: http://wiki.ros.org/hector_slam/Tutorials/SettingUpForYourRobot-->
    <param name="pub_map_odom_transform" value="true"/>
    <param name="map_frame" value="map" />
    <param name="base_frame" value="base_stabilized" /> <!-- no imu at the moment to get roll/pitch angles so base_frame == base_stabilized-->
    <param name="odom_frame" value="base_link" /><!--use without odom_frame-->

    <param name="scan_topic" value="scan" />
    <!--param name="odom_frame" value="nav" /-->
    
    <param name="output_timing" value="false"/>
    <param name="advertise_map_service" value="true"/>
    <param name="use_tf_scan_transformation" value="true"/>
    <param name="use_tf_pose_start_estimate" value="true"/>
    <param name="pub_map_odom_transform" value="true"/>
    <param name="map_with_known_poses" value="true"/>

    <!--Map Update parameters -->
    <param name="map_pub_period" value="5.0"/>
    <param name="update_factor_free" value="0.45"/>
    
    <param name="map_update_distance_thresh" value="0.02"/>
    <param name="map_update_angle_thresh" value="0.06"/>
    
    <!--Map size/start point-->
    <param name="map_resolution" value="0.025"/>
    <param name="map_size" value="2048"/>
    <param name="map_start_x" value="0.5"/>
    <param name="map_start_y" value="0.5"/>
    
    <param name="laser_min_dist" value="0.1" />
    <param name="laser_max_dist" value="6.5" />
    <param name="laser_z_min_value" value="-2.5"/>
    <param name="laser_z_max_value" value="6.5"/>

    <remap from="map" to="height_map" />
    <remap from="dynamic_map" to="height_map" />
  </node>
  
  <node pkg="hector_geotiff" type="geotiff_node" name="hector_height_geotiff_node" output="screen" launch-prefix="nice -n 15">
    <remap from="map" to="height_map" />
    <param name="map_file_path" type="string" value="$(find hector_geotiff)/maps" />
    <param name="map_file_base_name" type="string" value="RRL_2012_HectorDarmstadt_2m" />
    <param name="geotiff_save_period" type="double" value="55" />
    <param name="draw_background_checkerboard" type="bool" value="true" />
    <param name="draw_free_space_grid" type="bool" value="true" />
  </node>
</launch>
```

The comments I left in the xml file will help you in making your changes as the [ros wiki page](http://wiki.ros.org/hector_slam/Tutorials/SettingUpForYourRobot) describes.

Then, you want to download one of the [following](https://code.google.com/p/tu-darmstadt-ros-pkg/downloads/list) bag files from into your `catkin_ws` folder. Do

<pre class="terminal"><code>$ wget https://code.google.com/p/tu-darmstadt-ros-pkg/downloads/detail?name=Team_Hector_MappingBox_RoboCup_2011_Rescue_Arena.bag&can=2&q=</code></pre>

for example. 

We are all set to go. Open a terminal window, and launch the hector_slam system

<pre class="terminal"><code>$ roslaunch hector_slam_launch tutorial.launch</code></pre>

to start the [hector_mapping](http://wiki.ros.org/hector_mapping) node, the [hector_trajectory](http://wiki.ros.org/hector_trajectory_server) node and [hector_geotiff](http://wiki.ros.org/hector_geotiff) node. 

In another terminal, do

<pre class="terminal"><code>$ rosbag play Team_Hector_MappingBox_RoboCup_2011_Rescue_Arena.bag  --clock</code></pre>

You should see a pre-recorded mapping process in rviz. You could do your own slam mapping by recording your own bag file. Afterwards, feel free to record your geotiff map at any time by doing,

<pre class="terminal"><code>$ rostopic pub syscommand std_msgs/String "savegeotiff"</code></pre> 

in terminal. Your geotiff maps are saved in the `map_file_path` that you specified in the `hector_mapping.launch` file.

<!--
<a href="https://twitter.com/share" class="twitter-share-button" data-via="patmeansnoble">Tweet</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
-->