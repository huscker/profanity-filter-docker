from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator, metrics

DEFAULT_LATENCY_BUCKETS = (
    0.01,
    0.025,
    0.05,
    0.075,
    0.1,
    0.25,
    0.5,
    0.75,
    1.0,
    2.5,
    5.0,
    7.5,
    10.0,
    25.0,
    50.0,
    75.0,
    float("inf"),
)

instrumentator = Instrumentator(
    should_group_status_codes=True,
    should_ignore_untemplated=True,
    should_respect_env_var=False,
    should_instrument_requests_inprogress=True,
    excluded_handlers=["/metrics/"],
    inprogress_name="fastapi_inprogress",
    inprogress_labels=True,
)


instrumentator.add(
    metrics.request_size(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
    )
)

instrumentator.add(
    metrics.response_size(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
    )
)
instrumentator.add(
    metrics.latency(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
        buckets=DEFAULT_LATENCY_BUCKETS,
    )
)
instrumentator.add(
    metrics.requests(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
    )
)


def setup_monitoring(app: FastAPI):
    instrumentator.instrument(app)
    instrumentator.expose(app, include_in_schema=True, should_gzip=True)
