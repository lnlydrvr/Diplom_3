from selenium.webdriver.common.by import By

class MainPageLocators:
    ACCOUNT_PAGE_MENU_BUTTON = By.XPATH, './/p[contains(@class, "AppHeader_header__linkText") and text()="Личный Кабинет"]'
    LOGIN_PAGE_HEADER = By.XPATH, '//h2[text()="Вход"]'
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]'
    CONSTRUCTOR_HEADER = By.XPATH, '//h1[text()="Соберите бургер"]'
    CONSTRUCTOR_ADD_SECTION = By.XPATH, '//section[contains(@class, "BurgerConstructor_basket__29Cd7")]'
    BUN_INGREDIENT_TEXT = By.XPATH, '//p[text()="Краторная булка N-200i"]'
    BUN_COUNTER_CLASS = By.XPATH, '//p[@class="counter_counter__num__3nue1"]'
    INGREDIENT_DETAILS_POPUP = By.XPATH, '//h2[text()="Детали ингредиента"]'
    CLOSE_POPUP_CLASS = By.CLASS_NAME, 'Modal_modal__P3_V5'
    CLOSE_POPUP_BUTTON = By.XPATH, '//button[contains(@class, "close")]'
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    CREATE_ORDER_POPUP_CLASS = By.CLASS_NAME, 'Modal_modal__container__Wo2l_'
    CREATE_ORDER_POPUP_HEADER = By.XPATH, '//p[text()="идентификатор заказа"]'
    