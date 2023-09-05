# PBF
PBF(Protocolbuffer Binary Format) 파일은 공간 데이터를 압축하고 직렬화하는 데 사용되는 형식입니다. 

## PBF 파일의 기본적인 구조
int4: length of the BlobHeader message in network byte order
serialized BlobHeader message
serialized Blob message (size is given in the header)