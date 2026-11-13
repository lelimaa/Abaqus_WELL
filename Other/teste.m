% Lendo deslocamento da parede interna do poço (perfil)

clear all
close all
clc

% PATH = 'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL_';
% PATH = 'C:\Users\juani\Documents\Github\Abaqus_WELL';

% PATH = 'C:\Users\hidalgo\Documents\Gitlab\abaquswell';
% PATH = 'C:\app\abaqus-workdir\40';
% PATH = 'C:\Users\hidalgo\Documents\Gitlab\abaquswell';
% PATH = 'C:\Users\hidalgo\Desktop\Poseidon\analysis38';
PATH = 'C:\app\abaqus-workdir\98';


cd(PATH)

% filename = 'path_data_all_frames';
filename = 'rock_displacement_all_frames';

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
            % matriz_U1(n, t) = mean(dados_frame.("U1_Radial (m)")(idx_valor));
        end 
    end 
end 

eixo_tempo = instantes_tempo;
eixo_tempo_anos = eixo_tempo ./(60*60*24*365);
eixo_z = ref_nos.Z;

fprintf('>>> Matriz gerada: %d posições verticais x %d frames.\n' , num_nos, num_frames);

FontSize = 20;

figure()
hold on 
grid on

frames_interesse = [1, 120, 140, 185, round(num_frames/2), num_frames];
cores = lines(length(frames_interesse));
legendas = {'Initial', '2 Years', '7 Years', '10 Years', '12 Years', '30 Years'};

for i = 1:length(frames_interesse)
    idx = frames_interesse(i);

    plot(matriz_U1(:, idx)*1e3, abs(eixo_z), 'Color', cores(i,:), 'LineWidth',2);
end

tit1a = title('Evolution of the Well Closure Profile','Interpreter','Latex');
eixo1a = xlabel({'Radial Displacement $u_{1}$ [mm]'},'Interpreter','Latex');
eixo2a = ylabel('Depth Z [m]','Interpreter','Latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
set(gca,'Fontsize',FontSize)
set(gcf,'Color','w')
% xlim([0 6.8e-4])
grid minor

set(gca, 'YDir', 'reverse')

% xlabel('Deslocamento Radial U1 (mm)');
% ylabel('Profundidade Z (m)');
% title('Evolução do Perfil de Fechamento do Poço');
legend(legendas, 'Location', 'Northeast');
% set(gca, 'YDir', 'normal'); % Garante que o topo fique no topo

%%

% =========================================================================
% SCRIPT CORRIGIDO: Evolução do Perfil de Fechamento do Poço
% =========================================================================
clear; clc; close all;

%% 1. Leitura do Arquivo CSV

% PATH = 'C:\Users\hidalgo\Desktop\Poseidon\analysis38';
% PATH = 'C:\Users\hidalgo\Desktop\Poseidon\simulation4';
PATH = 'C:\app\abaqus-workdir\98';

cd(PATH)

nome_arquivo = 'rock_displacement_all_frames.csv'; % <-- Substitua pelo nome do seu arquivo

opts = detectImportOptions(nome_arquivo, 'VariableNamingRule', 'preserve');
data = readtable(nome_arquivo, opts);

%% 2. Configurações de Tempo
segundos_por_ano = 365 * 24 * 3600;

tempos_unicos_s = unique(data.("Time (s)"));
tempos_unicos_anos = tempos_unicos_s / segundos_por_ano;

anos_alvo = [0, 0.00274, 0.082192, 1, 2, 5, 30];
legendas  = {'Initial', '1 Day', '1 Month', '1 Year', '2 Years', '5 Years', '30 Years'};

cores = [
    0.00, 0.45, 0.74;  % Initial (Azul)
    0.85, 0.33, 0.10;  % 0.00274 Years (Laranja)
    0.93, 0.69, 0.13;  % 0.082192 Years (Amarelo)
    0.49, 0.18, 0.56;  % 1 Years (Roxo)
    0.47, 0.67, 0.19;  % 1 Years (Verde)
    0.64, 0.08, 0.18   % 5 Years (Brown)
    0.30, 0.75, 0.93   % 30 Years (Ciano)
];

%% 3. Configuração da Figura
FontSize = 14;
figure('Color', 'w', 'Position', [150, 100, 750, 600]);
hold on;
grid on;
grid minor;

%% 4. Plotagem com Limpeza de Duplicatas e Ordenação Correta
for i = 1:length(anos_alvo)
    ano_desejado = anos_alvo(i);
    
    % Encontra o instante de tempo mais próximo
    [~, idx_tempo] = min(abs(tempos_unicos_anos - ano_desejado));
    tempo_escolhido_s = tempos_unicos_s(idx_tempo);
    
    % Filtra os dados deste frame
    dados_frame = data(data.("Time (s)") == tempo_escolhido_s, :);
    
    z_raw  = abs(dados_frame.("Z Position (m)"));
    u1_raw = dados_frame.("U1 Displacement (m)") * 1000; % mm
    
    % ---------------------------------------------------------------------
    % CORREÇÃO DO ZIGUEZAGUE / DUPLICATAS:
    % Agrupa nós que tenham a mesma profundidade Z arredondada
    % e calcula a média de U1 para cada cota Z única.
    % ---------------------------------------------------------------------
    tbl_temp = table(round(z_raw, 4), u1_raw, 'VariableNames', {'Z', 'U1'});
    tbl_limpa = groupsummary(tbl_temp, 'Z', 'mean', 'U1');
    
    % Ordena de forma estritamente decrescente pela profundidade
    tbl_limpa = sortrows(tbl_limpa, 'Z', 'ascend');
    
    eixo_z_limpo  = tbl_limpa.Z;
    eixo_u1_limpo = tbl_limpa.mean_U1;
    
    % Plota a curva limpa
    plot(eixo_u1_limpo+6.35, eixo_z_limpo, ...
        'Color', cores(i, :), ...
        'LineWidth', 1.8, ...
        'DisplayName', legendas{i});
end

%% 5. Ajustes de Formatação
set(gca, 'YDir', 'reverse'); % Superfície no topo

title('Evolution of the Well Closure Profile', 'Interpreter', 'latex', 'FontSize', FontSize + 2);
xlabel('Annular gap [mm]', 'Interpreter', 'latex', 'FontSize', FontSize);
ylabel('Depth [m]', 'Interpreter', 'latex', 'FontSize', FontSize);

% ylim([2800 4000]); % Ajuste de profundidade como no gráfico de referência
xlim([-0.5 6.5]);

legend('Location', 'northwest', 'FontSize', FontSize - 2, 'Interpreter', 'latex');
set(gca, 'FontSize', FontSize, 'Box', 'on', 'TickDir', 'in');


%%
% %% Código corrigido 
% 
% % =========================================================================
% % SCRIPT: Perfil Vertical de Deslocamento Radial do Revestimento (Abaqus)
% % =========================================================================
% clear; clc; close all;
% 
% %% 1. Configurações e Leitura do CSV
% 
% PATH = 'C:\Users\hidalgo\Documents\Gitlab\abaquswell';
% 
% cd(PATH)
% 
% % filename = 'rock_displacement_all_frames';
% 
% 
% nome_arquivo = 'rock_displacement_all_frames.csv'; % <-- Substitua pelo nome do seu arquivo .csv
% 
% % 'preserve' garante a leitura exata dos nomes com parênteses e espaços
% opts = detectImportOptions(nome_arquivo, 'VariableNamingRule', 'preserve');
% data = readtable(nome_arquivo, opts);
% 
% %% 2. Conversão e Identificação Temporal
% segundos_por_ano = 365 * 24 * 3600;
% 
% % Obter todos os tempos únicos existentes no arquivo (em segundos e em anos)
% tempos_unicos_s = unique(data.("Time (s)"));
% tempos_unicos_anos = tempos_unicos_s / segundos_por_ano;
% 
% % Anos alvo desejados para a legenda
% anos_alvo = [0, 2, 7, 10, 12, 30];
% legendas  = {'Initial', '2 Years', '7 Years', '10 Years', '12 Years', '30 Years'};
% 
% % Cores idênticas às exibidas no gráfico de referência
% cores = [
%     0.00, 0.45, 0.74;  % Initial (Azul)
%     0.85, 0.33, 0.10;  % 2 Years (Laranja)
%     0.93, 0.69, 0.13;  % 7 Years (Amarelo)
%     0.49, 0.18, 0.56;  % 10 Years (Roxo)
%     0.47, 0.67, 0.19;  % 12 Years (Verde)
%     0.30, 0.75, 0.93   % 30 Years (Ciano)
% ];
% 
% %% 2. Filtrar Apenas o Instante Final (Último Frame de Tempo)
% % tempos = unique(data.("Time (s)"));
% % tempo_final = tempos(end);
% 
% % fprintf('>> Filtrando dados para o instante final: %.2f s (%.2f anos)\n', ...
% %     tempo_final, tempo_final / (365*24*3600));
% % 
% % % Extrai apenas as linhas do último frame
% % dados_final = data(data.("Time (s)") == tempo_final, :);
% 
% %% 3. Configuração da Figura
% FontSize = 16;
% figure('Color', 'w', 'Position', [150, 100, 750, 600]);
% hold on;
% grid on;
% grid minor;
% 
% %% 4. Loop para Buscar os Frames e Plotar os Perfis
% for i = 1:length(anos_alvo)
%     ano_desejado = anos_alvo(i);
% 
%     % Encontra o tempo do CSV mais próximo do ano desejado
%     [~, idx_tempo] = min(abs(tempos_unicos_anos - ano_desejado));
%     tempo_escolhido_s = tempos_unicos_s(idx_tempo);
% 
%     % Filtra os dados deste frame específico
%     dados_frame = data(data.("Time (s)") == tempo_escolhido_s, :);
% 
%     % Extrai e ordena conjuntamente pela profundidade Z
%     z_pos = dados_frame.("Z Position (m)");
%     u1_rad = dados_frame.("U1 Displacement (m)");
% 
%     tabela_frame = table(z_pos, u1_rad, 'VariableNames', {'Z', 'U1'});
%     tabela_frame = sortrows(tabela_frame, 'Z', 'descend'); % do topo para o fundo
% 
%     % Conversões para os eixos:
%     % X: metros para milímetros (x 1000)
%     % Y: profundidade positiva em módulo (|Z|)
%     eixo_x_mm = tabela_frame.U1 * 1000;
%     eixo_y_z  = abs(tabela_frame.Z);
% 
%     % Plota a curva do instante
%     plot(eixo_x_mm, eixo_y_z, ...
%         'Color', cores(i, :), ...
%         'LineWidth', 1.8, ...
%         'DisplayName', legendas{i});
% end
% 
% %% 5. Ajustes de Formatação e Eixos
% % Inverte o eixo vertical para que o topo fique na parte superior
% set(gca, 'YDir', 'reverse');
% 
% % Título e Rótulos com LaTeX
% title('Evolution of the Well Closure Profile', 'Interpreter', 'latex', 'FontSize', FontSize + 2);
% xlabel('Radial Displacement $u_1$ [mm]', 'Interpreter', 'latex', 'FontSize', FontSize);
% ylabel('Depth Z [m]', 'Interpreter', 'latex', 'FontSize', FontSize);
% 
% % Limites ajustáveis para enquadrar perfeitamente como na imagem
% ylim([2800 4000]); % Ajuste de profundidade
% % xlim([-10 0]);   % Descomente e ajuste os limites de X se desejar fixar a escala[cite: 10]
% 
% legend('Location', 'northeast', 'FontSize', FontSize - 2, 'Interpreter', 'latex');
% set(gca, 'FontSize', FontSize, 'Box', 'on', 'TickDir', 'in');

%% 3. Extrair e Ordenar os Nós pela Profundidade Z
% % Extração direta dos vetores
% z_pos = dados_final.("Z Position (m)");
% u1_rad = dados_final.("U1 Displacement (m)");
% 
% % Cria uma tabela temporária para ordenar os pares conjuntamente
% tabela_perfil = table(z_pos, u1_rad, 'VariableNames', {'Z', 'U1'});
% 
% % Ordena de forma decrescente pela profundidade Z (do topo para o fundo do poço)
% % Se preferir crescente, utilize 'ascend'
% tabela_perfil = sortrows(tabela_perfil, 'Z', 'descend');
% 
% eixo_z = tabela_perfil.Z;
% eixo_u1 = tabela_perfil.U1;

% %% 4. Plotagem do Gráfico (Profundidade no Eixo Y x U1 no Eixo X)
% FontSize = 14;
% figure('Color', 'w', 'Position', [200, 100, 600, 800]);
% 
% % Plota o deslocamento em mm ou m (aqui mantido em m conforme a unidade do Abaqus)
% plot(eixo_u1, abs(eixo_z), 'r-', 'LineWidth', 2);
% hold on;
% grid on;
% grid minor;
% 
% % Inverte o eixo Y para que o topo do poço fique na parte superior
% set(gca, 'YDir', 'reverse');
% 
% % Rótulos e Título
% xlabel('Deslocamento Radial $U_1$ [m]', 'Interpreter', 'latex', 'FontSize', FontSize);
% ylabel('Profundidade $|Z|$ [m]', 'Interpreter', 'latex', 'FontSize', FontSize);
% title(sprintf('Perfil de Deslocamento do Revestimento (t = %.1f s)', tempo_final), ...
%     'Interpreter', 'latex', 'FontSize', FontSize + 2);
% 
% legend({'U1: True Dist. along Path'}, 'Location', 'best', 'Interpreter', 'none');
% set(gca, 'FontSize', FontSize, 'Box', 'on', 'TickDir', 'out');

%% Lendo deslocamento em um ponto (base da formação)

instantes_tempo = unique(data.("Time (s)"));

FontSize = 20;

figure()
plot(instantes_tempo/(60*60*24*365),matriz_U1(end,:)*1e3, 'linewidth', 2)
tit1a = title('Evolution of the Formation Displacement ($z=z_{\mathrm{Bottom}}$) ','Interpreter','Latex');
eixo1a = xlabel({'Time [Years]'},'Interpreter','Latex');
eixo2a = ylabel('$u_{1}$ [mm]','Interpreter','Latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
set(gca,'Fontsize',FontSize)
set(gcf,'Color','w')
% xlim([0 6.8e-4])
grid minor

%% Lendo tensões no casing (perfil)

clear all
% close all
clc

% PATH = 'C:\Users\hidalgo\Documents\GitHub\Abaqus_WELL';
% PATH = 'C:\Users\juani\Documents\Github\Abaqus_WELL';
% PATH = 'C:\Users\hidalgo\Documents\Gitlab\abaquswell';
% cd(PATH)
% 
% filename = 'casing_stress_all_frames';

PATH = 'C:\Users\hidalgo\Desktop\Poseidon\J6CorrectedTubular';

cd(PATH)

filename = 'casing_stress_all_frames.csv'; % <-- Substitua pelo nome do seu arquivo

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
eixo_tempo_anos = eixo_tempo ./(60*60*24*365);
eixo_z = ref_nos.Z;

fprintf('>>> Matriz gerada: %d posições verticais x %d frames.\n' , num_nos, num_frames);

FontSize = 20;

figure()
hold on 
grid on

% frames_interesse = [1, 86];
frames_interesse = [1, 86, 106,151, round(num_frames/2), num_frames];

cores = lines(length(frames_interesse));
% legendas = {'Initial', '2 Years'};
legendas = {'Initial', '2 Years','7 Years','10 Years', '12 Years', '30 Years'};

for i = 1:length(frames_interesse)
    idx = frames_interesse(i);

    plot(matriz_U1(:, idx)/1e6-40, abs(eixo_z), 'Color', cores(i,:), 'LineWidth',2);
end

set(gca, 'YDir', 'reverse')

tit1a = title('Evolution of the Casing Stress Profile','Interpreter','Latex');
eixo1a = xlabel({'Mises [MPa]'},'Interpreter','Latex');
eixo2a = ylabel('Depth Z [m]','Interpreter','Latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
set(gca,'Fontsize',FontSize)
set(gcf,'Color','w')
% xlim([0 6.8e-4])
grid minor

% xlabel('Mises (MPa)');
% ylabel('Profundidade Z (m)');
% title('Evolução do Perfil de Tensão no Revestimento');
legend(legendas, 'Location', 'NorthWest');
% set(gca, 'YDir', 'normal'); % Garante que o topo fique no topo

%% Lendo tensão no casing em um ponto (base do revestimento)

FontSize = 20;

figure()
plot(instantes_tempo/(60*60*24*365),matriz_U1(end,:)/1e6-40, 'linewidth', 2)
tit1a = title('Evolution of the Casing Stress ($z=z_{\mathrm{Bottom}}$) ','Interpreter','Latex');
eixo1a = xlabel({'Time [Years]'},'Interpreter','Latex');
eixo2a = ylabel('Mises [MPa]','Interpreter','Latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
set(gca,'Fontsize',FontSize)
set(gcf,'Color','w')
% xlim([0 6.8e-4])
grid minor


% xlabel('time [years]')
% ylabel('Stress [MPa]')
% grid minor

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
eixo_tempo_anos = eixo_tempo ./(60*60*24*365);
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

