
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
# from schemas import SignUpModel
from database import session, engine
from models import User
from schemas import SignUpModel
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT

auth_router = APIRouter(
    prefix='/auth'
)

session = session(bind=engine)


@auth_router.get('/')
async def signup():
    return {'message': 'This is a signup page.'}

@auth_router.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail='User with this email is already exists')

    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail='User with this username is already exists')


    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
         is_active=user.is_active,
        is_staff=user.is_staff

    )

    session.add(new_user)
    session.commit()
    response_model = {
        'id': new_user.id,
        'username': new_user.username,
        'email': new_user.email,
        'is_active': new_user.is_active,
        'is_staff': new_user.is_staff

    }

    return response_model

#
# @auth_router.post('/login', status_code=status.HTTP_200_OK)
# async def login(user:LoginModel, Authorize: AuthJWT=Depends()):
#
#     db_user = session.query(User).filter(User.username == user.username).first()
#
#     if db_user and check_password_hash(db_user.password, user.password):
#         access_token = Authorize.create_access_token(subject=db_user.username)
#         refresh_token = Authorize.create_refresh_token(subject=db_user.username)
#
#         response = {
#             'access': access_token,
#             'refresh': refresh_token
#         }
#
#         return jsonable_encoder(response)
#
#     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid username or password.')
