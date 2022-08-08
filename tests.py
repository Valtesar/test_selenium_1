from YandexPages import SearchHelper
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("info level")


def test_yandex_search(browser):
    """Автоматизированный тест 'поиск в яндексе'"""

    """[WHEN] Введен Url в браузере https://yandex.ru/ 
       [THEN] На странице должно находится поле поиска
       [WHEN] Вводим в поле поиска 'Tensor'
       [THEN] Появляется таблица с подсказками
       [WHEN] Нажимаем клавишу 'Enter'
       [THEN] Появляется таблица результатов поиска
       [WHEN] Получаем ссылку первого элемента
       [THEN] Первый элемент соответствует сайту 'tensor.ru'"""

    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Тензор")

    try:
        assert yandex_main_page.check_popup()
    except AssertionError as error:
        logger.exception("Assertion popup is visible failed", exc_info=True)
        raise error

    yandex_main_page.press_enter()

    try:
        assert yandex_main_page.check_link()
    except AssertionError as error:
        logger.exception("Assertion when link checked on tensor.ru failed", exc_info=True)
        raise error


def test_yandex_images(browser):
    """Автоматизированный тест поиска картинок в яндексе"""

    """[WHEN] Введен Url в браузере https://yandex.ru/ 
       [THEN] Ссылка 'картинки' присутствует на странице
       [WHEN] Кликаем по ссылке 'картинки'
       [THEN] Проверям что url в браузере hhtps://yandex.ru/images/
       [WHEN] Открываем первую категорию картинок
       [THEN] Проверяем, что название категории отображается в поле поиска
       [WHEN] Открываем первую картинку
       [THEN] Проверяем, что картинка открылась (Картинка 1)
       [WHEN] Нажимаем на кнопку вперед
       [THEN] Проверяем, что картинка сменилась (Картинка 2)
       [WHEN] Нажимаем на кнопку назад
       [THEN] Проверяем, что картинка сменилась на (Картинка 1)"""

    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()

    try:
        assert yandex_main_page.go_to_images()
    except AssertionError as error:
        logger.exception("Assert click on images failed", exc_info=True)
        raise error

    try:
        assert yandex_main_page.check_images_changes()
    except AssertionError as error:
        logger.exception("Assert image changes failed", exc_info=True)
        raise error


