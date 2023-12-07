#TRATAR UMA LISTA
"""original = ['cub_r8_pdrnorm', 'slr_min', 'prod_aco_bruto','aco_vd_int', 'aco_vd_ext', 'aco_tt_tons_exp', 'aco_tt_exp_dol',
'aco_tt_tons_imp', 'aco_tt_imp_dol', 'ct_medm2_material','ct_medm2_maodeobra', 'custo_medm2', 'prc_gasol_med_ms','prc_diesel_med_ms', 
'cdi', 'valor_dolar', 'cresc_agro', 'divida','igpm', 'incc', 'ipca_acumulado', 'ipca_mensal', 'ipcm']"""
#RESULTADO DESEJADO:
"""original = 'cub_r8_pdrnorm' + 'slr_min' + 'prod_aco_bruto' + 'aco_vd_int' + 'aco_vd_ext' + 'aco_tt_tons_exp' + 'aco_tt_exp_dol'
 + 'aco_tt_tons_imp' + 'aco_tt_imp_dol' + 'ct_medm2_material' + 'ct_medm2_maodeobra' + 'custo_medm2' + 'prc_gasol_med_ms' + 
 'prc_diesel_med_ms' + 'cdi' + 'valor_dolar' + 'cresc_agro' + 'divida' + 'igpm' + 'incc' + 'ipca_acumulado' + 'ipca_mensal' + 'ipcm'"""


original = ['cub_r8_pdrnorm', 'slr_min', 'prod_aco_bruto','aco_vd_int', 'aco_vd_ext', 'aco_tt_tons_exp', 'aco_tt_exp_dol','aco_tt_tons_imp', 'aco_tt_imp_dol', 'ct_medm2_material','ct_medm2_maodeobra', 'custo_medm2', 'prc_gasol_med_ms','prc_diesel_med_ms', 'cdi', 'valor_dolar', 'cresc_agro', 'divida','igpm', 'incc', 'ipca_acumulado', 'ipca_mensal', 'ipcm']
lista = " + ".join(f"'{item}'" for item in original)
print(lista)