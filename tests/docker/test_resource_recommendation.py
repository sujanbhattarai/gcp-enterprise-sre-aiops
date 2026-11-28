from resource_recommendation import generate_recommendations


def make_report(
    cpu="HEALTHY",
    memory="HEALTHY",
    oom=False,
    running=True,
    exit_code=0,
    overall="HEALTHY"
):
    return {
        "container_state": {
            "oom_killed": oom,
            "running": running,
            "exit_code": exit_code
        },
        "cpu_throttling": {
            "status": cpu
        },
        "memory_status": memory,
        "overall_status": overall
    }


def test_critical_cpu():
    report = make_report(cpu="CRITICAL")
    results = generate_recommendations(report)

    assert results[0]["resource"] == "CPU"
    assert results[0]["severity"] == "CRITICAL"


def test_warning_cpu():
    report = make_report(cpu="WARNING")
    results = generate_recommendations(report)

    assert results[0]["severity"] == "WARNING"


def test_critical_memory():
    report = make_report(memory="CRITICAL")
    results = generate_recommendations(report)

    assert results[0]["resource"] == "Memory"
    assert results[0]["severity"] == "CRITICAL"


def test_warning_memory():
    report = make_report(memory="WARNING")
    results = generate_recommendations(report)

    assert results[0]["severity"] == "WARNING"


def test_oom_failure():
    report = make_report(
        oom=True,
        running=False,
        exit_code=137
    )

    results = generate_recommendations(report)

    assert results[0]["finding"] == "Container OOMKilled"
    assert results[0]["severity"] == "CRITICAL"


def test_application_failure():
    report = make_report(
        running=False,
        exit_code=1
    )

    results = generate_recommendations(report)

    assert results[0]["resource"] == "Application"


def test_multiple_bottlenecks():
    report = make_report(
        cpu="CRITICAL",
        memory="WARNING"
    )

    results = generate_recommendations(report)

    assert len(results) == 2


def test_healthy_container():
    report = make_report()
    results = generate_recommendations(report)

    assert results[0]["severity"] == "HEALTHY"


def test_unknown_cpu_metrics():
    report = make_report(cpu="UNKNOWN")
    results = generate_recommendations(report)

    assert results[0]["severity"] == "UNKNOWN"
