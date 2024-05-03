from aiogram import Dispatcher


from handlers import anketa, start

def include_routers(dp: Dispatcher):
    dp.include_router(
        start.router,
        anketa.router
    )