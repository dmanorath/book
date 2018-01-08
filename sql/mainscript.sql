-- CREATE DATABASE BookFinder;


USE BookFinder;
-- DROP table Users;
/*
CREATE TABLE Colleges(
	CID INT Primary Key auto_increment,
    CollegeName char(32) NOT NULL
    );
    
CREATE TABLE Users(
	UID INT Primary Key auto_increment,
    FirstName char(32) NOT NULL,
    LastName char(32) NOT NULL,
    Email text(128) NOT NULL,
    PassWord text(32) NOT NULL,
    CollegeId int NOT NULL,
    foreign key (CollegeId) references Colleges(CID)
);

    
CREATE TABLE Messages (
	MID INT Primary Key auto_increment,
    User1 INT NOT NULL,
    User2 INT NOT NULL,
    Content text (256) NOT NULL,
    foreign key (User1) references Users(UID),
	foreign key  (User2) references Users(UID)
    );

CREATE TABLE Listing(
	LID INT Primary Key auto_increment,
    UserID INT NOT NULL,
	CollegeID INT NOT NULL,
    BookTitle text(256) NOT NULL,
    ISBN INT,
    Price DECIMAL(3,2),
    Description text(512),
    foreign key (UserID) references Users(UID),
    foreign key (CollegeID) references Users(UID)
    );
*/
/*
select * from Users;
select * from Colleges;
select * from Messages;
select * from Listing;

UPDATE Listing SET BookTitle = 'New Book Title' WHERE LID = 1

INSERT INTO Users (FirstName, LastName, Email, PassWord, CollegeID)
VALUES ('Jack', 'Basdasda', 'sd@yassshoo.com', 'slkdj', 1);
*/
SELECT * FROM Listing WHERE CollegeID = 1
