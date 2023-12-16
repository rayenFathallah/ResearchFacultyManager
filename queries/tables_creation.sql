CREATE TABLE FACULTE ( 
  facno NUMBER PRIMARY KEY NOT NULL AUTO_INCREMENT, 
  facnom VARCHAR2(10), 
  adresse VARCHAR2(100), 
  libelle VARCHAR2(50) 
) ; 
CREATE TABLE LABORATOIRE ( 
  labno NUMBER PRIMARY KEY  AUTO_INCREMENT, 
  labnom VARCHAR2(50), 
  facno NUMBER, 
  FOREIGN KEY (facno) REFERENCES FACULTE(facno) 
); 
CREATE TABLE CHERCHEUR ( 
  chno NUMBER PRIMARY KEY AUTO_INCREMENT, 
  chnom VARCHAR2(50), 
  grade VARCHAR2(2) CHECK (grade IN ('E', 'D', 'A', 'MA', 'MC', 'PR')), 
  statut VARCHAR2(1) CHECK (statut IN ('P', 'C')), 
  daterecrut DATE, 
  salaire NUMBER, 
  prime NUMBER, 
  email VARCHAR2(100), 
  supno NUMBER, 
  labno NUMBER, 
  facno NUMBER, 
  FOREIGN KEY (supno) REFERENCES CHERCHEUR(chno), 
  FOREIGN KEY (labno) REFERENCES LABORATOIRE(labno), -- Assuming there is a LABORATOIRE table 
  FOREIGN KEY (facno) REFERENCES FACULTE(facno) -- Assuming there is a FACULTE table 
); 
CREATE TABLE PUBLICATION ( 
  pubno VARCHAR2(8) PRIMARY KEY , 
  titre VARCHAR2(100), 
  theme VARCHAR2(50), 
  type VARCHAR2(2) CHECK (type IN ('AS', 'PC', 'P', 'L', 'T', 'M')), 
  volume NUMBER, 
  date_edit DATE, 
  apparition VARCHAR2(100), 
  editeur VARCHAR2(50) 
);
CREATE TABLE PUBLIER ( 
  chno NUMBER, 
  pubno VARCHAR2(8), 
  rang NUMBER CHECK (rang > 0), 
  PRIMARY KEY (chno, pubno), 
  FOREIGN KEY (chno) REFERENCES CHERCHEUR(chno), 
  FOREIGN KEY (pubno) REFERENCES PUBLICATION(pubno) 
); 
CREATE TABLE historique_chercheurs ( 
  chno NUMBER, 
  chnom VARCHAR2(50), 
  grade VARCHAR2(2), 
  statut VARCHAR2(1), 
  daterecrut DATE, 
  salaire NUMBER, 
  prime NUMBER, 
  email VARCHAR2(100), 
  supno NUMBER, 
  labno NUMBER, 
  facno NUMBER, 
  action_type VARCHAR2(10), 
  action_date TIMESTAMP, 
  PRIMARY KEY (chno, action_type, action_date), 
  FOREIGN KEY (chno) REFERENCES CHERCHEUR(chno) 
)