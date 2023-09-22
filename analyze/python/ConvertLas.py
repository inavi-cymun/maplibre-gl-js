import laspy
import numpy as np
import pyproj

folder_path = "C:\\workspace\\analyze_maplibre\\maplibre-gl-js\\analyze\\data\\"
input_las = laspy.read(folder_path+"input.las")


#EPSG:32652
custom_crs = pyproj.CRS.from_proj4("+proj=utm +zone=52 +ellps=WGS84 +datum=WGS84 +units=m +no_defs")

# 원래 좌표계 정의 (예: WGS 84)
wgs84_crs = pyproj.CRS("EPSG:3857")  # 원래 좌표계: WGS 84

custom_crs2 = pyproj.CRS.from_proj4("+proj=aeqd +lat_0=37.4021746 +lon_0=127.1068385 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs")

# 좌표 변환기 생성
transformer = pyproj.Transformer.from_crs(custom_crs, custom_crs2, always_xy=True)


print(input_las.header)
print(input_las.header.point_count)
print(input_las.points.point_size)
print(input_las.header.y_scale)
print(input_las.header.z_scale)
print(input_las.header.creation_date)
print(input_las.points[0].x)
print(input_las.points[0].y)
print(input_las.points[0].z)
print(input_las.intensity.dtype)
print(input_las.points[1].x)
print(input_las.points[1].y)
print(input_las.points[1].z)
point_format = input_las.point_format
print(point_format)
print(list(point_format.dimension_names))

# 좌표 변환 수행
lon, lat = transformer.transform(input_las.points[0].x, input_las.points[0].y)

# 결과 출력
print(f"원래 좌표: ({lon}, {lat})")

#input_las.header.point_count = 3000000
#input_las.points = input_las.points[:3000000]
# Extract x, y, z data from the input LAS file
#x = input_las.x
#y = input_las.y
x, y = transformer.transform(input_las.x, input_las.y)
z = input_las.z
intensity = input_las.intensity

print("포인트 개수:", len(x))



# 3. 추출한 데이터를 배열로 만듭니다.
point_data = np.column_stack((x, y, z, intensity))

# 4. 데이터 형식을 변경합니다.
point_data = point_data.astype({"names": ["x", "y", "z", "intensity"], "formats": ["<f4", "<f4", "<f4", "<u1"]})


# 4. 배열을 바이너리로 저장합니다.
output_file_path = folder_path+"output.bin"
point_data.tofile(output_file_path)

print("Binary file saved:", output_file_path)



# Create the output LAS file
new_point_format = laspy.point.PointFormat(0) 
header = laspy.LasHeader(point_format=new_point_format, version="1.3")
#header.x_scale = 0.0000001
#header.y_scale = 0.0000001



with laspy.open(folder_path+"output_custom.las", mode="w", header=header) as output_las:
    point_record = laspy.ScaleAwarePointRecord.zeros(len(x), header=header)
    point_record.x = x
    point_record.y = y
    point_record.z = z
    point_record.intensity = intensity

    output_las.write_points(point_record)


# 데이터를 NumPy 배열로 복사하고 데이터 형식을 Float64로 변환
x = np.array(x, dtype=np.uint32)
y = np.array(y, dtype=np.uint32)
z = np.array(z, dtype=np.uint32)
intensity = np.array(intensity, dtype=np.uint16)


point_data  = np.stack((x, y, z, intensity), axis=-1)

# 데이터를 이진 파일로 저장
with open(folder_path+"output2.bin", "wb") as output_file:
    point_data.tofile(output_file)