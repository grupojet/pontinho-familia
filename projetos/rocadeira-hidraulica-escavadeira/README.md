# Projeto: Roçadeira hidráulica para braço de escavadeira Volvo

**Conversão de roçadeira de arrasto (TDP 540 rpm, engate de 3 pontos) em implemento
hidráulico pino-a-pino, com facas acionadas por motor hidráulico alimentado pelo
circuito auxiliar X1 (linha de martelo) da escavadeira.**

| Item | Conteúdo |
|---|---|
| Memorial descritivo e de cálculo | este arquivo |
| Cálculos reproduzíveis | [`calculos.py`](calculos.py) (`python3 calculos.py`) |
| Esquema hidráulico | [`esquema-hidraulico.svg`](esquema-hidraulico.svg) |
| Layout mecânico (vistas superior e lateral) | [`layout-mecanico.svg`](layout-mecanico.svg) |
| Detalhe 01 — eixo porta-facas e mancal, com cotas | [`detalhe-mancal.svg`](detalhe-mancal.svg) |
| Foto do implemento original | [`imagens/rocadeira-original.jpg`](imagens/rocadeira-original.jpg) |
| Benchmark de produtos e conversões semelhantes | [`benchmark.md`](benchmark.md) |

Revisão 1 — 09/11/2026 — projeto básico com detalhe do mancal e benchmark (rev. 0 em 08/11/2026). Antes da fabricação:
medir o implemento real, confirmar modelo da escavadeira e os dados do circuito X1
no manual Volvo, e submeter a revisão por engenheiro mecânico habilitado com emissão
de ART (o projeto envolve segurança de operador e terceiros).

---

## 1. Objeto e premissas

### 1.1 Equipamento de partida (conforme foto)

Roçadeira rotativa de facas articuladas, marca Netz, modelo com deck de chapa
dobrada, cabeçalho de engate de 3 pontos, caixa cônica central com entrada
horizontal para cardan de TDP (1 3/8" — 6 estrias, 540 rpm) com embreagem de
atrito, dois patins laterais, roda traseira de apoio e cortina de corrente.

Valores adotados (confirmar com trena e balança):

| Parâmetro | Valor adotado |
|---|---|
| Largura de corte / diâmetro de varredura | 1,50 m |
| Largura externa do deck | ≈ 1,60 m |
| Relação da caixa cônica | 1 : 1,47 (540 → ≈ 794 rpm no rotor) |
| Velocidade de ponta original | ≈ 62 m/s |
| Potência de trator recomendada pelo fabricante | 40 – 50 cv |
| Massa da roçadeira original | ≈ 300 kg |

### 1.2 Escavadeira

O usuário informou apenas "Volvo". O projeto é parametrizado para a faixa
**14 t a 22 t** (EC140, ECR145, EC200, EC210, EC220 — séries D/E), que é a faixa
coerente com um deck de 1,5 m (≈ 520 kg convertido). Dados a confirmar no manual do
operador e no menu de ferramentas do IECU (display) da máquina:

| Dado | Onde obter | Uso no projeto |
|---|---|---|
| Vazão máxima do circuito X1 (1 bomba) em modo martelo | manual / IECU | limitar a 117 L/min para o motor escolhido |
| Pressão de alívio do X1 | manual / IECU | 210 bar adotado como referência |
| Existência de linha de dreno (X3) ou necessidade de instalar retorno livre ao tanque | manual / concessionária | dreno de carcaça do motor |
| Diâmetro dos pinos da caçamba, entre-eixos e largura entre orelhas | medir na caçamba | cabeçote pino-a-pino |
| Tipo de engate rápido (S60/S70, pino-a-pino, Steelwrist) | visual | interface do cabeçote |

Valores típicos: pinos Ø70 mm (classe 14 t) e Ø80 mm (classe 20–22 t); vazão X1 de
1 bomba entre 150 e 220 L/min; pressão 200–250 bar.

### 1.3 Requisitos de projeto

1. Facas acionadas somente por fluxo de óleo do X1 (sem cardan, sem caixa cônica).
2. Velocidade de ponta das facas entre 60 e 80 m/s (igual ou superior à original).
3. Potência de corte contínua ≥ 28 kW (equivalente ao trator de 40–45 cv).
4. Motor hidráulico **não suporta cargas radiais nem axiais do rotor**.
5. Parada do rotor em ≤ 5 s após fechar o circuito, sem cavitação do motor.
6. Proteção contra arremesso de detritos em 360° e proteção da cabine.
7. Interface com a escavadeira idêntica à de uma caçamba (pinos originais).
8. Massa total ≤ 600 kg (abaixo da caçamba padrão de uma 14 t).

---

## 2. Concepção adotada

### 2.1 Alternativas analisadas

| | Opção A — motor vertical, acionamento direto (**adotada**) | Opção B — motor horizontal na entrada da caixa cônica |
|---|---|---|
| Descrição | Remove-se caixa cônica; novo mancal com eixo Ø60 apoiado em dois rolamentos cônicos; motor de pistões flangeado em cima, acoplado por luva estriada | Mantém a caixa; o cardan é substituído por um motor de pistões acoplado na estria 1 3/8" de entrada |
| Motor | A2FM 125 (125 cm³) a ≈ 890 rpm, 117 L/min | A2FM 180 (180 cm³) a ≈ 606 rpm, 115 L/min |
| Rendimento | motor 0,85 | motor 0,85 × caixa 0,95 |
| Altura do conjunto | baixa, CG centrado | motor horizontal saliente, mais exposto a galhos |
| Fabricação | mancal usinado (torno + fresa) | suporte soldado simples |
| Custo relativo | médio | baixo |
| Confiabilidade | padrão da indústria (roçadeiras hidráulicas de fábrica) | depende do estado da caixa; retentor de entrada sujeito a carga do acoplamento |

A **Opção A** é a solução de engenharia correta e compacta. A Opção B é aceitável
como protótipo rápido e os cálculos para ela constam no `calculos.py` (seção 4).

### 2.2 Descrição da Opção A

1. **Desmontagem**: retirar cardan, caixa cônica, cabeçalho de 3 pontos (torre e
   braços), roda traseira e seu garfo. Manter deck, disco porta-facas, facas,
   pinos de faca, patins e cortinas (que serão substituídas por mais pesadas).
2. **Reforço do deck**: chapa de 9,5 mm (3/8") soldada sobre o topo, 1 000 × 900 mm,
   centrada no eixo do rotor, com furação para o mancal e para o cabeçote. Reforçar
   as faces laterais internamente com cantoneira 3" × 3/8" na região dos patins.
3. **Mancal do rotor**: tubo mecânico Ø150 × 20 mm, comprimento 260 mm, usinado internamente a Ø110 H7 para os rolamentos, com dois
   rolamentos de rolos cônicos 32212 montados em "O", retentores em ambas as
   extremidades, graxeira e furo de alívio. Flange inferior soldado ao tubo e
   parafusado à chapa de reforço (8 × M16 cl. 10.9). Eixo Ø60 em SAE 1045
   beneficiado, com flange inferior para o disco porta-facas (mesma furação do disco
   original) e ponta superior estriada.
4. **Motor hidráulico**: Bosch Rexroth A2FM 125/61W (eixo inclinado, deslocamento
   fixo) ou equivalente Parker F12-110 / Danfoss H1B 110. Flange SAE sobre placa
   adaptadora de 25 mm parafusada ao topo do mancal. Transmissão por luva estriada
   bipartida (estria do motor ↔ estria do eixo), que admite pequenos desalinhamentos
   e desacopla cargas radiais.
5. **Bloco de controle do motor** fixado no deck junto ao motor (ver §4).
6. **Cabeçote pino-a-pino**: duas chapas laterais de 40 mm (LNE 500 ou Hardox 450)
   em forma trapezoidal, centradas no eixo do rotor e espaçadas conforme a largura
   entre orelhas da caçamba, unidas por travessas e por uma base de 20 mm
   parafusada/soldada à chapa de reforço. Buchas de aço temperado nos furos dos
   pinos, com graxeiras.
7. **Proteções**: cortinas de corrente em todas as faces (elos Ø8 mm, passo 50 mm,
   dupla fileira na frente), chapa defletora traseira, para-choque dianteiro em tubo
   Ø76 × 6 mm que também protege o motor e as mangueiras.
8. **Hidráulica**: mangueiras 1" (pressão SAE 100R13 e retorno SAE 100R12) e dreno
   1/2" SAE 100R2, com engates rápidos de face plana ISO 16028 no braço, protegidas
   por espiral e fixadas com abraçadeiras ao longo do braço (não ao cabeçote).

---

## 3. Memorial de cálculo (resumo — valores de `calculos.py`)

### 3.1 Rotação e torque do rotor

| Grandeza | Fórmula | Resultado |
|---|---|---|
| Rotação para 70 m/s | n = v / (π·D) · 60 | **891 rpm** (93,3 rad/s) |
| Torque contínuo para 28 kW | T = P / ω | **300 N·m** |
| Potência hidráulica bruta disponível (150 L/min × 210 bar) | P = Q·p | 52,5 kW |
| Δp útil no motor (210 − 20 bar de retorno) | | 190 bar |

### 3.2 Seleção do motor (Opção A, acionamento direto)

| Grandeza | Fórmula | Resultado |
|---|---|---|
| Deslocamento mínimo | V = 2π·T / (Δp·η_mh) | 110 cm³/rev |
| Vazão a 891 rpm | Q = V·n / η_v | 103 L/min |

Verificação dos motores comerciais a Δp = 190 bar:

| Motor | Torque (N·m) | Vazão a 891 rpm (L/min) | Potência no eixo (kW) | Rotação com 150 L/min |
|---|---|---|---|---|
| A2FM 107 / F12-110 | 291 | 100 | 27,2 | 1 332 rpm |
| **A2FM 125** | **340** | **117** | **31,8** | 1 140 rpm |
| A2FM 160 | 435 | 150 | 40,6 | 891 rpm |

**Adotado A2FM 125**: 13 % de reserva de torque sobre o requisito, vazão de 117 L/min
dentro do X1 de qualquer máquina da faixa, rotação máxima do motor (≈ 3 000 rpm)
muito acima do uso. Ajustar a vazão no IECU para **120 L/min**; a pressão de alívio
do X1 (210 bar) atua como limitador de torque, substituindo a embreagem de atrito do
cardan original.

### 3.3 Energia do rotor e frenagem

| Grandeza | Resultado |
|---|---|
| Momento de inércia (disco 22 kg Ø600 + 2 facas 4 kg a r = 0,68 m) | 4,69 kg·m² |
| Energia cinética a 891 rpm | 20,4 kJ |
| Torque de frenagem com alívio cruzado a 150 bar | 298 N·m |
| **Tempo de parada** | **≈ 1,5 s** (atende ≤ 5 s) |

Sem válvula de freio o rotor gira em roda-livre por mais de um minuto e o motor,
agindo como bomba sem alimentação, cavita e se danifica. O bloco de freio com
anticavitação é **obrigatório** (§4).

### 3.4 Eixo e rolamentos do mancal

| Verificação | Resultado |
|---|---|
| Tensão de torção com 300 N·m no Ø60 | 7 MPa (desprezível) |
| Impacto radial admitido de 20 kN no disco, balanço de 150 mm | M = 3 000 N·m → σ = 141 MPa |
| Tensão equivalente de von Mises | 142 MPa → **FS = 3,2** contra Sy = 450 MPa |
| Vida L10h do par 32212 (C = 125 kN) com carga equivalente 6 kN a 891 rpm | > 400 000 h |

As facas articuladas (pinos de faca originais) limitam o pico de carga transmitido
ao eixo em choque com pedra ou toco. Manter os pinos de faca e substituí-los a cada
troca de facas.

**Variante reforçada** (escolher se o uso incluir troncos acima de 50 mm, como fazem as
roçadeiras de fábrica do benchmark, que usam eixos de 82 a 95 mm):

| Verificação | Resultado |
|---|---|
| Eixo Ø80 mm em SAE 4140 beneficiado, impacto radial de 40 kN, balanço 150 mm | σ_eq = 119 MPa → **FS = 3,8** |
| Rolamentos 32216 (C = 190 kN), carga equivalente 10 kN a 891 rpm | L10h > 300 000 h |
| Carcaça | tubo Ø180 × 20 usinado a Ø140 H7 |

O desenho [`detalhe-mancal.svg`](detalhe-mancal.svg) traz a versão padrão Ø60 cotada e,
em nota, as dimensões da versão reforçada.

### 3.5 Mangueiras (a 117 L/min)

| Linha | Diâmetro | Velocidade | Limite | Situação |
|---|---|---|---|---|
| Pressão (A) | 1" | 3,9 m/s | 6 m/s | ok |
| Retorno (B) | 1" | 3,9 m/s | 4 m/s | ok |
| Dreno (T) | 1/2" | 0,6 m/s | — | ok, pressão de carcaça ≤ 2 bar |

### 3.6 Térmico

Perdas estimadas (motor + linhas + contrapressão) ≈ 12 kW. O trocador da escavadeira
é dimensionado para martelo hidráulico (regime semelhante). Monitorar temperatura do
óleo ≤ 80 °C nos ensaios; se exceder, reduzir vazão no IECU para ≈ 105 L/min.

### 3.7 Cabeçote pino-a-pino

Força dinâmica de referência: 520 kg × g × 3 = 15 kN. Cisalhamento duplo nos pinos
Ø70/Ø80: 1,5 a 2 MPa (irrelevante). O esforço dimensionante é a força do cilindro
da caçamba ao empurrar o deck contra o solo ou contra troncos, que não é controlável
por projeto do implemento. Por isso as orelhas copiam a espessura e o material das
orelhas da caçamba original (≈ 40 mm) e a base do cabeçote distribui a carga em uma
chapa de 9,5 mm soldada em todo o topo do deck.

---

## 4. Circuito hidráulico (ver `esquema-hidraulico.svg`)

Topologia: X1 em modo **martelo** (fluxo unidirecional, retorno de baixa pressão).
Rotação sempre no mesmo sentido; o sentido deve coincidir com o gume das facas
(conferir antes do primeiro acionamento; se invertido, trocar A e B no bloco).

Bloco de controle do motor (manifold em alumínio ou aço, cavidades SAE/Sun), instalado
no deck ao lado do motor:

| Função | Componente | Ajuste inicial |
|---|---|---|
| Limitação de pressão no sentido motor (proteção contra travamento) | válvula de alívio cruzado A → B | 230 bar (acima do alívio da máquina, só atua em pico) |
| Freio do rotor ao fechar o circuito | válvula de alívio cruzado B → A | 150 bar |
| Reposição de óleo durante a frenagem | válvula de retenção anticavitação B → A (retorno → entrada) | abertura 0,3 bar |
| Diagnóstico | tomada de teste tipo minimess na linha A | — |
| Dreno de carcaça do motor | linha T independente, sem válvulas, direta ao tanque | pressão ≤ 2 bar |

Componentes de linha:

| Item | Especificação |
|---|---|
| Mangueira de pressão | 1" SAE 100R13, 4SH, 350 bar, terminais JIC 1 5/16" ou flange SAE 6000 |
| Mangueira de retorno | 1" SAE 100R12, terminais idem |
| Mangueira de dreno | 1/2" SAE 100R2 |
| Engates rápidos | face plana ISO 16028, 1" (A e B) e 1/2" (T), com tampas |
| Fluido | o mesmo da escavadeira (ISO VG 46 ou conforme manual Volvo) |

Se a máquina não tiver linha de dreno dedicada no braço, instalar um retorno livre
ao tanque (kit de dreno Volvo ou tubulação própria) — **nunca** unir o dreno à linha
de retorno B, porque a contrapressão de retorno (≈ 20 bar) excede o limite do
retentor do motor.

---

## 5. Lista de materiais (BOM) — Opção A

| # | Descrição | Qtd | Observação |
|---|---|---|---|
| 1 | Motor hidráulico Rexroth A2FM 125/61W-VAB010 (ou Parker F12-110, Danfoss H1B 110) | 1 | flange SAE C 4 furos, eixo estriado |
| 2 | Bloco de controle do motor (alívio cruzado 2×, anticavitação, minimess) | 1 | ex.: Sun Hydraulics / Hydac / Bucher, 150 L/min |
| 3 | Rolamento de rolos cônicos 32212 | 2 | SKF / FAG / Timken |
| 4 | Retentor 60 × 85 × 10 (sup.) e 70 × 100 × 10 (inf.) | 1 + 1 | lábio duplo, NBR |
| 5 | Tubo mecânico Ø150 × 20 mm, L = 260 mm, furo usinado Ø110 H7 | 1 | SAE 1020/1045 |
| 6 | Eixo Ø65 × 450 mm em SAE 1045 beneficiado (bruto p/ usinar Ø60) | 1 | estria DIN 5480 ou SAE conforme motor |
| 7 | Luva estriada bipartida (motor ↔ eixo) | 1 | ou acoplamento de garras tipo Rotex 48 |
| 8 | Chapa 9,5 mm ASTM A36 1 000 × 900 mm (reforço do deck) | 1 | |
| 9 | Chapa 40 mm LNE 500 / Hardox 450 (orelhas do cabeçote) | 2 | conforme medidas da caçamba |
| 10 | Chapa 20 mm A36 (base e travessas do cabeçote) | 1 | ≈ 0,6 m² |
| 11 | Buchas de aço temperado para pinos Ø70 ou Ø80 | 4 | com graxeiras |
| 12 | Cantoneira 3" × 3/8" (reforço interno lateral) | 4 m | |
| 13 | Tubo Ø76 × 6 mm (para-choque / proteção do motor) | 4 m | |
| 14 | Corrente elo Ø8 mm (cortinas) | 60 m | dupla fileira frontal |
| 15 | Chapa 12,7 mm (patins novos) | 2 | perfil copiado dos originais |
| 16 | Mangueiras, terminais e engates (ver §4) | kit | comprimento conforme braço |
| 17 | Parafusos M16 cl. 10.9, porcas e arruelas travantes | 24 | |
| 18 | Facas e pinos de faca | jogo novo | originais Netz |
| 19 | Grade de proteção da cabine (policarbonato 12 mm + tela) | 1 | frontal e teto |

---

## 6. Sequência de fabricação e montagem

1. Medir a roçadeira (diâmetro de varredura, furação do disco, altura do deck) e a
   caçamba da escavadeira (Ø pinos, entre-eixos, largura entre orelhas). Atualizar
   os parâmetros em `calculos.py` e os desenhos.
2. Desmontar cardan, caixa, cabeçalho de 3 pontos, roda e cortinas. Lavar o deck.
3. Recuperar trincas e amassados do deck; cortar e soldar a chapa de reforço (solda
   MIG, eletrodo ER70S-6, cordões intermitentes 50/100 mm + contorno completo).
4. Usinar eixo, tubo do mancal, flanges e placa adaptadora. Montar rolamentos com
   pré-carga leve, encher 2/3 de graxa EP2.
5. Posicionar o mancal no centro geométrico do rotor (verificar com o disco montado:
   folga uniforme às paredes do deck), parafusar.
6. Soldar o cabeçote centrado no eixo do rotor; verificar paralelismo dos furos dos
   pinos com gabarito (tolerância 0,5 mm). Soldar com pré-aquecimento 100–150 °C nas
   chapas de alta resistência, eletrodo compatível (E7018 ou ER80S).
7. Montar motor, luva, bloco, mangueiras. Torquear M16 cl. 10.9 a 210 N·m.
8. Montar disco, facas novas e pinos. Balancear o conjunto estaticamente
   (diferença de massa entre facas ≤ 10 g).
9. Instalar cortinas, patins novos, para-choque e proteção de cabine.
10. Pintar e identificar (placa com massa, pressão e vazão máximas, sentido de giro).

---

## 7. Comissionamento e ensaios

1. Com o rotor **sem facas**, acoplar na escavadeira, conectar linhas e ligar no IECU
   o modo martelo com vazão mínima (≈ 40 L/min). Verificar sentido de giro, ruídos e
   vazamentos. Medir pressão na tomada minimess.
2. Aumentar a vazão em degraus de 20 L/min até 120 L/min. Registrar pressão e
   temperatura do óleo a cada degrau; pressão em vazio esperada entre 40 e 70 bar.
3. Ensaiar a frenagem: fechar o circuito a 120 L/min e cronometrar a parada do rotor
   (alvo ≤ 5 s). Ajustar a válvula de freio se necessário (nunca acima de 180 bar).
4. Montar as facas e repetir os itens 2 e 3 com o implemento a 300 mm do solo.
5. Ensaio em campo: 30 min em capim alto, depois 30 min em vegetação arbustiva
   até Ø 50 mm. Verificar temperatura do mancal (≤ 70 °C ao toque com termômetro
   infravermelho), temperatura do óleo (≤ 80 °C), aperto dos parafusos e trincas nas
   soldas (líquido penetrante no cabeçote após o primeiro dia).
6. Emitir relatório de comissionamento e liberar para operação.

---

## 8. Segurança operacional

- Operar somente com a grade de proteção da cabine instalada e as portas fechadas.
- Raio de exclusão de **100 m** para pessoas e veículos durante o corte.
- Nunca levantar o deck acima da altura dos olhos de uma pessoa com o rotor girando
  (as cortinas deixam de confinar os detritos).
- Não usar o deck como lâmina, martelo ou alavanca; o esforço do braço destrói o
  cabeçote e o deck.
- Antes de qualquer manutenção: rotor parado, motor da escavadeira desligado,
  pressão aliviada no X1, implemento apoiado no solo.
- Inspecionar facas, pinos de faca e cortinas diariamente. Facas trincadas ou com
  desgaste > 20 mm são descartadas em par.
- Manter o adesivo de sentido de giro e a placa de identificação legíveis.

---

## 9. Referências normativas e técnicas

- NR-12 — Segurança no trabalho em máquinas e equipamentos (proteções, aviso, parada).
- ISO 20474 / ABNT NBR ISO 20474 — máquinas de terraplenagem, requisitos de segurança.
- ISO 10263 / ISO 3449 (FOPS) e ISO 3471 (ROPS) — proteção do operador.
- ISO 4254-12 — máquinas agrícolas: segurança de roçadeiras rotativas (critério de
  velocidade de ponta e cortinas).
- Bosch Rexroth RE 91001 — motor A2FM (dados de rotação, pressão e dreno).
- Volvo CE — manual do operador e Service Manual da escavadeira (ajuste de X1,
  vazão/pressão por ferramenta no IECU).
- Shigley, *Projeto de Engenharia Mecânica* — critérios de eixos e rolamentos.
