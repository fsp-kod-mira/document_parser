
import grpc
import document_pb2
import document_pb2_grpc



def receive_chunks(file_url):
    # Устанавливаем соединение с gRPC сервером
    channel = grpc.insecure_channel('localhost:50051')
    stub = document_pb2_grpc.DocumentStub(channel)
    
    
    request = document_pb2.ExtractRequest(file_url=file_url)
    
    responses = stub.ExtractTextFromDocument(request)
    
    for response in responses:
        chunk = response#.file_content#.decode()
        print(chunk)

if __name__ == '__main__':
    file_url = "http://10.244.0.1/cv.docx"  # Замените на URL вашего документа
    receive_chunks(file_url)
