連線到mysql server
mysql –u用戶名  –p密碼;

建立與刪除database
create database 名稱;
drop database 名稱;

使用資料庫
use 資料庫名稱;

顯示資料庫與表
show databases;
show tables;

刪除表
drop tables user;

新建user表
create table user(id bigint not null auto_increment primary key comment "流水號",name varchar(255) not null comment "名稱",username varchar(255) not null comment "使用者名稱", password varchar(255) not null comment "密碼", time datetime not null default current_timestamp comment "時間戳");


使用INSERT 指令新增一筆資料到user 資料表中，這筆資料的username 和password 欄位必須是ply。接著繼續新增至少 4 筆隨意的資料。
insert into user values(null,ply,ply,ply,now());

使用SELECT 指令取得所有在user 資料表中的使用者資料。
select * from user;

使用SELECT 指令取得user 資料表中總共有幾筆資料。
select count(id) from user;

使用SELECT 指令取得所有在user 資料表中的使用者資料，並按照time 欄位，由近到遠排序。
select * from user order by time asc;

使用SELECT 指令取得user 資料表中第 2 ~ 4 共三筆資料，並按照time 欄位，由近到遠排序。
select * from user where id between 2 and 4 order by time asc;

使用SELECT 指令取得欄位username 是ply 的使用者資料。
select * from user where username like "ply";

使用SELECT 指令取得欄位username 是ply、且欄位password 也是ply的資料。
select * from user where username like "ply" and password like "ply";

使用UPDATE 指令更新欄位username 是ply 的使用者資料，將資料中的name欄位改成【丁滿】。
update user set name="丁滿" where username like "ply";

使用DELETE 指令刪除所有在user 資料表中的資料。
delete from user;

使用SELECT 搭配JOIN 的語法，取得所有留言，資料中須包含留言會員的姓名。
select * from message left join user on message.user_id=[user.id](http://user.id/);

使用SELECT 搭配JOIN 的語法，取得user 資料表中欄位username 是ply的所有留言，資料中須包含留言會員的姓名。
select * from user right join message on user.id=message.user_id where username like "ply";


![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/1.jpg)
![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/2.jpg)
![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/3.jpg)
![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/4.jpg)
![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/5.jpg)
![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/6.jpg)
![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/7.jpg)
![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/8.jpg)
![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/9.jpg)
![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/10.jpg)
![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/11.jpg)
![image](https://github.com/abc820219/codeingtranning/tree/main/week5/images/12.jpg)