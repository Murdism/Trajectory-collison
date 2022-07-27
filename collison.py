import numpy as np
import sympy 

class trajectory:
    def __init__(self,num_points):
        dimensions = (num_points, 3)
        self.points = np.zeros(dimensions)
        self.index = 0
        
    def add_point(self,point):
        self.points[self.index]=point
        self.index += 1
    def add_trajectory(self,trajectory):
        self.points = np.array(trajectory)
        self.index= self.points.shape[0]-1
    def print_trajectory(self):
        print(self.points)

    def compare_trajectory(self,trajectory):
        found = False
        for i,pointa in enumerate (self.points):
            for j,pointc in enumerate (trajectory.points):
                # if (self.compare_points(pointa,pointb)):
                #     print("Lines intersect!")
                #     break

                if (i < self.index and j < trajectory.index):
                    pointb = self.points[i+1]
                    pointd = trajectory.points[j+1]
                    soln = list(self.compare_points(pointa,pointb,pointc,pointd))
                    if (len(soln)!=0):
                        print("Lines intersect!")
                        print(soln)
                        found= True
        if not found:
            print("Lines do not intersect!")
                
    
    def compare_points(self,pointa,pointb,pointc,pointd):
        p1= sympy.Point (pointa[0],pointa[1])
        p2= sympy.Point (pointb[0],pointb[1])
        p3= sympy.Point (pointc[0],pointc[1])
        p4= sympy.Point (pointd[0],pointd[1])
        seg1 = sympy.Segment(p1,p2)
        seg2 = sympy.Segment(p3,p4)
     
        return (seg1.intersection(seg2))
      


arr=[[3,0],[0,4],[-1,0]]
arr2= [[4,2],[2,1],[2,4]]
traj1= trajectory(2)
traj2= trajectory(2)
traj1.add_trajectory(arr)
traj2.add_trajectory(arr2)
traj1.compare_trajectory(traj2)


