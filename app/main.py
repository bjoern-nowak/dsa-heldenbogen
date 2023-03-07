import argparse

import uvicorn

from app import logger
from app.logger import LogLevel

argParser = argparse.ArgumentParser()
argParser.add_argument("--workers", type=int, default=1, help="Count of worker processes")
argParser.add_argument("--reload", action='store_true', help="Reload changed resources at runtime")
argParser.add_argument("--loglevel",
                       type=LogLevel.argparse,
                       default=LogLevel.INFO,
                       choices=list(LogLevel),
                       help="Define lowest level to log"
                       )
args = argParser.parse_args()

config: uvicorn.Config = uvicorn.Config(
    'api.root:app',  # <file_path>:<variable>
    workers=args.workers,
    reload=args.reload,  # automatically load changed py-files
    log_level=args.loglevel.uvicorn,
)

if __name__ == '__main__':
    logger.init_config(args.loglevel)
    server = uvicorn.Server(config)
    server.run()
