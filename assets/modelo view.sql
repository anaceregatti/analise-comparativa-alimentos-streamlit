CREATE OR REPLACE VIEW `app-calculo-cardapio.TACO_USDA_DIR.food_data_nutrients_long` AS
WITH base AS (
  SELECT
    alimento_id, alimento, grupo, ivn, origem_animal,
    umidade_pct, energia_kcal, proteina_g, lipideos_g, colesterol_mg,
    carboidrato_g, fibra_alimentar_g,
    calcio_mg, magnesio_mg, manganes_mg, fosforo_mg, ferro_mg, sodio_mg, potassio_mg, cobre_mg, zinco_mg, se,
    rae_mcg, tiamina_mg, riboflavina_mg, niacina_mg, ac_pantontenico, piridoxina_mg, folato_dfe, vit_b12, c_mg,
    colina_total, vit_k_filoquinona, vit_a_ui, betacaroteno, vit_e_alfatocoferol, vitamina_d, luteina_zeoxantina,
    ac_graxos_total_saturados, col_18_e_1_indifernciado, col_18_e_2_indiferenciado, col_18_e_3_indiferenciado,
    col_22_e_6_n3_dha, col_20_e_5_n3_epa, ac_graxos_totais_monoinsaturados, ac_graxos_totais_poliinsaturados,
    triptofano, treonina, isoleucina, leucina, lisina, metionina, cisteina, tirosina, fenilalanina, valina, histidina
  FROM `app-calculo-cardapio.TACO_USDA_DIR.food_data_dir`
),
longo AS (
  SELECT
    alimento_id, alimento, grupo, ivn, origem_animal,
    nutriente,
    SAFE_CAST(REPLACE(CAST(valor AS STRING), ',', '.') AS FLOAT64) AS valor
  FROM base
  UNPIVOT ( valor FOR nutriente IN (
    umidade_pct, energia_kcal, proteina_g, lipideos_g, colesterol_mg,
    carboidrato_g, fibra_alimentar_g,
    calcio_mg, magnesio_mg, manganes_mg, fosforo_mg, ferro_mg, sodio_mg, potassio_mg, cobre_mg, zinco_mg, se,
    rae_mcg, tiamina_mg, riboflavina_mg, niacina_mg, ac_pantontenico, piridoxina_mg, folato_dfe, vit_b12, c_mg,
    colina_total, vit_k_filoquinona, vit_a_ui, betacaroteno, vit_e_alfatocoferol, vitamina_d, luteina_zeoxantina,
    ac_graxos_total_saturados, col_18_e_1_indifernciado, col_18_e_2_indiferenciado, col_18_e_3_indiferenciado,
    col_22_e_6_n3_dha, col_20_e_5_n3_epa, ac_graxos_totais_monoinsaturados, ac_graxos_totais_poliinsaturados,
    triptofano, treonina, isoleucina, leucina, lisina, metionina, cisteina, tirosina, fenilalanina, valina, histidina
  ))
)
SELECT
  'DIR' AS fonte,
  alimento_id, alimento, grupo, ivn, origem_animal, nutriente,
  CASE nutriente
    WHEN 'umidade_pct' THEN 'Umidade (%)'
    WHEN 'energia_kcal' THEN 'Energia (kcal)'
    WHEN 'proteina_g' THEN 'Proteína (g)'
    WHEN 'lipideos_g' THEN 'Lipídeos (g)'
    WHEN 'colesterol_mg' THEN 'Colesterol (mg)'
    WHEN 'carboidrato_g' THEN 'Carboidrato (g)'
    WHEN 'fibra_alimentar_g' THEN 'Fibra Alimentar (g)'
    WHEN 'calcio_mg' THEN 'Cálcio (mg)'
    WHEN 'magnesio_mg' THEN 'Magnésio (mg)'
    WHEN 'manganes_mg' THEN 'Manganês (mg)'
    WHEN 'fosforo_mg' THEN 'Fósforo (mg)'
    WHEN 'ferro_mg' THEN 'Ferro (mg)'
    WHEN 'sodio_mg' THEN 'Sódio (mg)'
    WHEN 'potassio_mg' THEN 'Potássio (mg)'
    WHEN 'cobre_mg' THEN 'Cobre (mg)'
    WHEN 'zinco_mg' THEN 'Zinco (mg)'
    WHEN 'se' THEN 'Se (µg)'
    WHEN 'rae_mcg' THEN 'RAE (mcg)'
    WHEN 'tiamina_mg' THEN 'Tiamina (mg)'
    WHEN 'riboflavina_mg' THEN 'Riboflavina (mg)'
    WHEN 'niacina_mg' THEN 'Niacina (mg)'
    WHEN 'ac_pantontenico' THEN 'Ác. Pantotênico (mg)'
    WHEN 'piridoxina_mg' THEN 'Piridoxina (mg)'
    WHEN 'folato_dfe' THEN 'Folato DFE (mcg)'
    WHEN 'vit_b12' THEN 'Vitamina B12 (µg)'
    WHEN 'c_mg' THEN 'Vitamina C (mg)'
    WHEN 'colina_total' THEN 'Colina Total (mg)'
    WHEN 'vit_k_filoquinona' THEN 'Vitamina K (filoquinona) (µg)'
    WHEN 'vit_a_ui' THEN 'Vitamina A (UI)'
    WHEN 'betacaroteno' THEN 'Betacaroteno (µg)'
    WHEN 'vit_e_alfatocoferol' THEN 'Vitamina E (alfa-tocoferol) (mg)'
    WHEN 'vitamina_d' THEN 'Vitamina D (µg)'
    WHEN 'luteina_zeoxantina' THEN 'Luteína + Zeaxantina (µg)'
    WHEN 'ac_graxos_total_saturados' THEN 'Ác. graxos total saturados (g)'
    WHEN 'col_18_e_1_indifernciado' THEN '18:1 indiferenciado (g)'
    WHEN 'col_18_e_2_indiferenciado' THEN '18:2 indiferenciado (g)'
    WHEN 'col_18_e_3_indiferenciado' THEN '18:3 indiferenciado (g)'
    WHEN 'col_22_e_6_n3_dha' THEN '22:6 n-3 (DHA) (g)'
    WHEN 'col_20_e_5_n3_epa' THEN '20:5 n-3 (EPA) (g)'
    WHEN 'ac_graxos_totais_monoinsaturados' THEN 'Ác. graxos totais monoinsaturados (g)'
    WHEN 'ac_graxos_totais_poliinsaturados' THEN 'Ác. graxos totais poliinsaturados (g)'
    WHEN 'triptofano' THEN 'Triptofano (g)'
    WHEN 'treonina' THEN 'Treonina (g)'
    WHEN 'isoleucina' THEN 'Isoleucina (g)'
    WHEN 'leucina' THEN 'Leucina (g)'
    WHEN 'lisina' THEN 'Lisina (g)'
    WHEN 'metionina' THEN 'Metionina (g)'
    WHEN 'cisteina' THEN 'Cisteína (g)'
    WHEN 'tirosina' THEN 'Tirosina (g)'
    WHEN 'fenilalanina' THEN 'Fenilalanina (g)'
    WHEN 'valina' THEN 'Valina (g)'
    WHEN 'histidina' THEN 'Histidina (g)'
    ELSE nutriente
  END AS nutriente_label,
  CASE
    WHEN nutriente = 'umidade_pct' THEN 'Água'
    WHEN nutriente = 'energia_kcal' THEN 'Energia'
    WHEN nutriente IN ('proteina_g','lipideos_g','carboidrato_g') THEN 'Macronutriente'
    WHEN nutriente = 'fibra_alimentar_g' THEN 'Fibra'
    WHEN nutriente IN ('colesterol_mg','ac_graxos_total_saturados','col_18_e_1_indifernciado',
                       'col_18_e_2_indiferenciado','col_18_e_3_indiferenciado','col_22_e_6_n3_dha',
                       'col_20_e_5_n3_epa','ac_graxos_totais_monoinsaturados','ac_graxos_totais_poliinsaturados')
         THEN 'Fração lipídeo'
    WHEN nutriente IN ('triptofano','treonina','isoleucina','leucina','lisina','metionina',
                       'cisteina','tirosina','fenilalanina','valina','histidina')
         THEN 'Aminoácido (fração proteínas)'
    WHEN nutriente IN ('calcio_mg','magnesio_mg','manganes_mg','fosforo_mg','ferro_mg',
                       'sodio_mg','potassio_mg','cobre_mg','zinco_mg','se')
         THEN 'Micronutriente - Mineral'
    WHEN nutriente IN ('rae_mcg','tiamina_mg','riboflavina_mg','niacina_mg','ac_pantontenico','piridoxina_mg',
                       'folato_dfe','vit_b12','c_mg','colina_total','vit_k_filoquinona','vit_a_ui','betacaroteno',
                       'vit_e_alfatocoferol','vitamina_d','luteina_zeoxantina')
         THEN 'Micronutriente - Vitamina'
    ELSE 'Outro'
  END AS categoria,
  CASE
    WHEN nutriente = 'umidade_pct' THEN 'teor de água no alimento (%)'
    WHEN nutriente = 'energia_kcal' THEN 'Calorias (kcal)'
    WHEN nutriente IN ('proteina_g','lipideos_g','carboidrato_g') THEN 'Macronutrientes'
    WHEN nutriente = 'fibra_alimentar_g' THEN 'Fibras (g)'
    WHEN nutriente IN ('colesterol_mg','ac_graxos_total_saturados','col_18_e_1_indifernciado',
                       'col_18_e_2_indiferenciado','col_18_e_3_indiferenciado','col_22_e_6_n3_dha',
                       'col_20_e_5_n3_epa','ac_graxos_totais_monoinsaturados','ac_graxos_totais_poliinsaturados')
         THEN 'Fração lipídeo'
    WHEN nutriente IN ('triptofano','treonina','isoleucina','leucina','lisina','metionina',
                       'cisteina','tirosina','fenilalanina','valina','histidina')
         THEN 'Aminoácido (fração proteínas)'
    WHEN nutriente IN ('calcio_mg','magnesio_mg','manganes_mg','fosforo_mg','ferro_mg',
                       'sodio_mg','potassio_mg','cobre_mg','zinco_mg','se')
         THEN 'Mineral'
    WHEN nutriente IN ('rae_mcg','tiamina_mg','riboflavina_mg','niacina_mg','ac_pantontenico','piridoxina_mg',
                       'folato_dfe','vit_b12','c_mg','colina_total','vit_k_filoquinona','vit_a_ui','betacaroteno',
                       'vit_e_alfatocoferol','vitamina_d','luteina_zeoxantina')
         THEN 'Vitamina'
    ELSE NULL
  END AS subcategoria,
  valor
FROM longo
WHERE valor IS NOT NULL;
