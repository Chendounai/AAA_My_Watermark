# =================================================================
#                 👇 只需在这里修改您的信息 👇
#                 👇 Just modify your info here 👇
# =================================================================

# 请在这里填入您的名字或ID
AUTHOR_NAME = "AIGC玄猫"

# 请在这里填入部署日期
DEPLOY_DATE = "2025-08-04"

# 您可以在下面的列表中添加、删除或修改任意多行欢迎语
# 每一行文字用英文双引号 " " 括起来，行与行之间用英文逗号 , 隔开
WELCOME_LINES = [
    f"欢迎使用由 {AUTHOR_NAME} 精心配置的 ComfyUI",
    f"部署日期: {DEPLOY_DATE}",
    "更新了数字人和其他视频插件，需要↓领取",
    "这是一个稳定、纯净的绿色环境包。",
    "由衷感谢bilibili@秋葉aaaki",
    "获取最新版，请关注微信公众号“玄猫AIGC隐研所”发送：安装包"
]

# =================================================================
#                 👆 修改区域结束，下方代码请勿改动 👆
#                 👆 End of modification area, do not change the code below 👆
# =================================================================


# --- 自动打印程序，无需修改 ---
# --- Auto-print program, no modification needed ---
separator = "=" * 70
print(f"\n\n{separator}")
for line in WELCOME_LINES:
    # 在每行文字前都增加一个换行符 \n 来创造宽松的间距
    print(f"\n      {line}")
print("\n" + separator + "\n\n")


# This tells ComfyUI that this custom node does not add any new nodes.
# It's just for running the code above on startup.
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
