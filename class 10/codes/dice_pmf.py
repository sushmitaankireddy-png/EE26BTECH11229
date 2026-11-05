# The implementation and plotting scripts are adapted from: \\
# {\hypersetup{urlcolor=blue}\url{https://github.com/gadepall/ncert-probability/tree/master/codes/sum}}
import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

#Sample size
simlen = 10000
#Possible outcomes
n = range(2,13)
# Generate X1 and X2
y = np.random.randint(1,7, size=(2, simlen))

#Generate X
X = np.sum(y, axis = 0)
#Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)
#Simulated probability
psim = counts/simlen
#Theoretical probability
n1 = np.arange(2,8)
n2 = np.arange(8,13)
panal1 = n1 - np.ones(6)
panal2 = 13*np.ones(5) - n2
panal = np.concatenate((panal1,panal2),axis=None)/36

#Plotting
plt.stem(n,psim, linefmt='C0-', markerfmt='C0o', label='Simulation')
plt.stem(n,panal, linefmt='C1-', markerfmt='C1o', label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()

#If using termux
#plt.savefig('figs/dice_pmf.pdf')
plt.savefig('figs/dice_pmf.png')
#subprocess.run(shlex.split("termux-open figs/dice_pmf.pdf"))
#else
plt.show()
