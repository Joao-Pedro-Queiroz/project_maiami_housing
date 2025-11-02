import pandas as pd
import numpy as np


def feature_engineering(df):
    """
    Aplica feature engineering no dataframe de Miami Housing.
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        Dataframe original com os dados de Miami Housing
        
    Retorna:
    --------
    pd.DataFrame
        Dataframe processado com as features transformadas
    """
    
    # Selecionar apenas as features necessárias
    features_to_keep = [
        'SALE_PRC', 
        'LND_SQFOOT', 
        'TOT_LVG_AREA', 
        'SPEC_FEAT_VAL', 
        'OCEAN_DIST', 
        'CNTR_DIST', 
        'age', 
        'avno60plus', 
        'month_sold', 
        'structure_quality'
    ]
    
    # Criar cópia do dataframe com apenas as features selecionadas
    df_processed = df[features_to_keep].copy()
    
    # 1. Remover linhas com structure_quality == 3 (outliers)
    print(f"Registros antes de remover quality 3: {len(df_processed)}")
    df_processed = df_processed[df_processed['structure_quality'] != 3].copy()
    print(f"Registros após remover quality 3: {len(df_processed)}")
    print(f"Registros removidos: {len(df) - len(df_processed)}")
    
    # 2. Aplicar transformação logarítmica
    log_features = ['SALE_PRC', 'LND_SQFOOT', 'TOT_LVG_AREA', 'SPEC_FEAT_VAL']
    
    for feature in log_features:
        # Adicionar 1 para evitar log(0) e criar nova coluna com prefixo 'log_'
        df_processed[f'log_{feature.lower()}'] = np.log1p(df_processed[feature])
    
    # Remover as features originais que foram transformadas em log
    df_processed = df_processed.drop(columns=log_features)
    
    # 3. Transformar OCEAN_DIST em ranking (1, 2, 3) e depois em dummies
    # Criar bins e converter para ranking numérico
    df_processed['ocean_dist_rank'] = pd.cut(
        df_processed['OCEAN_DIST'], 
        bins=3, 
        labels=[1, 2, 3]
    ).astype(int)
    
    # Remover OCEAN_DIST original
    df_processed = df_processed.drop(columns=['OCEAN_DIST'])
    
    # Converter ocean_dist_rank em dummy variables
    ocean_dummies = pd.get_dummies(
        df_processed['ocean_dist_rank'], 
        prefix='ocean_rank', 
        drop_first=True
    )
    
    # Adicionar dummies ao dataframe
    df_processed = pd.concat([df_processed, ocean_dummies], axis=1)
    
    # Remover ocean_dist_rank original
    df_processed = df_processed.drop(columns=['ocean_dist_rank'])
    
    # 4. Criar flag critical_month para month_sold
    # Meses críticos: 5, 6 e 11
    df_processed['critical_month'] = df_processed['month_sold'].isin([5, 6, 11]).astype(int)
    
    # Remover month_sold original
    df_processed = df_processed.drop(columns=['month_sold'])
    
    # 5. Converter structure_quality para dummy variables
    # Isso captura os efeitos não-lineares entre as categorias
    quality_dummies = pd.get_dummies(
        df_processed['structure_quality'], 
        prefix='quality', 
        drop_first=True
    )
    
    # Adicionar dummies ao dataframe
    df_processed = pd.concat([df_processed, quality_dummies], axis=1)
    
    # Remover structure_quality original
    df_processed = df_processed.drop(columns=['structure_quality'])
    
    # Resetar índice
    df_processed = df_processed.reset_index(drop=True)
    
    print("\n=== Feature Engineering Concluído ===")
    print(f"Shape final: {df_processed.shape}")
    print(f"\nFeatures finais:")
    print(df_processed.columns.tolist())
    
    return df_processed


