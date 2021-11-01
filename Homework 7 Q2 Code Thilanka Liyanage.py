import numpy as np
import matplotlib.pyplot as plt
lamexact=[]
dellam = []
n=[]
j=0
for j in range(2,101,1):
    k=0
    lamtot=0
    lamav=0
    for k in range(100):
        A= np.random.uniform(-1,1,size=(j,j))
        B= np.triu(A)+np.triu(A,1).transpose()
        D,V = np.linalg.eig(B)
        D.sort()
        L = len(D)
        lam = (D[L-1]-D[0])/(j-1)    
        lamtot = lamtot + lam
    lamav = lamtot/100
    dellam.append(lamav)
    n.append(j)
    func = 4/np.sqrt(3*n[j-2])
    lamexact.append(func)
print('lam exact =')
print(lamexact)
print('dellam =')
print(dellam)
print('n =')
print(n)

plt.plot(n,dellam)
plt.plot(n,lamexact)
plt.legend(["Avg mean level","Exact mean level"])
plt.xlabel("order (n)")
plt.ylabel("Average mean level spacing")
plt.title("Average mean level spacing vs. order")
plt.show()

