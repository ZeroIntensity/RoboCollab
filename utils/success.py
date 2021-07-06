from .embed import embed
from .color import color
async def success(ctx, body):
    return await embed(ctx, 'Success', body, color=color("mint"))