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

-https://www.facebook.com/profile.php?id=100002145048612-
-https://www.instagram.com/farkadadnan/
-https://www.linkedin.com/in/farkad-adnan-499972121/

 <p>
 <a href='https://mobile.twitter.com/farkadadnan'>
        <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/farkadadnan?label=%40farkadadnan&style=social" alt='Twitter' align="center"/>
    </a>
</p>

from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

print("""
   
"""

)

connection_string ='127.0.0.1:14550' #'tcp:127.0.0.1:5760'  #

vehicle = connect(connection_string, wait_ready=True)


    while not vehicle.is_armable:
        print(" 无人机正在初始化，请等待......")
        time.sleep(1)

    print("无人机初始化完毕，电机开始旋转")
    vehicle.mode = VehicleMode("GUIDED")
  
    vehicle.armed = True


ground_speed_Q = input("是否设置地速[y/n]： ")

num = 1
record = []
while True:

vehicle.mode = VehicleMode("RTL")
time.sleep(3)
vehicle.mode = VehicleMode("GUIDED")
vehicle.mode = VehicleMode("RTL")

filename = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + '.txt'
with open(filename, 'a') as file_object:
    for i in range(len(record)):
        file_object.write(str(i))
        file_object.write("    ")
        file_object.write(str(record[i]))
        file_object.write("\n")
vehicle.close()


