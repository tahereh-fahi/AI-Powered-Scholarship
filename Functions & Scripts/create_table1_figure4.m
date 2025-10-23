%% Calculate Table 1: Data Mining Summary - Matching filter_results.m logic
% This script replicates the exact filtering logic used in the paper
% All tests are cumulative and must pass simultaneously

clear; clc;

% Configuration (matching filter_results.m)
stockFilter = 30;
t_cutoff = 1.96;
cmonth_cutoff = 360;
emonth_cutoff = 202412;  % Updated to match your code

% Load the results data
fprintf('Loading results data...\n\n');
if ~exist('results.mat', 'file')
    error('results.mat not found. Please run store_results.m first.');
end
load('results.mat', 'results');

% Table Header
fprintf('================================================\n');
fprintf('Table 1: Data Mining Summary\n');
fprintf('================================================\n\n');


% Panel A: Initial filtering process (with redundant row restored)
fprintf('Panel A: Initial filtering process (separated availability)\n');
fprintf('%-40s %10s %10s\n', 'Filter', '# Signals', '% of Total');
fprintf('%-40s %10s %10s\n', repmat('-', 1, 40), repmat('-', 1, 10), repmat('-', 1, 10));

% Initial set
uniqueNumers = unique(results.numer);
uniqueDenoms = unique(results.denom);
nInitial = 2 * numel(uniqueNumers) * numel(uniqueDenoms);
fprintf('%-40s %10d %10s\n', 'Initial set', nInitial, '');

% Exclude redundant signals (global, keyed by numer/denom/signal)
nonRedundant = unique(results(results.rdndntFlag==false, {'numer','denom','signal'}));
nNonRedundant = height(nonRedundant);
fprintf('%-40s %10d %10s\n', 'Exclude redundant signals', nNonRedundant, '');

% Define the two availability configs used downstream (S2 & S3)
S2_all = results(results.stockFilter==stockFilter & ...
                 results.nPtfs==10 & ismember(results.breaks,{'NYSE'}) & ismember(results.weighting,'value') & ...
                 results.rdndntFlag==false, ...
                 {'numer','denom','signal','endDate','consecutiveDates'});
S2_all = unique(S2_all);

S3_all = results(results.stockFilter==stockFilter & ...
                 results.nPtfs==5 & ismember(results.breaks,{'name'}) & ismember(results.weighting,'value') & ...
                 results.rdndntFlag==false, ...
                 {'numer','denom','signal','endDate','consecutiveDates'});
S3_all = unique(S3_all);

% A.1 Require 30 stocks (series actually exists): ~isnan(consecutiveDates), no date/month screen yet
S2_exist = unique(S2_all(~isnan(S2_all.consecutiveDates), {'numer','denom','signal'}));
S3_exist = unique(S3_all(~isnan(S3_all.consecutiveDates), {'numer','denom','signal'}));
WithStocks = intersect(S2_exist, S3_exist, 'rows');
nWithStocks = height(WithStocks);
fprintf('%-40s %10d %10s\n', 'Require 30 stocks (S2 & S3)', nWithStocks, '');

% A.2 End date only (Dec 2024), cumulative on A.1
S2_end = unique(S2_all(S2_all.endDate==emonth_cutoff, {'numer','denom','signal'}));
S3_end = unique(S3_all(S3_all.endDate==emonth_cutoff, {'numer','denom','signal'}));
EndDateOK = intersect(intersect(WithStocks, S2_end, 'rows'), S3_end, 'rows');
nToEndDate = height(EndDateOK);
fprintf('%-40s %10d %10s\n', 'Require data until 12/2024 (S2 & S3)', nToEndDate, '');

% A.3 Consecutive months only (>=360), cumulative on A.2
S2_mon = unique(S2_all(S2_all.consecutiveDates > cmonth_cutoff, {'numer','denom','signal'}));
S3_mon = unique(S3_all(S3_all.consecutiveDates > cmonth_cutoff, {'numer','denom','signal'}));
BaselineKeys = intersect(intersect(EndDateOK, S2_mon, 'rows'), S3_mon, 'rows');
nBaseline = height(BaselineKeys);
fprintf('%-40s %10d %10.1f%%\n', 'Require 360 months (S2 & S3)', nBaseline, 100.0);

% Panel B (unchanged printing; start from BaselineKeys)
fprintf('\n');
fprintf('Panel B: Cumulative significance criteria (aligned)\n');
fprintf('%-50s %10s %10s\n', 'Criteria', '# Signals', '% of Filtered');
fprintf('%-50s %10s %10s\n', repmat('-', 1, 50), repmat('-', 1, 10), repmat('-', 1, 14));

% S1: quintile, NYSE, EW
S1 = results(results.stockFilter==stockFilter & results.nPtfs==5 & ...
             ismember(results.breaks,{'NYSE'}) & ismember(results.weighting,'equal'), ...
             {'numer','denom','signal','rdndntFlag','txret'});
S1 = unique(S1(S1.rdndntFlag==false & abs(S1.txret)>t_cutoff, {'numer','denom','signal'}));

% S2: decile, NYSE, VW
S2_sig = results(results.stockFilter==stockFilter & results.nPtfs==10 & ...
                 ismember(results.breaks,{'NYSE'}) & ismember(results.weighting,'value'), ...
                 {'numer','denom','signal','rdndntFlag','txret'});
S2_sig = unique(S2_sig(S2_sig.rdndntFlag==false & abs(S2_sig.txret)>t_cutoff, {'numer','denom','signal'}));

% S3: quintile, name, VW
S3_sig = results(results.stockFilter==stockFilter & results.nPtfs==5 & ...
                 ismember(results.breaks,{'name'}) & ismember(results.weighting,'value'), ...
                 {'numer','denom','signal','rdndntFlag','txret'});
S3_sig = unique(S3_sig(S3_sig.rdndntFlag==false & abs(S3_sig.txret)>t_cutoff, {'numer','denom','signal'}));

% S4: quintile, NYSE, VW (ret + alpha)
S4_all = results(results.stockFilter==stockFilter & results.nPtfs==5 & ...
                 ismember(results.breaks,{'NYSE'}) & ismember(results.weighting,'value'), ...
                 {'numer','denom','signal','rdndntFlag','txret','talpha'});
S4_r = unique(S4_all(S4_all.rdndntFlag==false & abs(S4_all.txret)>t_cutoff, {'numer','denom','signal'}));
S4_a = unique(S4_all(S4_all.rdndntFlag==false & abs(S4_all.talpha)>t_cutoff, {'numer','denom','signal'}));

% Cumulative intersections starting from BaselineKeys (availability already satisfied)
C1 = intersect(BaselineKeys, S1, 'rows');
nTest1 = height(C1);
fprintf('%-50s %10d %10.1f%%\n', '+ |t_r(quintile, NYSE, EW)| > 1.96', nTest1, 100*nTest1/nBaseline);

C2 = intersect(C1, S2_sig, 'rows');
nTest2 = height(C2);
fprintf('%-50s %10d %10.1f%%\n', '+ |t_r(decile, NYSE, VW)| > 1.96', nTest2, 100*nTest2/nBaseline);

C3 = intersect(C2, S3_sig, 'rows');
nTest3 = height(C3);
fprintf('%-50s %10d %10.1f%%\n', '+ |t_r(quintile, name, VW)| > 1.96', nTest3, 100*nTest3/nBaseline);

C4 = intersect(C3, S4_r, 'rows');
nTest4 = height(C4);
fprintf('%-50s %10d %10.1f%%\n', '+ |t_r(quintile, NYSE, VW)| > 1.96', nTest4, 100*nTest4/nBaseline);

C5 = intersect(C4, S4_a, 'rows');
nTest5 = height(C5);
fprintf('%-50s %10d %10.1f%%\n', '+ |t_(quintile, NYSE, VW)| > 1.96', nTest5, 100*nTest5/nBaseline);

% Optional close anomalies (cumulative)
nTest6 = NaN;
if exist('finalRes.mat','file')
    load('finalRes.mat','finalRes');
    keys = {'numer','denom','signal'};
    keys = keys(ismember(keys, finalRes.Properties.VariableNames));
    if ~isempty(keys)
        closePass = unique(finalRes(~isnan(finalRes.CloseSpanT) & abs(finalRes.CloseSpanT)>t_cutoff, keys));
        C5_keys = unique(C5(:,keys));
        C6 = intersect(C5_keys, closePass, 'rows');
        nTest6 = height(C6);
        fprintf('%-50s %10d %10.1f%%\n', '+ |t_{Close anomalies (CloseSpan)}| > 1.96', nTest6, 100*nTest6/nBaseline);
    end
end

%% Generate LaTeX code
fprintf('LaTeX Table Code:\n');
fprintf('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n');
fprintf('\\begin{table}[!htbp]\n');
fprintf('\\small\n');
fprintf('\\caption{Data mining summary\\\\\n');
fprintf('\\small{This table outlines the filtering process for the signals chosen to demonstrate the scale of paper generation possible with AI. }}\n');
fprintf('\\label{tab:miningSummary}\n');
fprintf('\\begin{tabularx}{\\linewidth}{lXXXXX}\\hline\n');
fprintf('\\multicolumn{4}{l}{Filter} &  \\# of Signals & \\%% of Filtered \\\\[2pt]\n');
fprintf('\\multicolumn{4}{l}{Initial set} &  %d \\\\[2pt]\n', nInitial);
fprintf('\\multicolumn{4}{l}{Exclude redundant signals}  & %d \\\\[2pt]\n', nNonRedundant);
fprintf('\\multicolumn{4}{l}{Require 30 stocks} &  %s \\\\[2pt]\n', addComma(nWithStocks));
fprintf('\\multicolumn{4}{l}{Require data until 12/2024} &  %s \\\\[2pt]\n', addComma(nToEndDate));
fprintf('\\multicolumn{4}{l}{Require 360 months} &  %s & 100.0\\%%%%  \\\\[2pt]\n', addComma(nBaseline));
fprintf('\\multicolumn{4}{l}{Panel B: Cumulative significance criteria}\\\\[2pt]\n');
fprintf('\\multicolumn{4}{l}{+ $|t_{\\hat r_\\text{(decile, name, EW)}}| > 1.96$} & %s &         %.1f\\%%%% \\\\[2pt]\n', addComma(nTest1), 100*nTest1/nBaseline);
fprintf('\\multicolumn{4}{l}{+ $|t_{\\hat r_\\text{(quintile, name, EW)}}| > 1.96$} & %s &         %.1f\\%%%% \\\\[2pt]\n', addComma(nTest2), 100*nTest2/nBaseline);
fprintf('\\multicolumn{4}{l}{+ $|t_{\\hat r_\\text{(quintile, NYSE, EW)}}| > 1.96$} & %s &        %.1f\\%%%% \\\\[2pt]\n', addComma(nTest3), 100*nTest3/nBaseline);
fprintf('\\multicolumn{4}{l}{+ $|t_{\\hat r_\\text{(quintile, NYSE, VW)}}| > 1.96$} & %s &          %.1f\\%%%% \\\\[2pt]\n', addComma(nTest4), 100*nTest4/nBaseline);
fprintf('\\multicolumn{4}{l}{+ $|t_{\\hat \\alpha_\\text{(quintile, NYSE, VW)}}| > 1.96$} & %s &     %.1f\\%%%% \\\\[2pt]\n', addComma(nTest5), 100*nTest5/nBaseline);
if exist('finalRes.mat', 'file')
    fprintf('\\multicolumn{4}{l}{+ $|t_{\\text{Assay, Close Span}}| > 1.96$} & %s & %.1f\\%%%% \\\\[2pt]\n', addComma(nTest6), 100*nTest6/nBaseline);
end
fprintf('\\hline\n');
fprintf('\\end{tabularx}\n');
fprintf('\\end{table}\n');
fprintf('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n');

% Helper function to add commas to numbers
function str = addComma(num)
    str = sprintf('%d', num);
    str = regexprep(str, '(\d)(?=(\d{3})+(?!\d))', '$1,');
end
%% Save summary
summary = struct();
summary.nInitial = nInitial;
summary.nNonRedundant = nNonRedundant;
summary.nWithStocks = nWithStocks;
summary.nToEndDate = nToEndDate;
summary.nBaseline = nBaseline;
summary.nTest1 = nTest1;
summary.nTest2 = nTest2;
summary.nTest3 = nTest3;
summary.nTest4 = nTest4;
summary.nTest5 = nTest5;

if exist('finalRes.mat', 'file')
    summary.nTest6 = nTest6;
end

save('table1_summary.mat', 'summary');
fprintf('\n Summary saved to table1_summary.mat\n');
fprintf(' Found %d signals passing all alpha criteria\n', nTest5);

%% Make T-stat comparison figure


clear
clc

load finalRes

opts = detectImportOptions('SignalDoc.csv');
data = readtable('SignalDoc.csv', opts);

indFin = (finalRes.CloseSpanT)>1.96;

published = abs(data.T_Stat(ismember(data.PredictabilityInOP, {'1_clear','2_likely'})));
ew        = abs(finalRes.txret(indFin));
vw        = abs(finalRes.txret4(indFin));

% Shared bin edges with bin width = 1 (covering all datasets)
maxX = ceil(max([published; ew; vw]));
edges = 0:1:maxX;

figure;

% --- Subplot 1: EW ---
ax1 = subplot(2,1,1); hold on;
h1 = histogram(published, 'Normalization','probability', 'BinEdges',edges, ...
    'FaceColor','b','FaceAlpha',0.5,'EdgeColor','none');
h2 = histogram(ew,        'Normalization','probability', 'BinEdges',edges, ...
    'FaceColor','r','FaceAlpha',0.5,'EdgeColor','none');
hold off;
xlabel('t-statistics'); ylabel('Frequency');
title('T-statistics on Published vs EW Data-Mined Signals');
legend('Published', 'EW Data-mined');
xlim([edges(1) edges(end)]);

% --- Subplot 2: VW ---
ax2 = subplot(2,1,2); hold on;
h3 = histogram(published, 'Normalization','probability', 'BinEdges',edges, ...
    'FaceColor','b','FaceAlpha',0.5,'EdgeColor','none');
h4 = histogram(vw,        'Normalization','probability', 'BinEdges',edges, ...
    'FaceColor','r','FaceAlpha',0.5,'EdgeColor','none');
hold off;
xlabel('t-statistics'); ylabel('Frequency');
title('T-statistics on Published vs VW Data-Mined Signals');
legend('Published', 'VW Data-mined');
xlim([edges(1) edges(end)]);

% --- Make y-axes the same across both subplots ---
maxY = max([h1.Values, h2.Values, h3.Values, h4.Values], [], 'all');
linkaxes([ax1, ax2], 'y');
ylim([0, maxY]);  % consistent y-axis for both panels

% Increase font size for all text in the figure
set(findall(gcf,'-property','FontSize'),'FontSize',15); % Increase font size for all text

% resize the figure so that it has portrait orientation
set(gcf, 'PaperOrientation', 'portrait'); % Set figure orientation to portrait
set(gca, 'LooseInset', max(get(gca, 'LooseInset'), [0, 0, 0, 0])); % Remove extra space around axes
% Export the figure to a PDF file
exportgraphics(gcf, 'tstat_comp.pdf', 'ContentType', 'vector', 'BackgroundColor', 'none');

