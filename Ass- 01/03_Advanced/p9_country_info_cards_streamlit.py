import streamlit as st
import requests

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        country_data = data[0]
        name = country_data["name"]["common"]

        capital = country_data.get("capital", ["N/A"])[0]
        population = country_data.get("population", "N/A")
        area = country_data.get("area", "N/A")
        currencies = country_data.get("currencies", {})     

        currency_names = ', '.join([currency_info["name"] for currency_info in currencies.values()]) or "N/A"
        region = country_data.get("region", "N/A")

        return name, capital, population, area, currency_names, region
    else:
        return None

def main():
    st.title("Country Information App")

    country_name = st.text_input("Enter a country name:")

    if country_name:
        country_info = fetch_country_data(country_name)
        if country_info:
            name, capital, population, area, currency, region = country_info
            
            st.subheader(f"Information about {name}:")
            st.write(f"Capital: {capital}")
            st.write(f"Population: {population}")
            st.write(f"Area: {area} km²")
            st.write(f"Currency: {currency}")
            st.write(f"Region: {region}")
        else:
            st.error("Country not found. Please check the name and try again.")

if __name__ == "__main__":
    main()