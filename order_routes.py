from fastapi import APIRouter

order_router = APIRouter(
    prefix='/ord'
)

@order_router.get('/')
async def order():
    return {'message': 'This is a order page.'}