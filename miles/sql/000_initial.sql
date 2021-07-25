create table intersection (
       userid serial primary key,
       taskid serial primary key
       );       


create table task(
      
      id serial primary key,
      taskname text not null,
      duedate date not null,
      overdue varchar(1)
      taskrec integer references intersection(taskid)
       
       );         


create table user (
       id serial primary key,
       email text unique not null,
       password text not null,
       userrec serial references intersection (userid),
      
       
);

  
