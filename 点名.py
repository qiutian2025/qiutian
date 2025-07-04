import random

def 随机点名(名单):
    if not 名单:
        return "名单为空，无法点名！"
    return random.choice(名单)

def 主程序():
    # 示例名单
    名单 = ["陈骏豪","戴沉毅","邓柯","冯子骏","顾雨萱","胡佳妍","黄彬","黄可馨","黄帪","蒋思诚","李翰","李雨欣","朱梓萱","刘梓豪","陆梓鑫","钱科颖","瞿佳怡","沈子恒","顾羽乐","谈芯妤","陶星雨","童子轩","王奕然","翁祖阳","席橙荣","熊浩铭","徐诗涵","杨子涵","杨紫轩","余浩晨","俞文博","袁佳怡","张亦宁","张梓嫣","赵一涵"	,"仲玲演","朱辰浩","朱凌萱","朱栩皞","朱奕彤","肖志杰","黄锦宸"
]
    
    while True:
        print("\n当前名单：", ", ".join(名单))
        print("1. 随机点名")
        print("2. 退出")
        选择 = input("请选择操作（输入 1 或 2）：")

        if 选择 == "1":
            被点名者 = 随机点名(名单)
            print(f"本次被点名的是：{被点名者}")
        elif 选择 == "2":
            print("退出点名系统。")
            break
        else:
            print("输入无效，请重新输入！")

if __name__ == "__main__":
    主程序()
