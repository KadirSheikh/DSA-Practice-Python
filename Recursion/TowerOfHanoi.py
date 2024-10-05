class Solution:
    def towerOfHanoi(self, n, src, des, aux):
        self.n = n
        self.src = src
        self.des = des
        self.aux = aux

        if n == 1:
            print(f"Move disk 1 from {src} to {des}")
            return
        
        self.towerOfHanoi(n-1, src, aux, des)
        print(f"Move disk {n} from {src} to {des}")
        self.towerOfHanoi(n-1, aux, des, src)
        
mySol = Solution()
n = 3
ans = mySol.towerOfHanoi(n, 'A', 'B', 'C')
print(ans)