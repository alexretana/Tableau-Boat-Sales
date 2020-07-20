#import our lovable pandas module
import pandas as pd


def parseBoatMaker():
    #import data from excel
    df = pd.read_excel('Sold_Boats_Report_07-13-2020_11_37_51.xlsx')

    #parse Boat Model column
    boat_s = df['Boat Model'].str.split(" ")

    #Assign Series from first item in split (mostly boat maker name)
    boat_model_name = boat_s.apply(lambda x: x[0])

    #add this series back in as a column
    df['boat_model_name'] = boat_model_name

    #save this back into the excel
    df.to_excel('Sold_Boats_Report_07-13-2020_11_37_51.xlsx')


if __name__ == '__main__':
    parseBoatMaker()