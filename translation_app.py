import ollama



prompt = """ 
        You are system that translate text from one language to another

        {user_query}

        Generate respone in below format
        Answer format :
        Translated text : "XXXXXXX"

        """

query = "translate this text in Hindi language. I am writing the code"


prompt = prompt.replace("user_query", query )
response = ollama.chat(

    model = "lama3.1",
    messages= [prompt = prompt ]
)


print(response["message"])
