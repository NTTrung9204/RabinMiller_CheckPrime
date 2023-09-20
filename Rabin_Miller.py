import time, sys
sys.setrecursionlimit(10000)
class RABIN_MILER:
    def __init__(self, testCase = 0, checkPrime = 0) -> None:
        self.checkPrime = checkPrime
        self.testCase = testCase

    def CHECK_RABIN_MILER__MULTI(self) -> bool:
        while self.testCase:
            self.checkPrime = int(input())
            if self.RABIN_MILER(self.checkPrime) : print("YES")
            else : print("NO")
            self.testCase -= 1

    def CHECK_RABIN_MILER__SINGLE(self) -> bool:
        if self.RABIN_MILER(self.checkPrime) : print("YES")
        else : print("NO")

    def MOD(self, a, n, m) -> bool:
        if n == 0 : return 1
        if n == 1 : return a%m
        if n % 2 == 0 : return self.MOD(a,n//2,m)**2%m
        return (self.MOD(a,n//2,m)**2%m)*(a%m)%m

    def TESTPRIME(self, n, a) -> bool:
        mod = n
        k = 0
        n = n - 1
        while n % 2 == 0:
            n = n//2
            k+=1
        m = n
        if self.MOD(a, m, mod) == 1 : return 1
        for i in range(k):
            power = self.MOD(a, 2**i, mod)
            if self.MOD(power, m, mod) == -1 or self.MOD(power, m, mod) == mod - 1 : return 1
        return 0

    def RABIN_MILER(self, n) -> bool:
        if n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13 or n == 17 or n == 19 or n == 23 or n == 29 or n == 31 or n == 37 : return 1
        if n < 37 : return 0
        checkList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        for i in checkList:
            if self.TESTPRIME(n, i) == 0 : return 0
        return 1

if __name__ == "__main__":
    checkNumber = 964443901723683675928496377997738516879759872140652468493523970213510160435352711586114670517165110126134933601695265955345463828864542182706265820453369581204976816065778526601508164968183212502279186049843850453984063622314801512863946716004181271030099407537558153908663501252208660375037562282333
    print(len(str(checkNumber)))
    start_time = time.time()

    RABIN_MILER(0, checkNumber).CHECK_RABIN_MILER__SINGLE()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Runing time: {elapsed_time} s")

