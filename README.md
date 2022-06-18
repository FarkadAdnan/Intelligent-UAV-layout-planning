# Intelligent-UAV-layout-planning
Intelligent UAV path planning simulation system is a software with fine operation control, strong platform integration, omnidirectional model building and application automation. It takes the UAV war between A and B in Zone C as the background. The core function of the system is to plan the UAV route through the simulation platform and verify th…

-  By:Farkad Adnan فرقد عدنان - 
 -E-mail: farkad.hpfa95@gmail.com 
-inst : farkadadnan 
- #farkadadnan , #farkad_adnan , فرقد عدنان# 
- FaceBook: كتاب عالم الاردوينو 
- inst : arduinobook
1. #كتاب_عالم_الاردوينو
2. #كتاب_عالم_الآردوينو

* facebook : https://www.facebook.com/profile.php?id=100002145048612
* instagram:  https://www.instagram.com/farkadadnan/
* linkedin : https://www.linkedin.com/in/farkad-adnan-499972121/


 <p>
 <a href='https://mobile.twitter.com/farkadadnan'>
        <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/farkadadnan?label=%40farkadadnan&style=social" alt='Twitter' align="center"/>
    </a>
</p>
# -----------------------------------------------
# UAVS
UAVS_Drone Intelligent UAV path planning simulation system is a software with fine operation control, strong platform integration, omnidirectional model building and application automation. It takes the UAV war between A and B in Zone C as the background. The core function of the system is to plan the UAV route through the simulation platform and verify the output. The data can be imported into the real UAV to make it accurately arrive at any position in the battlefield according to the specified route and support the joint action of multi-person and multi-device formation.
# 1. Software Interface

![1](https://user-images.githubusercontent.com/35774039/159815751-179eb8d7-5349-4367-9855-28ea4e5d7f92.jpg)
# 2. Software Architecture (plug-ins to be implemented for some extended functions)

![125012016-0ea2c380-e09c-11eb-9f04-5919bb37db61](https://user-images.githubusercontent.com/35774039/159815833-4486a26f-b262-4302-b2eb-1e993fb89c8b.png)
# 3. Code

![2](https://user-images.githubusercontent.com/35774039/159815877-95f1934a-8702-4517-b136-8b8b7fb3bbe0.png)
# Intelligent Control
![110713362-c7ffa280-823c-11eb-9d30-d08ae469522f](https://user-images.githubusercontent.com/35774039/159816901-548ae5f7-3c9b-404f-ac17-f2d3dbad2fbc.png)
![110713375-cdf58380-823c-11eb-8efd-367f4535d42b](https://user-images.githubusercontent.com/35774039/159816907-25a99d98-8bf2-4baf-a8c9-f15a0c4928cc.png)
# Directory Structure
```
drone_PathPlanning
	├─fence.txt
	├─leaflet_folium_plot.py
	├─mission.waypoints
	│          
	├─folium-0.12.1
	│              
	├─leaflet
	│          
	├─results
	│      
	├─Sampling_based_Planning
	│  ├─algorithm_mission_rrt2D
	│  │      algorithm_mission_batch_informed_trees.waypoints
	│  │      algorithm_mission_dubins_rrt_star.waypoints
	│  │      algorithm_mission_dynamic_rrt.waypoints
	│  │      algorithm_mission_extended_rrt.waypoints
	│  │      algorithm_mission_fast_marching_trees.waypoints
	│  │      algorithm_mission_informed_rrt_star.waypoints
	│  │      algorithm_mission_rrt.waypoints
	│  │      algorithm_mission_rrt_connect.waypoints
	│  │      algorithm_mission_rrt_star.waypoints
	│  │      algorithm_mission_rrt_star_smart.waypoints
	│  │      
	│  ├─indoor_obstacle_avoidance_rrt3D
	│  │      IOAPath_rrt3D.waypoints
	│  │      IOAPath_rrt_star3D.waypoints
	│  │      IOA_BIT_star3D.waypoints
	│  │      IOA_extend_rrt3D.waypoints
	│  │      
	│  ├─rrt_2D
	│  │      batch_informed_trees.py
	│  │      draw.py
	│  │      dubins_path.py
	│  │      dubins_rrt_star.py
	│  │      dynamic_rrt.py
	│  │      env.py
	│  │      extended_rrt.py
	│  │      fast_marching_trees.py
	│  │      informed_rrt_star.py
	│  │      judge.py
	│  │      plotting.py
	│  │      queue.py
	│  │      rrt.py
	│  │      rrt_connect.py
	│  │      rrt_star.py
	│  │      rrt_star_smart.py
	│  │      utils.py
	│  │      __init__.py
	│  │          
	│  ├─rrt_2D_
	│  │      
	│  ├─rrt_3D
	│  │     ABIT_star3D.py
	│  │     BIT_star3D.py
	│  │     dynamic_rrt3D.py
	│  │     env3D.py
	│  │     extend_rrt3D.py
	│  │     FMT_star3D.py
	│  │     informed_rrt_star3D.py
	│  │     plot_util3D.py
	│  │     queueL.py
	│  │     rrt3D.py
	│  │     rrt_connect3D.py
	│  │     rrt_star3D.py
	│  │     utils3D.py
	│  │          
	│  └─rrt_3D_
	│          
	└─Search_based_Planning
		├─algorithm_mission_Search2D
		│      algorithm_mission_Anytime_D_star.waypoints
		│      algorithm_mission_ARAstar.waypoints
		│      algorithm_mission_Astar.waypoints
		│      algorithm_mission_Best_First.waypoints
		│      algorithm_mission_bfs.waypoints
		│      algorithm_mission_Bidirectional_a_star.waypoints
		│      algorithm_mission_Bidirectional_dfs.waypoints
		│      algorithm_mission_Bidirectional_Dijkstra.waypoints
		│      algorithm_mission_Bidirectional_D_star.waypoints
		│      algorithm_mission_Bidirectional_D_star_Lite.waypoints
		│      algorithm_mission_Bidirectional_LPAstar.waypoints
		│      algorithm_mission_Bidirectional_LRTAstar.waypoints
		│      algorithm_mission_Bidirectional_RTAAStar.waypoints
		│      
		├─indoor_obstacle_avoidance_Search_3D
		│      IOA_Anytime_Dstar3D.waypoints
		│      IOA_Astar3D.waypoints
		│      IOA_bidirectional_Astar3D.waypoints
		│      IOA_Dstar3D.waypoints
		│      IOA_DstarLite3D.waypoints
		│      IOA_LP_Astar3D.waypoints
		│      IOA_LRT_Astar3D.waypoints
		│      IOA_RTA_Astar3D.waypoints
		│      
		├─Search_2D
		│     Anytime_D_star.py
		│     ARAstar.py
		│     Astar.py
		│     Best_First.py
		│     bfs.py
		│     Bidirectional_a_star.py
		│     dfs.py
		│     Dijkstra.py
		│     D_star.py
		│     D_star_Lite.py
		│     env.py
		│     LPAstar.py
		│     LRTAstar.py
		│     plotting.py
		│     queueL.py
		│     RTAAStar.py
		│          
		├─Search_2D_
		│      
		├─Search_3D
		│     Anytime_Dstar3D.py
		│     Astar3D.py
		│     bidirectional_Astar3D.py
		│     Dstar3D.py
		│     DstarLite3D.py
		│     env3D.py
		│     LP_Astar3D.py
		│     LRT_Astar3D.py
		│     plot_util3D.py
		│     queueL.py
		│     RTA_Astar3D.py
		│     utils3D.py
		│          
		└─Search_3D_
```
# Outdoor obstacle avoidance
Custom routes and obstacle areas
rrt_2D Path optimization effect chart
![116529610-c171db00-a90f-11eb-9506-8b2d7979d1f1](https://user-images.githubusercontent.com/35774039/159817489-e727f83b-0fc4-4bee-b6ba-e1f29495b488.png)
![116529702-cf276080-a90f-11eb-951e-f6e5ccd3f7ab](https://user-images.githubusercontent.com/35774039/159817497-6f728ad4-3b7a-4314-92e4-59aee86dc325.png)
# Indoor obstacle avoidance
Because the internal structure has the characteristics of narrow space and many distractions, the degree of route planning at this time is more focused on the effect of three-dimensional obstacle avoidance, and the map is meaningless.
![118637888-dd7ae500-b808-11eb-916b-530b1d8393ee](https://user-images.githubusercontent.com/35774039/159817578-bdca69a9-6b55-4802-b413-be9cb8d65b2f.gif)
# rrt_3D_Indoor obstacle avoidance renderings
![118637946-e966a700-b808-11eb-8006-f21af8f695be](https://user-images.githubusercontent.com/35774039/159817633-5ae0c8b9-413c-4f27-af6f-6687db218a69.png)
![118637923-e4a1f300-b808-11eb-83f0-5c9137af4a1a](https://user-images.githubusercontent.com/35774039/159817639-edbe120e-9496-4024-aabd-8753ec2ed06c.png)
![116529702-cf276080-a90f-11eb-951e-f6e5ccd3f7ab](https://user-images.githubusercontent.com/35774039/159817674-bfe92668-8769-46da-acd2-edd81bfcd147.png)
![116529610-c171db00-a90f-11eb-9506-8b2d7979d1f1](https://user-images.githubusercontent.com/35774039/159817687-9a26cef0-6f72-400b-983c-6eef06f532d1.png)





