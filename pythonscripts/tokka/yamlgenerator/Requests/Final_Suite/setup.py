from cx_Freeze import setup,Executable

includefiles = ['Resource/Config.json','tests/TestSuit_Age_categories.py','tests/auth-header-1.3.jar','tests/config_API.py']
includes = []
excludes = ['tkinter']
packages = ['requests','json','sys','os','unittest','pymysql','logging','xmlrunner']

setup(
    name = 'api_automation',
    version = '1.1',
    description = 'Rest_api_automation',
    author = 'sarath',
    author_email = 'chsivasarath@gmail.com',
    options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables = [Executable('ConfigToolAutomationPUT.py')]
)