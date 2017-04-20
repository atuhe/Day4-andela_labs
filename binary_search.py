class BinarySearch(list):
    def __init__(self, a, b):
        self.array = [x for x in range(b, a * b, b)]
        self.length = len(self.array)

    def search(self, param):
        count = 0
        print(self.array)

        array = self.array
        first = 0
        last = len(array)

        while first < last:
            try:
                count += 1
                mid = first + (last - first) // 2
                value = self.array[mid]
                if param == value:
                    return {"count": count, "index": mid}
                elif param > value:
                    if first == mid:
                        break
                    first = mid + 1
                else:
                    last = mid - 1
            except:
                break
        return {"count": count, "index": -1}
        # print(self.array)

mySearch = BinarySearch(120, 10)
print(mySearch.search(50))