import src.data
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    @allure.step('Открываем страницу логина')
    def open_login_page(self):
        self.open_url(src.data.LOGIN_PAGE_URL)
        self.wait_for_element(LoginPageLocators.LOG_IN_BUTTON, 'visibility')
        
    @allure.step('Авторизация пользователя')
    def user_login(self, create_user):
        email = create_user['email']
        password = create_user['password']
        self.send_keys(LoginPageLocators.EMAIL_INPUT_FORM, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT_FORM, password)
        self.click_on_element(LoginPageLocators.LOG_IN_BUTTON)
        self.wait_for_element(LoginPageLocators.CREATE_ORDER_BUTTON, 'visibility')
        
    @allure.step('Авторизация пользователя с созданием заказа')
    def user_login_with_order(self, login_user, create_order):
        email, password = login_user
        number = create_order
        self.send_keys(LoginPageLocators.EMAIL_INPUT_FORM, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT_FORM, password)
        self.wait_for_element(LoginPageLocators.LOG_IN_BUTTON, 'presence')
        self.click_on_element(LoginPageLocators.LOG_IN_BUTTON)
        return number
    
    @allure.step('Процесс авторизации')
    def user_login_in_main_page(self, create_user):
        self.open_login_page()
        self.user_login(create_user)