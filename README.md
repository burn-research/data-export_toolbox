# Toolbox for exporting simulation datasets

In this repo you can find some utilities to export/download data from Fluent and OpenFOAM simulations. 

## OpenFOAM data

In the openfoam directory, there is a pyhton script that can be used to parse the results of the simulation. It has to be submitted as a batch job (there is an example of a shell script to submit the job).

To run the script, you have to create a virtual environment with python, numpy and gzip. The virtual environment can be created by installing miniconda on your account on the cluster.

# Fluent
In the fluent directory there is a bash file for export/download data from Fluent simulations. 

On line 14 is the list of features to export. file_path should be the path to a txt file with the list of simulation paths to export. There is an example in the fluent directory. Note that this file is for 2D simulations with Ansys/R2019R3, if this is not your case adjust lines 20-21 accordingly. 

The bash file creates a csv file for each simulation that can be read with the pandas library in python. 
