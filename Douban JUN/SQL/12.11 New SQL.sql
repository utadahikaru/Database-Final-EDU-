ALTER TABLE users ADD imgURL VARCHAR (50)
go

insert into usersSee(userId,movieId,userRate)
values
('000000','010',8.6)

insert into usersLove(userId,castId,userLoveRate)
values
('000000','009',9.8)


update movies set movieRate = 8.7 where movieId='010'



