from loader import tm


@tm.forever(sleep_time=10)
async def _():
    tm.logger.info('Working hard!')
