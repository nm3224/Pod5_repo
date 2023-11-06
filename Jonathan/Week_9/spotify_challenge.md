# Spotify Challenge

Before getting started with the challenge, let's peek into all the tables in the Spotify database:

### Artists

| ID  | Name        |
| --- | ----------- |
| 1   | The Beatles |
| 2   | The Beetles |

### Albums

| ID  | Name       | YearReleased |
| --- | ---------- | ------------ |
| 1   | Abbey Road | 1969         |
| 2   | Let It Be  | 1970         |
| 3   | Help!      | 1965         |
| 4   | "1"        | 2000         |
| 5   | 125 Street | 2021         |

### Songs

| ID  | Song               | ArtistId | AlbumId |
| --- | ------------------ | -------- | ------- |
| 1   | Here Comes the Sun | 1        | 1       |
| 2   | Come Together      | 1        | 1       |
| 3   | Let It Be          | 1        | 2       |
| 4   | Yesterday          | 1        | 3       |
| 5   | Hey Jude           | 1        | 4       |
| 6   | Hey JTC            | 2        | 5       |

### Members

| ID  | Name   | ArtistID |
| --- | ------ | -------- |
| 1   | John   | 1        |
| 2   | Paul   | 1        |
| 3   | Ringo  | 1        |
| 4   | George | 1        |
| 2   | Paul   | 3        |

### ArtistMembers

| ID  | MemberID | ArtistID |
| --- | -------- | -------- |
| 1   | 2        | 1        |
| 2   | 2        | 3        |

## We're in great shape but we're missing a key ingredient: Musical Genres!

In the `Songs` table we've added another column called `Genre`.

### Songs

| ID  | Song               | ArtistId | AlbumId | Genre   |
| --- | ------------------ | -------- | ------- | ------- |
| 1   | Here Comes the Sun | 1        | 1       | Rock    |
| 2   | Come Together      | 1        | 1       | Rock    |
| 3   | Let It Be          | 1        | 2       | Rock    |
| 4   | Yesterday          | 1        | 3       | Rock    |
| 5   | Hey Jude           | 1        | 4       | Rock    |
| 6   | Hey JTC            | 2        | 5       | Hip Hop |

You will notice that we're repeating `Rock` a number of times. This may not seem like a problem but consider the following:

-   If we had to rename `Rock` and our `Songs` table contained a **million** `Rock` songs, the time to complete such a change would be very long!
-   If we also wanted to assign a genre to an album in the `Albums` table in a similar way, we would have repeated data in multiple tables

# Question 1

a) Briefly describe a better way of modeling genre data in the database to avoid some of the issues listed above. You can assume for the sake of simplicity there can be only one genre per song.
**Tip**: _Before answering, use pen and paper to sketch out the possibilities. Does your solution involve new table(s), column(s), row(s), relationship(s)?_

A better way to model the genre data is to create a SongGenreID where we assign "1" for Rock, and "2" for Hip Hop, etc.  This way we could update the genres as needed, and easily assign them to each song.  Separately, we can also create an AlbumGenreID to assign genres to specific albums, separate from particular songs within the albums.

b) What relationship best describes how genre relates to songs in your answer to Question 1a?

The songs to genre relationship is a many-to-one relationship as there would be a SongGenreID that can be used for many songs.

# Question 2

What changes would you make to the modeling of genre data if we could assign more than one genre to a song?

I think the way to go about this is to create SongGenreID's that incorporate multiple genres.  So, for example there can be a Rock&HipHop SongGenreID for songs that can be qualify as both Rock and Hip Hop.  I'm not sure if you could create a list of different SongGenreID's for the same song, so perhaps having SongGenreID's for multiple genres might be the best way.