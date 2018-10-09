from .Setup import *

@pytest.mark.usefixtures("driver_get")
class BaseTest:
    pass
