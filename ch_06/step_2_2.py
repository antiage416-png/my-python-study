import json
from pathlib import Path
from playwright.sync_api import Page
from step_1_1 import OUT_DIR # 이전에 작성한 모듈을 불러옵니다.
from step_1_2 import run_playwright
from step_1_3 import goto_best_goods

OUT_2_2 = OUT_DIR / f'{Path(__file__).stem}.json' #

def take_screenshots(page: Page, count: int = 15):
    # [수정 부분] 닫는 따옴표(')를 추가하여 선택자 문법 오류를 해결했습니다.
    selector = "li[class*='productCardResponsive_product_card']"
    
    # [추가 부분] 요소를 찾기 전에 화면에 나타날 때까지 기다려줍니다.
    # page.wait_for_selector(selector)
    
    # 기존 로직 유지
    locs = page.locator(selector).all()
    imgs_path = [] # 이 변수에 검색 결과를 저장
    
    for idx, loc in enumerate(locs[:count]): # li 태그 추출
        # [팁] 스크롤 없이도 Playwright가 해당 위치를 찾아가게 합니다.
        loc.scroll_into_view_if_needed() 
        
        path = OUT_DIR / f'{Path(__file__).stem}_{idx+1:03}.png'
        loc.screenshot(path=path) # 화면캡쳐
        imgs_path.append(path.as_posix())
        
    with open(OUT_2_2, 'w', encoding='utf-8') as fp: # 이미지경로를 json형태로 저장
        json.dump(imgs_path, fp, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    # 기존 메인 로직 유지
    play, browser, page = run_playwright(slow_mo=1000)
    goto_best_goods(page) # 베스트상품으로 이동
    
    # 사용자님이 원하셨던 캡처 실행
    take_screenshots(page) # 화면캡쳐
    
    browser.close()
    play.stop()