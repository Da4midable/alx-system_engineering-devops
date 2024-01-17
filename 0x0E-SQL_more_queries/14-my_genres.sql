--  uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name
FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_genres ON hbtn_0d_tvshows.tv_shows.id = hbtn_0d_tvshows.tv_genres.show_id
WHERE hbtn_0d_tvshows.tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
