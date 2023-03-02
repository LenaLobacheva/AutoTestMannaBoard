from selenium import webdriver


from pages.ad_to_favorites import Ad_to_favorites
from pages.del_ad import Del_ad
from pages.logout import Logout
from pages.return_to_archive import Return_from_archive
from pages.login_pages import Login_page
from pages.ad_to_archive import Ad_to_archive


def test_manna():
    driver = webdriver.Firefox(executable_path='C:\\Users\\MGaming\\PycharmProjects\\resource\\geckodriver.exe')

    print('Start Test')

    login = Login_page(driver)
    login.authorization()
    ad = Ad_to_favorites(driver)
    ad.ad_to_favorites()
    ar = Ad_to_archive(driver)
    ar.profile()
    ra = Return_from_archive(driver)
    ra.return_ad()
    da = Del_ad(driver)
    da.delete_ad()
    logout = Logout(driver)
    logout.user_logout()



