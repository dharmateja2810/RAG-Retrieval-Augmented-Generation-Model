from flask import Flask, render_template, request, jsonify
from model import load_pdf, split_text, create_chroma_db, load_chroma_collection, generate_answer
import chromadb
import os
app = Flask(__name__)

def start():
    dir  = os.getcwd()
    file_path = dir+"\\test.pdf"
    db_path = dir+"\\database"
    db_name = "source"
    
    pdf_text = load_pdf(file_path=file_path)
    chunked_text = split_text(text=pdf_text)

    chroma_client = chromadb.PersistentClient(path=db_path)

    # Check if collection exists
    existing_collections = chroma_client.list_collections()
    collection_names = [col.name for col in existing_collections]

    if db_name not in collection_names:
        create_chroma_db(documents=chunked_text, path=db_path, name=db_name)
    
    database = load_chroma_collection(path=db_path, name=db_name)
    
    return database

database = start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    prompt = data['prompt']
    response =  generate_answer(database,prompt)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
