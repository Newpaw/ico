#import asyncio

from .app import validation_ico, fetch_company_data_by_ico, fetch_companies_data_by_icos


## Example usage

def main():
    ## Synchronous fetch for a single ICO
    #ico = "48038725"
#
    #print(validation_ico(ico))
    #company = fetch_company_data_by_ico(ico)
    #if company:
    #    print(company.obchodniJmeno)  # Or any other way to display the company data
#
    ## Asynchronous fetch for a list of ICOs
    #icos = ["48038725", "25021796", "61860069"]
    #companies = asyncio.run(fetch_companies_data_by_icos(icos))
    #for company in companies:
    #    if company:
    #        print(company.obchodniJmeno)  # Or any other way to display the company data
    pass

if __name__=="__main__":
    main()