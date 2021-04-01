import logging.config


# 从字典获取配置信息
config = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)5s[%(process)6d|%(thread)6d](%(filename)s:%(lineno)d)  %(message)s',
        },
        # 其他的 formatter
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logging.log',
            'when':'D', # 单位 S:秒 M：分 H：小时 D：天
            'interval':1, # 时间间隔
            'backupCount': 5, # 保留最近X份的日志
            'encoding':'utf-8',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        # 其他的 handler
    },
    'loggers':{
        'StreamLogger': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'FileLogger': {
            # 既有 console Handler，还有 file Handler
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        # 其他的 Logger
    }
}

logging.config.dictConfig(config)
StreamLogger = logging.getLogger("StreamLogger")
FileLogger = logging.getLogger("FileLogger")
# 省略日志输出
