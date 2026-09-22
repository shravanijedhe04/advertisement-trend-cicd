
from analysis import load_data
from analysis import calculate_platform_trends
from analysis import calculate_ad_type_trends


def test_dataset_loads():

    df = load_data()

    assert len(df) > 0
    assert len(df.columns) > 0


def test_required_columns():

    df = load_data()

    required_columns = [
        "platform",
        "ad_type",
        "impressions",
        "clicks",
        "roi",
        "engagement_rate_percent"
    ]

    for column in required_columns:
        assert column in df.columns


def test_platform_analysis():

    df = load_data()

    result = calculate_platform_trends(df)

    assert len(result) > 0


def test_ad_type_analysis():

    df = load_data()

    result = calculate_ad_type_trends(df)

    assert len(result) > 0
