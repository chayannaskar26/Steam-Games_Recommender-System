#  Steam Games Recommender System
### A Content Based Recommender System for games available on Steam to play. Mostly contains famous titles from top Studios, like Ubisoft, Valve, Activision, EA , Bethesda, CD Projekt Red, Microsoft, etc.
### 'Data Mining' folder contains the code for fetching the data from Steam api. Since the api has limit of continous requests, the downloads are divided into batches based on different studios.

Column | Description
--- | ------
`appid` | Games Id on Steam
`title` | Title of the game
`short_description` | Description of the game
`is_free` | Whether the game is free to download or not
`suppoted_language` | Languages the is game is available in
`developer` | Developing studio
`publishers` | Publishing studio
`platforms` | Platforms on which the game is available to play.
`categories` | Categories of the games
`genres` | Genres of the game
`release_date` | Release date of the game
