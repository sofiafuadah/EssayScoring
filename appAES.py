import streamlit as st
import pandas as pd
import numpy as np
import json
import nltk
import re
import string
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

st.title('Penilaian Jawaban Esai Biologi')

#jawaban_siswa_df2 = pd.read_excel('data_Biologi.xlsx', sheet_name='jawaban') 
kunci_jawaban_df2 = pd.read_excel('kunciJawaban.xlsx')
#kunci_jawaban_df3 = pd.read_excel('data_Biologi.xlsx', sheet_name='soal')

Nama = st.text_input("Nama")
noAbsen = st.text_input("No. Absen")

list_jawaban=[]

st.markdown("Soal No. 1")
soal1 = st.markdown("Jelaskan bagaimana hewan planaria dapat menunjukkan suatu perairan tercemar atau tidak!")
jawaban1 = st.text_input("Masukkan Jawaban Anda:",key="jawaban1")
st.markdown("Soal No. 2")
soal2 = st.markdown("Jelaskan fungsi organel sel Vakuola!")
jawaban2 = st.text_input("Masukkan Jawaban Anda:", key="jawaban2")
st.markdown("Soal No. 3")
soal3 = st.markdown("Jelaskan fungsi organel sel Mitokondria!")
jawaban3 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban3")
st.markdown("Soal No. 4")
soal4 = st.markdown("Jelaskan fungsi organel sel Lisosom!")
jawaban4 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban4")
st.markdown("Soal No. 5")
soal5 = st.markdown("Jelaskan fungsi organel sel Nukleus!")
jawaban5 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban5")
st.markdown("Soal No. 6")
soal6 = st.markdown("Jelaskan fungsi Hemoglobin!")
jawaban6 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban6")
st.markdown("Soal No. 7")
soal7 = st.markdown("Jelaskan maksud istilah Depresi dan Elevasi!")
jawaban7 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban7")
st.markdown("Soal No. 8")
soal8 = st.markdown("Jelaskan maksud istilah Supinasi dan Pronasi!")
jawaban8 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban8")
st.markdown("Soal No. 9")
soal9 = st.markdown("Bagaimana proses inseminasi buatan dilakukan?")
jawaban9 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban9")
st.markdown("Soal No. 10")
soal10 = st.markdown("Mengapa penyerbukan bastar jarang terjadi secara alami?")
jawaban10 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban10")
st.markdown("Soal No. 11")
soal11 = st.markdown("Jelaskan faktor luar yang mempengaruhi pertumbuhan!")
jawaban11 = st.text_input("Masukkan Jawaban Anda:",key="jawaban11")
st.markdown("Soal No. 12")
soal12 = st.markdown("Jelaskan faktor-faktor yang mempengaruhi kerja enzim!")
jawaban12 = st.text_input("Masukkan Jawaban Anda:", key="jawaban12")
st.markdown("Soal No. 13")
soal13 = st.markdown("Jika perempuan bergolongan darah RH- mengandung RH+, janin pertama dapat bertahan hidup namun pada kehamilan kedua #janin RH+ mengalami eristoblatosis fetalis. Mengapa demikian? Jelaskan!")
jawaban13 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban13")
st.markdown("Soal No. 14")
soal14 = st.markdown("Sebutkan faktor-faktor yang mempengaruhi kelangsungan hidup suatu makhluk hidup?")
jawaban14 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban14")
st.markdown("Soal No. 15")
soal15 = st.markdown("Selain dikenal sebagai organ pernapasan, jelaskan mengapa paru-paru disebut juga sebagai organ ekskresi!")
jawaban15 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban15")
st.markdown("Soal No. 16")
soal16 = st.markdown("Jelaskan maksud dari bioteknologi!")
jawaban16 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban16")
st.markdown("Soal No. 17")
soal17 = st.markdown("Bagaimanakah bioteknologi mengatasi masalah penipisan persediaan bahan bakan minyak?")
jawaban17 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban17")
st.markdown("Soal No. 18")
soal18 = st.markdown("Bagaimana ciri-ciri biji yang persebarannya dibantu oleh angin?")
jawaban18 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban18")
st.markdown("Soal No. 19")
soal19 = st.markdown("Mengapa kultur jaringan menggunakan bagian tumbuhan yang masih muda?")
jawaban19 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban19")
st.markdown("Soal No. 20")
soal20 = st.markdown("Jelaskan mengapa pada bagian tanaman yang dicangkok dapat muncul akar!")
jawaban20 = st.text_input("Masukkan Jawaban Anda: ",key="jawaban20")

list_jawaban.append(jawaban1)
list_jawaban.append(jawaban2)
list_jawaban.append(jawaban3)
list_jawaban.append(jawaban4)
list_jawaban.append(jawaban5)
list_jawaban.append(jawaban6)
list_jawaban.append(jawaban7)
list_jawaban.append(jawaban8)
list_jawaban.append(jawaban9)
list_jawaban.append(jawaban10)
list_jawaban.append(jawaban11)
list_jawaban.append(jawaban12)
list_jawaban.append(jawaban13)
list_jawaban.append(jawaban14)
list_jawaban.append(jawaban15)
list_jawaban.append(jawaban16)
list_jawaban.append(jawaban17)
list_jawaban.append(jawaban18)
list_jawaban.append(jawaban19)
list_jawaban.append(jawaban20)



kunci_jawaban_df2['jawabanSiswa']=list_jawaban


if st.button('Submit'):
    def preprocess(text):
        if not isinstance(text, str): #memastikan bahwa input yang diberikan berupa string
            return ''
    
        #case folding
        text = text.lower() #mengubah ke bentuk huruf kecil
        text = text.translate(str.maketrans('', '', string.punctuation)) #menghapus tanda baca
        text = re.sub(r'\d+', '', text) #menghapus angka

        #tokenization
        tokens = word_tokenize(text)

        #stopword removal 
        stopword_remover = StopWordRemoverFactory().get_stop_words()
        tokens = [word for word in tokens if word not in stopword_remover]

        #stemming
        stemmer = StemmerFactory().create_stemmer()
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        return ' '.join(stemmed_tokens)

 
    kunci_jawaban_df2['PreJawabanSiswa'] = kunci_jawaban_df2['jawabanSiswa'].apply(preprocess)
    kunci_jawaban_df2['prePro'] = kunci_jawaban_df2['kunci jawaban'].apply(preprocess)
        
    def load(filename):
        with open(filename) as data_file:
            data = json.load(data_file)
        return data

    mydict = load('dictIPA.json')

    def get_synonyms(word):
        if word in mydict.keys():
            return mydict[word]['sinonim']
        else:
            return []

    def query_expansion(kunci_jawaban, jawaban_siswa):
        expanded_kunci_jawaban = []
        kunci_jawaban = nltk.word_tokenize(kunci_jawaban)
        jawaban_siswa = nltk.word_tokenize(jawaban_siswa)
        for kunci in kunci_jawaban:
            sinonim = get_synonyms(kunci)
            found = False
            for sin in sinonim:
                if sin in jawaban_siswa:
                    expanded_kunci_jawaban.append(sin)       
                    found = True
                    break
            if not found:
                expanded_kunci_jawaban.append(kunci)
        return expanded_kunci_jawaban   
    
    kunci_jawaban_qe2 = kunci_jawaban_df2['prePro']
    jawaban_siswa_qe2 = kunci_jawaban_df2['PreJawabanSiswa']
    i=0
    expanded_list=[]
    n=len(jawaban_siswa_qe2)
    for i in range(0,n,1):
        expended =' '.join(query_expansion(kunci_jawaban_qe2[i], jawaban_siswa_qe2[i]))
        expanded_list.append(expended)
    kunci_jawaban_df2['expanded']=expanded_list
    def tfidf(corpus):
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(corpus)
        return X

    tfidf_matrix_kunci = tfidf(kunci_jawaban_df2['expanded'])
    tfidf_matrix_siswa = tfidf(kunci_jawaban_df2['PreJawabanSiswa'])
    #menghitung nilai similarity
    def dice_similarity(str1, str2):
        # tokenization
        str1_tokens = set(word_tokenize(str1))
        str2_tokens = set(word_tokenize(str2))

        # similarity calculation
        intersection = len(str1_tokens.intersection(str2_tokens))
        dice_sim = 2 * intersection / (len(str1_tokens) + len(str2_tokens))

        return dice_sim  
    similarity_scores = []
    for i, jawaban_siswa in enumerate(kunci_jawaban_df2['PreJawabanSiswa']):
        dice_scores = []
        for j, kunci_jawaban in enumerate(kunci_jawaban_df2['expanded']):
            dice_scores.append(dice_similarity(jawaban_siswa, kunci_jawaban))
        similarity_scores.append(max(dice_scores))

    kunci_jawaban_df2['similarity_score'] = pd.DataFrame(similarity_scores)
    data_similarity=kunci_jawaban_df2['similarity_score']
    j=0
    n=len(kunci_jawaban_df2)
    tempData=0
    for i in range (n):
        tempData+=data_similarity[i]
    score=tempData/n
    def calculate_numeric_grade(x):
        if x >= 0 and x <= 0.05:
          return 5
        elif x >= 0.05 and x <= 0.1:
          return 10
        elif x >= 0.1 and x <= 0.15:
          return 15
        elif x >= 0.15 and x <= 0.2:
          return 20
        elif x >= 0.2 and x <= 0.25:
          return 25
          return 30
        elif x >= 0.3 and x <= 0.35:
          return 35
        elif x >= 0.35 and x <= 0.4:
          return 40
        elif x >= 0.4 and x <= 0.45:
          return 45
        elif x >= 0.45 and x <= 0.5:
          return 50
        elif x >= 0.5 and x <= 0.55:
          return 55
        elif x >= 0.55 and x <= 0.6:
          return 60
        elif x >= 0.6 and x <= 0.65:
          return 65
        elif x >= 0.65 and x <= 0.7:
          return 70
        elif x >= 0.7 and x <= 0.75:
          return 75
        elif x >= 0.75 and x <= 0.8:
          return 80
        elif x >= 0.8 and x <= 0.85:
          return 85
        elif x >= 0.85 and x <= 0.9:
          return 90
        elif x >= 0.9 and x <= 0.95:
          return 95
        elif x >= 0.95 and x <= 1:
          return 100
    hasil=calculate_numeric_grade(score)
    st.write("Nama = ",Nama)
    st.write("No.Absen = ",noAbsen)
    st.write("Score = ",hasil)