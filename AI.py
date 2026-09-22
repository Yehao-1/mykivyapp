import random
import json
def guess_geme():
#***********************#项目1：猜数字游戏************************
                        # 1. 导入随机数模块
                        # 2. 生成1-100之间的随机整数
    numbers=random.randint(1,100)
    min=1
    max=100
                        # 3. 循环接收用户输入
    print("------欢迎进入猜数字游戏!!!------")
    while True:
                        # 4. 获取用户输入
        user_input=input("请输入1-100中的一个整数!")
                        # 5. 校验输入是否为数字
        try:
            user_input=int(user_input)
        except ValueError:
            print("请输入正确的数字!!!")
            continue
                        #   6. 判断猜的结果
        if user_input == numbers:
            print("恭喜你猜对了!!!")
            user_input = input("是否继续游玩？，退出请输入q!!!")
            if user_input == "q":
                print("猜数字游戏已退出，欢迎下次使用!!!")
            break
        else:
            if user_input > numbers:
                print("猜大了，继续!!!")
                max=user_input
                print(f"范围是{min}--{max}")
            elif user_input < numbers:
                print("猜小了，继续!!!")
                min=user_input
                print(f"范围是{min}--{max}")


#*********************************************************************


def computer():
                        #项目2：命令行计算器
                        # 1. 定义运算函数
    def add(a,b):
        return a+b
    def subtraction(a,b):
        return a-b
    def multiplication(a,b):
        return a*b
    def division(a,b):
        if b==0:
            return print("被除数不能为0!!!")
        return a/b
    def remainder(a,b):
        if b==0:
            return print("被除数不能为0!!!")
        return a%b
    def power(a,b):
        return a**b
                        # 3. 获取用户输入

    while True:
        try:
            a=int(input("第一个数"))
            b=int(input("第二个数"))
            fh = input("请输入运算符号")
                        # 5. 捕获数字输入错误
                        # 4. 根据运算符执行对应逻辑
            if fh=="+":
                result=add(a,b)
            elif fh=="-":
                result=subtraction(a,b)
            elif fh=="*":
                result=multiplication(a,b)
            elif fh=="/":
                result=division(a,b)
            elif fh=="%":
                result=remainder(a,b)
            elif fh=="**":
                result=power(a,b)
            else:
                print("没有这个运算符哦!!!")
                continue
            if result is not None:
                print(f"结果是{result}")
            user_input=input("是否继续运算？，退出请输入q")
            if user_input=="q":
                print("计算机已退出，欢迎下次使用!!!")
                break
        except ValueError:
            print("请输入正确的符号或者数字")
            continue


#***********************************************************************



#项目3：Todo列表管理器

def memo():
    # 1. 加载本地保存的待办数据
    def load_todos():
        try:
            with open("todos.json", "r", encoding="utf-8") as f:
                return json.load(f)
        # 文件不存在时返回空列表
        except FileNotFoundError:
            return []

    # 2. 保存待办数据到本地文件
    def save_todos(todo_list):
        with open("todos.json", "w", encoding="utf-8") as f:
            json.dump(todo_list, f, ensure_ascii=False, indent=2)

    todo_list = load_todos()

    # 3. 主菜单循环
    while True:
        print("\n=== 备忘录 ===")
        print("1. 查看所有待办 2. 添加待办 3. 删除待办 4. 退出")
        choice = input("请输入操作编号：")

        if choice == "1":
            # 遍历打印所有待办
            if not todo_list:
                print("还没有待办事件噢!!!")
            else:
                for idx, todo in enumerate(todo_list, 1):
                    print(f"{idx}. {todo}")
        elif choice == "2":
            new_todo = input("输入新的待办事项：")
            todo_list.append(new_todo)
            save_todos(todo_list)
            print("添加成功！")
        elif choice == "3":
            del_idx = int(input("输入要删除的待办编号：")) -1
            if 0 <= del_idx < len(todo_list):
                todo_list.pop(del_idx)
                save_todos(todo_list)
                print("删除成功！")
            else:
                print("编号不存在")
        elif choice == "4":
            print("退出备忘录")
            break
        else:
            print("输入无效选项")

# ***********************************************************************

def finger_guess():
#项目4：石头剪刀布游戏
    choices=["石头","剪刀","布"]
    count=0
    computer_count=0
    user_count=0


    while True:
        sum = computer_count + user_count
        if sum <3:
            computer=random.choice(choices)
            user=input("请输入剪刀or石头or布进行比赛!!!\n")
            if user not in choices:
                print("不合规选择,请重新输入!!!")
            if user == computer:
                count+=1
                print(f"这是第{count}局，平局,继续!")
                user = input("请输入剪刀or石头or布进行比赛!!!\n")
            if user == "石头":
                if computer == "剪刀":
                    count+=1
                    user_count+=1
                    print(f"这是第{count}局\n恭喜你,你赢了!")
                else:
                    count+=1
                    computer_count+=1
                    print(f"这是第{count}局\n你输了!")
            if user == "剪刀":
                if computer == "石头":
                    count+=1
                    computer_count+=1
                    print(f"这是第{count}局\n你输了!")
                else:
                    count+=1
                    user_count+=1
                    print(f"这是第{count}局\n恭喜你,你赢了!")
            if user == "布":
                if computer == "石头":
                    count+=1
                    user_count+=1
                    print(f"这是第{count}局\n恭喜你,你赢了!")
                else:
                    count+=1
                    computer_count+=1
                    print(f"这是第{count}局\n你输了!")
        else:
            if computer_count>user_count:
                print("********游戏结束,很遗憾,您输了!!!********")
            if user_count>computer_count:
                print("********游戏结束,恭喜你,你赢了!!!********")
            break















#***********************************************************************

                            #整体实现调用

print("===== 欢迎使用ai助手 =====")
print("输入「猜数字」「计算器」「备忘录」「猜拳游戏」「退出」即可使用对应功能")
while True:
    command = input("\n请输入要使用的功能：").strip().lower()
    if "猜数字" in command:
        guess_geme()
        print("\n回到工具集主菜单~")
    elif "计算器" in command or "计算机" in command:
        computer()
        print("\n回到工具集主菜单~")
    elif "备忘录" in command:
        memo()
        print("\n回到工具集主菜单~")
    elif "猜拳游戏" in command:
        finger_guess()
        print("\n回到工具集主菜单~")
    elif "退出" in command or "q" in command:
        print("已退出工具集，再见")
        break
    else:
        print("未识别的指令，请重新输入！")
