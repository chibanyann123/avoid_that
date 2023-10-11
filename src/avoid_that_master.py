#!/usr/bin/env python3
#-*-coding:utr-8 -*-

import rospy
import smach
from happymimi_navigation.srv import NaviLocation
from enter_room.srv import EnterRoom

class Door(samch.State):
    def __init__(self):
        smach.State __init__(self,outcomes=['Door_end'])
        self.enter_room = rospy.ServiceProxy('/enter_room_server',EnterRoom)
    
    def execute(self):
        self.enter_room(0.5,0.3)
        return 'Door_end'
    

class navi(samch.State):
    def __init__(self):
        smach.State __init__(self,outcomes=['Navi_end'])
        self.nav = rospy.ServiceProxy('/navi_location_server',NaviLocation)
    
    def execute(self):
        self.navi.nav = ('living')
        return 'Navi_end'


if __name__=='__main__':
   sm  = smach.StateMachine(outcomes = ['fmm_end'])
   sm.userdata.navi_num = 0

   with sm:
       smach.StateMachine.add("Door",
                              Door(),
                              transitions = {"Door_end":"Navi"})
       
       smach.StateMachine.add("Navi",
                              Navi(),
                              transitions = {"Navi_end":"fmm_end"})
       
