import sys
import time

ChuShi = 0
JieShu = 3


while ChuShi < JieShu:
    UserName = input("Please input your name: ")
    if len(UserName) == 0:
        print("用户名不能为空，请重新输入！")
        ChuShi += 1
        continue
    with open('LockFile.txt','r') as LockFile:
        for LF in LockFile.readlines():
            if UserName == LF.strip():
                print("您输入的账号已被锁定！")
                sys.exit(1)

    with open('UserFile.txt','r') as UserFile:
        for UF in UserFile.readlines():
            MyUser = UF.strip()
            MyUser = MyUser.split()
            #print("user=",MyUser)
            #time.sleep(1)
            if MyUser[0] == UserName:
                pwd = input("Please input your password: ")
                if len(pwd) == 0:
                    print("密码不能为空，请重新输入用户名和密码！")
                    ChuShi += 1
                    break
                elif MyUser[0] == UserName and MyUser[1] == pwd:
                    print("登陆成功！")
                    sys.exit(0)
                else:
                    if ChuShi == 2:
                        with open('LockFile.txt','a') as SuoDing:
                            SuoDing.write('\n'+UserName)
                        print("密码输入次数太多，您的账号将被锁定！")
                        sys.exit(1)
                    print("密码错误，请重新输入用户名和密码！")
                    ChuShi+=1
                    break
            else:
                continue
        else:
            print("您输入的用户名不存在，请重新输入！")
            ChuShi+=1
            break
