import json
from typing import List, Dict


class Blueprint:
    """星际猎人蓝图类，存储蓝图核心信息"""

    def __init__(self, name: str, version: str, model: str, tags: List[str] = None):
        self.name = name
        self.version = version
        self.model = model
        self.tags = tags if tags else []  # 标签用于关联推荐

    def to_dict(self) -> Dict:
        """转换为字典用于存储"""
        return {
            "name": self.name,
            "version": self.version,
            "model": self.model,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """从字典创建蓝图对象"""
        return cls(
            name=data["name"],
            version=data["version"],
            model=data["model"],
            tags=data.get("tags", [])
        )

    def __str__(self):
        return f"蓝图名称：{self.name} | 版本：{self.version} | 型号：{self.model} | 标签：{', '.join(self.tags)}"


class TeamComposition:
    """配队方案类"""

    def __init__(self, name: str, blueprints: List[Blueprint], description: str = ""):
        self.name = name
        self.blueprints = blueprints
        self.description = description

    def to_dict(self) -> Dict:
        """转换为字典用于导出"""
        return {
            "name": self.name,
            "description": self.description,
            "blueprints": [bp.to_dict() for bp in self.blueprints]
        }


class BlueprintManager:
    """蓝图管理系统，负责蓝图的存储、增删改查"""

    def __init__(self):
        self.blueprints: List[Blueprint] = []  # 存储所有上传的蓝图
        self.team_compositions: List[TeamComposition] = []  # 存储所有配队方案

    def upload_blueprint(self, blueprint: Blueprint) -> None:
        """上传新蓝图"""
        self.blueprints.append(blueprint)
        print(f"✅ 成功上传蓝图：{blueprint.name}")

    def list_all_blueprints(self) -> None:
        """列出所有已上传蓝图"""
        if not self.blueprints:
            print("ℹ️ 当前没有已上传的蓝图")
            return
        print("\n📋 所有已上传蓝图：")
        for i, bp in enumerate(self.blueprints, 1):
            print(f"{i}. {bp}")

    def modify_blueprint(self, index: int, new_name: str, new_version: str, new_model: str,
                         new_tags: List[str]) -> bool:
        """修改指定索引的蓝图"""
        if 0 <= index < len(self.blueprints):
            old_bp = self.blueprints[index]
            self.blueprints[index] = Blueprint(new_name, new_version, new_model, new_tags)
            print(f"✅ 已修改蓝图：原名称「{old_bp.name}」→ 新名称「{new_name}」")
            return True
        print("❌ 错误：蓝图索引不存在")
        return False

    def delete_blueprint(self, index: int) -> bool:
        """删除指定索引的蓝图"""
        if 0 <= index < len(self.blueprints):
            deleted_bp = self.blueprints.pop(index)
            print(f"✅ 已删除蓝图：{deleted_bp.name}")
            return True
        print("❌ 错误：蓝图索引不存在")
        return False

    def query_blueprint_exact(self, name: str) -> List[Blueprint]:
        """精确匹配蓝图名称"""
        matches = [bp for bp in self.blueprints if bp.name == name]
        return matches

    def get_recommend_blueprints(self, target_bp: Blueprint) -> List[Blueprint]:
        """根据标签做蓝图关联推荐"""
        if not target_bp.tags:
            # 没有标签则返回同型号的其他蓝图
            return [bp for bp in self.blueprints if bp.model == target_bp.model and bp != target_bp][:3]

        # 计算标签重合度，返回重合度最高的3个蓝图
        recommend_list = []
        for bp in self.blueprints:
            if bp == target_bp:
                continue
            common_tags = len(set(target_bp.tags) & set(bp.tags))
            if common_tags > 0:
                recommend_list.append((common_tags, bp))

        # 按重合度排序，取前3个
        recommend_list.sort(reverse=True, key=lambda x: x[0])
        return [bp for (score, bp) in recommend_list[:3]]

    def save_team_composition(self, team: TeamComposition) -> None:
        """保存配队方案"""
        self.team_compositions.append(team)
        print(f"✅ 成功保存配队方案：{team.name}")

    def export_all_data(self, filename: str = "star_hunter_data.json") -> None:
        """导出所有蓝图和配队方案到JSON文件"""
        export_data = {
            "blueprints": [bp.to_dict() for bp in self.blueprints],
            "team_compositions": [
                {
                    "name": team.name,
                    "description": team.description,
                    "blueprint_names": [bp.name for bp in team.blueprints]
                }
                for team in self.team_compositions
            ]
        }
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)
            print(f"✅ 数据已成功导出到文件：{filename}")
        except Exception as e:
            print(f"❌ 导出失败：{str(e)}")

    def load_data_from_file(self, filename: str = "star_hunter_data.json") -> None:
        """从JSON文件导入已有数据"""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.blueprints = [Blueprint.from_dict(bp_data) for bp_data in data.get("blueprints", [])]
            print(f"✅ 成功从文件导入 {len(self.blueprints)} 个蓝图")
        except FileNotFoundError:
            print("ℹ️ 没有找到已存储的数据文件，将创建新文件")
        except Exception as e:
            print(f"❌ 导入失败：{str(e)}")


def create_team_by_blueprints(manager: BlueprintManager) -> None:
    """根据已有蓝图创建配队方案"""
    if not manager.blueprints:
        print("ℹ️ 当前没有已上传的蓝图，请先上传蓝图")
        return

    print("\n🔍 现有所有蓝图如下，请选择要加入配队的蓝图编号（多个用空格分隔）：")
    manager.list_all_blueprints()
    try:
        indices_input = input("请输入编号：").strip()
        indices = [int(i) - 1 for i in indices_input.split()]
        selected_bps = [manager.blueprints[i] for i in indices if 0 <= i < len(manager.blueprints)]

        if not selected_bps:
            print("❌ 没有选中任何有效蓝图")
            return

        team_name = input("请输入配队方案名称：").strip()
        team_desc = input("请输入配队方案描述（可选）：").strip()

        new_team = TeamComposition(team_name, selected_bps, team_desc)
        manager.save_team_composition(new_team)

        # 展示关联推荐
        print("\n🤝 为你推荐可搭配的其他蓝图：")
        recomended = set()
        for bp in selected_bps:
            recs = manager.get_recommend_blueprints(bp)
            for r in recs:
                recomended.add(r)
        if recomended:
            for i, rec_bp in enumerate(recomended, 1):
                print(f"{i}. {rec_bp}")
        else:
            print("没有找到合适的关联推荐")

    except ValueError:
        print("❌ 输入格式错误，请输入数字编号")


def main():
    """游戏配队程序主逻辑"""
    manager = BlueprintManager()
    # 启动时自动加载已有数据
    manager.load_data_from_file()

    print("===== 星际猎人蓝图与配队系统 =====")
    print("支持蓝图增删改查、精确匹配、配队保存导出、关联推荐")

    while True:
        print("\n请选择操作：")
        print("1. 上传新蓝图")
        print("2. 查看所有蓝图")
        print("3. 修改蓝图")
        print("4. 删除蓝图")
        print("5. 精确查询蓝图并创建配队")
        print("6. 导出所有数据到文件")
        print("7. 退出系统")
        choice = input("请输入选项（1-7）：").strip()

        if choice == "1":
            name = input("请输入蓝图名称：").strip()
            version = input("请输入蓝图模块or型号：").strip()
            model = input("请输入蓝图型号：").strip()
            tags_input = input("请输入蓝图标签（多个用逗号分隔，可选）：").strip()
            tags = [t.strip() for t in tags_input.split(",")] if tags_input else []
            blueprint = Blueprint(name, version, model, tags)
            manager.upload_blueprint(blueprint)

        elif choice == "2":
            manager.list_all_blueprints()

        elif choice == "3":
            manager.list_all_blueprints()
            if not manager.blueprints:
                continue
            try:
                idx = int(input("请输入要修改的蓝图编号：")) - 1
                new_name = input("请输入新的蓝图名称：").strip()
                new_version = input("请输入新的蓝图版本：").strip()
                new_model = input("请输入新的蓝图型号：").strip()
                new_tags_input = input("请输入新的标签（多个用逗号分隔）：").strip()
                new_tags = [t.strip() for t in new_tags_input.split(",")] if new_tags_input else []
                manager.modify_blueprint(idx, new_name, new_version, new_model, new_tags)
            except ValueError:
                print("❌ 输入格式错误，请输入数字编号")

        elif choice == "4":
            manager.list_all_blueprints()
            if not manager.blueprints:
                continue
            try:
                idx = int(input("请输入要删除的蓝图编号：")) - 1
                manager.delete_blueprint(idx)
            except ValueError:
                print("❌ 输入格式错误，请输入数字编号")

        elif choice == "5":
            query_name = input("请输入要精确匹配的蓝图名称：").strip()
            matches = manager.query_blueprint_exact(query_name)
            if not matches:
                print(f"❌ 没有找到名称完全等于「{query_name}」的蓝图")
                continue
            print(f"\n🔍 找到 {len(matches)} 个精确匹配结果：")
            for i, bp in enumerate(matches, 1):
                print(f"{i}. {bp}")
            # 创建配队
            create_team_by_blueprints(manager)

        elif choice == "6":
            filename = input("请输入导出文件名（默认star_hunter_data.json）：").strip() or "star_hunter_data.json"
            manager.export_all_data(filename)

        elif choice == "7":
            # 退出前自动保存数据
            manager.export_all_data()
            print("👋 感谢使用星际猎人配队系统，再见！")
            break

        else:
            print("❌ 无效选项，请重新输入")


if __name__ == "__main__":
    main()