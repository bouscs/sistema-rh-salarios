INSERT INTO taxas (iden, date_created, chave, valor) 
    select 1, '20-05-2021', 'inss_base_a', 82.5 from dual union all
    select 2, '20-05-2021', 'inss_base_b', 99.31 from dual union all
    select 3, '20-05-2021', 'inss_base_c', 132.2076 from dual union all
    select 4, '20-05-2021', 'inss_banda_a', 1100 from dual union all
    select 5, '20-05-2021', 'inss_banda_b', 2203.48 from dual union all
    select 6, '20-05-2021', 'inss_banda_c', 3305.22 from dual union all
    select 7, '20-05-2021', 'inss_fator_a', 0.075 from dual union all
    select 8, '20-05-2021', 'inss_fator_b', 0.09 from dual union all
    select 9, '20-05-2021', 'inss_fator_c', 0.12 from dual union all
    select 10, '20-05-2021', 'inss_fator_d', 0.14 from dual union all
    select 11, '20-05-2021', 'inss_banda_d', 6433.57 from dual union all
    select 12, '20-05-2021', 'inss_retorno_d', 751.97 from dual union all
    select 13, '20-05-2021', 'ir_dependente', 189.59 from dual union all
    select 14, '20-05-2021', 'ir_banda_a', 1903.98 from dual union all
    select 15, '20-05-2021', 'ir_banda_b', 2826.66 from dual union all
    select 16, '20-05-2021', 'ir_banda_c', 3751.06 from dual union all
    select 17, '20-05-2021', 'ir_banda_d', 4664.68 from dual union all
    select 18, '20-05-2021', 'ir_fator_a', 0.075 from dual union all
    select 19, '20-05-2021', 'ir_fator_b', 0.15 from dual union all
    select 20, '20-05-2021', 'ir_fator_c', 0.225 from dual union all
    select 21, '20-05-2021', 'ir_fator_d', 0.275 from dual union all
    select 22, '20-05-2021', 'ir_const_a', 142.8 from dual union all
    select 23, '20-05-2021', 'ir_const_b', 354.80 from dual union all
    select 24, '20-05-2021', 'ir_const_c', 636.13 from dual union all
    select 25, '20-05-2021', 'ir_const_d', 869.36 from dual;
    