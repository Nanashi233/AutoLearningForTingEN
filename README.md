# 这是一个自用的项目！

# AutoLearningForTingEN

## 项目简介
- `AutoLearningForTingEN` 是一个基于Python自动化的项目，用于24小时挂机自动完成《每日英语听力》打卡。
- 本项目建议搭配 **远程本地多用户桌面** 使用。

## 环境要求
- Windows环境
- Python 3.8 或更高版本
- 必要的依赖库（请参考下方安装说明）

## 安装&使用
1. 克隆项目到本地
   ```bash
   git clone https://github.com/Nanashi233/AutoLearningForTingEN.git
   ```
2. 进入项目目录
3. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
4. 将 **default.yaml** 复制一份并重命名为 **config.yaml**
5. 按需调整 **config.yaml** ：
    - 如果你在安装时没有使用默认路径，请调整 **TING_EN_APP_PATH**
    - 修改 **WEBHOOK** 与 **SECRET** 来实现钉钉机器人的通知推送（必要，否则无法正常运行）
    - 修改 **RUN_TIME** 以指定程序运行的时间（时间之间用英文逗号隔开，不限定个数，例如 **RUN_TIME: "9,14"** 指每天的9点与14点各执行一次）
6. 运行 **main.py** ：
   ```bash
   python main.py
   ```

## 配置文件说明
- DEBUG_MODE: 开启后会缩短等待时间
- TING_EN_APP_PATH：应用程序的可执行文件路径。
- TING_EN_IMAGE_NAME：应用程序的进程名称。
- WEBHOOK：钉钉机器人的 Webhook 地址。
- SECRET：钉钉机器人的密钥。
- IMAGE_DIR：存放图像资源的文件夹路径。
- RUN_TIME: 程序运行的时间

## 意外情况
- 若无法正常运行，请尝试修改 **IMAGE_DIR** 和 **TING_EN_IMAGE_NAME**
- 若修改后依旧无法正常运行，请按照src文件夹中的图片自行截图并替换