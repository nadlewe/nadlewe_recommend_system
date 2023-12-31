# 1. json 형식으로 파일을 받고
# 2. 제공받은 형식을 가공해서
# 3. 생성된 코스를 추출하는 기능

from reco_restaurant import reco_restaurant
from reco_cafe import reco_cafe
from reco_activity import reco_activity

from flask import Flask, request
import json
import random

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

TAGS_MAPPING = {
    "식사": "restaurant",
    "카페": "cafe",
    "활동": "activity",
}

@app.route('/api_test',methods=['POST'])
def get_json():

    #  1. 데이터를 json 형태로 받아오기
    try:
        data = request.get_json()  # POST로 받은 JSON 데이터 가져오기
        final_result = []
        for i in range(1, 4):
            if data:
                print(json.dumps(data, indent=4, ensure_ascii=False))  # 들여쓰기를 적용하여 JSON 데이터 출력
                
                # 2. json 데이터를 변수에 할당하기
                minPrice = data.get("minPrice", 0)
                maxPrice = data.get("maxPrice", 0)
                themes = data.get("themes", [])
                kinds = data.get("kinds", [])

                result_list= []
                course_price = 0
                # 3. themes의 값을 순서대로 확인하여 kinds값에 일치하는 데이터프레임의 행 출력
                for index, theme in enumerate(themes):                    
                    if theme == "식사":
                        # kinds의 값을 함수의 인자로 넘겨주어 조건에 맞는 행 출력
                        restaurant_info, menu_price, place_img = reco_restaurant(kinds, course_price)
                        result_list.append(restaurant_info)
                        if course_price <= maxPrice:
                            course_price += menu_price
                        else:
                            course_price += 0     
                        print(restaurant_info)
                    elif theme == '카페':
                        cafe_info, cafe_price = reco_cafe(kinds, course_price)
                        result_list.append(cafe_info)
                        if course_price <= maxPrice:
                            course_price += cafe_price
                        else:
                            course_price += 0    
                        print(cafe_info)
                    elif theme == '활동':
                        activity_info = reco_activity(kinds)
                        result_list.append(activity_info)
                        print(activity_info)
                    else:
                        print(f"[{theme}] = 정보를 찾을 수 없음")

                print(json.dumps(result_list, ensure_ascii=False, indent=2))
                
                result_info = {
                    "courseName": f"코스{i}",
                    "places": result_list,
                    "coursePrcice" : course_price,
                    "courseImage": place_img,
                }

                final_result.append(result_info)
            
            else:
                return {'message': 'JSON 데이터를 받지 못했습니다.'}, 400
        return final_result, 200

    except Exception as e:
        return {'message': '오류가 발생했습니다.', 'error': str(e)}, 500
    
    

#run
if __name__ == '__main__':  
    app.run()


