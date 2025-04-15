from dao.fragments import FragmentDAO
from sentence_transformers import SentenceTransformer
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

##model = SentenceTransformer("all-MiniLM-L6-v2")
model = SentenceTransformer("all-mpnet-base-v2")
class ChatOllamaBot:
    def __init__(self):
        self.model = SentenceTransformer("all-mpnet-base-v2")

    def chat(self, question):
        emb = self.model.encode(question)

        dao = FragmentDAO()
        framents = dao.getFragments(str(emb.tolist()))
        context = []
        for f in framents:
            print(f)
            context.append(f[2])

        #print(context[0])

        # Prepare Template
        documents = "\\n".join(c for c in context)
        #print(documents)

        # Define the prompt template for the LLM
        prompt = PromptTemplate(
            template="""You are an assistant for question-answering tasks.
            Use the following documents to answer the question.
            If you don't know the answer, just say that you don't know.
            Use five sentences maximum and keep the answer concise:
            Documents: {documents}
            Question: {question}
            Answer:
            """,
            input_variables=["question", "documents"],
        )

#         prompt = PromptTemplate(
#             template="""Eres un asistente para tareas de preguntas y respuestas de una universidad.
#             Utiliza los siguientes documentos para responder la pregunta. Contesta en castellano y usa
#             texto simple sin formatos.
#             Si no sabes la respuesta, simplemente di que no la sabes.
#             Utiliza cinco oraciones como máximo y mantén la respuesta concisa.
#             Documentos: {documents}
#             Pregunta: {question}
#             Answer:
#             """,
#             input_variables=["question", "documents"],
#         )
# #
        print(prompt)
        print(prompt.format(question=question, documents=documents))
        # exit(1)
        # Initialize the LLM with Llama 3.1 model
        # llm = ChatOllama(
        #     #model="llama3.1",
        #     model="deepseek-r1:70b",
        #     temperature=0,
        #     base_url = "http://136.145.77.77:11434"
        # )

        llm = ChatOllama(
            model="llama3.2",
            #model="phi3.5",
            #model = "gemma3:4b",
            temperature=0,
        )
        # Create a chain combining the prompt template and LLM
        rag_chain = prompt | llm | StrOutputParser()

        # Question

        answer = rag_chain.invoke({"question": question, "documents": documents})
        print(answer)
        return answer