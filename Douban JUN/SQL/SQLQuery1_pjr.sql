CREATE DATABASE DoubanJUN;
USE DoubanJUN;
create table users
(
    userId varchar(10) unique not null,
    userName varchar(20) not null,
    userpassword varchar(30) not null,
    IsAdmin tinyint default 0,
    MoviesNum int default 0,
    constraint Admin check(IsAdmin =1 or IsAdmin = 0)
);

<<<<<<< HEAD:Douban JUN/SQL/SQLQuery1_pjr.sql
create table movies(
movieId varchar(5) unique not null,
movieName varchar(50) unique not null,
movieNameCN varchar(100) not null,
movieRate float default 0,
movieclass varchar(15) not null,
movieCountry varchar(20) not null,
movieDuration int not null,
movieDate date not null,
imgURL varchar(500),
append text
);


create table casts(
castId varchar(5) unique not null,
castRate float default 0,
castName varchar(20) unique not null,
castNameCN varchar(30) not null,
castBirthday date not null,
castCountry varchar(15) not null,
castURL varchar(50)
=======
create table movies
(
    movieId varchar(5) unique not null,
    movieName varchar(50) unique not null,
    movieNameCN varchar(100) not null,
    movieRate float default 0,
    movieclass varchar(15) not null,
    movieCountry varchar(20) not null,
    movieDuration int not null,
    movieDate date not null,
    imgURL varchar(50),
    append text
);

create table casts
(
    castId varchar(5) unique not null,
    castRate float default 0,
    castName varchar(20) unique not null,
    castNameCN varchar(30) not null,
    castBirthday date not null,
    castCountry varchar(15) not null,
    castURL varchar(50)
>>>>>>> 47f2374f64e28983703fd42340a0323c23e82ccc:Douban JUN/SQL/SQLQuery1.sql
);

create table castShow
(
    movieId varchar(5) unique not null,
    castId varchar(5) unique not null,
    charactername varchar(20) not null,
    foreign key(movieId) references movies(movieId),
    foreign key(castId) references casts(castId)
);

create table usersSee
(
    userId varchar(10) unique not null,
    movieId varchar(5) unique not null,
    userRate float not null,
    foreign key(userId) references users(userId),
    foreign key(movieId) references movies(movieId)
);

create table usersLove
(
    userId varchar(10) unique not null,
    castId varchar(5) unique not null,
    userLoveRate float not null,
    foreign key(userId) references users(userId),
    foreign key(castId) references casts(castId)
);

<<<<<<< HEAD:Douban JUN/SQL/SQLQuery1_pjr.sql

insert into users (userId,userName,userpassword,IsAdmin,MoviesNum)
values('000000','JUN','mikumikuliu1234',1,0);

insert into movies (movieId,movieName,movieNameCN,movieRate,movieclass,movieCountry,movieDuration,movieDate,imgURL)
values
('001','Wonder Woman','ÉñÆæÅ®ÏÀ',7,'¶¯×÷ Ææ»Ã Ã°ÏÕ','ÃÀ¹ú','141','2017-06-02','https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2460006593.webp'),
('002','Vemon','¶¾Òº',7.3,'¶¯×÷ ¿Æ»Ã ¾ªã¤','ÃÀ¹ú','107','2018-11-09','https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2537158013.webp')
=======
select *
from dbo.users
insert into users
    (userId,userName,userpassword,IsAdmin,MoviesNum)
values('000000', 'JUN', 'testpassword', 1, 0);

insert into movies
    (movieId,movieName,movieNameCN,movieRate,movieclass,movieCountry,movieDuration,movieDate,append)
values
    ("001", "Wonder Woman", "ï¿½ï¿½ï¿½ï¿½Å®ï¿½ï¿½", 7, "ï¿½ï¿½ï¿½ï¿½ ï¿½ï¿½ï¿½ Ã°ï¿½ï¿½", "ï¿½ï¿½ï¿½ï¿½", "141", 2017-06-02, ""),
    ("002", "Vemon", "ï¿½ï¿½Òº", 7.3, "ï¿½ï¿½ï¿½ï¿½ ï¿½Æ»ï¿½ ï¿½ï¿½ï¿½", "ï¿½ï¿½ï¿½ï¿½", "107", 2018-11-09, "");
>>>>>>> 47f2374f64e28983703fd42340a0323c23e82ccc:Douban JUN/SQL/SQLQuery1.sql
