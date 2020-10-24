from pyrogram import Client

import config


try:
    import uvloop
except ImportError:
    uvloop = None
else:
    uvloop.install()

if __name__ == '__main__':
    Client(
        session_name='telecharm',
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    ).run()
