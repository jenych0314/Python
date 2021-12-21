def FindAll(string, target):
    indexes = []
    index = -1
    while True:
        index = string.find(target, index + 1)
        if index == -1:
            return indexes
        indexes.append(index)
        return indexes