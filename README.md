# 这是一个自用的项目，不保证可用！本项目仍在修改中！

# AutoLearningForTingEN

## 项目简介
- `AutoLearningForTingEN` 是一个 Python 项目，用于24小时挂机自动完成《每日英语听力》打卡。
- 该项目使用 pyautogui 进行图像匹配与点击，模仿人类操作。
- 本项目建议搭配 **远程本地多用户桌面** 使用。

## 环境要求
- Windows环境
- Python 3.8 或更高版本
- 必要的依赖库（请参考下方安装说明）

## 项目结构
```
AutoLearningForTingEN\
├── main.py
├── default.yaml
├── requirements.txt
└── modules\
    ├── __init__.py
    ├── app_manager.py
    ├── learner.py
    └── notifier.py
```

## 安装&使用
1. 克隆项目到本地：
   ```bash
   git clone https://github.com/Nanashi233/AutoLearningForTingEN.git
   ```
2. 进入项目目录。
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 将 default.yaml 复制一份并重命名为 config.yaml
5. 按需调整 config.yaml 。
6. 运行 main.py：
   ```bash
   python main.py
   ```

## 配置文件说明
- IMAGE_DIR：存放图像资源的文件夹路径。
- TING_EN_APP_PATH：应用程序的可执行文件路径。
- TING_EN_IMAGE_NAME：应用程序的进程名称。
- WEBHOOK：钉钉机器人的 Webhook 地址。
- SECRET：钉钉机器人的密钥。