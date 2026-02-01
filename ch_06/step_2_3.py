from step_1_2 import run_playwright
from step_1_3 import goto_best_goods
from step_2_1 import select_category, select_option
from step_2_2_1 import take_screenshots

def fetch_trends_by_filter(category: str = None, option: str = None):
    play, browser, page = run_playwright(slow_mo=500)
    goto_best_goods(page) # 베스트상품 페이지로 이동
    if category:
        select_category(page, category) # 카테고리 클릭
    if option:
        select_option(page, option) # 연령, 성별 등 세부 옵션 클릭
    take_screenshots(page)
    browser.close()
    play.stop()
if __name__ == '__main__':
    category, option = '패션의류', '10대 여성'
    fetch_trends_by_filter(category, option) # 쇼핑 트렌드 수집 함수