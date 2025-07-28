-- コードマスタデータ削除
truncate table skotune_ai.m_code;

-- コードマスタ追加
INSERT 
INTO skotune_ai.m_code(code_id, code_value, code_name) 
VALUES ('0001', '00', '分析採点マスター(JOYSOUND)')
, ('0001', '01', '分析採点AI(JOYSOUND)')
, ('0001', '10', '精密採点DX(DAM)')
, ('0001', '11', '精密採点Ai(DAM)');