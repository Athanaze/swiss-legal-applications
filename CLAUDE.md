ALWAYS USE THE PYTHON VENV named venv in this folder
take control of the situation with the setup, take initiative.
write what you are doing in a markdown file so that I can reproduce what has been done in another machine.
the data i want to put in the graph is at https://huggingface.co/datasets/liechticonsulting/private_jurisprudence 


and looks like this: see HEAD_OF_DATASET.png

for simplification we can only look at .pdf files (extract the file extension from the url column)

also i want to use the data from liechticonsulting/fedlex_articles and look at fedlex_articles_head.png
to see the head of the dataset. again for simplification we can have only the laws in french in the graph.

for important federal laws they are cited using the abbreviation, not with a RS number so we also need to use the fedlex dataset : liechticonsulting/fedlex
on huggingface (see fedlex.png for the head) for the correspondance RS_number <> Abbreviation

THE GOAL :

INSTALL AND SETUP graphrag : https://microsoft.github.io/graphrag/get_started/

then I want to process the data using a llm i have running locally on lmstudio.
here is an example of how to connect to it using curl:

curl http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mistralai_voxtral-small-24b-2507",
    "messages": [
        {
            "role": "system",
            "content": "Always answer in rhymes. Today is Thursday"
        },
        {
            "role": "user",
            "content": "What day is it today?"
        }
    ],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": false
}'

