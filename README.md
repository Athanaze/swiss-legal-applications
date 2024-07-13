# Particularités suisses

En Suisse, certaines assurances sont obligatoires, comme l'assurance maladie de base (LAMal) et l'assurance responsabilité civile pour les véhicules à moteur. D'autres sont fortement recommandées, comme l'assurance ménage et responsabilité civile privée.

Il est également important de noter que le système d'assurance sociale suisse (AVS, AI, APG) offre une couverture de base pour la retraite, l'invalidité et la perte de gain, que les assurances privées peuvent compléter.

Enfin, la Suisse a un système de surveillance des assurances très développé, avec l'Autorité fédérale de surveillance des marchés financiers (FINMA) qui veille à la protection des assurés et à la stabilité du système financier.


# Problèmes juridiques que l'on peut rencontrer en Suisse :

## 1. Droit de la famille

- Divorce et séparation
- Garde des enfants et pension alimentaire
- Adoption et filiation

## 2. Droit du travail

- Licenciement abusif
- Harcèlement au travail
- Conditions de travail et salaires

## 3. Droit pénal

- Vols et cambriolages
- Infractions liées aux drogues
- Violences domestiques

## 4. Droit des contrats

- Litiges commerciaux
- Non-respect des contrats de vente
- Problèmes de location immobilière

## 5. Droit des étrangers

- Permis de séjour et de travail
- Demandes d'asile
- Expulsions

## 6. Droit de la consommation

- Litiges liés à la consommation de biens et services
- Publicité mensongère
- Garantie des produits

## 7. Droit administratif

- Contestations de décisions administratives
- Problèmes liés à l'urbanisme et à la construction
- Questions fiscales

## 8. Droit de la propriété intellectuelle

- Violations de droits d'auteur
- Litiges de brevets et marques

---


# Notes

For vision tasks (e.g. using claude 3 haiku) it is **crucial** to orient the photos of documents correctly, otherwise the model starts to make stuff up, even at temp=0

# Multilangual embedding model

https://deepinfra.com/BAAI/bge-m3?version=babcf60cae0a1f438d7ade582983d4ba462303c2

"
BAAI/bge-m3
BGE-M3 is a versatile text embedding model that supports multi-functionality, multi-linguality, and multi-granularity, allowing it to perform dense retrieval, multi-vector retrieval, and sparse retrieval in over 100 languages and with input sizes up to 8192 tokens. The model can be used in a retrieval pipeline with hybrid retrieval and re-ranking to achieve higher accuracy and stronger generalization capabilities. BGE-M3 has shown state-of-the-art performance on several benchmarks, including MKQA, MLDR, and NarritiveQA, and can be used as a drop-in replacement for other embedding models like DPR and BGE-v1.5"

Run locally:

```python


from FlagEmbedding import BGEM3FlagModel

model = BGEM3FlagModel('BAAI/bge-m3')

embeddings=[model.encode(content)['dense_vecs'].tolist()]



```

# swiss-legal-applications

Useful resources regarding legal applications.

https://github.com/HazyResearch/legalbench/

https://aclanthology.org/2021.nllp-1.3.pdf

https://arxiv.org/pdf/2309.12269v4


https://elsevier-ssrn-document-store-prod.s3.amazonaws.com/23/03/18/ssrn_id4392741_code627779.pdf?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJIMEYCIQDXpwTjpl7pBk9i7jQV%2FdC3u0rTwZWMiz4x4FoYbrB8VgIhAN7X7ct02wFXUSWLiUjF51pOptlOsW49JhEfeTOko7jxKscFCNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBBoMMzA4NDc1MzAxMjU3IgwwZ5%2BrFY%2FwMQiR%2FLwqmwVOsKquiexldCKenyp%2BP4v6OyFpxaWPttZkbu0acL6ZIvFEHTHOiCTirEWIBZl1IMvRaOMxeV6MsHATT1QR9ttDf1GvBYlOh44yRqhGPipIoo8sGboVxxnmtbaYegU0XRFV2FNSphmZ7AU32Lgy526wdYQjPEEPdjHLdjRk9EEc324yFxsEo4OyBq2JenT2DNLksGA3xPhvi2fv3wWELpLxBM8lxOUhq1hQO0fprZlCpaGMeyYqPdpQjMQpjyPpvF2%2BVEbnXGO4vj7AzNh%2FMAPv4JpveZV3dzMo5i7%2BTVZ7AwdPLOrSz7Jq7gJX%2FV0sK8jL4lLcn%2FYJ1kseSas6w%2BDYkjii8S8FooNqE1m4kkvFpvX%2FKpT6KC6xExmnLP7wlX3kVZLalqLLaLgtlO3ZqujjtIqvfuQNmolAqtZjTtxfoKUJRTMvPPTO5fkby%2BWWclnvcaHhCfE%2FKBue6XGCfAzUZfwypIQoXRltwosGjP91BO%2F%2F9OgqKlYjM1bteN%2Bc%2Fv5Ntj%2ByrYgS4JO3qA3j3cpfpScCiYgq80crNRGESwG2ZzhbUqbcmEF%2B0s6bVP8paZ4pkyfIN3VdufS4dMGnDMmszqy5Wm8X55wQs7jcQ8ZOrkhZsMZq0IOmGLjFwjx1sQ%2Fev99swyOPX00%2FkMDym1D0bAScoSOMMAovC8954DVT4k5FhmBqln33cr7RmHy0ztCnmsTMtZFlbkHnaGcR6LCXX01LDEEnumAvVmaPB1QrP%2FzzH%2BqybVibUd%2Bn798JvhAYLieg827NAWhkQvbBRrIfTtZfthVeZindLRKCI0xKFD5QnDk%2F0MUCJHulOQDTcNWzXWD%2FkNsXpB%2ByzQgQrj%2FAmMQPYiZzua6sNgvTEuWpazK0g9MKyiMvpX2CMNTI8bMGOrABwtO0H1bZpD5fZn3toAcZkkC4qAzF5CRcxbY%2FJkhnzyeU9Bf28tdAfbVz2zHiNq0ubHm91fsn00O%2Br1iRHHRZsDeDAK44xSVEkrUO2z84%2Fzg63bBVBR59C7pXfKGaHYdnx9owwYIjH0UYEhPEHRsoUlMYaJrUtKCuK0tho3XlM9B8%2FTlON4EGs9vEomo8hpS1OkcbBA6KTI6ZRpCSR79Iotbo1U3FtluKhy22XN2s4xE%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240626T195321Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAUPUUPRWEXRIMIMVJ%2F20240626%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=efe29b6ebbfffb79e75c8e6fc341d17b806865d8c099fdac060380d7d55bcb2a

## laws.json

Contains all the federal laws. fileUrl.value contains the link for the xml version of each law.
The uuid has been generated by us, just to give a unique identifier to each of them. It has no connection with other identification methods.

## Websites

[bger.ch](https://www.bger.ch/)

- Build queries and call via CURL

  https://fedlex.data.admin.ch/en-CH/sparql

- Nice structure with unique, ascending number (just leave the /2024 at the end no matter what). The earliest we got working is 30000

  https://droitpourlapratique.ch/decision/90584/2024
  
  All the content is within ```<div id="print_main">```

  https://droitpourlapratique.ch/decision/90584/2024
  
---
## AI tools

### Langchain script

Extract the xml articles (also referenced as "article"  from a legal point of view) from a local xml file and embeds them in a chroma database.


/!\ Splits the articles that are too big in the middle, with no precautions /!\

Requires the user to press enter to launch the embedding (in vscode this opens up a pop up on top)

```python

import xml.etree.ElementTree as ET
import tiktoken
import random
import matplotlib.pyplot as plt
import os
import getpass
from langchain_core.documents.base import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

os.environ['OPENAI_API_KEY'] = "<key here or just a environment variable>"

def chroma_db_from_xml_file(xml_file, chroma_dir_name, metadata, add_to_existing=False):
    MAX_T = 8192

    def extract_articles():
        tree = ET.parse(xml_file)
        root = tree.getroot()
        articles = []
        
        def find_articles(element):
            if "article" in element.tag:
                articles.append(ET.tostring(element, encoding='unicode'))
            for child in element:
                find_articles(child)
        
        find_articles(root)
        return articles


    def split_if_necessary(string_arr):
        enc = tiktoken.get_encoding("cl100k_base")
        new_string_arr = []
        for e in string_arr:
            if len(enc.encode(e)) > MAX_T:
                mid = len(e) // 2
                a, b = e[:mid], e[mid:]
                new_string_arr.append(a)
                new_string_arr.append(b)
            else:
                new_string_arr.append(e)
        print(len(string_arr), len(new_string_arr))
        
        rerun_algo = False
        for s in new_string_arr:
            if len(enc.encode(e)) > MAX_T:
                rerun_algo = True
        
        if rerun_algo:
            return split_if_necessary(new_string_arr)
        
        return new_string_arr

    def get_token_counts(string_array):
        token_counts = []
        enc = tiktoken.get_encoding("cl100k_base")
        for string in string_array:
            t = len(enc.encode(string))
            if t > MAX_T:
                print(t)
            token_counts.append(t)

        return token_counts
    def display_token_count_chart(string_array):
        token_counts = get_token_counts(string_array)

        plt.figure(figsize=(10, 30))
        plt.bar(range(len(string_array)), token_counts)
        plt.xlabel('String Index')
        plt.ylabel('Token Count')
        plt.title('Token Count Distribution')
        
        # Add a horizontal red line at 8192
        plt.axhline(y=MAX_T, color='red', linestyle='-', linewidth=1)
        
        plt.show()

    articles = extract_articles()
    s_a = split_if_necessary(articles)
    display_token_count_chart(s_a)
    COST_PER_1M_TOKEN = 0.13
    n_tokens = sum(get_token_counts(s_a))
    input(f"N TOKENS {n_tokens}\nPRICE USD {COST_PER_1M_TOKEN*(n_tokens/1000000)}")
    
    documents = []
    for l in s_a:
        doc = Document(page_content = l)
        doc.metadata=metadata
        documents.append(doc)

    if(add_to_existing):
        db = Chroma(embedding_function=OpenAIEmbeddings(), persist_directory=chroma_dir_name)
        db.add_documents(documents)
        return db
    
    return Chroma.from_documents(documents, OpenAIEmbeddings(), persist_directory=chroma_dir_name)
```

Somehow hard to find via google, so here it is:
[Document class documentation](https://api.python.langchain.com/en/latest/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document)


---



---

### Created and maintained by [Liechti Consulting](https://liechticonsulting.com) &nbsp; :switzerland:

Need AI-powered solutions? sacha@liechticonsulting.com :rocket:

---
