from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

llm = OllamaLLM(model="llama3.2")

prompt = PromptTemplate(
    input_variables=["text"],
    template="""
        Extract 3 important keywords from this:
        {text}
    """
)

#text = """To the best of our knowledge, however, the Transformer is the ﬁrst transduction model relying
#entirely on self-attention to compute representations of its input and output without using sequence-
#aligned RNNs or convolution. In the following sections, we will describe the Transformer, motivate
#"""
text = input("Data: ")
response = llm.invoke(prompt.format(text=text))
print("Text: ", text)
print("Keywords: ", response)
