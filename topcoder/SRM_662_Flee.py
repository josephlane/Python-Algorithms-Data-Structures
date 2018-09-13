
Problem Statement
    
You are a point in the plane. You start at the coordinates (0, 0) and you want to flee far away, to the coordinates (10^100, 0). Your path can be any continuous curve.  You are given tuple (integer)s x and y. For each valid i, there is a guard standing on the point with coordinates (x[i], y[i]). The guards do not move. You want to avoid the guards as much as possible.  Formally, for any point P in the plane, we define its safety level S(P) as the distance to the closest guard. The safety level of a path is the minimum safety level of a point on the path. Find a path with the largest possible safety level and return its safety level.
Definition
    
Class:
Flee
Method:
maximalSafetyLevel
Parameters:
tuple (integer), tuple (integer)
Returns:
float
Method signature:
def maximalSafetyLevel(self, x, y):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Notes
-
Your return value must have an absolute or a relative error smaller than 1e-9.
Constraints
-
x will contain between 1 and 3 elements, inclusive.
-
x and y will contain the same number of elements.
-
Each element in x and y will be between -1,000 and 1,000, inclusive.
Examples
0)

    
{1,1,-7}
{5,-5,0}
Returns: 5.0
You can go from (0, 0) to (10^100, 0) directly. The safety level of this path is 5, because when you are at (1, 0) the distance to the closest guard is 5.
1)

    
{1,1}
{-5,-5}
Returns: 5.0990195135927845
One optimal path is the following polyline: (0, 0) -- (-100, 0) -- (-100, -10000) -- (10^100, 0).
2)

    
{1,1,-8}
{5,-5,0}
Returns: 5.0990195135927845

3)

    
{232,312,-432}
{498,-374,24}
Returns: 432.6661530556787

4)

    
{0}
{0}
Returns: 0.0
Each valid path starts in the point (0, 0). This point contains a guard and therefore its safety level is 0. Hence, the safety level of any valid path will be 0.
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.