from SimplexMethodTool import SimplexMethodTool

text = """
    x1  x2  x3  R1  R2  x4  Solution
z   -4  -1  0   -100 -100 0 0
R1 3 1 0 1 0 0 3
R2 4 3 -1 0 1 0 6
x4 1 2 0 0 0 1 4
""" 
simplex = SimplexMethodTool(text)

"""
Operations
    rename {rowName} {columnName}
    A{rowNumber} = {{, -}numerator/denominator}*A{rowNumber} {+, -} {{, -}numerator/denominator}*A{rowNumber} {+, -} ...
"""
