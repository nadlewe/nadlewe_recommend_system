from Filter_Budget import filter_by_budget
from Filter_Theme import filter_by_theme
from Filter_Cuisine import filter_by_cuisine

# 예시 데이터베이스
places = [
    {"name": "한식당", "type": "식당", "cuisine": "한식", "average_cost": 30000},
    {"name": "중국집", "type": "식당", "cuisine": "중식", "average_cost": 20000},
    {"name": "스시집", "type": "식당", "cuisine": "일식", "average_cost": 40000},
    {"name": "분식집", "type": "식당", "cuisine": "분식", "average_cost": 10000},
    {"name": "이탈리안 레스토랑", "type": "식당", "cuisine": "양식", "average_cost": 50000},
    {"name": "카페 드림", "type": "카페", "cuisine": "기타", "average_cost": 15000},
    {"name": "에스케이프 룸", "type": "액티비티", "cuisine": "기타", "average_cost": 25000},
    {"name": "포토 스튜디오", "type": "사진", "cuisine": "기타", "average_cost": 30000},
    # ... 추가 장소 데이터
]

def create_course(places, number_of_places):
    return places[:number_of_places]


def recommend_places(budget, number_of_places, themes, cuisines):
    filtered_places = filter_by_budget(places, budget)
    
    for theme in themes:
        filtered_places = filter_by_theme(filtered_places, theme)
    for cuisine in cuisines:
        filtered_places = filter_by_cuisine(filtered_places, cuisine)
    
    course = create_course(filtered_places, number_of_places)
    
    return course

def main():
    user_budget = 500000  # 예산
    user_number_of_places = 3  # 장소 개수
    user_themes = ["식당", "카페", "액티비티"]  # 데이트 테마
    user_cuisines = ["한식", "일식", "양식"]  # 음식 종류

    recommended_course = recommend_places(user_budget, user_number_of_places, user_themes, user_cuisines)

    for place in recommended_course:
        print(f"장소 이름: {place['name']}, 유형: {place['type']}, 평균 비용: {place['average_cost']}원")

if __name__ == "__main__":
    main()