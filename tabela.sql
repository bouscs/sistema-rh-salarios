CREATE TABLE taxas (
   iden integer NOT NULL,
   date_created date NOT NULL,
   chave varchar(20) NOT NULL,
   valor number NOT NULL,
   PRIMARY KEY (iden)
);

ALTER TABLE taxas ADD UNIQUE (chave);
    

    