CREATE OR REPLACE PROCEDURE ajouter_chercheur( 
  p_chno NUMBER, 
  p_chnom VARCHAR2, 
  p_grade VARCHAR2, 
  p_statut VARCHAR2, 
  p_daterecrut DATE, 
  p_salaire NUMBER, 
  p_prime NUMBER, 
  p_email VARCHAR2, 
  p_supno NUMBER, 
  p_labno NUMBER, 
  p_facno NUMBER 
) AS 
BEGIN 
  INSERT INTO chercheur (chno, chnom, grade, statut, daterecrut, salaire, prime, email, supno, labno, facno) 
  VALUES (p_chno, p_chnom, p_grade, p_statut, p_daterecrut, p_salaire, p_prime, p_email, p_supno, p_labno, p_facno); 
END ajouter_chercheur; 
CREATE OR REPLACE PROCEDURE modifier_profil_chercheur( 
  p_chno NUMBER, 
  p_grade VARCHAR2, 
  p_statut VARCHAR2, 
  p_salaire NUMBER, 
  p_labno NUMBER 
) AS 
BEGIN 
  UPDATE chercheur 
  SET grade = p_grade, statut = p_statut, salaire = p_salaire, labno = p_labno 
  WHERE chno = p_chno; 
END modifier_profil_chercheur; 
CREATE OR REPLACE FUNCTION chercheurs_max_publications( 
  p_facno NUMBER, 
  p_start_date DATE, 
  p_end_date DATE 
) RETURN SYS_REFCURSOR AS 
  v_cursor SYS_REFCURSOR; 
BEGIN 
  OPEN v_cursor FOR 
    SELECT c.* 
    FROM chercheur c 
    JOIN publier pu ON c.chno = pu.chno 
    JOIN publication pub ON pu.pubno = pub.pubno 
    JOIN laboratoire lab ON c.labno = lab.labno 
    WHERE lab.facno = p_facno 
    	AND pub.date_edit BETWEEN p_start_date and p_end_date   
    ORDER BY COUNT(pub.pubno) DESC 
    FETCH FIRST 1 ROWS ONLY; 
 
  RETURN v_cursor; 
END chercheurs_max_publications; 
CREATE OR REPLACE PROCEDURE supprimer_chercheur( 
  p_chno NUMBER 
) AS 
BEGIN 
  DELETE FROM chercheur WHERE chno = p_chno; 
END supprimer_chercheur;