create table users(
userId varchar(10) unique not null,
userName varchar(20) not null,
userpassword varchar(30) not null,
IsAdmin tinyint default 0,
MoviesNum int default 0,
constraint Admin check(IsAdmin =1 or IsAdmin = 0)
)

create table movies(
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
)

create table casts(
castId varchar(5) unique not null,
castRate float default 0,
castName varchar(20) unique not null,
castNameCN varchar(30) not null,
castBirthday date not null,
castCountry varchar(15) not null,
castURL varchar(50)
)

create table castShow(
movieId varchar(5) not null,
castId varchar(5) not null,
charactername varchar(20) not null
)

create table usersSee(
userId varchar(10) unique not null,
movieId varchar(5) unique not null,
userRate float not null,
constraint foreign key(userId) references users(userId),
constraint foreign key(movieId) references movies(movieId)
)

create table usersLove(
userId varchar(10) unique not null,
castId varchar(5) unique not null,
userLoveRate float not null,
constraint foreign key(userId) references users(userId),
constraint foreign key(castId) references casts(castId)
)



<<<<<<< HEAD:Douban JUN/SQL/初级建表_pjr.sql
insert into movies(movieId,movieName,movieNameCN,movieRate,movieclass,movieCountry,movieDuration,movieDate,append)
values
("001","Wonder Woman","神奇女侠",7,"动作 奇幻 冒险","美国","141",2017-06-02,""),
("002","Vemon","毒液",7.3,"动作 科幻 惊悚","美国","107",2018-11-09,"")

insert into casts
values
('001',8.2,'Gaierjaduo','盖尔加朵',1978-02-23,'America','C:\Database-Final-EDU-\Douban JUN\GUIs\image\盖尔加朵.jpg')
=======
>>>>>>> 47f2374f64e28983703fd42340a0323c23e82ccc:Douban JUN/SQL/初级建表.sql
