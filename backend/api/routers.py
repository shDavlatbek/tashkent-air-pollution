# You can import routers from files like this
from api.users import router as router_users
from api.auth import router as router_auth
from api.station import router as router_station

all_routers = [
    router_users,
    router_auth,
    router_station
]
