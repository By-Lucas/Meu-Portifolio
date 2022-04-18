from decouple import config

API_PIX_PRODUCTION_MODE = config('API_PIX_PRODUCTION_MODE', default=False, cast=bool)
API_PIX_URL_BASE = config('API_PIX_URL_BASE')

API_PIX_CLIENT_ID = config('API_PIX_CLIENT_ID')
API_PIX_CLIENT_SECRET = config('API_PIX_CLIENT_SECRET')
API_PIX_PRIVATE_TOKEN = config('API_PIX_PRIVATE_TOKEN')
API_PIX_KEY = config('API_PIX_KEY')
API_PIX_WEBHOOK_SECRET = config('API_PIX_WEBHOOK_SECRET')
