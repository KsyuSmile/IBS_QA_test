from selenium.webdriver.common.by import By

from web.base_page import BasePage


class ButtonExample(BasePage):
    LOCATOR_USERS = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[1]")
    LOCATOR_SINGLE_USERS = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[2]")
    LOCATOR_SINGLE_USERS_NF = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[3]")
    LOCATOR_LIST_RESOURCE = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[4]")
    LOCATOR_SINGLE_RESOURCE = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[5]")
    LOCATOR_SINGLE_RESOURCE_NF = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[6]")
    LOCATOR_CREATE = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[7]")
    LOCATOR_UPDATE_PUT = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[8]")
    LOCATOR_UPDATE_PATCH = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[9]")
    LOCATOR_UPDATE_DELETE = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[10]")
    LOCATOR_REGISTER_SUCCES = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[11]")
    LOCATOR_REGISTER_UNSUCCES = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[12]")
    LOCATOR_LOGIN_SUCCES = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[13]")
    LOCATOR_LOGIN_UNSUCCES = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[14]")
    LOCATOR_DELAYED_RESPONSE = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[15]")

    def click_button_to_users(self):
        return self.find_element(self.LOCATOR_USERS).click()

    def click_button_to_single_users(self):
        return self.find_element(self.LOCATOR_SINGLE_USERS).click()

    def click_button_to_single_users_nf(self):
        return self.find_element(self.LOCATOR_SINGLE_USERS_NF).click()

    def click_button_to_list_resource(self):
        return self.find_element(self.LOCATOR_LIST_RESOURCE).click()

    def click_button_to_single_resource(self):
        return self.find_element(self.LOCATOR_SINGLE_RESOURCE).click()

    def click_button_to_single_resource_nf(self):
        return self.find_element(self.LOCATOR_SINGLE_RESOURCE_NF).click()

    def click_button_to_create(self):
        return self.find_element(self.LOCATOR_CREATE).click()

    def click_button_to_update_put(self):
        return self.find_element(self.LOCATOR_UPDATE_PUT).click()

    def click_button_to_update_patch(self):
        return self.find_element(self.LOCATOR_UPDATE_PATCH).click()

    def click_button_to_delete(self):
        return self.find_element(self.LOCATOR_UPDATE_DELETE).click()

    def click_button_to_register_succes(self):
        return self.find_element(self.LOCATOR_REGISTER_SUCCES).click()

    def click_button_to_register_unsucces(self):
        return self.find_element(self.LOCATOR_REGISTER_UNSUCCES).click()

    def click_button_to_login_succes(self):
        return self.find_element(self.LOCATOR_LOGIN_SUCCES).click()

    def click_button_to_login_unsucces(self):
        return self.find_element(self.LOCATOR_LOGIN_UNSUCCES).click()

    def click_button_to_delay_res(self):
        return self.find_element(self.LOCATOR_DELAYED_RESPONSE).click()


class ResExample(BasePage):
    LOCATOR_RESPONSE_CODE = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/section[1]/div[2]/div[2]/p[1]/strong[1]/span[1]")
    LOCATOR_RESPONSE_BODY = (By.XPATH, "//body/div[2]/div[1]/div[1]/section[1]/div[2]/div[2]/pre[1]")

    def check_response_code(self):
        return self.find_element(self.LOCATOR_RESPONSE_CODE).text

    def check_response_body(self):
        return self.find_element(self.LOCATOR_RESPONSE_BODY).text


