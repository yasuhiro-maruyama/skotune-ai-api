-- ユーザー取得SQL
SELECT user_id, user_name, password, administrator_flg FROM skotune_ai.user WHERE user_id = :user_id;