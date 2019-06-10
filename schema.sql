drop table if exists user_id_and_pass;
create table user_id_and_pass (
  id integer primary key autoincrement,
  userid string not null,
  password string not null
);