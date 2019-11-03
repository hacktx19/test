import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def test():
	file = "data.db"
	conn = create_db_connection(file)


def create_db_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_table(conn):
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS orgs (
                                        id integer PRIMARY KEY,
                                        org_name text NOT NULL,
                                        resources text
                                    ); """

    try:
        c = conn.cursor()
        c.execute(sql_create_projects_table)
    except Error as e:
        print(e)



def get_from_db(conn):
	cur = conn.cursor()


def post_to_db(conn):
	cur = conn.cursor()


def get_from_chatbot(str):
	print("[BOT] Message `" + str + "` received")
	# Chatbot is supposed to poll str for relevant keywords and then query the database
	result = str
	return result



@app.route('/', methods=['GET'])
def home():
	return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/message', methods=['GET'])
def getMessage():
	query_parameters = request.args
	query = query_parameters.get('query')

	if(query):
		print("Got message `" + query + "` Sending to chatbot")
		result = get_from_chatbot(query)
		test()

	result = query_parameters
	return jsonify(result)

app.run()
