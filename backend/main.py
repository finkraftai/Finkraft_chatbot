# # import openai
# # import signal
# # import re

# # # Initialize OpenAI client
# # client = openai.AzureOpenAI(
# #     azure_endpoint="https://finkdataopenai.openai.azure.com/",
# #     api_key='d57b4f240c6f4c12bb8d316469e45f69',
# #     api_version="2024-02-15-preview"
# # )

# # # Function to extract Finkraft information from the text file
# # def extract_finkraft_info(filename):
# #     with open(filename, 'r', encoding='utf-8') as file:
# #         data = file.read()
# #     # Example: Extracting relevant information about Finkraft
# #     # You can modify this part based on what specific information you want to extract
# #     return data


# # # Function to handle queries and generate responses
# # def query(user_input):
    
# #     if not bot_response:
# #         # Call OpenAI API to generate a response based on user input
# #         completion = client.chat.completions.create(
# #             model="gpt-35-turbo",
# #             messages=[
# #                 {"role": "system", "content": "I'm a chat bot"},
# #                 {"role": "user", "content": user_input}
# #             ],
# #             temperature=0.7,
# #             max_tokens=150,
# #             top_p=1.0,
# #             frequency_penalty=0,
# #             presence_penalty=0,
# #             stop=None
# #         )
# #         bot_response = completion.choices[0].message.content
    
# #     return bot_response

# # # Main function to handle user interaction
# # def main():
# #     print("Welcome! Chat with the bot (Press Ctrl+C to exit)")
# #     try:
# #         while True:
# #             user_input = input("You: ")
# #             bot_response = query(user_input)
# #             print("Bot:", bot_response)
# #     except KeyboardInterrupt:
# #         print("\nChat ended.")

# # if __name__ == "__main__":
# #     main()
# # import openai
# # import re

# # # Your API key and endpoint
# # client = openai.AzureOpenAI(
# #     azure_endpoint="https://finkdataopenai.openai.azure.com/",
# #     api_key='d57b4f240c6f4c12bb8d316469e45f69',
# #     api_version="2024-02-15-preview"
# # )

# # # Load and store the content of all_website_data.txt
# # def load_finkraft_data():
# #     with open('all_website_data.txt', 'r', encoding='utf-8') as file:
# #         return file.read()

# # # Extract information from the loaded text
# # def extract_info(data, query):
# #     pattern = re.compile(re.escape(query), re.IGNORECASE)
# #     matches = pattern.finditer(data)
# #     results = []
# #     for match in matches:
# #         start_index = max(0, match.start() - 100)  # Get 100 characters before the match
# #         end_index = min(len(data), match.end() + 100)  # Get 100 characters after the match
# #         results.append(data[start_index:end_index])
# #     if results:
# #         return "\n...\n".join(results)
# #     else:
# #         return f"No specific information found for '{query}' in the provided data."

# # # Query function to handle both Finkraft-related and general queries
# # def query(user_input, data):
# #     extracted_response = extract_info(data, user_input)
# #     if "No specific information found" not in extracted_response:
# #         return extracted_response
    
# #     completion = client.chat.completions.create(
# #         model="gpt-35-turbo",
# #         messages=[
# #             {"role": "system", "content": "I'm a chat bot"},
# #             {"role": "user", "content": user_input}
# #         ],
# #         temperature=0.7,
# #         max_tokens=150,
# #         top_p=1.0,
# #         frequency_penalty=0,
# #         presence_penalty=0,
# #         stop=None
# #     )
# #     bot_response = completion.choices[0].message.content
# #     return bot_response

# # # Main function to handle user interaction
# # def main():
# #     print("Welcome! Chat with the bot (Press Ctrl+C to exit)")
# #     data = load_finkraft_data()  # Load data once at the start
# #     try:
# #         while True:
# #             user_input = input("You: ")
# #             bot_response = query(user_input, data)
# #             print("Bot:", bot_response)
# #     except KeyboardInterrupt:
# #         print("\nChat ended.")

# # if __name__ == "__main__":
# #     main()


# # from flask import Flask, request, jsonify
# # import openai
# # import re
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS, cross_origin  # Import CORS module

# # app = Flask(__name__)
# # CORS(app) 


# # # Your API key and endpoint
# # client = openai.AzureOpenAI(
# #     azure_endpoint="https://finkdataopenai.openai.azure.com/",
# #     api_key='d57b4f240c6f4c12bb8d316469e45f69',
# #     api_version="2024-02-15-preview"
# # )

# # # Load and store the content of all_website_data.txt
# # def load_finkraft_data():
# #     with open('all_website_data.txt', 'r', encoding='utf-8') as file:
# #         return file.read()

# # data = load_finkraft_data() 

# # def extract_info(data, query):
# #     pattern = re.compile(re.escape(query), re.IGNORECASE)
# #     matches = pattern.finditer(data)
# #     results = []
# #     for match in matches:
# #         start_index = max(0, match.start() - 100)  # Get 100 characters before the match
# #         end_index = min(len(data), match.end() + 100)  # Get 100 characters after the match
# #         results.append(data[start_index:end_index])
# #     if results:
# #         return "\n...\n".join(results)
# #     else:
# #         return f"No specific information found for '{query}' in the provided data."

# # # Query function to handle both Finkraft-related and general queries
# # def query(user_input, data):
# #     extracted_response = extract_info(data, user_input)
# #     if "No specific information found" not in extracted_response:
# #         return extracted_response
    
# #     completion = client.chat.completions.create(
# #         model="gpt-35-turbo",
# #         messages=[
# #             {"role": "system", "content": "I'm a chat bot"},
# #             {"role": "user", "content": user_input}
# #         ],
# #         temperature=0.7,
# #         max_tokens=150,
# #         top_p=1.0,
# #         frequency_penalty=0,
# #         presence_penalty=0,
# #         stop=None
# #     )
# #     bot_response = completion.choices[0].message.content
# #     return bot_response

# # @app.route('/chat', methods=['POST'])
# # def chat():
# #     user_input = request.json.get('message')
# #     response = query(user_input, data)
# #     return jsonify({'response': response})

# # if __name__ == "__main__":
# #     app.run(debug=True)


# # from flask import Flask, request, jsonify
# # import openai
# # import re
# # from flask_cors import CORS
# # import mysql.connector
# # from mysql.connector import errorcode

# # app = Flask(__name__)
# # CORS(app)

# # # Azure OpenAI configuration
# # openai.api_base = "https://finkdataopenai.openai.azure.com/"
# # openai.api_key = 'd57b4f240c6f4c12bb8d316469e45f69'
# # openai.api_version = "2024-02-15-preview"

# # # MySQL connection configuration
# # mysql_config = {
# #     'host': 'localhost',
# #     'user': 'root',
# #     'password': '1234',
# #     'database': 'STUDEN1',
# #     'raise_on_warnings': True
# # }

# # # Initialize MySQL connection
# # def get_db_connection():
# #     conn = mysql.connector.connect(**mysql_config)
# #     return conn

# # # Create the table if it doesn't exist
# # def create_table(cursor):
# #     table_schema = (
# #         "CREATE TABLE IF NOT EXISTS CHATGPT ("
# #         "  email_id VARCHAR(255) PRIMARY KEY,"
# #         "  user_input TEXT NOT NULL,"
# #         "  bot_response TEXT NOT NULL"
# #         ")"
# #     )
# #     try:
# #         cursor.execute(table_schema)
# #     except mysql.connector.Error as err:
# #         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
# #             print("CHATGPT table already exists.")
# #         else:
# #             print(err.msg)

# # # Load and store the content of all_website_data.txt
# # def load_finkraft_data():
# #     try:
# #         with open('all_website_data.txt', 'r', encoding='utf-8') as file:
# #             return file.read()
# #     except FileNotFoundError:
# #         return "Data file not found."

# # data = load_finkraft_data()

# # # Function to extract relevant information from the data
# # def extract_info(data, query):
# #     pattern = re.compile(re.escape(query), re.IGNORECASE)
# #     matches = pattern.finditer(data)
# #     results = []
# #     for match in matches:
# #         start_index = max(0, match.start() - 100)  # Get 100 characters before the match
# #         end_index = min(len(data), match.end() + 100)  # Get 100 characters after the match
# #         results.append(data[start_index:end_index])
# #     if results:
# #         return "\n...\n".join(results)
# #     else:
# #         return f"No specific information found for '{query}' in the provided data."

# # # Query function to handle both Finkraft-related and general queries
# # def query(user_input, data, cursor, conn, email_id):
# #     extracted_response = extract_info(data, user_input)
# #     if "No specific information found" not in extracted_response:
# #         bot_response = extracted_response
# #     else:
# #         completion = openai.ChatCompletion.create(
# #             model="gpt-35-turbo",
# #             messages=[
# #                 {"role": "system", "content": "I'm a chat bot"},
# #                 {"role": "user", "content": user_input}
# #             ],
# #             temperature=0.7,
# #             max_tokens=150,
# #             top_p=1.0,
# #             frequency_penalty=0,
# #             presence_penalty=0
# #         )
# #         bot_response = completion.choices[0].message['content']
    
# #     # Check if email ID already exists in the database
# #     cursor.execute("SELECT COUNT(*) FROM CHATGPT WHERE email_id = %s", (email_id,))
# #     if cursor.fetchone()[0] == 0:
# #         # Insert initial row for this chat session if email ID does not exist
# #         insert_initial_row(cursor, conn, email_id)
# #     # Update conversation in the MySQL database
# #     update_row(cursor, conn, email_id, user_input, bot_response)
    
# #     return bot_response

# # # Insert initial row in the database
# # def insert_initial_row(cursor, conn, email_id):
# #     insert_query = "INSERT INTO CHATGPT (email_id, user_input, bot_response) VALUES (%s, %s, %s)"
# #     cursor.execute(insert_query, (email_id, '', ''))
# #     conn.commit()

# # # Update row in the database
# # def update_row(cursor, conn, email_id, user_input, bot_response):
# #     update_query = (
# #         "UPDATE CHATGPT "
# #         "SET user_input = CONCAT(user_input, %s), "
# #         "    bot_response = CONCAT(bot_response, %s) "
# #         "WHERE email_id = %s"
# #     )
# #     cursor.execute(update_query, (f'\nUser: {user_input}', f'\nBot: {bot_response}', email_id))
# #     conn.commit()

# # @app.route('/chat', methods=['POST'])
# # def chat():
# #     user_input = request.json.get('message')
# #     email_id = request.json.get('email_id')
# #     if not user_input or not email_id:
# #         return jsonify({'error': 'No message or email ID provided'}), 400

# #     conn = get_db_connection()
# #     cursor = conn.cursor()
    
# #     response = query(user_input, data, cursor, conn, email_id)
    
# #     cursor.close()
# #     conn.close()
    
# #     return jsonify({'response': response})

# # if __name__ == "__main__":
# #     # Initialize database connection and create table if it doesn't exist
# #     conn = get_db_connection()
# #     cursor = conn.cursor()
# #     create_table(cursor)
# #     cursor.close()
# #     conn.close()

# #     # Run the Flask application
# #     app.run(debug=True)


# # from flask import Flask, jsonify
# # import openai
# # import re
# # from flask_cors import CORS
# # import mysql.connector
# # from mysql.connector import errorcode

# # app = Flask(__name__)
# # CORS(app)

# # # Azure OpenAI configuration
# # openai.api_base = "https://finkdataopenai.openai.azure.com/"
# # openai.api_key = 'd57b4f240c6f4c12bb8d316469e45f69'
# # openai.api_version = "2024-02-15-preview"

# # # MySQL connection configuration
# # mysql_config = {
# #     'host': 'localhost',
# #     'user': 'root',
# #     'password': '1234',
# #     'database': 'STUDEN1',
# #     'raise_on_warnings': True
# # }

# # # Initialize MySQL connection
# # def get_db_connection():
# #     conn = mysql.connector.connect(**mysql_config)
# #     return conn

# # # Create the table if it doesn't exist
# # def create_table(cursor):
# #     table_schema = (
# #         "CREATE TABLE IF NOT EXISTS CHATGPT ("
# #         "  email_id VARCHAR(255) PRIMARY KEY,"
# #         "  user_input TEXT NOT NULL,"
# #         "  bot_response TEXT NOT NULL"
# #         ")"
# #     )
# #     try:
# #         cursor.execute(table_schema)
# #     except mysql.connector.Error as err:
# #         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
# #             print("CHATGPT table already exists.")
# #         else:
# #             print(err.msg)

# # # Load and store the content of all_website_data.txt
# # def load_finkraft_data():
# #     try:
# #         with open('all_website_data.txt', 'r', encoding='utf-8') as file:
# #             return file.read()
# #     except FileNotFoundError:
# #         return "Data file not found."

# # data = load_finkraft_data()

# # # Function to extract relevant information from the data
# # def extract_info(data, query):
# #     pattern = re.compile(re.escape(query), re.IGNORECASE)
# #     matches = pattern.finditer(data)
# #     results = []
# #     for match in matches:
# #         start_index = max(0, match.start() - 100)  # Get 100 characters before the match
# #         end_index = min(len(data), match.end() + 100)  # Get 100 characters after the match
# #         results.append(data[start_index:end_index])
# #     if results:
# #         return "\n...\n".join(results)
# #     else:
# #         return f"No specific information found for '{query}' in the provided data."

# # # Query function to handle both Finkraft-related and general queries
# # def query(user_input, data, cursor, conn, email_id):
# #     extracted_response = extract_info(data, user_input)
# #     if "No specific information found" not in extracted_response:
# #         bot_response = extracted_response
# #     else:
# #         completion = openai.ChatCompletion.create(
# #             model="gpt-35-turbo",
# #             messages=[
# #                 {"role": "system", "content": "I'm a chat bot"},
# #                 {"role": "user", "content": user_input}
# #             ],
# #             temperature=0.7,
# #             max_tokens=150,
# #             top_p=1.0,
# #             frequency_penalty=0,
# #             presence_penalty=0
# #         )
# #         bot_response = completion.choices[0].message['content']
    
# #     # Check if email ID already exists in the database
# #     cursor.execute("SELECT COUNT(*) FROM CHATGPT WHERE email_id = %s", (email_id,))
# #     if cursor.fetchone()[0] == 0:
# #         # Insert initial row for this chat session if email ID does not exist
# #         insert_initial_row(cursor, conn, email_id)
# #     # Update conversation in the MySQL database
# #     update_row(cursor, conn, email_id, user_input, bot_response)
    
# #     return bot_response

# # # Insert initial row in the database
# # def insert_initial_row(cursor, conn, email_id):
# #     insert_query = "INSERT INTO CHATGPT (email_id, user_input, bot_response) VALUES (%s, %s, %s)"
# #     cursor.execute(insert_query, (email_id, '', ''))
# #     conn.commit()

# # # Update row in the database
# # def update_row(cursor, conn, email_id, user_input, bot_response):
# #     update_query = (
# #         "UPDATE CHATGPT "
# #         "SET user_input = CONCAT(user_input, %s), "
# #         "    bot_response = CONCAT(bot_response, %s) "
# #         "WHERE email_id = %s"
# #     )
# #     cursor.execute(update_query, (f'\nUser: {user_input}', f'\nBot: {bot_response}', email_id))
# #     conn.commit()

# # def ask_for_input():
# #     email_id = input("Enter your email ID: ")
# #     user_input = input("Enter your message: ")
# #     return email_id, user_input

# # @app.route('/chat', methods=['GET'])
# # def chat():
# #     email_id, user_input = ask_for_input()
# #     if not user_input or not email_id:
# #         return jsonify({'error': 'No message or email ID provided'}), 400

# #     conn = get_db_connection()
# #     cursor = conn.cursor()
    
# #     response = query(user_input, data, cursor, conn, email_id)
    
# #     cursor.close()
# #     conn.close()
    
# #     return jsonify({'response': response})

# # if __name__ == "__main__":
# #     # Initialize database connection and create table if it doesn't exist
# #     conn = get_db_connection()
# #     cursor = conn.cursor()
# #     create_table(cursor)
# #     cursor.close()
# #     conn.close()

# #     # Run the Flask application
# #     app.run(debug=True)



# import mysql.connector
# from mysql.connector import errorcode
# import json
# import openai
# from fuzzywuzzy import fuzz

# # MySQL connection configuration
# mysql_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '1234',
#     'database': 'STUDEN1',
#     'raise_on_warnings': True
# }

# # Load Finkraft data from JSON file
# with open('finkraft_data.json', 'r') as file:
#     finkraft_data = json.load(file)

# # Initialize OpenAI client
# client = openai.AzureOpenAI(
#     azure_endpoint="https://finkdataopenai.openai.azure.com/",
#     api_key='d57b4f240c6f4c12bb8d316469e45f69',
#     api_version="2024-02-15-preview"
# )

# def extract_information(data, query, threshold=80):
#     """
#     Recursively extract relevant information from nested data based on the user's query
#     with fuzzy matching.
#     """
#     # Normalize the query
#     query = query.lower()
    
#     # Define a list to hold matching values
#     extracted_values = []
    
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if fuzz.partial_ratio(query, key.lower()) >= threshold:
#                 if isinstance(value, (dict, list)):
#                     nested_values = extract_information(value, query, threshold)
#                     extracted_values.extend(nested_values)
#                 else:
#                     extracted_values.append(str(value))
#             elif isinstance(value, (dict, list)):
#                 nested_values = extract_information(value, query, threshold)
#                 extracted_values.extend(nested_values)
#     elif isinstance(data, list):
#         for item in data:
#             nested_values = extract_information(item, query, threshold)
#             extracted_values.extend(nested_values)
    
#     return extracted_values

# def is_related_to_finkraft(query):
#     """
#     Check if the query is related to FinKraft AI using fuzzy matching.
#     Adjust the threshold as needed for accuracy.
#     """
#     keywords = ["finkraft", "fink", "fink ai", "finkraft ai"]
#     query = query.lower()
    
#     for keyword in keywords:
#         if fuzz.partial_ratio(query, keyword) >= 90:  # Adjust threshold as needed
#             return True
#     return False

# def query(user_input, cursor, conn, email_id):
#     try:
#         # Check if the query is related to FinKraft AI
#         if not is_related_to_finkraft(user_input):
#             return "I'm a chatbot providing information about FinKraft AI. Please ask about FinKraft AI."

#         # Extract relevant information from finkraft_data
#         info = extract_information(finkraft_data, user_input)

#         if info:
#             # Format the extracted information
#             bot_response = "\n".join(info)
#         else:
#             # Call OpenAI API using appropriate method if info not found in JSON
#             completion = client.chat.completions.create(
#                 model="gpt-35-turbo",
#                 messages=[
#                     {"role": "system", "content": "I'm a chatbot providing information about FinKraft AI. Here is the FinKraft AI data."},
#                     {"role": "user", "content": user_input}
#                 ],
#                 temperature=0.7,
#                 max_tokens=150,
#                 top_p=1.0,
#                 frequency_penalty=0,
#                 presence_penalty=0,
#                 stop=None
#             )
#             bot_response = completion.choices[0].message.content

#         # Update conversation in the MySQL database
#         update_row(cursor, conn, email_id, user_input, bot_response)
#         return bot_response

#     except mysql.connector.Error as err:
#         print(f"Error executing MySQL query: {err}")
#         return None

# def create_table(cursor):
#     table_schema = (
#         "CREATE TABLE IF NOT EXISTS CHATGPT ("
#         "  email_id VARCHAR(255) PRIMARY KEY,"
#         "  user_input TEXT NOT NULL,"
#         "  bot_response TEXT NOT NULL"
#         ")"
#     )
#     try:
#         cursor.execute(table_schema)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("CHATGPT table already exists.")
#         else:
#             print(err.msg)

# def insert_initial_row(cursor, conn, email_id):
#     insert_query = "INSERT INTO CHATGPT (email_id, user_input, bot_response) VALUES (%s, %s, %s)"
#     cursor.execute(insert_query, (email_id, '', ''))
#     conn.commit()

# def update_row(cursor, conn, email_id, user_input, bot_response):
#     update_query = (
#         "UPDATE CHATGPT "
#         "SET user_input = CONCAT(user_input, %s), "
#         "    bot_response = CONCAT(bot_response, %s) "
#         "WHERE email_id = %s"
#     )
#     cursor.execute(update_query, (f'\nUser: {user_input}', f'\nBot: {bot_response}', email_id))
#     conn.commit()

# def main():
#     try:
#         # Connect to MySQL
#         conn = mysql.connector.connect(**mysql_config)
#         cursor = conn.cursor()

#         # Create table if not exists
#         create_table(cursor)

#         # Prompt for email ID
#         email_id = input("Enter your email ID: ")
#         print("Welcome! Chat with the bot (Press Ctrl+C to exit)")

#         while True:
#             user_input = input("You: ")
#             bot_response = query(user_input, cursor, conn, email_id)
#             print("Bot:", bot_response)

#     except mysql.connector.Error as err:
#         print(f"MySQL error: {err}")

#     except KeyboardInterrupt:
#         print("\nChat ended.")

#     finally:
#         # Close cursor and connection
#         if 'cursor' in locals() and cursor:
#             cursor.close()
#         if 'conn' in locals() and conn:
#             conn.close()

# if __name__ == "__main__":
#     main()

# import mysql.connector
# from mysql.connector import errorcode
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import json
# import openai
# from fuzzywuzzy import fuzz

# # MySQL connection configuration
# mysql_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '1234',
#     'database': 'STUDEN1',
#     'raise_on_warnings': True
# }

# # Initialize Flask app
# app = Flask(__name__)
# CORS(app)

# # Load Finkraft data from JSON file
# with open('finkraft_data.json', 'r') as file:
#     finkraft_data = json.load(file)

# # Initialize OpenAI client
# client = openai.AzureOpenAI(
#     azure_endpoint="https://finkdataopenai.openai.azure.com/",
#     api_key='d57b4f240c6f4c12bb8d316469e45f69',
#     api_version="2024-02-15-preview"
# )

# def extract_information(data, query, threshold=80):
#     """
#     Recursively extract relevant information from nested data based on the user's query
#     with fuzzy matching.
#     """
#     # Normalize the query
#     query = query.lower()
    
#     # Define a list to hold matching values
#     extracted_values = []
    
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if fuzz.partial_ratio(query, key.lower()) >= threshold:
#                 if isinstance(value, (dict, list)):
#                     nested_values = extract_information(value, query, threshold)
#                     extracted_values.extend(nested_values)
#                 else:
#                     extracted_values.append(str(value))
#             elif isinstance(value, (dict, list)):
#                 nested_values = extract_information(value, query, threshold)
#                 extracted_values.extend(nested_values)
#     elif isinstance(data, list):
#         for item in data:
#             nested_values = extract_information(item, query, threshold)
#             extracted_values.extend(nested_values)
    
#     return extracted_values

# def is_related_to_finkraft(query):
#     """
#     Check if the query is related to FinKraft AI using fuzzy matching.
#     Adjust the threshold as needed for accuracy.
#     """
#     keywords = ["finkraft", "fink", "fink ai", "finkraft ai"]
#     query = query.lower()
    
#     for keyword in keywords:
#         if fuzz.partial_ratio(query, keyword) >= 90:  # Adjust threshold as needed
#             return True
#     return False

# def query(user_input, cursor, conn, email_id):
#     try:
#         # Check if the query is related to FinKraft AI
#         if not is_related_to_finkraft(user_input):
#             return "I'm a chatbot providing information about FinKraft AI. Please ask about FinKraft AI."

#         # Extract relevant information from finkraft_data
#         info = extract_information(finkraft_data, user_input)

#         if info:
#             # Format the extracted information
#             bot_response = "\n".join(info)
#         else:
#             # Call OpenAI API using appropriate method if info not found in JSON
#             completion = client.chat.completions.create(
#                 model="gpt-35-turbo",
#                 messages=[
#                     {"role": "system", "content": "I'm a chatbot providing information about FinKraft AI. Here is the FinKraft AI data."},
#                     {"role": "user", "content": user_input}
#                 ],
#                 temperature=0.7,
#                 max_tokens=150,
#                 top_p=1.0,
#                 frequency_penalty=0,
#                 presence_penalty=0,
#                 stop=None
#             )
#             bot_response = completion.choices[0].message.content

#         # Update conversation in the MySQL database
#         update_row(cursor, conn, email_id, user_input, bot_response)
#         return bot_response

#     except mysql.connector.Error as err:
#         print(f"Error executing MySQL query: {err}")
#         return None

# def create_table(cursor):
#     table_schema = (
#         "CREATE TABLE IF NOT EXISTS CHATGPT ("
#         "  email_id VARCHAR(255) PRIMARY KEY,"
#         "  user_input TEXT NOT NULL,"
#         "  bot_response TEXT NOT NULL"
#         ")"
#     )
#     try:
#         cursor.execute(table_schema)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("CHATGPT table already exists.")
#         else:
#             print(err.msg)

# def insert_initial_row(cursor, conn, email_id):
#     insert_query = "INSERT INTO CHATGPT (email_id, user_input, bot_response) VALUES (%s, %s, %s)"
#     cursor.execute(insert_query, (email_id, '', ''))
#     conn.commit()

# def update_row(cursor, conn, email_id, user_input, bot_response):
#     select_query = "SELECT * FROM CHATGPT WHERE email_id = %s"
#     cursor.execute(select_query, (email_id,))
#     result = cursor.fetchone()

#     if result:
#         # If user exists, update the existing row
#         update_query = (
#             "UPDATE CHATGPT "
#             "SET user_input = CONCAT(user_input, %s), "
#             "    bot_response = CONCAT(bot_response, %s) "
#             "WHERE email_id = %s"
#         )
#         cursor.execute(update_query, (f'\nUser: {user_input}', f'\nBot: {bot_response}', email_id))
#     else:
#         # If user does not exist, insert a new row
#         insert_query = "INSERT INTO CHATGPT (email_id, user_input, bot_response) VALUES (%s, %s, %s)"
#         cursor.execute(insert_query, (email_id, f'User: {user_input}', f'Bot: {bot_response}'))
    
#     conn.commit()

# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         data = request.get_json()
#         message = data['message']
#         email = data['email'] 
        
#         # Connect to MySQL
#         conn = mysql.connector.connect(**mysql_config)
#         cursor = conn.cursor()

#         # Create table if not exists
#         create_table(cursor)

#         # Query bot response
#         bot_response = query(message, cursor, conn, email)

#         # Close cursor and connection
#         cursor.close()
#         conn.close()

#         return jsonify({'response': bot_response})

#     except Exception as e:
#         return jsonify({'error': str(e)})

# if __name__ == "__main__":
#     app.run(debug=True)
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import openai
from fuzzywuzzy import fuzz
# MySQL connection configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'STUDEN1',
    'raise_on_warnings': True
}
# Initialize Flask app
app = Flask(__name__)
CORS(app)
# Load Finkraft data from JSON file
with open('finkraft_data.json', 'r') as file:
    finkraft_data = json.load(file)
# Initialize OpenAI client
client = openai.AzureOpenAI(
    azure_endpoint="https://finkdataopenai.openai.azure.com/",
    api_key='d57b4f240c6f4c12bb8d316469e45f69',
    api_version="2024-02-15-preview"
)
def extract_information(data, query, threshold=80):
    """
    Recursively extract relevant information from nested data based on the user's query
    with fuzzy matching.
    """
    # Normalize the query
    query = query.lower()
    # Define a list to hold matching values
    extracted_values = []
    if isinstance(data, dict):
        for key, value in data.items():
            if fuzz.partial_ratio(query, key.lower()) >= threshold:
                if isinstance(value, (dict, list)):
                    nested_values = extract_information(value, query, threshold)
                    extracted_values.extend(nested_values)
                else:
                    extracted_values.append(str(value))
            elif isinstance(value, (dict, list)):
                nested_values = extract_information(value, query, threshold)
                extracted_values.extend(nested_values)
    elif isinstance(data, list):
        for item in data:
            nested_values = extract_information(item, query, threshold)
            extracted_values.extend(nested_values)
    return extracted_values
def is_related_to_finkraft(query):
    """
    Check if the query is related to FinKraft AI using fuzzy matching.
    Adjust the threshold as needed for accuracy.
    """
    keywords = ["finkraft", "fink", "fink ai", "finkraft ai"]
    query = query.lower()
    for keyword in keywords:
        if fuzz.partial_ratio(query, keyword) >= 90:  # Adjust threshold as needed
            return True
    return False
def query(user_input, cursor, conn, email_id):
    # try:
    #     # Check if the query is related to FinKraft AI
    #     if not is_related_to_finkraft(user_input):
    #         return "I'm a chatbot providing information about FinKraft AI. Please ask about FinKraft AI."
    #     # Extract relevant information from finkraft_data
    #     info = extract_information(finkraft_data, user_input)
    #     if info:
    #         # Format the extracted information
    #         bot_response = "\n".join(info)
    #     else:
    #         # Call OpenAI API using appropriate method if info not found in JSON
    #         completion = client.chat.completions.create(
    #             model="gpt-35-turbo",
    #             messages=[
    #                 {"role": "system", "content": "I'm a chatbot providing information about FinKraft AI. Here is the FinKraft AI data."},
    #                 {"role": "user", "content": user_input}
    #             ],
    #             temperature=0.7,
    #             max_tokens=150,
    #             top_p=1.0,
    #             frequency_penalty=0,
    #             presence_penalty=0,
    #             stop=None
    #         )
    #         bot_response = completion.choices[0].message.content
    #     # Update conversation in the MySQL database
    #     update_row(cursor, conn, email_id, user_input, bot_response)
    #     return bot_response
    # except mysql.connector.Error as err:
    #     print(f"Error executing MySQL query: {err}")
    #     return None
        try:
            # Check for casual responses
            if user_input.lower() in ["hi", "hello","hii"]:
                return "Hi there! How can I assist you today?"
            elif user_input.lower() in ["thanks", "thank you"]:
                return "You're welcome!"
            elif user_input.lower() == "okay":
                return "Alright!"

            # Check if the query is related to FinKraft AI
            if not is_related_to_finkraft(user_input):
                return "I'm a chatbot providing information about FinKraft AI. Please ask about FinKraft AI."

            # Extract relevant information from finkraft_data
            info = extract_information(finkraft_data, user_input)

            if info:
                # Format the extracted information
                bot_response = "\n".join(info)
            else:
                # Call OpenAI API using appropriate method if info not found in JSON
                completion = client.chat.completions.create(
                    model="gpt-35-turbo",
                    messages=[
                        {"role": "system", "content": "I'm a chatbot providing information about FinKraft AI. Here is the FinKraft AI data."},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.7,
                    max_tokens=150,
                    top_p=1.0,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop=None
                )
                bot_response = completion.choices[0].message.content

            # Update conversation in the MySQL database
            update_row(cursor, conn, email_id, user_input, bot_response)
            return bot_response

        except mysql.connector.Error as err:
            print(f"Error executing MySQL query: {err}")
            return None
def create_table(cursor):
    table_schema = (
        "CREATE TABLE IF NOT EXISTS CHATGPT ("
        "  email_id VARCHAR(255) PRIMARY KEY,"
        "  user_input TEXT NOT NULL,"
        "  bot_response TEXT NOT NULL"
        ")"
    )
    try:
        cursor.execute(table_schema)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("CHATGPT table already exists.")
        else:
            print(err.msg)
def insert_initial_row(cursor, conn, email_id):
    insert_query = "INSERT INTO CHATGPT (email_id, user_input, bot_response) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (email_id, '', ''))
    conn.commit()
def update_row(cursor, conn, email_id, user_input, bot_response):
    select_query = "SELECT * FROM CHATGPT WHERE email_id = %s"
    cursor.execute(select_query, (email_id,))
    result = cursor.fetchone()
    if result:
        # If user exists, update the existing row
        update_query = (
            "UPDATE CHATGPT "
            "SET user_input = CONCAT(user_input, %s), "
            "    bot_response = CONCAT(bot_response, %s) "
            "WHERE email_id = %s"
        )
        cursor.execute(update_query, (f'\nUser: {user_input}', f'\nBot: {bot_response}', email_id))
    else:
        # If user does not exist, insert a new row
        insert_query = "INSERT INTO CHATGPT (email_id, user_input, bot_response) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (email_id, f'User: {user_input}', f'Bot: {bot_response}'))
    conn.commit()
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data['message']
        email = data['email']
        # Connect to MySQL
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        # Create table if not exists
        create_table(cursor)
        # Query bot response
        bot_response = query(message, cursor, conn, email)
        # Close cursor and connection
        cursor.close()
        conn.close()
        return jsonify({'response': bot_response})
    except Exception as e:
        return jsonify({'error': str(e)})
if __name__ == "__main__":
    app.run(debug=True)