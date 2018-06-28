SET STORAGE_ENGINE = INNODB;
DROP DATABASE IF EXISTS BlogDB;
CREATE DATABASE BlogDB;
USE BlogDB;

CREATE TABLE Editor ( 
UserName CHAR(30) NOT NULL,
Name CHAR(30) NOT NULL,
Email CHAR(50) NOT NULL,
TitleOfBLog CHAR(50) NOT NULL,
DateOfBirth DATE NOT NULL,
PRIMARY KEY (UserName)
);
INSERT INTO Editor values('Mystery', 'MysteryMan', 'MysteryMan@somewhere.com', 'FunStuff', '1994-10-11');
INSERT INTO Editor values('JohnEveryday', 'John', 'John@somewhere', 'Everyday', '1990-08-11');

CREATE TABLE Post (
PostUserName CHAR(30) NOT NULL,
PostID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
Title CHAR (50) NOT NULL,
TimestampID TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
Content LONGTEXT NOT NULL,
FOREIGN KEY (PostUserName) references Editor(UserName) ON DELETE CASCADE
);
INSERT INTO Post(PostUserName,Title,Content) values('Mystery','Post1', 'aa' );
INSERT INTO Post(PostUserName,Title,Content) values('Mystery','Post2','sss');
INSERT INTO Post(PostUserName,Title,Content) values('JohnEveryday','Post3','dddd');
INSERT INTO Post(PostUserName,Title,Content) values('Mystery','Post4','fffff');
INSERT INTO Post(PostUserName,Title,Content) values('JohnEveryday','Post5','gggggg');
INSERT INTO Post(PostUserName,Title,Content) values('JohnEveryday','Post6','hhhhhhh');

CREATE TABLE Comment (
CName CHAR(30),
CEmail CHAR(50),
CommentID INT AUTO_INCREMENT PRIMARY KEY,
TimeStamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
CContent LONGTEXT NOT NULL,
On_p INTEGER,
FOREIGN KEY(On_p) references Post(PostID) ON DELETE CASCADE
);
INSERT INTO Comment(CName, CEmail, CContent) values('Petras','Petras@Anyksciai.com','Kai lievai');
INSERT INTO Comment(CName, CEmail, CContent) values('Jonas','Jonas@Kaunas.com','Ziauriai geras');
INSERT INTO Comment(CName, CEmail, CContent) values('Petriukas','Petriukas@Anyksciai.com','Ka nusisnekat?');
INSERT INTO Comment(CName, CEmail, CContent) values('Jonukas','Jonuakas@Kaunas.com','Hahah visi jus lopai');
INSERT INTO Comment(CName, CEmail, CContent) values('Tomas','Tomas@Alytus.com','Geras sitas :D');
INSERT INTO Comment(CName, CEmail, CContent) values('Tomis','Tomis@Kaunas.com','Tylek');
INSERT INTO Comment(CName, CEmail, CContent) values('Vytautas','Vytautas@Vilnius.com','Blalalallaal');
INSERT INTO Comment(CName, CEmail, CContent) values('Mindaugas','Mindaugas@Trakai.com','As Karaliuuuuus');
INSERT INTO Comment(CName, CEmail, CContent) values('Algirdas','Algirdas@Poland.com','O as Lenkijos karalius');
INSERT INTO Comment(CName, CEmail, CContent) values('Barbora','Barbora@Radvila.com','Manes visi nori');

CREATE TABLE Category (
CategoryID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
CategoryName CHAR(50)
);
INSERT INTO Category(CategoryName) values ('Musing');
INSERT INTO Category(CategoryName) values ('Work');
INSERT INTO Category(CategoryName) values ('Social');
INSERT INTO Category(CategoryName) values ('General');

CREATE TABLE Assigned(
PoPrKey int not null,
CatPrKey int not null,
#PRIMARY KEY (PoPrKey, CatPrKey),
FOREIGN KEY (PoPrKey) references Post(PostID) ON DELETE CASCADE,
FOREIGN KEY (CatPrKey) references Category(CategoryID) ON DELETE CASCADE
);
Insert INTO Assigned VALUES
(1,1),
(1,2),
(2,1),
(2,4),
(4,1),
(4,2),
(5,3),
(5,4),
(6,3),
(6,1),
(3,1);

# Query1
SELECT Name,Email, TIMESTAMPDIFF(Year,DateOfBirth,CURRENT_TIMESTAMP) AS Age
FROM editor;
# Query2
SELECT PostUserName, TitleOfBlog, count(PostID) AS CoutnedPost FROM editor, post
WHERE PostUserName=Username GROUP BY username;
#Query3
SELECT PostUserName, Title, TimestampID, GROUP_CONCAT(CategoryName) AS categories FROM Post, Category, Assigned WHERE Assigned.PoPrKey=Post.PostID and Assigned.CatPrKey=Category.CategoryID GROUP BY PoPrKey;