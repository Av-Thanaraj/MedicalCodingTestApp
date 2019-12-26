import upload_report
import nltk
from nltk.tokenize import sent_tokenize,  word_tokenize
from nltk.corpus import stopwords


def report_feature_extract():
    arr = []
    medical_data = upload_report.extract_data_from_pdf('E:\\RajTestReport\\RajTestMedicalReport.pdf')
    medical_data_by_sen = sent_tokenize(medical_data)
    for sen in medical_data_by_sen:
        print(word_tokenize(sen))
        for (word, tag) in nltk.pos_tag(word_tokenize(sen)):
            if tag not in ["NN", "JJ"] and word not in set(stopwords.words("english")) and word not in ["."]:
                arr.append(word)
                print(word, tag)


report_feature_extract()
corpus_root = "E:\\Trainning\\Genia4ERtask1.iob2"
reader = read_gmb(corpus_root)
data = list(reader)