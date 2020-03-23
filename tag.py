import streamlit as st
import syntok.segmenter as segmenter
import nltk
import json

def tokenize(text,lemma_stop = False):
    
    sentenceC = []
    for parg in segmenter.process(text):
        for sentence in parg:
            sentenceC.append(' '.join([token.value for token in sentence ]))
    sub = sentenceC

    return sentenceC



with open("multi.txt", encoding='utf-8') as fd:
    example_news_group =fd.read().split('****')





index = st.selectbox('Examples', range(len(example_news_group)))

news = example_news_group[index].split("++++")

order = []

for new,idx in zip(news,range(len(news))):
    sentences = tokenize(new)
    "==========================================================================================="
    for i,j in zip(range(len(sentences)),sentences):
        "Noticia "+str(idx)+"-# "+ str(i)+" : " +j
        # number = st.sidebar.number_input(value=0,label='Sentence# '+str(i) ,min_value=-1,max_value=len(example_news))
        number = st.sidebar.checkbox("New "+str(idx)+ " Sentence# "+str(i))
        # if number == -1 :
            # continue
        if not number:
            continue
        # order.append((number,j))
        order.append(((idx,i),j))


# st.write(len(sentences))
# st.write(len(order))
order.sort(key= lambda order : order[0] )


if st.button("Save"):
    with open("summary"+str(index)+".json" ,'w',encoding='utf-8') as fd:
        json.dump(order,fd)

# with open("summary "+str(index)+".json",'r',encoding='utf-8') as fd:
#     order = json.load(fd)

# order

