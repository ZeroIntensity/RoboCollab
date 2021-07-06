from .embed import embed
from .color import color
async def error(ctx, body):
    return await embed(ctx, 'Error', body, color=color("light_red"))