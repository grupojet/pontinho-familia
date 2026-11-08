# Benchmark — projetos e produtos semelhantes

Pesquisa na web em 08/11/2026. Os dados vêm de páginas de fabricantes, revendas e
fóruns; não foram verificados de forma independente. Onde dois anúncios divergiam, o
valor está marcado como aproximado.

## 1. Roçadeiras rotativas de fábrica para escavadeira (acionamento direto)

| Produto | Largura | Massa | Vazão | Pressão | Motor / transmissão | Porte da escavadeira |
|---|---|---|---|---|---|---|
| Diamond Mowers Excavator Rotary 50" / 60" | 1,27 / 1,52 m | 730 / 845 kg | 75–175 L/min | 207 bar | pistões, direto (sem caixa) | 6–25 t / 10–25 t |
| Diamond Mowers 72" | 1,83 m | ≈ 1 040 kg | 60–155 L/min | 207 bar | pistões, direto | até 25 t |
| Blue Diamond Brush Cutter 60" Extreme Duty | 1,52 m | ≈ 545 kg | — | — | opções de motor **80, 100, 125 e 160 cm³** | escavadeira |
| Brush Wolf Heavy-Duty X 42"/48" | 1,07 / 1,22 m | ≈ 400 kg | 53–140 L/min | — | pistões radiais, direto; mancal Eskridge | mini/retro |
| Brush Wolf Full-Size HD X 60"/72" | 1,52 / 1,83 m | ≈ 785 kg | 75–170 L/min | — | pistões, direto; mancal Eskridge eixo 3,75" (95 mm) | escavadeira |
| Brush Wolf Standard-Duty X 36"–48" | 0,9–1,2 m | ≈ 315 kg | 30–150 L/min | — | motor Geroler + **caixa de 90° original** (igual à nossa Opção B) | mini/retro |
| Baumalight CXC530 / 542 / 550 | 0,76–1,27 m | — | 30–190 L/min | — | pistões de eixo inclinado, **dreno de carcaça "crítico"**; não recomendam rotor > 1 800 rpm acima de 42" | 2–10 t |
| MenSe RP8L (Finlândia) | 1,90 m | 305 kg | 80–100 L/min | 200 bar | duas facas, leve | 8–15 t |
| FAE RCM/SSL-175 (para minicarregadeira) | 1,86 m | 910 kg | 90–170 L/min | — | orbital 195 cm³ | 75–135 hp |

## 2. Produtos brasileiros encontrados

| Fabricante | Produto | Observação |
|---|---|---|
| MK Engenharia (Mafra/SC) | roçadeira hidráulica para escavadeiras de 2,5 a 10 t | facas rotativas, válvula anti-choque; sem ficha técnica pública |
| Super Metal | roçadeira hidráulica p/ escavadeira, retro e pá | 860 kg, seis lâminas, vegetação até 40 mm |
| Deltractor | DELRC1500 / HD | para minicarregadeira e retroescavadeira |
| War Equipamentos | WAR55RC 1,4 m | para minicarregadeira |

## 3. Conversões caseiras de roçadeira de TDP (fóruns TractorByNet, HeavyEquipmentForums, AgTalk)

Padrão recorrente das conversões relatadas:

- **Motor na entrada da caixa cônica**, acoplado por luva estriada 1 3/8"–6 estrias, com
  deslocamentos de 6,5 a 9,6 pol³ (107–157 cm³) para 540–600 rpm com 17–20 gpm
  (65–75 L/min). Um fabricante europeu (Hydrokit) vende kit pronto nesse conceito:
  motor 100 cm³, 540 rpm com 55 L/min, 18 kW a 210 bar.
- **Acionamento direto** com acoplamento de garras (Lovejoy) entre motor e cubo do
  porta-facas, sem caixa — relatado por quem já construiu roçadeira hidráulica.
- Mancal do rotor: construtores buscam caixas de mancal fundidas (Omni Gear) ou
  improvisam com cubo de eixo de reboque (não recomendado).
- Avisos repetidos: válvula de alívio/cushion no motor, retenção para roda-livre
  (o rotor vira bomba ao cortar o fluxo), dreno de carcaça, pino de cisalhamento ou
  embreagem como limitador de torque, e acionar o fluxo com o motor diesel em marcha
  lenta para evitar choque nas facas.
- Lacunas: nenhum tópico traz cálculo de eixo, mancal ou frenagem; vários relatam
  vedação do motor rompida por operar acima de ≈ 200 bar sem alívio.

## 4. Circuito X1 Volvo

Nenhuma fonte oficial com números de vazão/pressão do X1 foi encontrada; o folheto
Volvo só diz que vazão e pressão são ajustáveis na cabine. Anúncios de máquinas usadas
citam 115–120 L/min (EC140) e 160 L/min (EC220) para o auxiliar. **Confirmar no manual
da máquina ou na concessionária** antes de ajustar o IECU.

## 5. Comparação com o nosso projeto

| Item | Nosso projeto | Mercado | Conclusão |
|---|---|---|---|
| Motor | A2FM 125 (pistões, direto) | Blue Diamond oferece 80–160 cm³; Diamond e Brush Wolf HD usam pistões diretos | dentro da faixa, mantido |
| Vazão | 117 L/min a 210 bar | 75–175 L/min a 207 bar para 1,5 m | coerente |
| Massa | ≈ 520 kg | 545 kg (Blue Diamond 60") a 845 kg (Diamond 60") | nosso deck é agrícola, mais leve; reforço de 9,5 mm é indispensável |
| Eixo do rotor | Ø60 mm, FS 3,2 p/ 20 kN | Brush Wolf HD: 82–95 mm (corta troncos de 250 mm) | **se a meta incluir troncos > 50 mm, subir para Ø75–80 mm e rolamentos 32215/32216** |
| Rotação | 891 rpm (70 m/s) | Baumalight limita a 1 800 rpm acima de 42" | ok |
| Dreno de carcaça | obrigatório, linha própria | Baumalight: "crítico"; fóruns: causa comum de falha | confirmado |
| Freio / anticavitação | bloco com alívio cruzado + retenção | prática padrão nos produtos e exigência dos fóruns | confirmado |
| Opção B (caixa original) | alternativa | Brush Wolf Standard-Duty e kit Hydrokit usam exatamente isso | validada como caminho de baixo custo |
| Proteção da cabine | grade frontal/teto | Diamond e Baumalight exigem | mantido |

## 6. Fontes

- Diamond Mowers — [folheto Excavator Rotary Mower](https://info.diamondmowers.com/hubfs/Diamond%20Mowers%20-%20Excavator%20Rotary%20Mower%20-%20Brochure.pdf), [folheto Excavator Heads](https://info.diamondmowers.com/hubfs/Diamond_Mowers_Excavator_Brochure.pdf), [Parish Tractor](https://www.parishtractor.com/product/excavator-rotary-mowers)
- Blue Diamond — [Mini Excavator Brush Cutter HD](https://www.bluediamondattachments.com/mini-excavator-brush-cutter-heavy-duty), [Brush Cutter 60 Extreme Duty spec sheet](https://www.bluediamondattachments.com/uploads/specs/Brush-Cutter-60-Extreme-Duty-Excavator-Spec-Sheet-101624.pdf)
- Brush Wolf — [Heavy-Duty X](https://rippingitoutdoors.com/products/brush-wolf-heavy-duty-x-brush-cutter-series-cutting-width-42-48-inches-hydraulic-flow-range-14-37-gpm-for-excavators-backhoe), [Full-Size HD X](https://rippingitoutdoors.com/products/brush-wolf-full-size-heavy-duty-x-brush-cutter-series-cutting-width-60-72-inches-hydraulic-flow-range-20-45-gpm-for-excavators-backhoe), [Standard-Duty X](https://m.reach.dog/shop/ripping-it-outdoors/products/brush-wolf-standard-duty-x-brush-cutter-series-cutting-width-36-42-48-inches-hydraulic-flow-range-8-40-gpm-for-excavators-backhoe), [página para escavadeiras](https://www.brushwolf.com/brush-cutters/excavators-backhoes/)
- Baumalight — [CXC530](https://baumalight.com/cutters/en/cxc530.php?usa), [CXC542](https://baumalight.com/cutters/en/cxc542.php?cad), [manual do operador CXC](https://baumalight.com/support/pdf/brushcutt/sn/owner_manuals/CXC530/CXC%20Brush%20Cutt%20OM.pdf)
- FAE — [RCM/SSL ficha](https://www.fae-group.com/en_AU/media/download/2025/07/rcm_ssl_rotary_cutters_for_skid_steers_fae_en-ap_13512.pdf), [RCM/SSL produto](https://www.fae-group.com/en_CA/products/land-clearing/hydraulic-driven-heads/rotary-cutters-for-skid-steers/rcm-ssl)
- MenSe RP — [AgriExpo](https://www.agriexpo.online/pt/prod/clark-engineering/product-4601556-189817.html)
- Hydrokit — [kit motor hidráulico TDF 100 cm³](https://www.hydrokit.com/en/produit/agricultural/tools-drive/hydraulic-pto/pto-hyd-motor-kit-100cm3-18kw-xrp15536-xpr245128.html), [kit supressão de cardan](https://www.hydrokit.com/agricultural/trailer-solutions/cardan-shaft-suppression-kit-xrp20054.html)
- Brasil — [MK Engenharia](https://www.mkengenharia.ind.br/#contato), [Super Metal](https://supermetal.com.br/implementos/rocadeira-hidraulica/), [Deltractor](https://deltractor.com.br/rocadeira), [War Equipamentos](https://www.warequipamentos.com.br/acessorios-mini-carregadeira/rocadeira-hidraulica-simples-warrc1400)
- Fóruns — [Running a PTO bush hog off excavator](https://www.tractorbynet.com/forums/threads/running-a-pto-bush-hog-off-excavator.431077/), [Brush Hog conversion from PTO to Hydraulic](https://www.tractorbynet.com/forums/threads/brush-hog-conversion-from-pto-to-hydraulic.381109/), [Hydraulic motor help / rotary cutter conversion](https://www.tractorbynet.com/forums/threads/hydraulic-motor-help-rotary-cutter-conversion.310400/), [Hydraulic brush hog on excavator – return line](https://www.tractorbynet.com/forums/threads/hydraulic-rush-hog-on-excavator-return-line.386571/), [Source for bearing housing](https://www.tractorbynet.com/forums/threads/source-for-cast-iron-bearing-housing-for-hydraulic-motor-driven-shredder-brush-cutter.430855/), [Modifying bush hog from PTO to hydraulic](https://www.heavyequipmentforums.com/threads/modifing-bush-hog-from-pto-driven-to-hydraulic.39800/), [Building bush hog – motor choice](https://www.heavyequipmentforums.com/threads/building-bush-hog-need-help-with-hyd-motor-choice.18845/)
- Patentes — [US9648806 Hydraulic brush cutter](https://patents.google.com/patent/US9648806), [US7980278 Brush cutting head with internally housed drive and bearing](https://patents.google.com/patent/US7980278)
- Volvo — [EC200E/EC220E folheto](https://www.volvoce.com/-/media/volvoce/local/emea/europe/excavators/volvocomparisonbrochurecrawlerexcavatorec200eec220eenglish.pdf?v=D4pKPw)
