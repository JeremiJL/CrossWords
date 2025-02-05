create table game (
  gameId int GENERATED BY DEFAULT ON NULL AS IDENTITY,
  solution varchar2(30) not null,
  primary key(gameId)
);

create table puzzle (
    puzzleId int GENERATED BY DEFAULT ON NULL AS IDENTITY,
    correct_word varchar2(30) not null,
    hint varchar2(100) not null,
    gameId int,
    primary key(gameId,puzzleId),
    foreign key (gameId) references game(gameId)
)