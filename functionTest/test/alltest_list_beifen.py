from project.yinniqianbaoshanghu.tipstest.testtips import TestTips
from project.yinniqianbaoshanghu.settingstest.testsettings import TestSettings
from project.yinniqianbaoshanghu.logouttest.testlogout import TestLogout
def caselist():

    alltestnames = [
    'project.yinniqianbaoshanghu.zhugongnengceshi.zhuliuchengtest.TestZhuGongNeng',
    'project.yinniqianbaoshanghu.logintest.testlogin.TestLogin',
    'project.yinniqianbaoshanghu.tipstest.testtips.TestTips',
    'project.yinniqianbaoshanghu.settingstest.testsettings.TestSettings',
    'project.yinniqianbaoshanghu.logouttest.testlogout.TestLogout',

    ]
    print ('suite read case list success!! ')
    return alltestnames