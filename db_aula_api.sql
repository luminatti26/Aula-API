create database aula_api;

use aula_api;

create table pessoas(
codigo int auto_increment,
nome varchar(30),
primary key(codigo)
);

select * from pessoas;

insert into pessoas(nome) values ("Lucas");


