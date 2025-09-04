from pypdf import PdfReader
from os import listdir
from langchain_text_splitters import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
#from dao.docs import DocDAO
#from dao.fragments import FragmentDAO
from sentence_transformers import SentenceTransformer

#model = SentenceTransformer("all-MiniLM-L6-v2")
model = SentenceTransformer("all-mpnet-base-v2")


files = listdir("../files")
print(files)

target = files[0]

fname = "../files/" + target
reader = PdfReader(fname)
pdf_texts = [p.extract_text().strip() for p in reader.pages]

# Filter the empty strings
pdf_texts = [text for text in pdf_texts if text]

print("Frist page pf Document*************************")
print(pdf_texts[0])
print("END Document *****************************\n\n")

#exit(0)
# split
character_splitter = RecursiveCharacterTextSplitter(
    # separators=["\n\n", "\n", ". ", " ", ""],
    separators=["\n", ". ", " ", ""],
    chunk_size=300,
    chunk_overlap=25,
    length_function=len,
    is_separator_regex=False
)
# character_split_texts = character_splitter.split_text('\n\n'.join(pdf_texts))
character_split_texts = character_splitter.split_text(''.join(pdf_texts))

print("\nCharacter Splits")
print("total splits: ", len(character_split_texts))
print("Data: ")
print(character_split_texts)
#
print("\n *****Detailed Splits")
for index, split in enumerate(character_split_texts):
    print(index, ' ', split)
print("\n *****End Detailed Splits")
exit(1)

print("Character Splits")

print("See SPLIT 10 *************")
print(character_split_texts[10])
print()
print("END SPLIT 10 *************\n\n")
print(f"\nTotal chunks: {len(character_split_texts)}")

print("DEBUG - see All Splits*************")
[print(t) for t in character_split_texts]
print()
print("DEBUG End All Splits*************")

# Token
token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=50, tokens_per_chunk=300)

token_split_texts = []
for text in character_split_texts:
    token_split_texts += token_splitter.split_text(text)

print("All Token Split *************")
# [print(t) for t in token_split_texts]
i = 0
for t in token_split_texts:
    print(i, " ", t)
    i = i + 1
print("End AllToken Split *************\n\n")
print(f"\nTotal Splitted chunks: {len(token_split_texts)}\n\n")
# exit(1)

