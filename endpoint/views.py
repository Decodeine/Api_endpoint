from django.http import JsonResponse
import datetime

from django.views.decorators.http import require_GET

@require_GET
def get_info(request):
    # Get query parameters
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # Validate that both parameters are provided
    if not (slack_name and track):
        return JsonResponse({"error": "Both slack_name and track are required."}, status=400)

    # Get the current day and time in UTC format
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub file URL
    github_file_url = "https://github.com/Gbotemi-ojo/hng-task1-backend/blob/main/app.js"

    # GitHub repo URL
    github_repo_url = "https://github.com/Gbotemi-ojo/hng-task1-backend"

    # Create a response dictionary
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data, status=200)
