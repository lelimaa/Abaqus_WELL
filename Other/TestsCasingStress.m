clear all
close all
clc

% inputs of lenghts

x1 = 2000;
x2 = 4000;
H = x2-x1;

z1 = 0;
z2 = z1+H;

L = z2-z1;

g = 9.81;

rho_s = 7850;
rho_f = 1000;

Gamma = (rho_s-rho_f) * g;

De = 244.5e-3;
th = 11.05e-3;
Di = De-2*th;

S = pi*(De^2-Di^2)/4;

V = S * L;

mass_s = rho_s * V;

E = rho_f * V * g;
W = rho_s * V * g;

R = W - E;

sigma_top = R/S

%% 1a seção

z = 1000;

E1 = rho_f * S * z * g;
W1 = rho_s * S * z * g;

Fl = R - Gamma* S * z

% 2a seção

E2 = rho_f * S * (L-z) * g;
W2 = rho_s * S * (L-z) * g;

Fl = Gamma * S * (L-z)

sigma_l = Fl / S

%% plotando gráfico

X = x1:10:x2;
Z = z1:10:z2;

Sigma_z = Gamma * (L-Z);

figure()
plot(Sigma_z/1e6,-X)
xlabel({'$\sigma_{z}$ [MPa]'},'Interpreter','Latex')
ylabel({'$z$ [m]'},'Interpreter','Latex')
grid on


%% Fazendo de outra forma, por tensões desde a base

y = z;

sigma_b = - rho_f * g * L
sigma_t = Gamma * L

sigma_y = Gamma * L - rho_s*g*y 

FL1 = Gamma * L * S - rho_s * g * y * S

FL2 = -rho_f * g * L * S + rho_s * g * (x2-y) * S

%%

Y = X;

Sigma_y = Gamma * L - rho_s * g * Y ;

figure()
plot(Sigma_y/1e6,-X)
xlabel({'$\sigma_{z}$ [MPa]'},'Interpreter','Latex')
ylabel({'$z$ [m]'},'Interpreter','Latex')
grid on

%% Overlay of plots

figure()
plot(Sigma_z/1e6, -X, 'r-')
hold on 
plot(Sigma_y/1e6,-X, 'b-')
xlabel({'$\sigma_{z}$ [MPa]'},'Interpreter','Latex')
ylabel({'$z$ [m]'},'Interpreter','Latex')
grid on

%% New test considering the sea column above

clear all
% close all
clc

rho_s = 7950; % density of casing steel
rho_f = 1000; % density of the fluid
g = 9.81; % gravity acceleration on earth

H = 1000; % height of the water column before first lithology
PH = rho_f * g * H % pressure above the first lithology
factor_ppg = 119.826; % convert factor to get pressure in ppg
PH_ppg = PH / (H * g * factor_ppg) % pressure in ppg
% PH_cal = PH_ppg * H * g * factor_ppg; % calculating the pressure in the reverse way

L = 3250; % length of the casing 

epsilon = 1000; % difference to calculate y1
gamma = 1000; % difference to calculate y2
Ll = L - gamma; % another length from "cut" 1
Lll = L - gamma - epsilon; % length of the desired region to be analyzed

h = H+L; % total depth of the base of the casing 

hl = H + Ll; % another base from "cut" test

y1 = H+0*epsilon; % first casing's point of analysis 
% y2 = y1+Lll;
y2 = H + L; % second casing's point of analysis

Y = y1:10:y2; % region of interest 

alpha = Y - H; % first part of the sectioned casing for investigating stresses
beta = h - Y ; % remaining part of the sectioned casing for investigating stresses
% delta = beta - gamma; % difference to calculate using only the region of interest (not good)

Sigma_b = rho_f * g *h; % stress on the base of the entire casing
% Sigma_bl = rho_f * g * hl;

Sigma_y = -Sigma_b + rho_s * g * beta;
% Sigma_yl = -Sigma_bl + rho_s * g * (hl - Y);

figure()
plot(Sigma_y/1e6,-Y, 'r-')
% hold on
% plot(Sigma_yl/1e6,-Y, 'b-')
grid on

%% Sugestão do gemini (engenharia reversa)

w_s = 77989.4;
rho_s_cal = w_s/g;
sigma_surf = 289975800;

y_top = 2000;
y_base = 4000;

sigma_top = sigma_surf - (w_s * y_top)
sigma_base = sigma_surf - (w_s * y_base)

delta_y = (sigma_top - sigma_base)/(y_base-y_top)

Z = 2000:5:4000;

Sigma_y_sug = sigma_surf - delta_y * Z;

figure()
plot(Sigma_y_sug/1e6, -Z, 'b-')
hold on 
plot(Sigma_y/1e6, -Y, 'r-')
grid on

% Conclusion: use the derived one 

%% Final derived expression for calculating the stresses as inputs

clear all
% close all
clc

rho_s = 7950; % density of casing steel
rho_f = 1000; % density of the fluid
g = 9.81; % gravity acceleration on earth

H = 1000; % height of the water column above casing

PH = rho_f * g * H % pressure above the first lithology;
factor_ppg = 119.826; % convert factor to get pressure in ppg
PH_ppg = PH / (H * g * factor_ppg) % pressure in ppg;
% PH_cal = PH_ppg * H * g * factor_ppg; % calculating the pressure in the reverse way

L = 3250; % length of the casing 

epsilon = 1000; % difference to calculate y1
gamma = 1000; % difference to calculate y2
Ll = L - gamma; % another length from "cut" 1
Lll = L - gamma - epsilon; % length of the desired region to be analyzed

h = H+L; % total depth of the base of the casing 

hl = H + Ll; % another base from "cut" test

y1 = H + 1*epsilon; % first casing's point of analysis 
y2 = H + L - 1*gamma; % second casing's point of analysis 

Y = y1:10:y2; % region of interest 

alpha = Y - H; % first part of the sectioned casing for investigating stresses
beta = h - Y ; % remaining part of the sectioned casing for investigating stresses


Sigma_b = rho_f * g *h; % stress on the base of the entire casing

Sigma_y = -Sigma_b + rho_s * g * beta; % vertical stress in any depth of the casing


figure()
plot(Sigma_y/1e6,-Y, 'r-')
xlabel({'$\sigma_{z}$ [MPa]'},'Interpreter','Latex')
ylabel({'$z$ [m]'},'Interpreter','Latex')
grid on

%% New test considering cement on the base

clear all
% close all
clc

rho_s = 7950; % density of casing steel
rho_f = 1000; % density of the fluid
rho_c = 1900; % density of cement
g = 9.81; % gravity acceleration on earth

H = 2000; % height of the water column above casing

PH = rho_f * g * H % pressure above the first lithology;
factor_ppg = 119.826; % convert factor to get pressure in ppg
PH_ppg = PH / (H * g * factor_ppg) % pressure in ppg;
% PH_cal = PH_ppg * H * g * factor_ppg; % calculating the pressure in the reverse way

L = 5000; % length of the casing 
Lc = 0; % length of the cement (TOC)

epsilon = 1000; % difference to calculate y1
gamma = 250; % difference to calculate y2
Ll = L - gamma - epsilon; % length of the desired region to be analyzed

h = H+L; % total depth of the base of the casing 

hl = H + Ll; % another base from "cut" test

y1 = H + 1*epsilon; % first casing's point of analysis 
% y2 = H + L - 1*gamma; % second casing's point of analysis 
y2 = h;

Y = y1:10:y2; % region of interest 

alpha = Y - H; % first part of the sectioned casing for investigating stresses
beta = h - Y ; % remaining part of the sectioned casing for investigating stresses


Sigma_b = rho_f * g * (L-Lc) + rho_c*g*Lc; % stress on the base of the entire casing

Sigma_y = -Sigma_b + rho_s * g * (h-Y); % vertical stress in any depth of the casing


figure()
plot(Sigma_y/1e6,-Y, 'r-')
xlabel({'$\sigma_{z}$ [MPa]'},'Interpreter','Latex')
ylabel({'$z$ [m]'},'Interpreter','Latex')
grid on


%% Testing with pressures

clear all
clc

rho_s = 7950; % density of casing steel
rho_f = 1000; % density of the fluid
rho_c = 1900; % density of cement
g = 9.81; % gravity acceleration on earth

H = 2000; % height of the water column above casing

L = 5000; % length of the casing 
Lc = 1000; % length of the cement (TOC)

h = H+L; % total depth of the base of the casing 
yl1 = h-Lc;

Y1 = 0:1:yl1; % region of interest 
Y2 = yl1:1:h;

S1 = rho_f * g * Y1;
S2 = rho_f * g * yl1 + rho_c * g * Y2;

figure()
plot(Y1,S1)
hold on
plot(Y2,S2)
grid on

%% New Methodology (27/05/2026)

% clear all
% close all
clc

rho_s = 7935; % density of casing steel
rho_w = 1000; % density of the water above well
rho_fi = 1000; % density of the internal fluid
rho_fa = 1000; % density of the external fluid @ annular space
rho_cem = 1900; % density of cement
g = 9.81; % gravity acceleration on earth

H = 2000; % height of the water column above well
L = 3500; % length of the casing 
Lc = 750; % length of the cement (TOC)

yb = H+L; 
yc = H+L-Lc; % top of cement

f_in_m = 0.0254;

Do = 9 + 7/8;
Do = Do * f_in_m;
th = 0.625;
th = th * f_in_m;
Di = Do-2*th;

Ao = (pi * Do^2)/4;
Ai = (pi * Di^2)/4;

As = Ao-Ai;

% pressures at region above well

Y0 = 0:0.1:H;
P0 = rho_w * g * Y0;

% figure()
% plot(Y0,P0/1e6)
% grid minor

% pressures at region internal the casing

Y1 = H:0.1:yb;
P_int = rho_w * g * H + rho_fi * g * (Y1-H);

% figure()
% plot(Y1,P_int/1e6)
% grid minor

% pressures at region internal the casing (above TOC)

Y1_atoc = H:0.1:yc;
P_int_atoc = rho_w * g * H + rho_fi * g * (Y1_atoc-H);

% pressures at region internal the casing (below TOC)

Y1_btoc = yc+0.1:0.1:yb;
P_int_btoc = rho_w * g * H + rho_fi * g * (Y1_btoc-H);

% pressures at annular space above TOC

Y2 = H:0.1:yc;
P_out1 = rho_w * g * H + rho_fa * g * (Y2-H);

% figure()
% plot(Y2,P_out1/1e6)
% grid minor

% pressures at annular space along TOC

Y3 = yc+0.1:0.1:yb;
P_out2 = rho_w * g * H + rho_fa * g * (yc-H) + rho_cem * g * (Y3 - yc);

FontSize = 18;

figure()
plot(P0/1e6,Y0,'linewidth',2)
hold on
plot(P_int/1e6,Y1,'linewidth',2)
plot(P_out1/1e6,Y2,'linewidth',2)
plot(P_out2/1e6,Y3,'linewidth',2)
eixo1a = xlabel({'P [MPa]'},'Interpreter','Latex');
eixo2a = ylabel({'y [m]'},'Interpreter','Latex');
tit1a = title('Pressures','Interpreter','Latex');
leg1a = legend('Above Well','Inner','Annular','AnnularCem','interpreter','latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');

%% calculating real axial stress

% stress in the bottom

P_int_b = rho_w * g * H + rho_fi * g * (yb-H);
% P_out1_b = rho_w * g * H + rho_fa * g * (yb-H);
P_out1_b = rho_w * g * H + rho_w * g * H + rho_fa * g * (yc-H) + rho_cem * g * (yb-yc);

F_real_b = P_int_b*Ai-P_out1_b*Ao;

sigma_b = F_real_b/As;

% stress at any point of casing (H<y<yb)

YN = H:0.1:yb;

F_real = F_real_b + rho_s * g * As * (yb-YN);

sigma_y = sigma_b + rho_s * g * (yb-YN);

% stress at the top of cement

sigma_c = sigma_b + rho_s * g * (yb-yc);

figure()
plot(sigma_y/1e6,YN)
hold on 
scatter(sigma_c/1e6,yc)
scatter(sigma_b/1e6,yb)
eixo1a = xlabel({'$\sigma_{y}$ [MPa]'},'Interpreter','Latex');
eixo2a = ylabel({'y [m]'},'Interpreter','Latex');
tit1a = title('Stress in Casing','Interpreter','Latex');
% leg1a = legend('Above Well','Inner','Annular','AnnularCem','interpreter','latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
% set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');

% axial effective stress

sigma_ef = sigma_y + ((rho_w * g * yb + rho_fa * g * (YN-H))*Ao-(rho_w * g * yb + rho_fi * g * (YN-H))*Ai)/As;


figure()
plot(sigma_ef/1e6, YN)
eixo1a = xlabel({'$\sigma_{y}$ [MPa]'},'Interpreter','Latex');
eixo2a = ylabel({'y [m]'},'Interpreter','Latex');
tit1a = title('Stress in Casing','Interpreter','Latex');
% leg1a = legend('Above Well','Inner','Annular','AnnularCem','interpreter','latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
% set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');



%% Testando a solução a partir das pressões calculadas

sigma_ef_yb = (rho_s - rho_cem*Ao/As + rho_fi * Ai/As)*g*(yb-YN);

sigma_ef_c = (rho_s-rho_cem*Ao/As+rho_fi*Ai/As)*g*(yb-yc);

sigma_ef_yt = sigma_ef_c + (rho_s-rho_fa*Ao/As + rho_fi*Ai/As)*g*(yc-YN);

figure()
plot(sigma_ef/1e6, YN)
hold on 
plot(sigma_ef_yt/1e6,YN)
plot(sigma_y/1e6,YN)
eixo1a = xlabel({'$\sigma_{y}$ [MPa]'},'Interpreter','Latex');
eixo2a = ylabel({'y [m]'},'Interpreter','Latex');
tit1a = title('Stress in Casing','Interpreter','Latex');
% leg1a = legend('Above Well','Inner','Annular','AnnularCem','interpreter','latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
% set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');

%% Testando solução nova mesclando as hidropressões (08/06/26)

% Step1
Pi_yb = rho_w * g * H + rho_fi * g * (yb-H);
Po_yb = rho_w * g * H + rho_fa * g * (yc-H) + rho_cem * g * (yb-yc);

F_real_yb = Pi_yb * Ai - Po_yb * Ao;

F_real_y = F_real_yb + rho_s * g * As * (yb - YN);

sigma_real_y = F_real_y / As;

ylim1 = find(YN == yc, 1, 'first');

% above TOC

sigma_efetiva_y_atoc = sigma_real_y(1:ylim1) + (P_out1*Ao-P_int_atoc*Ai)/As;

% along TOC

sigma_efetiva_y_btoc = sigma_real_y(ylim1+1:end) + (P_out2*Ao-P_int_btoc*Ai)/As;

sigma_efetiva_y = zeros(1,length(YN));

sigma_efetiva_y(1:ylim1) = sigma_efetiva_y_atoc;
sigma_efetiva_y(ylim1+1:end) = sigma_efetiva_y_btoc;

figure()
plot(sigma_real_y/1e6,YN,'linewidth',2)
eixo1a = xlabel({'$\sigma_{z}$ [MPa]'},'Interpreter','Latex');
eixo2a = ylabel({'z [m]'},'Interpreter','Latex');
tit1a = title('Stress in Casing','Interpreter','Latex');
% leg1a = legend('Above Well','Inner','Annular','AnnularCem','interpreter','latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
% set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');

figure()
plot(sigma_efetiva_y/1e6,YN,'linewidth',2)
eixo1a = xlabel({'$\sigma_{y}$ [MPa]'},'Interpreter','Latex');
eixo2a = ylabel({'y [m]'},'Interpreter','Latex');
tit1a = title('Stress in Casing','Interpreter','Latex');
% leg1a = legend('Above Well','Inner','Annular','AnnularCem','interpreter','latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
% set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');

figure()
hold on
plot(sigma_real_y/1e6,YN)
plot(sigma_efetiva_y/1e6,YN)
eixo1a = xlabel({'$\sigma_{y}$ [MPa]'},'Interpreter','Latex');
eixo2a = ylabel({'y [m]'},'Interpreter','Latex');
tit1a = title('Stress in Casing','Interpreter','Latex');
leg1a = legend('Real','Effective','interpreter','latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');

%% 

figure()
hold on
plot(sigma_real_y/1e6,YN)
% plot(sigma_efetiva_y/1e6,YN)
plot(sigmas_new1/1e6,ys_new1)
eixo1a = xlabel({'$\sigma_{y}$ [MPa]'},'Interpreter','Latex');
eixo2a = ylabel({'y [m]'},'Interpreter','Latex');
tit1a = title('Stress in Casing','Interpreter','Latex');
leg1a = legend('Novel','Last (Hydra)','interpreter','latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');

%% Novo teste com a expressão obtida de F_real

F_real_y_base_modelo = F_real_yb + rho_s * g * As * (yb-5250);
sigma_real_y_base_modelo = F_real_y_base_modelo / As

F_real_y_topo_modelo = F_real_yb + rho_s * g * As * (yb-2100);
sigma_real_y_topo_modelo = F_real_y_topo_modelo / As

%% Plotagem e comparação do modelo base

sigma_y_bottom_model = -0.077842 * 4150 + 346.254;

sigma_y_top_model = -0.077842 * 2500 + 346.254;


figure()
plot(sigma_real_y/1e6,YN,'linewidth',2)
hold on
scatter(sigma_y_bottom_model, 4150,'linewidth',2)
scatter(sigma_y_top_model, 2500,'linewidth',2)
eixo1a = xlabel({'$\sigma_{z}$ [MPa]'},'Interpreter','Latex');
eixo2a = ylabel({'z [m]'},'Interpreter','Latex');
tit1a = title('Stress in Casing','Interpreter','Latex');
% leg1a = legend('Above Well','Inner','Annular','AnnularCem','interpreter','latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
% set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');


%% Formulation without cement

% YNOCEM = H:0.1:yb;
% 
% sigma_b_nocem = rho_w * g * yb;
% sigma_z_nocem = sigma_b_nocem + rho_s * g * (yb-YNOCEM);

figure()
plot(sigma_real_y/1e6,YN,'linewidth',2)
hold on
plot(sigma_z_nocem/1e6,YN,'linewidth',2)
eixo1a = xlabel({'$\sigma_{z}$ [MPa]'},'Interpreter','Latex');
eixo2a = ylabel({'z [m]'},'Interpreter','Latex');
tit1a = title('Stress in Casing','Interpreter','Latex');
leg1a = legend('With cement','No cement','interpreter','latex');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');

%% Lendo os dois arquivos csv de tensão no casing e na rocha

% Lendo o primeiro arquivo
% dados1 = readtable('C:\Users\hidalgo\Desktop\Axisymmetric\StressesCement.csv');
dados1 = readtable('C:\Users\juani\Documents\Github\Abaqus_WELL\Other\StressesCement.csv');

% Lendo o segundo arquivo
% dados2 = readtable('C:\Users\hidalgo\Desktop\Axisymmetric\StressesNoCement.csv');
dados2 = readtable('C:\Users\juani\Documents\Github\Abaqus_WELL\Other\StressesNoCement.csv');

time_cement = table2array(dados1(1:401,1));
stress_casing_cement = table2array(dados1(1:401,2));

time_nocement = table2array(dados2(1:383,1));
stress_casing_nocement = table2array(dados2(1:383,2));

FontSize = 20;

figure()
plot(time_cement/(60*60*24*365),stress_casing_cement/1e6,'linewidth',2)
hold on
plot(time_nocement/(60*60*24*365),stress_casing_nocement/1e6,'linewidth',2)
eixo1a = xlabel({'Time [years]'},'Interpreter','Latex');
eixo2a = ylabel({'Mises [MPa]'},'Interpreter','Latex');
tit1a = title('Stress in Casing','Interpreter','Latex');
leg1a = legend('With cement','No cement','interpreter','latex','location','best');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
% set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');

time2_cement = table2array(dados1(:,3));
stress_rock_cement = table2array(dados1(:,4));

time2_nocement = table2array(dados2(:,3));
stress_rock_nocement = table2array(dados2(:,4));

figure()
plot(time2_cement/(60*60*24*365),stress_rock_cement/1e6)
hold on
plot(time2_nocement/(60*60*24*365),stress_rock_nocement/1e6)
eixo1a = xlabel({'Time [years]'},'Interpreter','Latex');
eixo2a = ylabel({'Mises [MPa]'},'Interpreter','Latex');
tit1a = title('Stress in Casing','Interpreter','Latex');
leg1a = legend('With cement','No cement','interpreter','latex','location','best');
set(eixo1a,'Fontsize',FontSize)
set(eixo2a,'Fontsize',FontSize)
set(tit1a,'Fontsize',FontSize)
set(leg1a,'Fontsize',FontSize)
% grid on
grid minor
% set(gca, 'YDir', 'reverse');
set(gca,'Fontsize',FontSize);
set(gcf,'Color','w');