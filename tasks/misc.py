import config
from loader import tm


@tm.forever(sleep_time=config.DEFAULT_TASK_SLEEP)
async def _():
    tm.logger.info('Working hard!')
