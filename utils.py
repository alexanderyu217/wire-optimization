from xlrd import*

def get_worksheet(filename):
    """
    Opens the spreadsheet of name FILENAME and returns the first sheet.
    """
    xl_in = open_workbook(filename)
    return xl_in.sheet_by_index(0)

def get_cell(worksheet, row, col):
    """
    Returns the value stored in the worksheet at (ROW, COL).
    """
    return worksheet.cell_value(row, col)

def get_data(filename):
    """
    Parses the spreadsheet of name FILENAME and returns a 2D array.
    array[row][col] is the value of the spreadsheet's first sheet at (ROW, COL)
    """
    converted = []
    worksheet = get_worksheet(filename)
    for row in range(worksheet.nrows):
        converted.append([])
        col = 0
        elem = get_cell(worksheet, row, col)
        while (elem):
            converted[row].append(elem)
            col += 1
            if col < worksheet.ncols:
                elem = get_cell(worksheet, row, col)
            else:
                elem = None
    return converted

class PriorityQueue:
    """
    Naive implementation of the priority queue.
    """

    def __init__(self, lst):
        self.data = []
        for item in lst:
            self.push(item[0], item[1])
    
    def push(self, data, priority):
        if self.is_empty():
            self.data.append([data, priority])
        else:
            self.data.append([data, priority])
            self.data.sort(key = lambda d: d[1])
    
    def update(self, data, priority):
        if data not in self.data:
            self.push(data, priority)
        else:
            for i in range(len(self.data)):
                if data == self.data[i][0]:
                    self.data[i][1] = priority

    def pop(self):
        return self.data.pop(0)[0]

    def is_empty(self):
        return not len(self.data)

    def top(self):
        return self.data[0][0]

