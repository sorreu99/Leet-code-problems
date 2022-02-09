a = [2, 1, 4, 7, 6]

tar = 7


class solution:
    def twosum(self, a, tar):
        d = {}
        for x, y in enumerate(a):
            b = tar-y
            if y not in d:
                d[b] = x

            else:
                return [d[y], x]
        return[]


ex = solution()
b = ex.twosum(a, tar)

print(b)
