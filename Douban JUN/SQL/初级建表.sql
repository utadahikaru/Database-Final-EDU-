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
movieId varchar(5) unique not null,
castId varchar(5) unique not null,
charactername varchar(20) not null,
constraint foreign key(movieId) references movies(movieId),
constraint foreign key(castId) references casts(castId)
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


insert into users(userId,userName,userpassword,IsAdmin,MoviesNum)
values
("000000","JUN","mikumikuliu1234",1,0)

insert into movies(movieId,movieName,movieNameCN,movieRate,movieclass,movieCountry,movieDuration,movieDate,append)
values
("001","Wonder Woman","神奇女侠",7,"动作 奇幻 冒险","美国","141",2017-06-02,"")

