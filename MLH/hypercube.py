from pyDOE import *
import numpy as np
import matplotlib.pylab as plt

# code to generate the Maximin Latin Hypercube in the parameter space
# in order to train the emulator:
# 250 models for 3 parameters (MSc thesis)

params = 3 # how many params
runs = 250 # how many points in parameter space

# generate the data
lhd = lhs(params,samples=runs,criterion="maximin")
#lhd = lhs(100,criterion="maximin")
print(np.shape(lhd))
print(lhd)

# plot the data
fig,ax  = plt.subplots()
ax.plot(lhd[:,0]*2,lhd[:,1]*500+100,'.b')
#ax.axvline(x=1.15)
#ax.axhline(y=3.58)
plt.xlabel(r'$\alpha_{cool}$')
plt.ylabel('$V_{SN}$')
ax.set_xlim(0,2)
ax.set_ylim(100,600)
#xgrid = np.linspace(0.2,1.2,runs+1)
#ygrid = np.linspace(1,4,runs+1)
#ax.set_xticks(xgrid,minor=True)
#ax.set_xticks([0.2,0.4,0.6,0.8,1,1.2],minor=False)
#ax.set_yticks(ygrid,minor=True)
#ax.set_yticks([1,2.5,4],minor=False)
#ax.grid(which="major")
#ax.grid(which="minor")
ax.set_box_aspect(1)
plt.show()

fig,ax  = plt.subplots()
ax.plot(lhd[:,0]*2,lhd[:,2]+0.5,'.b')
#ax.axvline(x=1.15)
#ax.axhline(y=3.58)
plt.xlabel(r'$\alpha_{cool}$')
plt.ylabel('$F_{stab}$')
ax.set_xlim(0,2)
ax.set_ylim(0.5,1.5)
#xgrid = np.linspace(0.2,1.2,runs+1)
#ygrid = np.linspace(1,4,runs+1)
#ax.set_xticks(xgrid,minor=True)
#ax.set_xticks([0.2,0.4,0.6,0.8,1,1.2],minor=False)
#ax.set_yticks(ygrid,minor=True)
#ax.set_yticks([1,2.5,4],minor=False)
#ax.grid(which="major")
#ax.grid(which="minor")
ax.set_box_aspect(1)
plt.show()

fig,ax  = plt.subplots()
ax.plot(lhd[:,1]*500+100,lhd[:,2]+0.5,'.b')
#ax.axvline(x=1.15)
#ax.axhline(y=3.58)
plt.xlabel('$V_{SN}$')
plt.ylabel('$F_{stab}$')
ax.set_xlim(100,600)
ax.set_ylim(0.5,1.5)
#xgrid = np.linspace(0.2,1.2,runs+1)
#ygrid = np.linspace(1,4,runs+1)
#ax.set_xticks(xgrid,minor=True)
#ax.set_xticks([0.2,0.4,0.6,0.8,1,1.2],minor=False)
#ax.set_yticks(ygrid,minor=True)
#ax.set_yticks([1,2.5,4],minor=False)
#ax.grid(which="major")
#ax.grid(which="minor")
ax.set_box_aspect(1)
plt.show()

# 3D projection
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(lhd[:,0]*2,lhd[:,1]*500+100,lhd[:,2]+0.5, marker='.')
ax.set_xlabel(r'$\alpha_{cool}$')
ax.set_ylabel('$V_{SN}$')
ax.set_zlabel('$F_{stab}$')
plt.show()

# save the data
#outfile = '/home/chandro/emulator/tfm/hypercube_'+str(params)+'p_'+str(runs)+'.dat'
##outfile = '/home/chandro/emulator/tfm/input.dat'
#tofile = zip(lhd[:,0]*2,lhd[:,1]*500+100,lhd[:,2]+0.5)
#with open(outfile,'w') as outf:
#    outf.write('# alpha_cool, V_SN, f_stab\n')
#    np.savetxt(outf,list(tofile))
#    outf.closed
#
