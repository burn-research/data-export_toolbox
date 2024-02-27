import gzip
import numpy as np

def get_array(path, feature, t, n_cells, zipped):
    # This is hardcoded here but I'm not sure if
    # it's true everytime so modify as needed
    n_line = 21

    if zipped:
        filename = f'{path}/{t:g}/{feature}.gzip'
        with gzip.open(filename) as f:
            lines =  f.readlines()
            array = np.array(lines[n_line:n_line+n_cells], dtype=np.float64)
    else:
        filename = f'{path}/{t:g}/{feature}'
        with open(filename) as f:
            lines =  f.readlines()
            array = np.array(lines[n_line:n_line+n_cells], dtype=np.float64)

    return array

def get_ncells(path, feature, zipped):
    # See line 6
    n_line = 19
    
    if zipped:
        filename = f'{path}/0/{feature}.gzip'
        with gzip.open(filename) as f:
            lines =  f.readlines()
            n_cells = np.int64(lines[n_line])
    else:   
        filename = f'{path}/0/{feature}' 
        with open(filename) as f:
            lines =  f.readlines()
            n_cells = np.int64(lines[n_line])

    return n_cells    

def build_data_matrix(path, ti, tf, dt, features, zipped=False):
    n_timesteps = np.int64((tf-ti)/dt)+1
    timesteps = np.linspace(ti, tf, n_timesteps)
    n_features = len(features)
    n_cells = get_ncells(path, features[0], zipped)
    D = np.empty((n_features*n_cells, n_timesteps))

    for i, f in enumerate(features):
        for j, t in enumerate(timesteps):
            array = get_array(path, f, t, n_cells, zipped)
            D[i*n_cells:(i+1)*n_cells, j] = array

            print(f'Reading {f} file {j+1}/{n_timesteps}       ',
                  flush=True, end='\r')
    
    return D

if __name__ == '__main__':
    # This should be modified as needed
    path_data = '/home/emunoz/simulations/meth_detailed'
    path_save = '/workdir/aprocacci/Data/ICNC2024'
    ti = 0 # Initial time step
    tf = 1 # Final time step
    dt = 1e-3 # Time delta

    # Features to include in the data matrix
    features = ['T', 'CH4', 'CO', 'CO2', 'H2', 'H2O', 'N2', 'O2', 'OH']
    D = build_data_matrix(path_data, ti, tf, dt, features)
    np.save(f'{path_save}/D_f10.npy', D)
