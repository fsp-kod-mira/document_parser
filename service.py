import grpc
from concurrent import futures
import document_pb2
import document_pb2_grpc
import fitz
from docx import Document
from striprtf.striprtf import rtf_to_text
import requests
import docx2txt
from document_parsers import *
import os

grpc_port = '[::]:50051'

class DocumentServicer(document_pb2_grpc.DocumentServicer):
    def ExtractTextFromDocument(self, request, context):
        print(request.file_url)

        text = controller(request.file_url)

        chunk_size = 2048 
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i + chunk_size]
            response = document_pb2.StreamResponse(file_content=chunk.encode())
            yield response   



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    document_pb2_grpc.add_DocumentServicer_to_server(DocumentServicer(), server)
    server.add_insecure_port(grpc_port)
    server.start()
    server.wait_for_termination()



def controller(file_url):
    response = requests.get(file_url)
    file_extension = os.path.splitext(file_url)[-1]

    if response.status_code == 200:
        try:
            os.mkdir("downloads")
        except: 
            pass
        
        temp_filename = "downloads/" + generate_random_name(file_extension)
        with open(temp_filename, 'wb') as f:
            f.write(response.content)

        extracted_text = ""
        if ".pdf" in file_extension:
            extracted_text = extract_text_from_pdf(temp_filename)
        elif ".docx" in file_extension:
            extracted_text = extract_text_from_docx(temp_filename)
        elif ".rtf" in file_extension:
            extracted_text = extract_text_from_rtf(temp_filename)
        elif ".doc" in file_extension:
            extracted_text = extract_text_from_doc(temp_filename)
    os.remove(temp_filename)
    return extracted_text



if __name__ == '__main__':
    print(f"Run server on {grpc_port}")
    serve()
    
