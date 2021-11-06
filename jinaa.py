#from IPython import get_ipython


from jina import Flow, Executor, requests, Document, DocumentArray
import pandas as pd
import numpy as np 
import torch
from numba import jit


from ctypes import *
lib8 = cdll.LoadLibrary('/home/gopinath/miniconda3/pkgs/cudatoolkit-11.3.1-h2bc3f7f_2/lib/libcudart.so.11.0')


model = "sentence-transformers/paraphrase-distilroberta-base-v1"

flow = (
    Flow()
    .add(
        name="text_encoder",
        uses="jinahub://TransformerTorchEncoder",
        uses_with={"pretrained_model_name_or_path": model, 'device':'cuda'},
        
    )
    .add(
        name="text_indexer",
        uses='jinahub://SimpleIndexer',
        #uses_with={'device': 'cuda'},
        
    )
)


query = Document(text = "study of penguins antartica")
with flow:
    response = flow.search(inputs = query,parameters={'limit':20},uses_with ={'device':'cpu'},gpus='all' ,return_results = True)



matches = response[0].docs[0].matches


for i in matches[:20]:
    print(str(i.text))
    print("series :", i.tags['show'])
    print("season :", i.tags['season'])
    print("episode :", i.tags['episode'])
    print("speaker :", i.tags['speaker'])
    
    print("_________________________________________________________________________________________________________________-")
