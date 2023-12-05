from flask import Flask, request, jsonify
import mariadb
import json
import random


app = Flask(__name__)

@app.route('/extract_info', methods=['POST'])
def extract_info():
    input_data = request.get_json()
    themes = input_data["themes"]
    min_price = input_data["minPrice"]
    max_price = input_data["maxPrice"]
    kinds = input_data["kinds"]

    results = []
    current_price = 0

    for theme in themes:
        if theme == "식사":
            result = extract_restaurant_info(current_price, kinds)
        elif theme == "카페":
            result = extract_cafe_info(current_price, kinds)
        elif theme == "활동":
            result = extract_activity_info(current_price, kinds)
        else:
            result = {"error": f"Invalid theme: {theme}"}

        
        results.append(result)

    return jsonify(results)


@app.route('/extract_restaurant_info', methods=['POST'])
def extract_restaurant_info():
    # 요청 데이터 받기
    input_data = request.get_json()
    min_price = input_data["minPrice"]
    max_price = input_data["maxPrice"]
    kinds = input_data["kinds"]

    conn = mariadb.connect(
        user="root",
        password="1234",
        host="127.0.0.1",
        port=3306,
        database="study"
    )
    cursor = conn.cursor()

    # 가격대와 종류(tags) 중 하나라도 일치하는 행을 추출하는 SQL 쿼리 실행
    query = f"SELECT * FROM restaurant_info_v3 WHERE (place_price >= {min_price} AND place_price <= {max_price}) OR tags IN ({', '.join(['%s']*len(kinds))})"
    cursor.execute(query, tuple(kinds))
    result = cursor.fetchall()

    conn.close()

    # 결과에서 무작위로 1개의 행 추출
    random_row = random.choice(result)

    # 추출한 행을 JSON 형식으로 변환하여 반환
    extracted_result = {
        'placeName': random_row[0],
        'rate': random_row[3],
        'menu': random_row[5],
        'placePrice': random_row[6],
        'placeImage': random_row[8]
    }

    print(extracted_result)

    return jsonify(extracted_result)

@app.route('/extract_cafe_info', methods=['POST'])
def extract_cafe_info():
    # 요청 데이터 받기
    input_data = request.get_json()
    min_price = input_data["minPrice"]
    max_price = input_data["maxPrice"]
    kinds = input_data["kinds"]

    conn = mariadb.connect(
        user="root",
        password="1234",
        host="127.0.0.1",
        port=3306,
        database="study"
    )
    cursor = conn.cursor()

    # 가격대와 종류(tags) 중 하나라도 일치하는 행을 추출하는 SQL 쿼리 실행
    query = f"SELECT * FROM restaurant_info_v3 WHERE (place_price >= {min_price} AND place_price <= {max_price}) OR tags IN ({', '.join(['%s']*len(kinds))})"
    cursor.execute(query, tuple(kinds))
    result = cursor.fetchall()

    conn.close()

    # 결과에서 무작위로 1개의 행 추출
    random_row = random.choice(result)

    # 추출한 행을 JSON 형식으로 변환하여 반환
    extracted_result = {
        'placeName': random_row[0],
        'rate': random_row[3],
        'menu': random_row[5],
        'placePrice': random_row[6],
        'placeImage': random_row[8]
    }

    print(extracted_result)

    return jsonify(extracted_result)

@app.route('/extract_activity_info', methods=['POST'])
def extract_activity_info():
    # 요청 데이터 받기
    input_data = request.get_json()
    min_price = input_data["minPrice"]
    max_price = input_data["maxPrice"]
    kinds = input_data["kinds"]

    conn = mariadb.connect(
        user="root",
        password="1234",
        host="127.0.0.1",
        port=3306,
        database="study"
    )
    cursor = conn.cursor()

    # 가격대와 종류(tags) 중 하나라도 일치하는 행을 추출하는 SQL 쿼리 실행
    query = f"SELECT * FROM restaurant_info_v3 WHERE (place_price >= {min_price} AND place_price <= {max_price}) OR tags IN ({', '.join(['%s']*len(kinds))})"
    cursor.execute(query, tuple(kinds))
    result = cursor.fetchall()

    conn.close()

    # 결과에서 무작위로 1개의 행 추출
    random_row = random.choice(result)

    # 추출한 행을 JSON 형식으로 변환하여 반환
    extracted_result = {
        'placeName': random_row[0],
        'rate': random_row[3],
        'menu': random_row[5],
        'placePrice': random_row[6],
        'placeImage': random_row[8]
    }

    print(extracted_result)

    return jsonify(extracted_result)

if __name__ == '__main__':
    app.run()