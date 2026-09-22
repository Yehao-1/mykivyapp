
'''
import json

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
    print("\n=== Todo管理器 ===")
    print("1. 查看所有待办 2. 添加待办 3. 删除待办 4. 退出")
    choice = input("请输入操作编号：")

    if choice == "1":
        # 遍历打印所有待办
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
        print("退出程序")
        break
    else:
        print("输入无效选项")
'''from work2 import Blueprint


class blueprint:
    def __init__(self,name,modou,version):
        self.name = name
        self.modou = modou
        self.version = version
    def __str__(self):
        return f"蓝图名字{self.name},{self.modou},{self.version}"
bp1=blueprint("大盾","b2 ",2.0)
print(bp1)

class BlueprintManager:
    def __init__(self):
        self.blueprints = []
    def add_blueprint(self,blueprint):
        self.blueprints.append(blueprint)
        print(f"成功上传蓝图{blueprint.name}")
    def query_blueprint(self,name):
        result=[blueprint for blueprint in self.blueprints if name in blueprint.name]
        return result

def mian():
    manager = BlueprintManager()
    print("=======星际猎人蓝图与配对系统========")
    while True:
        print("\n请选择操作","1.上传蓝图","2.删除蓝图","3.按名称查询蓝图并对其进行配队","4.退出系统")
        select=input("请输入选项")
        if select=="1":
            name=input("请输入蓝图名字")
            modou=input("请输入所拥有的（超主）模块or（小船）型号")
            version=input("请输蓝图点数（例如大盾2.0）")
            blueprint=Blueprint(name,modou,version)
            manager.add_blueprint(blueprint)

        elif select=="3":
            if not manager.blueprints:
                print("请先上传蓝图")
                continue
            name=input("请输入要匹配的蓝图名称：")
            matches=manager.query_blueprint(name)
            if not matches:
                print(f"没有找到名称包含<{name}>的蓝图")
                continue
            print(f"\n找到{len()}")




