# Toolbox for exporting simulation datasets

In this repo you can find some utilities to export/download data from Fluent and OpenFOAM simulations. 

## OpenFOAM data

In the openfoam directory, there is a pyhton script that can be used to parse the results of the simulation. It has to be submitted as a batch job (there is an example of a shell script to submit the job).

To run the script, you have to create a virtual environment with python, numpy and gzip. The virtual environment can be created by installing miniconda on your account on the cluster.