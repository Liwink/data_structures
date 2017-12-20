# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self.size = 0

    def ReadData(self):
        self.size = int(input())
        self._data = [int(s) for s in input().split()]
        assert self.size == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def SiftDown(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        maxIndex = i
        if r < self.size and self._data[r] < self._data[maxIndex]:
            maxIndex = r
        if l < self.size and self._data[l] < self._data[maxIndex]:
            maxIndex = l
        if i != maxIndex:
            self._swaps.append((i, maxIndex))
            self._data[i], self._data[maxIndex] = self._data[maxIndex], self._data[i]
            self.SiftDown(maxIndex)

    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        for i in reversed(range(int(self.size / 2))):
            self.SiftDown(i)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
