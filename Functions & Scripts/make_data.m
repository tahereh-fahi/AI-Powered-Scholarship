%% Download compustat variables not downloaded as part of the Assaying Anomalies install

clear
clc

% Get numerators 
opts = detectImportOptions('Mining_Variable_List.xlsx', 'Sheet', 'Numerators');
numer = readtable('Mining_Variable_List.xlsx', opts);

% And denominators
opts = detectImportOptions('Mining_Variable_List.xlsx', 'Sheet', 'Denominators');
denom = readtable('Mining_Variable_List.xlsx', opts);

% WRDS username and password
username = usernameUI(); 
pass = passwordUI();

% Find the ones we need to download
nNumer = height(numer); 
nDenom = height(denom);

dataPath = '../Data/COMPUSTAT/'; 

numerToDwnld = false(nNumer, 1);
denomToDwnld = false(nDenom, 1);

% Numerators
for i =1:nNumer
    if ~exist([dataPath,char(numer.acronym(i)),'.mat']) & ~strcmp(char(numer.acronym(i)), 'me_datadate')
        numerToDwnld(i) = true;
    end
end

% Denominators
for i =1:nDenom
    if ~exist([dataPath,char(denom.acronym(i)),'.mat']) & ~strcmp(char(denom.acronym(i)), 'me_datadate')
        denomToDwnld(i) = true;
    end
end

% Download if any
dataToDwnld = unique([numer.acronym(numerToDwnld); denom.acronym(denomToDwnld)]');

% Adjust the DO variable to avoid errors with special-case DO in SQL
isDO = strcmpi(dataToDwnld, 'DO');
dataToDwnld(isDO) = {'"do"'};

if ~isempty(dataToDwnld)
    getCOMPUSTATAdditionalData(username, pass, dataToDwnld, 'annual');
end


%% Create me_datadate

clear
clc

if ~exist('./Data', 'dir')
    mkdir('Data'); % Create the folder if it doesn't exist
    addpath('./Data');
end

load me
load dates

% Assign December me to June to line up with fiscal-year-ends for most
% companies
me_datadate = lag(me, 6, nan);
juneInd = dates - 100*floor(dates/100) == 6;
me_datadate(~juneInd,:) = nan;

% Save the variable in the 'Data' subfolder
save(fullfile('.','Data', 'me_datadate.mat'), 'me_datadate');
