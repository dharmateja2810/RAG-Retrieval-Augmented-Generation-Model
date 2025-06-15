# RAG MODEL (Retrieval-Augmented Generation )  
Large Language Models are are trained on vast amount of data , but the issue with LLM is they cannot provide correct results with new info and information in 
specific context. To solve this issue RAG models are used , a rag  model is trained on specific data to get more accurate results

This implementatoion  uses Google's Gemini model to train the RAG model  
the data is converted into chromadb  

## Documentation
Check out the [Documentation](https://drive.google.com/file/d/18uzzuKolIkDei0wcgLO_0pkPn8SfnSSc/view?usp=sharing) for further details.

## Installation  
   1. Clone the repo:  
      git clone https://github.com/dharmateja2810/RAG.git  
      cd RAG  
   2.Set up a virtual environment  
      python3 -m venv env  
      source env/bin/activate  On Windows use `env\Scripts\activate`  
   3.Install dependencies:  
     pip install -r requirements.txt  
   in model.py os.environ["GEMINI_API_KEY"]= "your_api_key_here" replace with  the API key  
   4.Run the project:  
     python app.py  

## usage   
   replace test.pdf with your pdf file   
  
## Contributing  
   Contributions are welcome! Please fork the repository and submit a pull request for review.  

   Fork the repository  
   Create a new branch (git checkout -b feature-branch)  
   Commit your changes (git commit -m 'Add new feature')  
   Push to the branch (git push origin feature-branch)  
   Create a new Pull Request  

## Contact  
   Dharma Teja - dharmanarisetty@gmail.com  
