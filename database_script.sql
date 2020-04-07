create database oscres_db;
use oscres_db;
create table if not exists university_course (
    name varchar(256) not null,
    country varchar(256) not null, 
    city varchar(256) not null, 
    subject varchar(256), 
    min_ietls float);