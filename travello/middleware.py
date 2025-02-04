from django.shortcuts import redirect
from .models import VisitorTracking, Destination
from django.utils.deprecation import MiddlewareMixin

def get_client_ip(request):
    """Extract client IP address from request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class DestinationLimitMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        """Restrict non-logged-in users to only 2 destination views using IP tracking."""
        if request.user.is_authenticated:
            return None  # Allow logged-in users full access

        destination_id = view_kwargs.get('id')
        if not destination_id:
            return None  # Only enforce limit on destination views

        ip = get_client_ip(request)
        visitor, created = VisitorTracking.objects.get_or_create(ip_address=ip)
        visitor.save()

        # If already visited 2 destinations, redirect to login
        if visitor.visited_destinations.count() >= 2 and not request.user.is_authenticated:
            return redirect('login')

        # If the destination is not already visited, add it
        destination = Destination.objects.get(id=destination_id)
        visitor.visited_destinations.add(destination)

        return None
