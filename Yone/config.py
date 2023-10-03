
import json
import os


def get_user_list(config, key):
    with open("{}/Yone/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True

    API_ID = "12227067"
    API_HASH = "b463bedd791aa733ae2297e6520302fe"
    TOKEN = "5207268348:AAEZfXfXMQpdFVLYyal04_iSQcVuJh4W1l8"
    OWNER_ID = "2105971379"
    OWNER_USERNAME = "sultan11100"
    SUPPORT_CHAT = "Yone_Support"
    JOIN_LOGGER = "-1001841879487"
    EVENT_LOGS = "-1001908711819"
    BOT_USERNAME = "YoneTg_Robot"
    BOT_NAME = "Yone 2.0 "
    # 
    # DATABASE_URL = "postgres://ixweewbx:9OoB_feF6d6wK1W4YycgwHzRHQXezsNA@arjuna.db.elephantsql.com/ixweewbx"  # sql
    DATABASE_URL = "postgres://yxjakrab:SmHBUYHKeIt8ikRr0tEEXM1p51E7Lq-U@jelani.db.elephantsql.com/yxjakrab"  # sql
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    REDIS_URL = "redis://default:6wNSFvZpFp7gwxebagkWV5TGkqtE0pCs@redis-10055.c14.us-east-1-2.ec2.cloud.redislabs.com:10055"

    INSPECTOR = get_user_list("elevated_users.json", "ins")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    REQUESTER = get_user_list("elevated_users.json", "req")

    CERT_PATH = None
    STRICT_GBAN = True
    PORT = "8080"
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 20
    ALLOW_EXCL = True
    ALLOW_CHATS = True
    PHOTO = "https://graph.org/file/324a12454d23b5d78dd48.jpg" # Miss Poppy Music Pic
    INFOPIC = True


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
