from typing import Callable, List
import math

#DO NOT MAKE UNNECESSARY CHANGES
class DistanceFuncs:

  def calc_distance(self, point_a: List[float], point_b: List[float], dist_func)->float:
    return dist_func(point_a, point_b)
      
  @staticmethod
  def euclidean(point_a: List[float], point_b: List[float])->float:
    
    """Calculates Euclidean Distance between two points Example:
    >>> DistanceFuncs.euclidean([1,1],[1,1])
    0.0"""
 
    return math.dist(point_a, point_b)

  @staticmethod
  def manhattan_distance(point_a: List[float], point_b: List[float]):
    manhattan_dist = 0
    zip_object = zip(point_a, point_b)
   
    for point_a_i, point_b_i in zip_object:
      manhattan_dist += abs(point_a_i-point_b_i)
    
    return manhattan_dist
  
 
    
    
  @staticmethod
  def jaccard_distance(point_a: List[float], point_b: List[float]):
    point_a_size = len(point_a) 
    point_b_size = len(point_b)
      
    intersect = list(set(point_b) & set(point_a))
    intersect_size = len(intersect)
      
    jaccard_index = intersect_size  / (point_a_size + point_b_size - intersect_size)  
    jaccard_dist = 1 - jaccard_index 

    return jaccard_dist


def main():
  point_a = [2.4, 3.1, 7.8]
  point_b = [3.1, 4.7, 8.3]

  distance = DistanceFuncs()
  print("Point a coordinates:", point_a)
  print("Point b coordinates:", point_b)
  print("Euclidean Distance:",distance.calc_distance(point_a, point_b, DistanceFuncs.euclidean))
  print("Manhattan Distance:",distance.calc_distance(point_a, point_b, DistanceFuncs.manhattan_distance))
  print("Jaccard_distance:",distance.calc_distance(point_a, point_b, DistanceFuncs.jaccard_distance))




if __name__ =="__main__":
  main()