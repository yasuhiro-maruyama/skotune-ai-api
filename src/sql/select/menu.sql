-- メニュー取得SQL
SELECT
    label
    , icon
    , content
    , administrator_flg
    , sort 
FROM
    skotune_ai.menu 
WHERE
    (:admin = true OR administrator_flg = false) 
ORDER BY
    sort;
