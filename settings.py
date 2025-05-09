pip install dj-database-url
 import dj-database-url
 import os
DATABASES = {
  "default": dj_database_url.parse(os.environ.get("postgresql://test_db_7ex5_user:R1hb0ijjhIeXTK37ph6beJOoYIjtsjwS@dpg-d0epgos9c44c738a9ovg-a.oregon-postgres.render.com/test_db_7ex5"))
}
