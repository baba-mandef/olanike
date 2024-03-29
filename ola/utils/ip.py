def get_ip(request):
    x_forwaded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwaded_for:
        ip = x_forwaded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
