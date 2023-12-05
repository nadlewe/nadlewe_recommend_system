# activity에 해당하는 장소를 추천하는 기능


import pandas as pd
import re
import random

# CSV 파일 경로 설정
file_path = '/Users/chominjun/Desktop/Workspace/PYTHON_workspace/recommend_system/Data/activity_info.csv'

# CSV 파일 읽기
try:
    df = pd.read_csv(file_path)
    # 데이터프레임 출력
    print(df)
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path}")
except Exception as e:
    print(f"오류 발생: {e}")

def reco_activity(kinds):
    pattern = re.compile(fr'\b(?:{"|".join(kinds)})\b', flags=re.IGNORECASE)
    matching_rows = df[df['tags'].apply(lambda x: bool(pattern.search(x)) if pd.notna(x) else False)]
 
    if not matching_rows.empty:
        result_list = []
        for index, row in matching_rows.iterrows():
            restaurant_info = {
                "Place Name": row['name'],
                "Rate": row['rate'],
                "Place Image": row['image_URL']
            }
            result_list.append(restaurant_info)
        # print("추천하는 활동 정보:")
        val = len(result_list)
        ran = random.randint(1, val)
        result = result_list[ran]
        # print(json.dumps(result_list, ensure_ascii=False, indent=2))

        # print(result)
        return(result)
    else:
        print(f"'{kinds}'에 해당하는 활동이 없습니다.")


# kinds=["맥주/소주", "한식", "영화"]
# reco_activity(kinds)