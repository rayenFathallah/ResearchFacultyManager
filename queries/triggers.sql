CREATE OR REPLACE TRIGGER before_update_chercheur 
BEFORE UPDATE ON chercheur 
FOR EACH ROW 
BEGIN 
  INSERT INTO historique_chercheurs 
  VALUES ( 
    :OLD.chno, 
    :OLD.chnom, 
    :OLD.grade, 
    :OLD.statut, 
    :OLD.daterecrut, 
    :OLD.salaire, 
    :OLD.prime, 
    :OLD.email, 
    :OLD.supno, 
    :OLD.labno, 
    :OLD.facno, 
    'UPDATE', 
    SYSTIMESTAMP 
  ); 
END before_update_chercheur; 
CREATE OR REPLACE TRIGGER before_delete_chercheur 
BEFORE DELETE ON chercheur 
FOR EACH ROW 
BEGIN 
  INSERT INTO historique_chercheurs 
  VALUES ( 
    :OLD.chno, 
    :OLD.chnom, 
    :OLD.grade, 
    :OLD.statut, 
    :OLD.daterecrut, 
    :OLD.salaire, 
    :OLD.prime, 
    :OLD.email, 
    :OLD.supno, 
    :OLD.labno, 
    :OLD.facno, 
    'DELETE', 
    SYSTIMESTAMP 
  ); 
END before_delete_chercheur; 
CREATE OR REPLACE TRIGGER before_insert_update_chercheur 
BEFORE INSERT OR UPDATE ON chercheur 
FOR EACH ROW 
DECLARE 
  v_directeur_grade VARCHAR2(2); 
  v_directeur_students_d NUMBER; 
  v_directeur_students_e NUMBER; 
BEGIN 
  -- Retrieve the grade and counts of students supervised by the director (supervisor) 
  SELECT grade, COUNT(*)  
  INTO v_directeur_grade, v_directeur_students_d 
  FROM chercheur 
  WHERE supno = :NEW.supno AND grade = 'D' 
  GROUP BY grade; 
 
  SELECT grade, COUNT(*)  
  INTO v_directeur_grade, v_directeur_students_e 
  FROM chercheur 
  WHERE supno = :NEW.supno AND grade = 'E' 
  GROUP BY grade; 
 
  -- Check if the new chercheur has grade 'D' or 'E', if the director has grade 'PR', and if the director has reached the maximum capacity 
  IF (:NEW.grade = 'D' AND v_directeur_students_d >= 20) OR (:NEW.grade = 'E' AND v_directeur_students_e >= 30) THEN 
    RAISE_APPLICATION_ERROR(-20001, 'Le directeur a atteint la capacité maximale d''encadrement pour ce grade.'); 
  END IF; 
END before_insert_update_chercheur; 
CREATE OR REPLACE TRIGGER before_update_chercheur_salaire 
BEFORE UPDATE ON chercheur 
FOR EACH ROW 
BEGIN 
  -- Check if the new salary is less than the current salary 
  IF :NEW.salaire < :OLD.salaire THEN 
    RAISE_APPLICATION_ERROR(-20002, 'La diminution du salaire d''un chercheur est interdite.'); 
  END IF; 
END before_update_chercheur_salaire; 
CREATE OR REPLACE TRIGGER before_update_check_timing_chercheur 
BEFORE INSERT OR UPDATE OR DELETE 
ON CHERCHEUR  
FOR EACH ROW 
DECLARE 
  v_current_day VARCHAR2(9); 
  v_current_hour NUMBER; 
BEGIN 
  -- Get the current day and hour 
  v_current_day := TO_CHAR(SYSDATE, 'DY'); 
  v_current_hour := TO_NUMBER(TO_CHAR(SYSDATE, 'HH24')); 
 
  -- Check if it's a business day and working hours 
  IF (v_current_day NOT IN ('SAT', 'SUN')) AND (v_current_hour BETWEEN 8 AND 18) THEN 
    -- Valid timing, allow the update 
    NULL; 
  ELSE 
    RAISE_APPLICATION_ERROR(-20003, 'Les mises à jour ne sont autorisées que pendant les jours ouvrables (de 8h à 18h).'); 
  END IF; 
END before_update_check_timing_chercheur; 
CREATE OR REPLACE TRIGGER before_update_check_timing_publication 
BEFORE INSERT OR UPDATE OR DELETE 
ON PUBLICATION 
FOR EACH ROW 
DECLARE 
  v_current_day VARCHAR2(9); 
  v_current_hour NUMBER; 
BEGIN 
  -- Get the current day and hour 
  v_current_day := TO_CHAR(SYSDATE, 'DY'); 
  v_current_hour := TO_NUMBER(TO_CHAR(SYSDATE, 'HH24')); 
 
  -- Check if it's a business day and working hours 
  IF (v_current_day NOT IN ('SAT', 'SUN')) AND (v_current_hour BETWEEN 8 AND 18) THEN 
    -- Valid timing, allow the update 
    NULL; 
  ELSE 
    RAISE_APPLICATION_ERROR(-20003, 'Les mises à jour ne sont autorisées que pendant les jours ouvrables (de 8h à 18h).'); 
  END IF; 
END before_update_check_timing_publication; 
CREATE OR REPLACE TRIGGER before_update_check_timing_faculte 
BEFORE INSERT OR UPDATE OR DELETE 
ON FACULTE 
FOR EACH ROW 
DECLARE 
  v_current_day VARCHAR2(9); 
  v_current_hour NUMBER; 
BEGIN 
  -- Get the current day and hour 
  v_current_day := TO_CHAR(SYSDATE, 'DY'); 
  v_current_hour := TO_NUMBER(TO_CHAR(SYSDATE, 'HH24')); 
 
  -- Check if it's a business day and working hours 
  IF (v_current_day NOT IN ('SAT', 'SUN')) AND (v_current_hour BETWEEN 8 AND 18) THEN 
    -- Valid timing, allow the update 
    NULL; 
  ELSE 
    RAISE_APPLICATION_ERROR(-20003, 'Les mises à jour ne sont autorisées que pendant les jours ouvrables (de 8h à 18h).'); 
  END IF; 
END before_update_check_timing_faculte; 
CREATE OR REPLACE TRIGGER before_update_check_timing_laboratoire 
BEFORE INSERT OR UPDATE OR DELETE 
ON laboratoire 
FOR EACH ROW 
DECLARE 
  v_current_day VARCHAR2(9); 
  v_current_hour NUMBER; 
BEGIN 
  -- Get the current day and hour 
  v_current_day := TO_CHAR(SYSDATE, 'DY'); 
  v_current_hour := TO_NUMBER(TO_CHAR(SYSDATE, 'HH24')); 
 
  -- Check if it's a business day and working hours 
  IF (v_current_day NOT IN ('SAT', 'SUN')) AND (v_current_hour BETWEEN 8 AND 18) THEN 
    -- Valid timing, allow the update 
    NULL; 
  ELSE 
    RAISE_APPLICATION_ERROR(-20003, 'Les mises à jour ne sont autorisées que pendant les jours ouvrables (de 8h à 18h).'); 
  END IF; 
END before_update_check_timing_laboratoire; 
CREATE OR REPLACE TRIGGER before_update_check_timing_publier 
BEFORE INSERT OR UPDATE OR DELETE 
ON publier 
FOR EACH ROW 
DECLARE 
  v_current_day VARCHAR2(9); 
  v_current_hour NUMBER; 
BEGIN 
  -- Get the current day and hour 
  v_current_day := TO_CHAR(SYSDATE, 'DY'); 
  v_current_hour := TO_NUMBER(TO_CHAR(SYSDATE, 'HH24')); 
 
  -- Check if it's a business day and working hours 
  IF (v_current_day NOT IN ('SAT', 'SUN')) AND (v_current_hour BETWEEN 8 AND 18) THEN 
    -- Valid timing, allow the update 
    NULL; 
  ELSE 
    RAISE_APPLICATION_ERROR(-20003, 'Les mises à jour ne sont autorisées que pendant les jours ouvrables (de 8h à 18h).'); 
  END IF; 
END before_update_check_timing_publier; 
