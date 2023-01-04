from typing import List

from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.routing import BaseRoute

import logger


# TODO may not be necessary, may remove
# props to https://gaganpreet.in/posts/hyperproductive-apis-fastapi/
def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    logger.debug("Simplify route names.")
    __log_routes(app.routes, "Before:")
    mapped_route_names = set()
    for route in app.routes:
        if isinstance(route, APIRoute):
            if route.name in mapped_route_names:
                raise RuntimeError(f"Duplicate route function name \"{route.name}\" after simplifying.")
            route.operation_id = route.name
            mapped_route_names.add(route.name)
    __log_routes(app.routes, "After:")


def __log_routes(routes: List[BaseRoute], preline: str) -> None:
    logger.debug("%s %s", preline, [r.name for r in routes if isinstance(r, APIRoute)])
