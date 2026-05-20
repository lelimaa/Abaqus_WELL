% Lendo deslocamento da parede interna do poço (perfil)

clear all
close all
clc

% PATH = 'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_';
PATH = 'C:\Users\juani\Documents\Github\Abaqus_WELL_';
cd(PATH)

filename = 'path_data_all_frames';

data = readtable(filename, 'VariableNamingRule', 'preserve');

instantes_tempo = unique(data.("Time (s)"));
nos_unicos = unique(data.("Node Label"));

% data.Properties.VariableNames = strtrim(data.Properties.VariableNames);

% instantes_tempo = unique(data.Time_s_);
% nos_unicos = unique(data.Node_Label);

num_frames = length(instantes_tempo);
num_nos = length(nos_unicos);

[unq_nodes, idx] = unique(data.("Node Label"));

% profundidades = data.Vertical_Pos_m_(idx);
profundidades = data.("Z Position (m)")(idx);

ref_nos = table(unq_nodes, profundidades, 'VariableNames', {'Label', 'Z'});
ref_nos = sortrows(ref_nos, 'Z', 'descend');

matriz_U1 = zeros(num_nos, num_frames);

for t = 1:num_frames

    dados_frame = data(data.("Time (s)") == instantes_tempo(t), :);

    for n = 1:num_nos

        label_alvo = ref_nos.Label(n);
        idx_valor = dados_frame.("Node Label") == label_alvo;

        if any(idx_valor)
            % valores_temporarios = dados_frame.("U1 Displacement (m)")(idx_valor);
            % matriz_U1(n, t) = valores_temporarios(1);
            % matriz_U1(n, t) = dados_frame.("U1 Displacement (m)")(idx_valor);
            matriz_U1(n, t) = mean(dados_frame.("U1 Displacement (m)")(idx_valor));
        end 
    end 
end 

eixo_tempo = instantes_tempo;
eixo_z = ref_nos.Z;

fprintf('>>> Matriz gerada: %d posições verticais x %d frames.\n' , num_nos, num_frames);

figure()
hold on 
grid on

frames_interesse = [1, round(num_frames/2), num_frames];
cores = lines(length(frames_interesse));
legendas = {'Inicio', '15 Anos', '30 Anos'};

for i = 1:length(frames_interesse)
    idx = frames_interesse(i);

    plot(matriz_U1(:, idx)*1e3, eixo_z, 'Color', cores(i,:), 'LineWidth',2);
end

set(gca, 'YDir', 'reverse')

xlabel('Deslocamento Radial U1 (mm)');
ylabel('Profundidade Z (m)');
title('Evolução do Perfil de Fechamento do Poço');
legend(legendas, 'Location', 'best');
set(gca, 'YDir', 'normal'); % Garante que o topo fique no topo

%% Lendo tensões no casing (perfil)

clear all
% close all
clc

PATH = 'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_';
cd(PATH)

filename = 'casing_stress_all_frames';

data = readtable(filename, 'VariableNamingRule', 'preserve');

instantes_tempo = unique(data.("Time (s)"));
nos_unicos = unique(data.("Node Label"));

% data.Properties.VariableNames = strtrim(data.Properties.VariableNames);

% instantes_tempo = unique(data.Time_s_);
% nos_unicos = unique(data.Node_Label);

num_frames = length(instantes_tempo);
num_nos = length(nos_unicos);

[unq_nodes, idx] = unique(data.("Node Label"));

% profundidades = data.Vertical_Pos_m_(idx);
profundidades = data.("Z Position (m)")(idx);

ref_nos = table(unq_nodes, profundidades, 'VariableNames', {'Label', 'Z'});
ref_nos = sortrows(ref_nos, 'Z', 'descend');

matriz_U1 = zeros(num_nos, num_frames);

for t = 1:num_frames

    dados_frame = data(data.("Time (s)") == instantes_tempo(t), :);

    for n = 1:num_nos

        label_alvo = ref_nos.Label(n);
        idx_valor = dados_frame.("Node Label") == label_alvo;

        if any(idx_valor)
            % valores_temporarios = dados_frame.("U1 Displacement (m)")(idx_valor);
            % matriz_U1(n, t) = valores_temporarios(1);
            % matriz_U1(n, t) = dados_frame.("U1 Displacement (m)")(idx_valor);
            % matriz_U1(n, t) = mean(dados_frame.("U1 Displacement (m)")(idx_valor));
            matriz_U1(n, t) = mean(dados_frame.("Mises (Pa)")(idx_valor));
        end 
    end 
end 

eixo_tempo = instantes_tempo;
eixo_z = ref_nos.Z;

fprintf('>>> Matriz gerada: %d posições verticais x %d frames.\n' , num_nos, num_frames);

figure()
hold on 
grid on

frames_interesse = [1, round(num_frames/2), num_frames];
cores = lines(length(frames_interesse));
legendas = {'Inicio', '15 Anos', '30 Anos'};

for i = 1:length(frames_interesse)
    idx = frames_interesse(i);

    plot(matriz_U1(:, idx)/1e6, eixo_z, 'Color', cores(i,:), 'LineWidth',2);
end

set(gca, 'YDir', 'reverse')

xlabel('Mises (MPa)');
ylabel('Profundidade Z (m)');
title('Evolução do Perfil de Tensão no Revestimento');
legend(legendas, 'Location', 'best');
set(gca, 'YDir', 'normal'); % Garante que o topo fique no topo

%% Lendo tensão no casing em um ponto (base do revestimento)

figure()
plot(instantes_tempo/(60*60*24*365),matriz_U1(end,:)/1e6)
xlabel('time [years]')
ylabel('Stress [MPa]')
grid minor

%% Lendo temperaturas no casing (perfil)

clear all
close all
clc

PATH = 'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_';
cd(PATH)

filename = 'casing_temperature_all_frames';

data = readtable(filename, 'VariableNamingRule', 'preserve');

instantes_tempo = unique(data.("Time (s)"));
nos_unicos = unique(data.("Node Label"));

% data.Properties.VariableNames = strtrim(data.Properties.VariableNames);

% instantes_tempo = unique(data.Time_s_);
% nos_unicos = unique(data.Node_Label);

num_frames = length(instantes_tempo);
num_nos = length(nos_unicos);

[unq_nodes, idx] = unique(data.("Node Label"));

% profundidades = data.Vertical_Pos_m_(idx);
profundidades = data.("Z Position (m)")(idx);

ref_nos = table(unq_nodes, profundidades, 'VariableNames', {'Label', 'Z'});
ref_nos = sortrows(ref_nos, 'Z', 'descend');

matriz_U1 = zeros(num_nos, num_frames);

for t = 1:num_frames

    dados_frame = data(data.("Time (s)") == instantes_tempo(t), :);

    for n = 1:num_nos

        label_alvo = ref_nos.Label(n);
        idx_valor = dados_frame.("Node Label") == label_alvo;

        if any(idx_valor)
            % valores_temporarios = dados_frame.("U1 Displacement (m)")(idx_valor);
            % matriz_U1(n, t) = valores_temporarios(1);
            % matriz_U1(n, t) = dados_frame.("U1 Displacement (m)")(idx_valor);
            % matriz_U1(n, t) = mean(dados_frame.("U1 Displacement (m)")(idx_valor));
            matriz_U1(n, t) = mean(dados_frame.("NT (K)")(idx_valor));
        end 
    end 
end 

eixo_tempo = instantes_tempo;
eixo_z = ref_nos.Z;

fprintf('>>> Matriz gerada: %d posições verticais x %d frames.\n' , num_nos, num_frames);

figure()
hold on 
grid on

frames_interesse = [1, round(num_frames/2), num_frames];
cores = lines(length(frames_interesse));
legendas = {'Inicio', '15 Anos', '30 Anos'};

for i = 1:length(frames_interesse)
    idx = frames_interesse(i);

    plot(matriz_U1(:, idx), eixo_z, 'Color', cores(i,:), 'LineWidth',2);
end

set(gca, 'YDir', 'reverse')

xlabel('Temperature (K)');
ylabel('Profundidade Z (m)');
title('Evolução do Perfil de Temperatura no Revestimento');
legend(legendas, 'Location', 'best');
set(gca, 'YDir', 'normal'); % Garante que o topo fique no topo

%% Lendo tensao da parede interna do poço (perfil)

clear all
% close all
clc

PATH = 'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_';
cd(PATH)

filename = 'rock_stress_all_frames';

data = readtable(filename, 'VariableNamingRule', 'preserve');

instantes_tempo = unique(data.("Time (s)"));
nos_unicos = unique(data.("Node Label"));

% data.Properties.VariableNames = strtrim(data.Properties.VariableNames);

% instantes_tempo = unique(data.Time_s_);
% nos_unicos = unique(data.Node_Label);

num_frames = length(instantes_tempo);
num_nos = length(nos_unicos);

[unq_nodes, idx] = unique(data.("Node Label"));

% profundidades = data.Vertical_Pos_m_(idx);
profundidades = data.("Z Position (m)")(idx);

ref_nos = table(unq_nodes, profundidades, 'VariableNames', {'Label', 'Z'});
ref_nos = sortrows(ref_nos, 'Z', 'descend');

matriz_U1 = zeros(num_nos, num_frames);

for t = 1:num_frames

    dados_frame = data(data.("Time (s)") == instantes_tempo(t), :);

    for n = 1:num_nos

        label_alvo = ref_nos.Label(n);
        idx_valor = dados_frame.("Node Label") == label_alvo;

        if any(idx_valor)
            % valores_temporarios = dados_frame.("U1 Displacement (m)")(idx_valor);
            % matriz_U1(n, t) = valores_temporarios(1);
            % matriz_U1(n, t) = dados_frame.("U1 Displacement (m)")(idx_valor);
            % matriz_U1(n, t) = mean(dados_frame.("U1 Displacement (m)")(idx_valor));
            matriz_U1(n, t) = mean(dados_frame.("Mises (Pa)")(idx_valor));
        end 
    end 
end 

eixo_tempo = instantes_tempo;
eixo_z = ref_nos.Z;

fprintf('>>> Matriz gerada: %d posições verticais x %d frames.\n' , num_nos, num_frames);

figure()
hold on 
grid on

frames_interesse = [1, round(num_frames/2), num_frames];
cores = lines(length(frames_interesse));
legendas = {'Inicio', '15 Anos', '30 Anos'};

for i = 1:length(frames_interesse)
    idx = frames_interesse(i);

    plot(matriz_U1(:, idx)/1e6, eixo_z, 'Color', cores(i,:), 'LineWidth',2);
end

set(gca, 'YDir', 'reverse')

xlabel('Mises (MPa)');
ylabel('Profundidade Z (m)');
title('Evolução do Perfil de Tensão na Formação');
legend(legendas, 'Location', 'best');
set(gca, 'YDir', 'normal'); % Garante que o topo fique no topo

%% Lendo tensão na formação em um ponto (base da formação)

figure()
plot(instantes_tempo/(60*60*24*365),matriz_U1(end,:)/1e6)
xlabel('time [years]')
ylabel('Stress [MPa]')
grid minor

%% Lendo temperaturas na rocha (perfil)

clear all
% close all
clc

PATH = 'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_';
cd(PATH)

filename = 'rock_temperature_all_frames';

data = readtable(filename, 'VariableNamingRule', 'preserve');

instantes_tempo = unique(data.("Time (s)"));
nos_unicos = unique(data.("Node Label"));

% data.Properties.VariableNames = strtrim(data.Properties.VariableNames);

% instantes_tempo = unique(data.Time_s_);
% nos_unicos = unique(data.Node_Label);

num_frames = length(instantes_tempo);
num_nos = length(nos_unicos);

[unq_nodes, idx] = unique(data.("Node Label"));

% profundidades = data.Vertical_Pos_m_(idx);
profundidades = data.("Z Position (m)")(idx);

ref_nos = table(unq_nodes, profundidades, 'VariableNames', {'Label', 'Z'});
ref_nos = sortrows(ref_nos, 'Z', 'descend');

matriz_U1 = zeros(num_nos, num_frames);

for t = 1:num_frames

    dados_frame = data(data.("Time (s)") == instantes_tempo(t), :);

    for n = 1:num_nos

        label_alvo = ref_nos.Label(n);
        idx_valor = dados_frame.("Node Label") == label_alvo;

        if any(idx_valor)
            % valores_temporarios = dados_frame.("U1 Displacement (m)")(idx_valor);
            % matriz_U1(n, t) = valores_temporarios(1);
            % matriz_U1(n, t) = dados_frame.("U1 Displacement (m)")(idx_valor);
            % matriz_U1(n, t) = mean(dados_frame.("U1 Displacement (m)")(idx_valor));
            matriz_U1(n, t) = mean(dados_frame.("NT (K)")(idx_valor));
        end 
    end 
end 

eixo_tempo = instantes_tempo;
eixo_z = ref_nos.Z;

fprintf('>>> Matriz gerada: %d posições verticais x %d frames.\n' , num_nos, num_frames);

figure()
hold on 
grid on

frames_interesse = [1, round(num_frames/2), num_frames];
cores = lines(length(frames_interesse));
legendas = {'Inicio', '15 Anos', '30 Anos'};

for i = 1:length(frames_interesse)
    idx = frames_interesse(i);

    plot(matriz_U1(:, idx), eixo_z, 'Color', cores(i,:), 'LineWidth',2);
end

set(gca, 'YDir', 'reverse')

xlabel('Temperature (K)');
ylabel('Profundidade Z (m)');
title('Evolução do Perfil de Temperatura no Revestimento');
legend(legendas, 'Location', 'best');
set(gca, 'YDir', 'normal'); % Garante que o topo fique no topo

%% Lendo temperatura na formação em um ponto (base da formação)

figure()
plot(instantes_tempo/(60*60*24*365),matriz_U1(end,:))
xlabel('time [years]')
ylabel('Stress [MPa]')
grid minor