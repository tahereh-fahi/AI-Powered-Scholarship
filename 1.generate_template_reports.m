clear
clc

% Start with the default path
restoredefaultpath; 

% Path to the MATLAB asset pricing package
matlabPackagePath = '../'; 
paperPackagePath = './'; 

% Add the relevant folders (with subfolders) to the path
addpath(genpath([matlabPackagePath, 'Data']))
addpath(genpath([matlabPackagePath, 'Functions']))
addpath(genpath([matlabPackagePath, 'Library Update']))
addpath(genpath(paperPackagePath));

% Navigate to the paper folder
cd(paperPackagePath)

%% Download COMPUSTAT variables & make me_datadate

run('make_data.m');

%% Run 30K univariate sorts

run('run_data_mining.m');

%% Organize results (results.mat)

run('organize_results.m');

%% Filter the results (printRes.mat)

run('filter_results.m');

%% Run protocol on filtered signals

run('run_protocol.m');