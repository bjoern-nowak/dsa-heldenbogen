import uvicorn

config: uvicorn.Config = uvicorn.Config(
    'api.root:app',  # <file_path>:<variable>
    reload=True,  # automatically load changed py-files
    log_level='debug',  # values: critical, error, warning, info, debug, trace
)

if __name__ == '__main__':
    server = uvicorn.Server(config)
    server.run()
