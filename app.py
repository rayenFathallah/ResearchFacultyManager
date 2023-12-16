import uuid
from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
import cx_Oracle

# instantiate the app
app = Flask(__name__)
app.config.from_object(Config)

def create_connection():
    try :
        connection_string = f'{app.config["ORACLE_USER"]}/{app.config["ORACLE_PASSWORD"]}@{app.config["ORACLE_DSN"]}/{app.config["ORACLE_SID"]}'
        return cx_Oracle.connect(
            connection_string)
    except cx_Oracle.DatabaseError as e:
        # Log the error or handle it as needed
        print(f"Database connection error: {e}")
        raise  # Reraise the exception to propagate it further

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

 ### Faculty 
@app.route('/faculties/<faculty_id>', methods=['PUT', 'DELETE'])
def single_book(faculty_id):
    conn = create_connection() 
    cursor = conn.cursor() 
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        cursor.execute("UPDATE FACULTE SET facnom = :1, adresse = :2, libelle = :3 WHERE facno = :4",
                       (post_data.get('facnom'), post_data.get('adresse'), post_data.get('libelle'), faculty_id))

        # Commit the changes
        conn.commit()
        response_object['message'] = 'Faculty updated!'
    if request.method == 'DELETE':
        cursor.execute("DELETE FROM FACULTE WHERE facno = :1", (faculty_id,))
        response_object['message'] = 'Faculty removed!'
        conn.commit() 
        cursor.close() 
        conn.close() 
    return jsonify(response_object)



@app.route('/faculties', methods=['GET', 'POST'])
def all_facultes():
    response_object = {'status': 'success'}
    conn = create_connection() 
    cursor = conn.cursor()
    if request.method == 'POST':
        post_data = request.get_json()
        new_faculty = {"facnom":post_data.get('facnom') , 
                    "adresse" : post_data.get('adresse'), 
                    "libelle" : post_data.get('libelle')} 
        insert_query = "INSERT INTO FACULTE (facnom, adresse, libelle) VALUES (:facnom, :adresse, :libelle)"
        cursor.execute(insert_query, facnom = new_faculty['facnom'],adresse = new_faculty['adresse'],libelle=new_faculty['libelle'])
        conn.commit()
        cursor.close()
        conn.close()
        response_object['message'] = 'Faculty added!'
        return jsonify(response_object)
    else:
        try :
            cursor.execute("SELECT * FROM faculte")
            result = cursor.fetchall()
            formatted_result = []
            for elem in result : 
                formatted_result.append({'facno': elem[0],'facnom' : elem[1],'adresse' : elem[2],'libelle':elem[3]}) 
            response_object['faculties'] = formatted_result

            cursor.close()
            conn.close()
            return jsonify(items=response_object)
        except cx_Oracle.DatabaseError as e:
            cursor.close()
            conn.close()
            return jsonify(error=str(e)), 500
    

### Labos 

@app.route('/labos', methods=['GET', 'POST'])
def all_labs():
    response_object = {'status': 'success'}
    conn = create_connection() 
    cursor = conn.cursor()
    if request.method == 'POST':
        post_data = request.get_json()
        new_lab = {"labnom":post_data.get('labnom') , 
                    "facno" : post_data.get('facno')}
        insert_query = "INSERT INTO laboratoire (labnom, facno) VALUES (:labnom , : facno)"
        cursor.execute(insert_query, labnom = new_lab['labnom'],facno = new_lab['facno'])
        conn.commit()
        cursor.close()
        conn.close()
        response_object['message'] = 'Lab added!'
        return jsonify(response_object)
    else:
        try :
            cursor.execute("SELECT * FROM laboratoire")
            result = cursor.fetchall()
            formatted_result = []
            for elem in result : 
                formatted_result.append({'labno': elem[0],'labnom' : elem[1],'facno' : elem[2]}) 
            response_object['labos'] = formatted_result

            cursor.close()
            conn.close()
            return jsonify(items=response_object)
        except cx_Oracle.DatabaseError as e:
            cursor.close()
            conn.close()
            return jsonify(error=str(e)), 500
@app.route('/labos/<lab_id>', methods=['PUT', 'DELETE'])
def single_lab(lab_id):
    conn = create_connection() 
    cursor = conn.cursor() 
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        cursor.execute("UPDATE laboratoire SET facno = :1, labnom:2 WHERE labno = :3",
                       (post_data.get('facno'), post_data.get('labnom'), lab_id))

        # Commit the changes
        conn.commit()
        response_object['message'] = 'Faculty updated!'
    if request.method == 'DELETE':
        cursor.execute("DELETE FROM laboratoire WHERE labno = :1", (lab_id,))
        response_object['message'] = 'Lab removed!'
        conn.commit() 
        cursor.close() 
        conn.close() 
    return jsonify(response_object)


 ### Publications 

@app.route('/publications', methods=['GET', 'POST'])
def all_pubs():
    response_object = {'status': 'success'}
    conn = create_connection() 
    cursor = conn.cursor()
    if request.method == 'POST':
        post_data = request.get_json()
        new_pub = {"titre":post_data.get('titre') , 
                    "theme" : post_data.get('theme'),
                    "type" : post_data.get('type'), 
                    "volume":post_data.get('volume') , 
                    "date_edit" : post_data.get("date"), 
                    "apparition" : post_data.get("apparition"), 
                    "editeur" : post_data.get("editeur"),
                    "pubno" : post_data.get("pubno"),
                    "chercheurs" : post_data.get("chercheurs")
                    }
        insert_query = "INSERT INTO publication (pubno, titre, theme,type,volume,date_edit,apparition,editeur) VALUES (:pubno, :titre , : theme, :type,:volume , :date_edit , :apparition, :editeur)"
        cursor.execute(insert_query, pubno = new_pub['pubno'],titre= new_pub['titre'],theme = new_pub['type'],type = new_pub['type'], volume = new_pub['volume'],date_edit = datetime.strptime(new_pub['date_edit'], "%d-%b-%Y"),apparition = new_pub['apparition'],editeur = new_pub['editeur'])
        insert_query2 = "INSERT INTO publier (pubno,chno) VALUES (:pubno , :chno)" 
        for elem in new_pub['chercheurs'] : 
            cursor.execute(insert_query2,pubno = new_pub['pubno'],chno= elem)
        conn.commit()
        cursor.close()
        conn.close()
        response_object['message'] = 'Publication added!'
        return jsonify(response_object)
    else:
        try :
            cursor.execute("SELECT * FROM publication")
            result = cursor.fetchall()
            formatted_result = []
            for elem in result : 
                formatted_result.append({'pubno': elem[0],'titre' : elem[1],'theme' : elem[2],'type':elem[3],'volume':elem[4],'date':elem[5],'apparition' : elem[6],'editeur': elem[7]}) 
            
            response_object['publications'] = formatted_result
            cursor.close()
            conn.close()
            return jsonify(items=response_object)
        except cx_Oracle.DatabaseError as e:
            cursor.close()
            conn.close()
            return jsonify(error=str(e)), 500
@app.route('/publications/<pub_id>', methods=['PUT', 'DELETE'])
def single_pub(pub_id):
    conn = create_connection() 
    cursor = conn.cursor() 
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        cursor.execute("UPDATE publication SET titre = :1, theme:2, type:3, volume:4, date:5, apparition:6, editeur:7 WHERE pubno = :8",
                       (post_data.get('titre'), post_data.get('theme'),post_data.get('type'),post_data.get('volume'),post_data.get('date'),post_data.get('apparition'),post_data.get('editeur'), pub_id))

        # Commit the changes
        conn.commit()
        response_object['message'] = 'Publication updated!'
    if request.method == 'DELETE':
        cursor.execute("DELETE FROM publication WHERE pubno = :1", (pub_id,))
        response_object['message'] = 'Publication removed!'
        conn.commit() 
        cursor.close() 
        conn.close() 
    return jsonify(response_object)

### chercheurs 
@app.route('/chercheurs', methods=['GET', 'POST'])
def all_cherch():
    response_object = {'status': 'success'}
    conn = create_connection() 
    cursor = conn.cursor()
    if request.method == 'POST':
        post_data = request.get_json()
        new_pub = {"chnom":post_data.get('chnom') , 
                    "grade" : post_data.get('grade'),
                    "statut" : post_data.get('statut'), 
                    "daterecrut":post_data.get('daterecrut') , 
                    "salaire" : post_data.get("salaire"), 
                    "prime" : post_data.get("prime"), 
                    "email" : post_data.get("email"),
                    "supno" : post_data.get("supno"),
                    "labno" : post_data.get("labno"),
                    "facno" : post_data.get("facno"),
                    }
        insert_query = "INSERT INTO chercheur (chnom, grade, statut,daterecrut,salaire,prime,email,supno,labno,facno) VALUES (:chnom, :grade , :statut, :daterecrut,:salaire , :prime , :email, :supno,:labno,:facno)"
        cursor.execute(insert_query, chnom = new_pub['chnom'],grade= new_pub['grade'],statut = new_pub['statut'],daterecrut = datetime.strptime(new_pub['daterecrut'], "%d-%b-%Y") , salaire = new_pub['salaire'],prime = new_pub['prime'],email = new_pub['email'],supno = new_pub['supno'],labno=new_pub['labno'],facno=new_pub['facno'])
        conn.commit()
        cursor.close()
        conn.close()
        response_object['message'] = 'Researcher added!'
        return jsonify(response_object)
    else:
        try :
            cursor.execute("SELECT * FROM chercheur")
            result = cursor.fetchall()
            formatted_result = []
            for elem in result : 
                formatted_result.append({'chno': elem[0],'chnom' : elem[1],'grade' : elem[2],'statut':elem[3],'daterecrut':elem[4],'salaire':elem[5],'prime' : elem[6],'email': elem[7],"supno":elem[8],"labno":elem[9],"facno":elem[10]}) 
            
            response_object['chercheurs'] = formatted_result
            cursor.close()
            conn.close()
            return jsonify(items=response_object)
        except cx_Oracle.DatabaseError as e:
            cursor.close()
            conn.close()
            return jsonify(error=str(e)), 500
@app.route('/chercheurs/<cherch_id>', methods=['PUT', 'DELETE'])
def single_cherch(cherch_id):
    conn = create_connection() 
    cursor = conn.cursor() 
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        cursor.execute("UPDATE chercheur SET titre = :1, theme:2, type:3, volume:4, date:5, apparition:6, editeur:7 WHERE pubno = :8",
                       (post_data.get('titre'), post_data.get('theme'),post_data.get('type'),post_data.get('volume'),post_data.get('date'),post_data.get('apparition'),post_data.get('editeur'), pub_id))

        # Commit the changes
        conn.commit()
        response_object['message'] = 'Publication updated!'
    if request.method == 'DELETE':
        cursor.execute("DELETE FROM chercheur WHERE chno = :1", (cherch_id,))
        response_object['message'] = 'Researcher removed!'
        conn.commit() 
        cursor.close() 
        conn.close() 
    return jsonify(response_object)
 ### publier : 
@app.route('/publicas', methods=['GET'])
def all_publicas():
    response_object = {'status': 'success'}
    conn = create_connection() 
    cursor = conn.cursor()
    try :
        cursor.execute("select ch.chnom, pub.pubno, pub.titre,pub.theme,pub.type,pub.volume,pub.date_edit,pub.apparition,pub.editeur from chercheur ch, publication pub, publier pb where pub.pubno = pb.pubno and ch.chno = pb.chno ")
        result = cursor.fetchall()
        formatted_result = []
        #columns = [desc[0].lower() for desc in cursor.description]
        #formatted_result= [dict(zip(columns, row)) for row in result]
        publications = {}

        # Iterate through the rows and aggregate researchers for each publication
        for row in result:
            pubno = row[1]  # Assuming pubno is the second column in the result
            chercheur_name = row[0]  # Assuming chnom is the first column in the result
            if pubno not in publications:
                # Initialize the publication with an empty list of researchers
                publications[pubno] = {
                    'pubno': pubno,
                    'titre': row[2],
                    'theme': row[3],
                    'type': row[4],
                    'volume': row[5],
                    'date_edit': row[6],
                    'apparition': row[7],
                    'editeur': row[8],
                    'chercheurs': []
                }
            # Add the researcher name to the list of researchers for this publication
            publications[pubno]['chercheurs'].append(chercheur_name)
        response_object['publicas']= list(publications.values())
        cursor.close()
        conn.close()
        return jsonify(items=response_object)
    except cx_Oracle.DatabaseError as e:
        cursor.close()
        conn.close()
        return jsonify(error=str(e)), 500








if __name__ == '__main__':
    app.run()
