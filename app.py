from flask import Flask, request, jsonify
import mariadb
import json
import random
import csv

app = Flask(__name__)

@app.route('/extract_place_info', methods=['POST'])
def extract_place_info():
    # 요청 데이터 받기
    input_data = request.get_json()
    min_price = input_data["minPrice"]
    max_price = input_data["maxPrice"]
    kinds = input_data["kinds"]
    place_result = []

    for kind in kinds:
        if kind == "한식" | kind == "중식" | kind == "일식" | kind == "양식" | kind == "분식" | kind == "기타":
            with open('./restaurant_info_v3.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                res_result = []
                for row in reader:
                    if kind == row[2]:
                        res_result.append(row)
            # 결과에서 무작위로 1개의 행 추출
            random_row = random.choice(res_result)
            # 추출한 행을 JSON 형식으로 변환하여 반환
            extracted_result = {
                'placeName': random_row[0],
                'rate': random_row[3],
                'menu': random_row[5],
                'placePrice': random_row[6],
                'placeImage': random_row[8]
            }
            place_result.append(extracted_result)

        elif kind == "카페" | kind == "맥주/소주" | kind == "막걸리" | kind == "와인" | kind=="위스키" | kind=="칵테일":
            with open('./cafe_info_v3.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cafe_result = []
                for row in reader:
                    if kind == row[2]:
                        cafe_result.append(row)
            # 결과에서 무작위로 1개의 행 추출
            random_row = random.choice(cafe_result)
            # 추출한 행을 JSON 형식으로 변환하여 반환
            extracted_result = {
                'placeName': random_row[0],
                'rate': random_row[3],
                'menu': random_row[5],
                'placePrice': random_row[6],
                'placeImage': random_row[8]
            }
            place_result.append(extracted_result)

        elif kind == "게임/오락" | kind == "힐링" | kind == "방탈출" | kind == "클래스" | kind == "영화" | kind == "전시" | kind == "책방":
            with open('./activity_info_v4.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                act_result = []
                for row in reader:
                    if kind == row[2]:
                        act_result.append(row)
            # 결과에서 무작위로 1개의 행 추출
            random_row = random.choice(act_result)
            # 추출한 행을 JSON 형식으로 변환하여 반환
            extracted_result = {
                'placeName': random_row[0],
                'rate': random_row[3],
                'menu': random_row[5],
                'placePrice': random_row[6],
                'placeImage': random_row[8]
            }
            place_result.append(extracted_result)
    print(extracted_result)

    return jsonify(extracted_result)

if __name__ == '__main__':
    app.run()