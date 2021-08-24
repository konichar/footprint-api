from datetime import timedelta
# from starlette.middleware.sessions import SessionMiddleware
import uvicorn
from settings import Settings
import fastapi
from fastapi import FastAPI, Request
from app.app import  generalAuth as CreateApp
# from router import router as Router

# from db_utils.database import connect_db, disconnect_db 


__all__ = ["app"]


app = FastAPI(
    version="0.0.1",
    debug=Settings.DEBUG,
    title=Settings.PROJECT_NAME,
    docs_url="/",
    redoc_url="/redoc/",
    servers=[
        {"url": Settings.PROD_SERVER_URL, "description": "Production server"},
        {"url": "http://127.0.0.1:8000/", "description": "Local Development Server"},
    ],
    description="The Foot print API",
    default_response_class=fastapi.responses.ORJSONResponse,
    # on_startup=[connect_db],
    # on_shutdown=[disconnect_db],
    
    # swagger_ui_init_oauth={
    #     "clientId": Settings.CLIENT_ID,
    #     "clientSecret": Settings.CLIENT_SECRET
    # }
)


# app.add_middleware(SessionMiddleware, secret_key=Settings.SECRET_KEY)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )


# app.include_router(Router, tags=["Deploy"], prefix="/deploy")


@app.get("/entry")
async def entry(request: Request):
    
    return {"answer": 'this is the answer'}

@app.get("/auth")
def auth(session:str, forwarder:str, reciever:str):
    config_vars = dict()
    config_vars['SESSION'] = session
    config_vars['FORWARDER'] = forwarder
    config_vars['RECIEVER'] =  reciever
    return CreateApp(data=config_vars)

if __name__ == "__main__":
    uvicorn.run(
        app,
        debug=Settings.DEBUG,
        host=Settings.HOST,
        port=Settings.PORT,
        reload=Settings.RELOAD,
        use_colors=Settings.COLOR_LOGS,
        log_level=Settings.LOGGER_LEVEL,
        # proxy_headers=True,
    )
