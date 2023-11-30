# Api_endpoint
This is a Django API endpoint that provides information based on the provided query parameters.
It returns data such as:
The current day and time in UTC format
The provided Slack name
The specified track and relevant GitHub URLs

Usage
Endpoint URL: /get_info/

HTTP Method: GET

Request Parameters
slack_name (required): The Slack name for which information is requested.
track (required): The specified track for which information is requested.

Example
GET /get_info/?slack_name=johndoe&track=web-development

Response
{
  "slack_name": "johndoe",
  "current_day": "Monday",
  "utc_time": "2023-11-08T12:00:00Z",
  "track": "web-development",
  "github_file_url": "https://github.com/Decodeine/Api_endpoint/blob/master/endpoint/views.py",
  "github_repo_url": "https://github.com/Decodeine/Api_endpoint/tree/master/endpoint",
  "status_code": 200
}

Error Response
{
  "error": "Both slack_name and track are required.",
  "status_code": 400
}


