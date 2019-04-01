import uiautomator2 as u2
import time

d = u2.connect('192.168.0.45')


def startApp(start):
    app = ''
    d.debug = True
    d.app_start(app)
    print('连接成功，启动成功')
    return start


def login(login):
    d(text="请输入手机号").click()
    d(text="请输入手机号").send_keys('')
    d(resourceId="com.ruanjie.lotterybible:id/et_password").send_keys('12345678')
    d.click(0.935, 0.597)
    d.xpath("//android.widget.Button[@text='登 录']").click()


    print('登陆成功')
    time.sleep(3)
    d.press('back')
    time.sleep(3)
    d.press("back")
    return login

def xinshuitest(xinsh):
    d(resourceId="com.ruanjie.lotterybible:id/iv_heartwater").click()
    # d(className="android.widget.ImageView", instance=6).wait_timeout(20)
    time.sleep(5)
    a = 1
    while a < 2:
        d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
        d.click(0.887, 0.539)
        d(resourceId="com.ruanjie.lotterybible:id/tv_zan").click()
        # d(resourceId="com.ruanjie.lotterybible:id/close_kaijiang").click()
        # d(resourceId="com.ruanjie.lotterybible:id/tv_remark").click()
        # d(resourceId="com.ruanjie.lotterybible:id/edit_text").send_keys('加油加油')
        # d(resourceId="com.ruanjie.lotterybible:id/tv_send").click()
        time.sleep(2)
        d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
        d.click(0.038, 0.064)
        d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
        a = a + 1
    # d(resourceId="com.ruanjie.lotterybible:id/tv_create_post").click()
    # d(resourceId="com.ruanjie.lotterybible:id/re_title").send_keys('心水发帖测试')
    # d(description=u"2000字以内,选中文字即可编辑颜色").click()
    # d.set_fastinput_ime(True)
    # d.send_keys("测试发帖")
    # d(resourceId="com.ruanjie.lotterybible:id/rb_color_3").click(timeout=10)
    # d(resourceId="com.ruanjie.lotterybible:id/tv_commit").click()
    d.press("back")
    d.press("back")
    return xinsh

def liuhe(liuhe):
    d(resourceId="com.ruanjie.lotterybible:id/ll_lhc_cxzs").click()
    time.sleep(3)
    d(resourceId="com.ruanjie.lotterybible:id/img_pic", className="android.widget.ImageView", instance=1).click()
    time.sleep(1)
    d.press("back")
    d(resourceId="com.ruanjie.lotterybible:id/img_pic", className="android.widget.ImageView", instance=2).click()
    time.sleep(1)
    d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
    d.press("back")
    d(resourceId="com.ruanjie.lotterybible:id/img_pic", className="android.widget.ImageView", instance=3).click()
    time.sleep(1)
    d.press("back")
    d(resourceId="com.ruanjie.lotterybible:id/img_pic", className="android.widget.ImageView", instance=4).click()
    time.sleep(1)
    d.press("back")
    d(resourceId="com.ruanjie.lotterybible:id/img_pic", className="android.widget.ImageView", instance=5).click()
    time.sleep(1)
    d.press("back")
    d(resourceId="com.ruanjie.lotterybible:id/img_pic", className="android.widget.ImageView", instance=6).click()
    time.sleep(1)
    d.press("back")
    d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
    d(resourceId="com.ruanjie.lotterybible:id/img_pic", className="android.widget.ImageView", instance=4).click()
    time.sleep(1)
    d.press("back")
    d(resourceId="com.ruanjie.lotterybible:id/img_pic", className="android.widget.ImageView", instance=5).click()
    time.sleep(2)
    d.press("back")
    d(resourceId="com.ruanjie.lotterybible:id/img_pic", className="android.widget.ImageView", instance=6).click()
    time.sleep(1)
    d.press("back")
    d(resourceId="com.ruanjie.lotterybible:id/img_pic", className="android.widget.ImageView", instance=7).click()
    time.sleep(1)
    # d.press("back")
    # d(resourceId="com.ruanjie.lotterybible:id/img_pic", className="android.widget.ImageView", instance=8).click()
    d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
    d(resourceId="com.ruanjie.lotterybible:id/tv_name", text=u"香港挂牌").click()
    time.sleep(1)
    d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
    d(resourceId="com.ruanjie.lotterybible:id/tv_name", text=u"百万富翁").click()
    time.sleep(1)
    d(className="android.widget.LinearLayout", instance=10).click()
    time.sleep(2)
    d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
    d(resourceId="com.ruanjie.lotterybible:id/tv_name", text=u"东方心经").click()
    time.sleep(2)
    d(className="android.widget.LinearLayout", instance=10).click()
    time.sleep(1)
    d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
    d(resourceId="com.ruanjie.lotterybible:id/tv_name", text=u"港澳大拼盘").click()
    time.sleep(1)
    d(className="android.widget.LinearLayout", instance=10).click()
    time.sleep(1)
    d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
    d(resourceId="com.ruanjie.lotterybible:id/tv_name", text=u"六合宝典").click()
    time.sleep(1)
    d(className="android.widget.LinearLayout", instance=20)
    d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
    d(resourceId="com.ruanjie.lotterybible:id/tv_name", text=u"六合财富").click()
    time.sleep(1)
    d(resourceId="com.ruanjie.lotterybible:id/name", text=u"B").click()

    d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
    d.press("back")
    time.sleep(1)
    d.press("back")
    return liuhe

def loginout(lo):
    d(resourceId="com.ruanjie.lotterybible:id/iv_tab_icon", className="android.widget.ImageView", instance=4).click()
    time.sleep(1)
    d.swipe(0.433, 0.859, 0.436, 0.286, 0.5)
    d(resourceId="com.ruanjie.lotterybible:id/tv_account_settings").click()
    d(resourceId="com.ruanjie.lotterybible:id/bt_sign_out").click()
    return lo

a=0
while a<1000:
    print(startApp(str))
    print(login(str))
    # print(xinshuitest(str))
    print(liuhe(str))
    print(loginout(str))
    a= a+1
