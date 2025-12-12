from .public import urlpatterns as public_patterns
from .manage import urlpatterns as manage_patterns

urlpatterns = public_patterns + manage_patterns
