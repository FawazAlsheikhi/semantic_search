# -*- coding: utf-8 -*-
"""Task22.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yBvg6i_GsMk--P2nuSG-mfqCDbuIcEpx

# Task 2
- Raghad Al-Rasheed
- Fawwaz Alsheikhi

using the E5 model as the embedding model and translated dataset from huggingface
"""


"""## Downloading the Embedding model"""

from sentence_transformers import SentenceTransformer
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import math
from scipy import spatial


model = SentenceTransformer("intfloat/multilingual-e5-large")

"""## Downloading Translated data from english to arabic"""

from datasets import load_dataset


ds = load_dataset("Helsinki-NLP/news_commentary", "ar-en",split="train")

import pandas as pd

df = pd.DataFrame(ds['translation'])

df['ar']

df['ar'][0]

"""### Extracting the first 10000 rows out of the data"""

df=df.head(10000)

df['ar'].shape

documents =[doc for doc in df['ar']]

documents[9999]

"""## Embedding the sentences by rows"""

embeddings = model.encode(documents)

from sentence_transformers import SentenceTransformer
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import math
from scipy import spatial
import scipy

def semantic_search(query, embeddings, documents):
    query_embedding = model.encode(query)

    document_embeddings = embeddings
    scores = [scipy.spatial.distance.cosine(query_embedding, doc) for doc in document_embeddings]
    ls1 = list()
    for i, score in enumerate(scores):
        ls1.append([documents[i],score])

    print(scores.index(min(scores)))
    most_similar_doc = documents[scores.index(min(scores))]
    print("Most similar document", most_similar_doc)
    return ls1

output = semantic_search("ـ لم يكن من السهل قط أن ينخرط المرء في محادثة عقلانية حول قيمة الذهب.",embeddings, documents)

documents[999]

"""### Extracting top three related sentences"""

ranked = sorted(output, key=lambda x: x[1])
ranked[:3]

df

"""## using english with arabic to see the semantic search of multilangual model"""

df['ar']

df['en']

df_ar = df['ar'].tolist()[:5000]

df_en = df['en'].tolist()[:5000]

combined_list = df_ar + df_en

print(len(combined_list))

embeddings1 = model.encode(combined_list)

def semantic_search(query):
    query_embedding = model.encode(query)

    document_embeddings = embeddings1
    scores = [scipy.spatial.distance.cosine(query_embedding, doc) for doc in document_embeddings]
    ls1 = list()
    for i, score in enumerate(scores):
        ls1.append([combined_list[i],score])

    print(scores.index(min(scores)))
    most_similar_doc = combined_list[scores.index(min(scores))]
    print("Most similar document", most_similar_doc)
    ranked = sorted(ls1, key=lambda x: x[1])
    return ranked[0], ranked[1], ranked[2]

output = semantic_search("لذهب بعشرة آلاف دولار؟")


import gradio as gr

demo = gr.Interface(fn=semantic_search,inputs = ["text"], outputs=["text", "text", "text"])
if __name__ == "__main__":
    demo.launch()
