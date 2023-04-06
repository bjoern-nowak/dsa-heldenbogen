import argparse

import uvicorn

from dsaheldenbogen.app import logger
from dsaheldenbogen.app.logger import LogLevel

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
    log_level=args.loglevel.uvicorn,  # uvicorn server log level, not python
)

if __name__ == '__main__':
    logger.init_config(args.loglevel)  # python log level
    server = uvicorn.Server(config)
    server.run()
