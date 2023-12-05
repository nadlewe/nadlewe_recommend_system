import json
import random
import csv


def extract_place_info():
    # 요청 데이터 받기
    #input_data = request.get_json()
    min_price = 100000
    max_price = 300000
    kinds = ["와인","칵테일","방탈출"]
    place_result = []

    for kind in kinds:
        if kind == "한식" or kind == "중식" or kind == "일식" or kind == "양식" or kind == "분식" or kind == "기타":
            with open('./restaurant_info_v3.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                next(reader)  # 헤더를 건너뛰기 위해 next() 함수를 사용합니다.
                res_result = []
                for row in reader:
                    if kind == row["tags"].split(','):
                        res_result.append(row)
            # 결과에서 무작위로 1개의 행 추출
            random_row = res_result[random.randrange(len(res_result))]
            # 추출한 행을 JSON 형식으로 변환하여 반환
            extracted_result = {
                'placeName': random_row['name'],
                'rate': random_row['rate'],
                'menu': random_row['representative_menu'],
                'placePrice': random_row['place_price'],
                'placeImage': random_row['img_URL']
            }
            place_result.append(extracted_result)

        elif kind == "카페" or kind == "맥주/소주" or kind == "막걸리" or kind == "와인" or kind=="위스키" or kind=="칵테일":
            with open('./cafe_info_v3.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                next(reader)  # 헤더를 건너뛰기 위해 next() 함수를 사용합니다.
                cafe_result = []
                for row in reader:
                    if kind == row["tags"].split(','):
                        cafe_result.append(row)
            # 결과에서 무작위로 1개의 행 추출
            random_row = cafe_result[random.randrange(len(cafe_result))]
            # 추출한 행을 JSON 형식으로 변환하여 반환
            extracted_result = {
                'placeName': random_row['name'],
                'rate': random_row['rate'],
                'menu': random_row['representative_menu'],
                'placePrice': random_row['place_price'],
                'placeImage': random_row['img_URL']
            }
            place_result.append(extracted_result)

        elif kind == "게임/오락" or kind == "힐링" or kind == "방탈출" or kind == "클래스" or kind == "영화" or kind == "전시" or kind == "책방":
            with open('./activity_info_v4.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                next(reader)  # 헤더를 건너뛰기 위해 next() 함수를 사용합니다.
                act_result = []
                for row in reader:
                    if kind == row["tags"].split(','):
                        act_result.append(row)
                        print("matching")
            # 결과에서 무작위로 1개의 행 추출
            random_row = act_result[random.randrange(len(act_result))]
            # 추출한 행을 JSON 형식으로 변환하여 반환
            extracted_result = {
                'placeName': random_row['name'],
                'rate': random_row['rate'],
                'placeImage': random_row['img_URL']
            }
            place_result.append(extracted_result)
    print(extracted_result)

    return extracted_result

if __name__ == '__main__':
    extract_place_info()
