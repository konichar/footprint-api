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

    app.process_formation()["worker"].scale(1)


# app.delete()
# config = app.config()
# onfig['New_var'] = 'new_val'
# newconfig = config.update({u'TEST1': u'A1', u'TEST2': u'A2', u'TEST3': u'A3'})
# proclist = app.process_formation()
#  app.process_formation()['web'].scale(0)
# logdrainlist = app.logdrains()
# accepts the same params as above - lines|dyno|source|timeout (passed to requests)
# log = heroku_conn.stream_app_log(<app_id_or_name>, lines=1, timeout=100)
# #or
# for line in app.stream_log(lines=1):
#      print(line)
# builds
# app.create_build('https://github.com/konichar/parsesig/tarball/master')
