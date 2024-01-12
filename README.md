# Business Data Fetcher

The Business Data Fetcher is a Python tool for asynchronously fetching business data for Czech companies based on their ICO (business identifier). It uses the aiohttp library for asynchronous HTTP requests.

## Prerequisites

Before using this tool, make sure you have Python 3.7 or higher installed.

## Installation

To install the required dependencies, you can use pip:

```bash
pip install -r requirements.txt
```

# Usage
You can use the Business Data Fetcher to retrieve business data for a single ICO or multiple ICOs with concurrent requests.

## Fetching Data for a Single ICO

To fetch business data for a single Czech ICO synchronously, you can use the following code:

```python
Copy code
from business_data_fetcher import fetch_company_data_by_ico

ico = "12345678"  # Replace with the ICO you want to fetch data for
company_data = fetch_company_data_by_ico(ico)
if company_data:
    print(company_data)
else:
    print("Invalid ICO or data retrieval failed.")
```

To fetch business data asynchronously, you can use the following code:

```python
from business_data_fetcher import async_fetch_company_data_by_ico

ico = "12345678"  # Replace with the ICO you want to fetch data for

async def main():
    company_data = await async_fetch_company_data_by_ico(ico)
    if company_data:
        print(company_data)
    else:
        print("Invalid ICO or data retrieval failed.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## Fetching Data for Multiple ICOs
To fetch business data for multiple Czech ICOs with concurrent requests, you can use the following code:

```python
from business_data_fetcher import fetch_companies_data_by_icos

icos = ["12345678", "87654321"]  # Replace with a list of ICOs you want to fetch data for

def main():
    company_data_list = fetch_companies_data_by_icos(icos)
    for i, company_data in enumerate(company_data_list):
        if company_data:
            print(f"Company {i + 1}:")
            print(company_data)
        else:
            print(f"Invalid ICO or data retrieval failed for Company {i + 1}.")

if __name__ == "__main__":
    main()
```

## License
This project is licensed under the MIT License.

```css
This `README.md` provides information on how to install and use your tool for retrieving business data from Czech companies based on their ICO. Users can follow this guide to install the tool and then fetch data for individual ICOs or multiple ICOs concurrently.
```