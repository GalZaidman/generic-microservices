from aiohttp import web


async def create_user():
    return web.Response(text='User create')