--  uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name AS name
FROM tv_show_genres, tv_genres, tv_shows 
WHERE tv_shows.title = 'Dexter' 
AND tv_shows.id = tv_show_genres.tv_show_id 
AND tv_genres.id = tv_show_genres.genre_id 
GROUP BY name
ORDER BY name ASC
