from aomaker import aomaker
from aomaker.cache import config
from aomaker.log import logger


@aomaker.command("--hello", help="say hello ", default="hello,aomaker", show_default=True)
def hello2(word):
    config.set("word", word)


@aomaker.hook
def say_hello():
    word = config.get("word")
    logger.success(word)
