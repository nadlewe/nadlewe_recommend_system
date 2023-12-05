# restaurant에 해당하는 장소를 추천하는 기능


import pandas as pd
import re
import json
import random

# CSV 파일 경로 설정
file_path = '/Users/chominjun/Desktop/Workspace/PYTHON_workspace/recommend_system/Data/restaurant_info.csv'

# CSV 파일 읽기
try:
    df = pd.read_csv(file_path)
    # 데이터프레임 출력
    print(df)
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path}")
except Exception as e:
    print(f"오류 발생: {e}")

kinds = ["양식", "막걸리"]

def reco_restaurant(kinds):
    pattern = re.compile(fr'\b(?:{"|".join(kinds)})\b', flags=re.IGNORECASE)
    matching_rows = df[df['tags'].apply(lambda x: bool(pattern.search(x)) if pd.notna(x) else False)]
 
    if not matching_rows.empty:
        result_list = []
        for index, row in matching_rows.iterrows():
            restaurant_info = {
                "Place Name": row['name'],
                "Rate": row['rate'],
                "Menu": row['representative_menu'],
                "Place Price": row['place_price'],
                "Place Image": row['image_URL']
            }
            result_list.append(restaurant_info)
        # print("추천하는 레스토랑 정보:")
        val = len(result_list)
        ran = random.randint(1, val)
        # print(ran)
        result = result_list[ran]
        # print(json.dumps(result_list, ensure_ascii=False, indent=2))

        # print(result)
        return(result)
    else:
        print(f"'{kinds}'에 해당하는 레스토랑이 없습니다.")


reco_restaurant(kinds)
            # placeName: string
            # rate: double
            # menu: string
            # menuDetail: string
            # placePrice: int
            # placeImage: file

# {
#     "minPrice":70000,
#     "maxPrice":130000,
#     "themes":["식사","식사","카페","카페","활동"],
#     "kinds":["한식","와인","칵테일","방탈출"]
# }