from selenium.webdriver.common.by import By
from base_page_object import BasePage
from os import getcwd
from PIL import Image


class AutomationUploadPage(BasePage):
    locator_dictionary = {
        "fileId": (By.ID, 'id_file'),
        "button": (By.NAME, 'upload_file'),
        "uploadPage": (By.XPATH, "/html/body/nav/div/ul[1]/li/a"),
        "permission": (By.XPATH, '/html/body/main')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url="127.0.0.1:8000")

    def get_text(self):
        self.find_element(*self.locator_dictionary['permission']).text

    def file_upload(self, fileType):

     
        """TODO: get context.filetype and append it to save + path """
        """BUG: Application shouldn't just check mime-types """
        rootPath = getcwd() + '/sample_files/pil_red.' + fileType
        print(rootPath*100)

        if fileType in ('png', 'gif', 'jpeg'):
            img = Image.new('RGB',(60, 30),color='red')
            img.save(rootPath)

        elif fileType in ('txt','rtf','doc','xls','xlsx','docx'):
            with open(rootPath, 'w+') as tmp_file:
                tmp_file.write("test")
        else:
            print("File type not supported\n")

        self.find_element(*self.locator_dictionary['fileId']).send_keys(rootPath)
        self.find_element(*self.locator_dictionary['button']).click()


