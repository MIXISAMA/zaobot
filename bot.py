import nonebot
from nonebot.adapters.onebot.v11 import Adapter
import database
from fastapi.middleware.cors import CORSMiddleware

nonebot.init()
app = nonebot.get_asgi()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

driver = nonebot.get_driver()
driver.register_adapter(Adapter)
driver.on_startup(
    lambda: database.connect(
        driver.config.database_url,
        driver.config.admin_secret,
        driver.config.admin_username,
        driver.config.admin_password,
        app,
    )
)
driver.on_shutdown(database.disconnect)

plugins = [
    'nonebot_plugin_apscheduler',
    
    # 'plugins.schedule',
    'plugins.help',
    'plugins.record',
    'plugins.zao',
    'plugins.fudu',
    'plugins.countdown',
    'plugins.caihongpi',
    'plugins.yesorno',
    'plugins.suoxie',

    'plugins.choyen',
    'plugins.phlogo',
    # 'plugins.wordcloud',

    # 'plugins.olympic',
]

for plugin in plugins:
    nonebot.load_plugin(plugin)

if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")    
    nonebot.run(app="__mp_main__:app")
