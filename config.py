import os

from dotenv import load_dotenv

config = {
    "multi": [
        {
            "account": "...",
            "password": "...",
        },
    ],
    "push": {
        "type": "workWechat",
        "key": {
            "corpSecret": "slF...",
            "corpid": "ww9...",
        },
        "agentid": 1000002,
        "msgtype": "markdown",
    },
}
# 从环境变量中取用户名密码
load_dotenv()
config.get("multi").clear()
config.get("multi").append({"account": os.getenv("USERNAME189"), "password": os.getenv("PASSWORD189")})