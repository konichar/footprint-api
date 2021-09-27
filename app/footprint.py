from decouple import config
import heroku3
import uuid

HEROKU_API_KEY = config("HEROKU_API_KEY")
heroku_conn = heroku3.from_key(HEROKU_API_KEY)


def footprint_walt():
    appy = heroku_conn.create_app(name=f"footprint-{uuid.uuid4().hex[:8]}")
    appy.create_build(f'{config("GIT_URL")}/tarball/master')
    appy.config().update(
        {
            f"API_HASH": f'{config("API_HASH")}',
            f"API_ID": f'{config("API_ID")}',
            f"CHATINPUT": f'{config("CHATINPUT")}',
            f"CHATOUTPUT": f'{config("CHATOUTPUT")}',
            f"REDISTOGO_URL": f'{config("REDISTOGO_URL")}',
            f"SESSION": f'{config("SESSION")}',
            f"HEROKU_API_KEY": f'{config("HEROKU_API_KEY")}',
        }
    )
    app = heroku_conn.apps()[appy.name]
    # time.sleep(5)
    app.process_formation()["worker"].scale(1)
