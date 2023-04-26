from SimplexMethodTool import SimplexMethodTool

table = """
x1  x2 x3 x4 R1 R2 x5  Solution
r -30/100 -90/100 0 0 -100 -100 0 0
R1 1 1 -1 0 1 0 0 800
R2  21/100 -30/100 0 0 0 0 1 0
x5 3/100 -1/100 0 -1 0 1 0 0
""" 
simplex = SimplexMethodTool(table)