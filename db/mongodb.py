import motor.motor_asyncio

from models.user import User


async def init_mongodb():
    MOTOR_CLIENT = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
    DATABASE = MOTOR_CLIENT.temp
    await init_beanie(
        database=DATABASE,
        document_models=[
            User,
        ],
    )
