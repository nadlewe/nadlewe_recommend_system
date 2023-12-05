import csv

# 파일 경로 및 필터링 조건 설정
file_path = '/Users/kangdonghee/Desktop/2023-2/SB&Start-up/소비창/cafe_info_v3.csv'
min_price = 100000
max_price = 300000
kinds = ["와인", "칵테일", "방탈출"]
place_result = []

# CSV 파일을 열고 조건에 맞는 행을 찾습니다.
with open(file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        # place_price 열의 값을 정수로 변환합니다.
        # place_price가 비어있거나 숫자가 아닌 경우를 대비하여 예외 처리를 합니다.
        try:
            price = int(row['place_price'])
        except ValueError:
            continue  # 가격 정보가 유효하지 않으면 이 행을 건너뜁니다.

        # 가격이 지정된 범위 내에 있는지 확인합니다.
        if min_price <= price <= max_price:
            # tags 열의 값이 kinds 배열에 있는 태그 중 하나와 일치하는지 확인합니다.
            tags = row['tags'].split(',')
            if any(kind in tags for kind in kinds):
                place_result.append(row)

# 결과 출력
for place in place_result:
    print(place)
