
import pandas as pd


def load_data():
    return pd.read_csv("cleaned_advertisement_dataset.csv")


def calculate_platform_trends(df):
    return df.groupby("platform").agg(
        Average_ROI=("roi", "mean"),
        Average_Engagement=("engagement_rate_percent", "mean"),
        Total_Impressions=("impressions", "sum"),
        Total_Clicks=("clicks", "sum")
    ).reset_index()


def calculate_ad_type_trends(df):
    return df.groupby("ad_type").agg(
        Average_ROI=("roi", "mean"),
        Average_Engagement=("engagement_rate_percent", "mean"),
        Total_Impressions=("impressions", "sum")
    ).reset_index()


if __name__ == "__main__":

    df = load_data()

    print("Advertisement Trend Detection")
    print("--------------------------------")

    print("Number of records:", len(df))
    print("Number of columns:", len(df.columns))

    print("\nPlatform Trends:")
    print(calculate_platform_trends(df))

    print("\nAdvertisement Type Trends:")
    print(calculate_ad_type_trends(df))
