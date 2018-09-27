class InputReader:
    # read the whole file and create object
    def __init__(self,input_file_name):
        with open(input_file_name) as file:
            data = file.readlines()
        self.input_file = data

    def InterpretFile(self):
        separator_counter = 0
        for i in self.input_file:
            if i[0] == '#':
                separator_counter += 1
            else:
                if separator_counter == 1:
                    self.AddItem(i)
                elif separator_counter == 2:
                    self.AddBag(i)
                elif separator_counter == 3:
                    self.AddFittingLimit(i)
                elif separator_counter == 4:
                    self.AddUnaryInclusive(i)
                elif separator_counter == 5:
                    self.AddUnaryExclusive(i)
                elif separator_counter == 6:
                    self.AddBinaryEqual(i)
                elif separator_counter == 7:
                    self.AddBinaryNotEqual(i)
                elif separator_counter == 8:
                    self.AddMutualInclusive(i)

    def AddItem(self,line):
        item, weight = line.split()

    def AddBag(self,line):
        Bag, capacity = line.split()

    def AddFittingLimit(self,line):
        lower_limit, upper_limit = line.split()

    def AddUnaryInclusive(self,line):
        ui = line.split()
        item = ui[0]
        bags = ui[1:]

    def AddUnaryExclusive(self,line):
        ue = line.split()
        item = ue[0]
        bags = ue[1:]

    def AddBinaryEqual(self,line):
        item1, item2 = line.split()

    def AddBinaryNotEqual(self,line):
        item1, item2 = line.split()

    def AddMutualInclusive(self,line):
        item1, item2, bag1, bag2 = line.split()


inpuuut = 'input1.txt'
reader = InputReader(inpuuut)
reader.InterpretFile()