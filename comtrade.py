import fromcomtradepkg
import pandas
import os

directory = os.getcwd() + '/data'
subscription_key = '9be8b0a6438a4940bd592c691bb2c4ca'

# function to get all available country-pair export data
def get_all_exports(freq : str, year : list):
    date = year
    if freq == 'M':
        date = f'{year}01,{year}02,{year}03,{year}04,{year}05,{year}06,{year}07,{year}08,{year}09,{year}10,{year}11,{year}12'
    mydf = fromcomtradepkg.getFinalData(subscription_key, typeCode='C', freqCode=freq, clCode='HS', period=date,
                                    reporterCode=None, cmdCode='TOTAL', flowCode='X', partnerCode=None,
                                    partner2Code=None,
                                    customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                    aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
    df = pandas.DataFrame(mydf)
    file_name = f'comtrade_{year}{freq}.csv'
    df.to_csv(os.path.join(directory, file_name), header = True)

# function to get all available total-export data (i.e., partner is world)
def get_total_exports(freq : str, year : list):
    date = year
    if freq == 'M':
        date = f'{year}01,{year}02,{year}03,{year}04,{year}05,{year}06,{year}07,{year}08,{year}09,{year}10,{year}11,{year}12'
    mydf = fromcomtradepkg.getFinalData(subscription_key, typeCode='C', freqCode=freq, clCode='HS', period=date,
                                    reporterCode=None, cmdCode='TOTAL', flowCode='X', partnerCode=0,
                                    partner2Code=None,
                                    customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                    aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
    df = pandas.DataFrame(mydf)
    file_name = f'comtrade_total_{year}{freq}.csv'
    df.to_csv(os.path.join(directory, file_name), header = True)

# putting it all together
def main():
    print("")
    year = input("What year do you want data for? Format: YYYY.\n")
    print("")
    freq = input("What frequency do you want for this data? Type M for monthly, A for annual, or B for both.\n")
    print("")
    print("Processing.... It will take a few minutes.")
    print("")
    if (freq == 'B'):
        get_all_exports('A', year)
        get_all_exports('M', year)
        get_total_exports('A', year)
        get_total_exports('M', year)
    else:
        get_all_exports(freq, year)
        get_total_exports(freq, year)
    print("All done! Check the data folder to see your new files.\n")

if __name__ == "__main__":
    main()
