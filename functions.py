import h5py
import os

def get_cosmology(filename,sim=None,time=None,scalef=True):

    # function that gets the cosmology from the header of hdf5 files

    # input:
    # filename: hdf5 file (whole path) whose header contains the cosmology parameters

    # output:
    # h0,omega_M,omega_L,omega_B,ns,sigma8
    # sim=True: simulation,boxsize,units_boxsize,particle_number,particle_mass,units_particle_mass
    # time=True: snap,redshift
    # scale=True (needs time=True): scale_f
    
    f = h5py.File(filename,"r")

    global h0,omega_M,omega_L,omega_B,ns,sigma8
    h0 = float(f['header'].attrs['h0'])
    omega_M = float(f['header'].attrs['omega_M'])
    omega_L = float(f['header'].attrs['omega_L'])
    omega_B = float(f['header'].attrs['omega_B'])
    ns = float(f['header'].attrs['ns'])
    sigma8 = float(f['header'].attrs['sigma8'])

    if sim == True:

        global simulation,boxsize,units_boxsize,particle_number,particle_mass,units_particle_mass
        simulation = f['header'].attrs['simulation']
        boxsize = int(f['header'].attrs['boxsize'])
        units_boxsize = f['header'].attrs['units_boxsize']
        particle_number = int(f['header'].attrs['particle_number(1D)'])
        particle_mass = float(f['header'].attrs['particle_mass'])
        units_particle_mass = f['header'].attrs['units_particle_mass']
        
    if time == True:

        global snap,redshift
        snap = int(f['header'].attrs['snapshot'])
        redshift = float(f['header'].attrs['redshift'])

        if scalef == True:

            global scale_f
            var = filename.split('hlist_')[1]
            scale_f = float(var.split('_def')[0])

    f.close()
    return


def generic_function(model,sim,snap,proper=None,SAM=None,h0,minval,maxval,npoints,outfile):

    vol = np.arange(0,64,1)
    mhhalo = np.array([]) ; mhalo = np.array([]) ; type_gal = np.array([])

    # histogram
    a = np.linspace(minval,maxval,npoints) # bin positions (edges)
    c = (a[0:-1]+a[1:])/2 # centers
    w = (-a[0]+a[1]) # width
    array = 0
    
    for i in vol:
        
        if SAM == galform:

            gal_file = "/home/chandro/Galform_Out/v2.7.0/stable/"+sim+"/"+model+"/iz"+str(snap)+"/ivol"+str(i)+"/galaxies.hdf5"
            f = h5py.File(gal_file,"r")
            
            if proper == HMF:

                mhhalo = f["Output001/mhhalo"][()]
                mhalo = f["Output001/mhalo"][()]
                type_gal = f["Output001/type_gal"][()]
                f.close()
                ind = np.logical_and(mhhalo==mhalo,type_gal==0) # galaxies formed in host haloes and that are central
                H, bins = np.histogram(np.log10(mhhalo[ind]),a) # in Msun/h
                array += H
                
            elif proper == LF:


        elif SAM == shark:

            if proper == HMF:
                
            elif proper == LF:


    ind = np.where(array > 0)
    # save data
    tofile = zip(c[ind],c[ind]-w/2,c[ind]+w/2,array[ind]/(w*(boxsize)**3))
    with open(outfil, 'w') as outf: # written mode (not appended)
        outf.write('# log(Mh/Msun)_midpoint, log(Mh/Msun)_low, log(Mh/Msun)_high, Density of haloes/dlog(Mh/Msun)_midpoint\n')
        np.savetxt(outf,list(tofile))#,fmt=('%.5f'))
        outf.closed

    return
