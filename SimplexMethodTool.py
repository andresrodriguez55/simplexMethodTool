from Value import Value
from NumericalOperations import NumericalOperations

class SimplexMethodTool:
    def __init__(self, stringTable):
        self.stringTable = stringTable
        self.numericalOperations = NumericalOperations()
        self.__initializeTable()
        self.execute()
    
    def __initializeTable(self):
        lines = self.stringTable.strip().split("\n")
        
        self.columnNames = lines[0].replace('|', ' ').split()
        self.rowNames = []
        self.valueTable = []

        toIterate = lines[1:]
        if "-+" in toIterate[0]:
            toIterate = toIterate[1:]

        for line in lines[1:]:
            lineValues = line.split()
            self.rowNames.append(lineValues[0].replace('|', ' ').split("\t")[0])
            row = []
            for col in lineValues[1:]:
                values = col.split("\t")[0].split('/')
                if(len(values) == 2):
                    row.append(Value(int(values[0]), int(values[1])))
                else:
                    row.append(Value(int(values[0]), 1))
                
            self.valueTable.append(row)
  
    def __printTable(self):
        stringValues = [[repr(value) for value in row] for row in self.valueTable]
        
        max_row_name_length = max(len(name) for name in self.rowNames)

        col_widths = [max(len(repr(val)) for val in column) for column in zip(self.columnNames, *stringValues)]

        print(f"{'  ' * (max_row_name_length + 1)}{' | '.join(f'{name:<{col_widths[i]}}' for i, name in enumerate(self.columnNames))}")

        print(f"{'  ' * (max_row_name_length + 1)}{'-+-'.join('-' * col_widths[i] for i in range(len(self.columnNames)))}")

        for i, row in enumerate(stringValues):
            row_str = " | ".join(f"{' ' * (col_widths[j] - len(str(row[j])))}{row[j]}" for j in range(len(row)))
            print(f"{self.rowNames[i]:<{max_row_name_length}} | {row_str}")
        print()
    
    def __sumSubtractionHelper__(self, array1, array2, operation):
        newRow = []
        for index, valueOperand1 in enumerate(array1):
            valueOperand2 = array2[index] 
            newValueDenominator = valueOperand1.denominator * valueOperand2.denominator
            newValueNumerator =  valueOperand1.numerator * valueOperand2.denominator
            if operation == '+':
                newValueNumerator += valueOperand2.numerator * valueOperand1.denominator
            else:
                newValueNumerator -= valueOperand2.numerator * valueOperand1.denominator

            newRow.append(Value(newValueNumerator, newValueDenominator))

        return newRow
    
    def __sum__(self, array1, array2):
        return self.__sumSubtractionHelper__(array1, array2, "+")
    
    def __subtraction__(self, array1, array2):
        return self.__sumSubtractionHelper__(array1, array2, "-")
    
    def __mul__(self, array, constant):
        value = constant.split('/')
        numerator = int(value[0])
        denominator = 1 
        if len(value) > 1:
            denominator = int(value[1])
        
        return [Value(val.numerator * numerator, val.denominator * denominator) for val in array]

    def matrixOperation(self, string):
        operation = string.split()
        if operation[0] == "rename":
            index = self.rowNames.index(operation[1])
            self.rowNames[index] = operation[2]
            return
        
        destinationIndex = int("".join(c for c in operation[0] if c.isdigit())) - 1

        result = [0 for x in range(len(self.valueTable[destinationIndex]))]
        isPositive = True
        for term in operation[2:]:
            if term == '+':
                isPositive = True
                continue
            if term == '-':
                isPositive = False
                continue
            
            values = term.split('*')
            if len(values) == 1:
                operandIndex = int("".join(c for c in values[0] if c.isdigit())) - 1
                result = self.__sum__(result, self.valueTable[operandIndex]) if isPositive else self.__subtraction__(result, self.valueTable[operandIndex])
            else:
                operandIndex = int("".join(c for c in values[1] if c.isdigit())) - 1
                toSum = self.__mul__(self.valueTable[operandIndex], values[0])
                result = self.__sum__(result, toSum) if isPositive else self.__subtraction__(result, toSum)
        
        self.valueTable[destinationIndex] = result

    def execute(self):
        while(True):
            try:
                self.__printTable()
                operation = input()
                if operation == '\n':
                    continue
                if operation == "end":
                    return
                self.matrixOperation(operation)
            except:
                continue