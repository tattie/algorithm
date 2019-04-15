
# 模反数
def modreverse(a,n):
    b=1
    while True:
        if (a*b)%n == 1:
            return b
        b += 1


# print(modreverse(11,240))
P=7
Q=41
N=P*Q
M=(P-1)*(Q-1) # N的欧拉函数
E=11 # E需要和M互素
D=131 # D是E的模反数之一

# 指数取模
def expmod(N,E,X):
    result = X
    t = result % N
    for i in range(1, E):
        result = result * t
        result = result % N
    return result
    

def encrypt(N,E,X):
    return expmod(N,E,X)
    
def decrypt(N,D,Y):
    return expmod(N,D,Y)


Y=encrypt(N,E,97)
print(Y)
print(decrypt(N,D,Y))


