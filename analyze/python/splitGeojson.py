import json
import os
 
 # 폴더 생성 --------------------------------------------------------------------------
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
 
# Json분할 --------------------------------------------------------------------
 
def splitgeoJson(Jsonfilename):
    #json 파일 읽기
    with open(Jsonfilename, 'r', encoding='UTF8') as rf:
        geojson = json.load(rf)
 
    #저장 폴더 생성    
    path ='C:\\workspace\\analyze_maplibre\\maplibre-gl-js\\analyze\\data\\geoJson'
 
    createFolder(path)

    # 전체 데이터를 100만 개씩 끊어서 분할
    features = geojson['features']
    num_features = len(features)
    chunk_size = 1000000
 
    for i in range(0, num_features, chunk_size):
        chunk = features[i:i + chunk_size]

        # json 파일 저장 경로
        start_idx = i + 1
        fileName = path + f'\\chunk_{start_idx}.json'
        print(fileName)

        # json 객체 생성
        geo = dict()
        geo['type'] = 'FeatureCollection'
        geo['features'] = chunk

        # json 파일 저장
        with open(fileName, 'w', encoding='UTF8') as wf:
            json.dump(geo, wf, ensure_ascii=False)  # 한글 유니코드 저장 방지

#-------------------------------------------------------------------------------

if __name__ == '__main__':

    splitgeoJson('C:\\workspace\\analyze_maplibre\\maplibre-gl-js\\analyze\\data\\output.geojson')

    os.system("pause")
