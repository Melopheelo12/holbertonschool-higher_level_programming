SELECT t.title, s.genre_id
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS s
    ON t.id = s.show_id
ORDER BY t.title ASC, s.genre_id ASC;