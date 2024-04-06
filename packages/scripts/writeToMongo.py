import fitz  
import requests
from io import BytesIO
from pymongo import MongoClient


pdf_urls = ["https://iapp.org/media/pdf/resource_center/Brazilian_General_Data_Protection_Law.pdf", "https://www.equalrightstrust.org/sites/default/files/ertdocs//Decree-Law No. 5%2C452_Consolidation of Labor Laws.pdf", "https://portaldeimigracao.mj.gov.br/images/resolucoes_normativas/RESOLUÇÃO_CNIG_MJSP_Nº_45_DE_9_DE_SETEMBRO_DE_2021.pdf", "https://www.colombobritanico.edu.co/wp-content/uploads/2021/08/2.5-Internal-Labor-Regulations-CCB-Version-2-Updated-09-03-2021.pdf","https://www.colombobritanico.edu.co/wp-content/uploads/2021/08/2.5-Internal-Labor-Regulations-CCB-Version-2-Updated-09-03-2021.pdf"]
def extract_text_from_pdf_url(pdf_url):
    response = requests.get(pdf_url)
    print('resp', response)
    if response.status_code == 200:
        document = fitz.open(stream=BytesIO(response.content), filetype="pdf")
        text = ""
        for page in document:
            text += page.get_text()
        return text
    else:
        return "Failed to retrieve PDF from the URL."
for url in pdf_urls:
    pdf_text  = extract_text_from_pdf_url(pdf_url)
    connection_uri = "mongodb+srv://MongoDB:MongoDB@cluster0.8zhmall.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(connection_uri)
    db_name = client.Hackathon
    collection_name = db_name.Test
    document = {"br_data": pdf_text}
    collection_name.insert_one(document)
