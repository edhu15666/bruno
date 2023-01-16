
# Zenvia app (Zapp)

Simple application that export prometheus metrics

## Endpoints

Endpoints are exposed on port `5000` by default

|Verb|URL|Description|
|-|-|-|
|GET|/status|basic healthcheck|
|GET|/tasks|list of tasks|
|GET|/failone|5xx endpoint|
|GET|/failtwo|4xx endpoint|
|GET|/failthree|Exception endpoint|
|GET|/metrics| prometheus metrics|

## Exported Prometheus Metrics


|Metric|Type|Description|
|-|-|-|
|flask_http_request_exceptions_total|COUNTER|Total number of HTTP requests which resulted in an exception|
|flask_http_request_total|COUNTER|Total number of HTTP requests|
|flask_http_request_duration_seconds|HISTOGRAM|Flask HTTP request duration in seconds|
|process_resident_memory_bytes|GAUGE|Resident memory size in bytes|
|process_cpu_seconds_total|COUNTER|Total user and system CPU time spent in seconds|

## How to run

```
$ pip install -r requirements.txt
$ python app.py
```
