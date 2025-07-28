-- メニューマスタデータ削除
truncate table skotune_ai.m_menu;

-- メニューマスタ追加
INSERT 
INTO skotune_ai.m_menu(sort, label, icon, content, administrator_flg) 
VALUES ( 
    1
    , 'ホーム'
    , '<svg width="24"          height="24"          viewBox="0 0 24 24"          fill="none"          xmlns="http://www.w3.org/2000/svg"        >          <path            d="M3 10L12 3L21 10V20C21 20.55 20.55 21 20 21H4C3.45 21 3 20.55 3 20V10Z"            stroke="black"            stroke-width="2"            stroke-linecap="round"            stroke-linejoin="round"          />          <path            d="M9 21V12H15V21"            stroke="black"            stroke-width="2"            stroke-linecap="round"            stroke-linejoin="round"          />        </svg>'
    , '/home'
    , false
) 
, ( 
    2
    , '検索'
    , '<svg          width="24"          height="24"          viewBox="0 0 24 24"          fill="none"          xmlns="http://www.w3.org/2000/svg"        >          <circle cx="11" cy="11" r="8" stroke="black" stroke-width="2" />          <line            x1="16.65"            y1="16.65"            x2="21"            y2="21"            stroke="black"            stroke-width="2"            stroke-linecap="round"          />        </svg>'
    , '/search'
    , false
) 
, ( 
    3
    , '採点履歴登録'
    , '<svg          width="24"          height="24"          viewBox="0 0 24 24"          fill="none"          xmlns="http://www.w3.org/2000/svg"        >          <rect            x="3"            y="3"            width="18"            height="18"            rx="2"            stroke="black"            stroke-width="2"          />          <path            d="M8 12L11 15L16 9"            stroke="black"            stroke-width="2"            stroke-linecap="round"            stroke-linejoin="round"          />        </svg>'
    , '/score'
    , false
) 
, ( 
    4
    , '楽曲レコメンド'
    , '<svg          width="24"          height="24"          viewBox="0 0 24 24"          fill="none"          xmlns="http://www.w3.org/2000/svg"        >          <path            d="M16 3V14.5C16 15.88 14.88 17 13.5 17C12.12 17 11 15.88 11 14.5C11 13.12 12.12 12 13.5 12C13.83 12 14.14 12.06 14.43 12.17L14.5 12.2V6.7L10 7.5V18.5C10 19.88 8.88 21 7.5 21C6.12 21 5 19.88 5 18.5C5 17.12 6.12 16 7.5 16C7.83 16 8.14 16.06 8.43 16.17L8.5 16.2V5L16 3Z"            fill="black"          />        </svg>'
    , '/model'
    , false
) 
, ( 
    5
    , '管理者'
    , '<svg          width="24"          height="24"          viewBox="0 0 24 24"          fill="none"          xmlns="http://www.w3.org/2000/svg"        >          <path            d="M12 2L5 5v9c0 5 5 8 7 8s7-3 7-8V5l-7-3z"            stroke="black"            stroke-width="2"            fill="none"          />          <path            d="M12 8l1 3h3l-2.5 2 1 3-2.5-2-2.5 2 1-3-2.5-2h3z"            stroke="black"            stroke-width="1.5"            fill="none"          />        </svg>'
    , '/administrator'
    , true
) 
, ( 
    6
    , 'マイリスト'
    , '<svg          width="24"          height="24"          viewBox="0 0 24 24"          fill="none"          xmlns="http://www.w3.org/2000/svg"        >          <path            d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"            stroke="black"            stroke-width="2"            fill="none"            stroke-linejoin="round"          />        </svg>'
    , '/mylist'
    , false
) 
, ( 
    7
    , '設定'
    , '<svg          width="24"          height="24"          viewBox="0 0 24 24"          fill="none"          xmlns="http://www.w3.org/2000/svg"          stroke="black"          stroke-width="2"          stroke-linecap="round"          stroke-linejoin="round"        >          <path d="M12 15.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z" />          <path            d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83           2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33           1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2           2 2 0 0 1-2-2v-.09a1.65 1.65 0 0 0-1-1.51           1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0           2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82           1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2           2 2 0 0 1 2-2h.09a1.65 1.65 0 0 0 1.51-1           1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83           2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33           1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2           2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51           1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0           2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82           1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2           2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"          />        </svg>'
    , '/setting'
    , false
);
