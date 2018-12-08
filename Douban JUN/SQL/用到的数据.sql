insert into movies(movieId,movieName,movieNameCN,movieRate,movieclass,movieCountry,movieDuration,movieDate,append)
values
("001","Wonder Woman","神奇女侠",0,"动作 奇幻 冒险","美国","141",20170602,""),
("002","Venom","毒液",0,"动作 科幻 惊悚","美国","107",20181109,""),
("003","Inception","盗梦空间",0,"剧情 科幻 悬疑","美国","148",20100901,"奥斯卡提名"),
("004","Leon","这个杀手不太冷",0,"剧情 动作 犯罪","美国","110",19940914,"日本电影学院奖提名"),
("005","Titanic","泰坦尼克号",0,"剧情 爱情 灾难","美国","194",19980403,""),
("006","Adios a mi concubina","霸王别姬",0,"剧情 爱情 同性","中国","171",19930101,"奥斯卡提名"),
("007","The Godfather","教父",0,"剧情 犯罪","美国","175",19720315,"奥斯卡提名"),
("008","Pretty Woman","风月俏佳人",0," 动作 犯罪","美国","110",19940914,"奥斯卡最佳女主角提名"),
("009","Good Will Hunting","心灵捕手",0,"剧情","美国","126",19971205,"奥斯卡提名"),
("010","Brokeback Mountain","断背山",0,"剧情 爱情 同性","美国","134",20050902,"威尼斯电影节上映"),
("011","Forrest Gump","阿甘正传",0,"剧情 爱情","美国","142",19940623,"奥斯卡金像奖")

insert into users(userId,userName,userpassword,IsAdmin,MoviesNum)
values
("000000","JUN","hualiyingping",1,0),
("000001","test1","hualiyingping1",0,0),
("000002","test2","hualiyingping2",0,0),
("000003","test3","hualiyingping3",0,0),
("000004","test4","hualiyingping4",0,0),
("000005","test5","hualiyingping5",0,0),
("000006","test6","hualiyingping6",0,0),
("000007","test7","hualiyingping7",0,0)





insert into casts(castId,castRate,castName,castNameCN,castBirthday,castCountry,castURL)
values
("001",0,"Gal Gadot","盖尔 加朵",19850430,"以色列",""),
("002",0,"Tom Hardy","汤姆 哈迪",19770915,"英国",""),
("003",0,"Leonardo DiCaprio","莱昂纳多 迪卡普里奥",19741111,"美国",""),
("004",0,"Natalie Portman","娜塔丽 波特曼",19810609,"以色列",""),
("005",0,"Leslie Cheung","张国荣",19560912,"中国",""),
("006",0,"Al Pacino","阿尔 帕西诺",19400425,"美国",""),
("007",0,"Julia Roberts","茱莉亚 罗伯茨",19671028,"美国",""),
("008",0,"Matt Damon","马特 达蒙",19701008,"以色列",""),
("009",0,"Anne Hathaway","安妮 海瑟薇",19821112,"美国",""),
("010",0,"Tom Hanks","汤姆 汉克斯",19560709,"美国","")


insert into castShow(movieId,castId,charactername)
values
("001","001","Diana"),
("002","002","Eddie Brock"),
("003","003","Cobb"),
("003","002","Eames"),
("004","004","Mathilda"),
("005","003","Jack"),
("006","005","DieYi Cheng"),
("007","006","Michael Corleone"),
("008","007","Vivian"),
("009","008","Will"),
("010","009","Lureen Newsome"),
("011","010","Forrest Gump")



