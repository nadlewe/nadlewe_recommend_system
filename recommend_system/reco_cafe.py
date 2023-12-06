# cafe에 해당하는 장소를 추천하는 기능


import pandas as pd
import re
import json
import random

# CSV 파일 경로 설정
file_path = 'recommend_system/Data_v2/cafe_info.csv'

# CSV 파일 읽기
try:
    df = pd.read_csv(file_path)
    # 데이터프레임 출력
    print(df)
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path}")
except Exception as e:
    print(f"오류 발생: {e}")

def reco_cafe(kinds, price):
    pattern = re.compile(fr'\b(?:{"|".join(kinds)})\b', flags=re.IGNORECASE)
    matching_rows = df[df['tags'].apply(lambda x: bool(pattern.search(x)) if pd.notna(x) else False)]
 
    if not matching_rows.empty:
        result_list = []
        for index, row in matching_rows.iterrows():
            cafe_info = {
                "Place Name": row['name'],
                "Rate": row['rate'],
                "Menu": row['representative_menu'],
                "Place Price": row['place_price'],
                "Place Image": row['image_URL']
            }
            result_list.append(cafe_info)
        # print("추천하는 카페 정보:")
        # print(json.dumps(result_list[3], ensure_ascii=False, indent=2))
        val = len(result_list)
        ran = random.randint(1, val)
        result = result_list[ran]
        if result["Place Price"] == -1:
            price += 0
        else:
            price += result["Place Price"]
        return(result, price) 
    else:
        print(f"'{kinds}'에 해당하는 카페가 없습니다.")

# kinds = ["한식", "막걸리", ]

# print(reco_cafe(kinds, 0))