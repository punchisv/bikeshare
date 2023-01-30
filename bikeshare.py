import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def city_select():

    city_list = []
    city_list = list(CITY_DATA.keys())

    print("\n\tPlease select the City:")
    print(2*"\t"+"by Entering (1) for Chicago at the Prompt")
    print(2*"\t"+"by Entering (2) for New York City at the Prompt")
    print(2*"\t"+"by Entering (3) for Washington at the Prompt")
    print(2*"\t"+"or by Entering (x)|(X) to EXIT at the Prompt")

    keyboard_input = input("\nPlease make your selection, 1 2 3 or x >>> ")

    if (keyboard_input == '1' or keyboard_input == '2' or  keyboard_input == '3' or  keyboard_input == 'x') or  keyboard_input == 'X':
         if keyboard_input == 'x' or keyboard_input == 'X':
             print("\n******Bye!!! See you later")
             exit()

         else:
             x = int(keyboard_input)
             x -= 1
             for i in range(len(city_list)):
                 if i == x:
                    return(city_list[i])
    else:
        print("\nWrong Entry !")
        exit()


def month_select():

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    print("\n\tPlease select the Month:")
    print(2*"\t"+"by Entering (1) for January at the Prompt")
    print(2*"\t"+"by Entering (2) for February at the Prompt")
    print(2*"\t"+"by Entering (3) for March at the Prompt")
    print(2*"\t"+"by Entering (4) for April at the Prompt")
    print(2*"\t"+"by Entering (5) for May at the Prompt")
    print(2*"\t"+"by Entering (6) for June at the Prompt")
    print(2*"\t"+"by Entering (7) for All at the Prompt")

    keyboard_input = input("\nPlease make your selection, 1 2 3 4 5 6 7 >>> ")
    x = int(keyboard_input)
    x -= 1

    for i in range(len(months)):
        if i == x:
           return(months[i])

    print("\nWrong Entry !\n")
    exit()

def day_select():
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

    print("\n\tPlease select the Day of the week:")
    print(2*"\t"+"by Entering (1) for Sunday at the Prompt")
    print(2*"\t"+"by Entering (2) for Monday at the Prompt")
    print(2*"\t"+"by Entering (3) for Tuesday at the Prompt")
    print(2*"\t"+"by Entering (4) for Wednesday at the Prompt")
    print(2*"\t"+"by Entering (5) for Thursday at the Prompt")
    print(2*"\t"+"by Entering (6) for Friday at the Prompt")
    print(2*"\t"+"by Entering (7) for Saturday at the Prompt")
    print(2*"\t"+"by Entering (8) for All at the Prompt")

    keyboard_input = input("\nPlease make your selection, 1 2 3 4 5 6 7 8 >>> ")
    x = int(keyboard_input)
    x -= 1

    for i in range(len(days)):
        if i == x:
           return(days[i])

    print("\nWrong Entry !\n")
    exit()


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Line 91
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = city_select()

    # get user input for month (all, january, february, ... , june)
    month = month_select()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = day_select()

    print('-'*40)
    print("\n*****Selections: {}, {}, {} ".format(city.title(),month.title(),day.title()))
    input("\nPress Carriage Return(Enter) to Continue >>> ")
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Line 115
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #print(CITY_DATA)
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    #print(df['month'].head(1)
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    print(10*"\n" + "*****Entering time_stats()")
    input("\nPress Carriage Return(Enter) to Continue >>> ")

    """Displays statistics on the most frequent times of travel."""
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    #print(df['month'].value_counts().head(6))
    string = dict(df['month'].value_counts().head(1))
    for key, value in string.items():
        print("\nNumber of Counts for Month of {}, is {}".format(months[key - 1], value))


    # display the most common day of week
    #print(df['day_of_week'].value_counts().head(7))
    string = dict(df['day_of_week'].value_counts().head(1))
    for key, value in string.items():
        print("\nNumber of Counts for a Weekday is for {} and is {}.".format(key, value))


    # display the most common start hour
    df['time_hour'] = df['Start Time'].dt.hour
    ##print(df['time_hour'].value_counts().head(24))
    string = dict(df['time_hour'].value_counts().head(1))
    for key, value in string.items():
        print("\nMost common start hour is {}th and Count is {}.".format(key + 1, value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("\n*****Leaving time_stats()")
    input("\nPress Carriage Return(Enter) to Continue >>> ")


def station_stats(df):
    print(10*"\n" + "*****Entering station_stats()")
    input("\nPress Carriage Return(Enter) to Continue >>> ")

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    #print(df['Start Station'].value_counts().head())
    string = dict(df['Start Station'].value_counts().head(1))
    #print(string)
    for key, value in string.items():
        print("\nMost commonly used \"Start Station\" is \"{}\" with Counts numbering {}.".format(key, value))
    # display most commonly used end station
    #print(df['End Station'].value_counts().head())
    string = dict(df['End Station'].value_counts().head(1))
    for key, value in string.items():
        print("\nMost commonly used \"End Station\" is \"{}\" with Counts numbering {}.".format(key, value))

    # display most frequent combination of start station and end station trip
    # Creating an EXTRA COLUMN called 'start_end_stations' and filled it with '1's.
    df.insert(6, "start_end_stations", '1')
    # By iterating through DataFrame filled that COLUMN with combined 'Start Station' and 'End Station'.
    for i in range(len(df)):
        df['start_end_stations'].values[i] = df['Start Station'].values[i] + ", " + df['End Station'].values[i]
    #print(df['start_end_stations'].value_counts().head())
    string = dict(df['start_end_stations'].value_counts().head(1))
    for key, value in string.items():
        print("\nMost frequent combination of \"Start Station and End Station\" is \"{}\" with a Count of {}.".format(key, value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("\n*****Leaving station_stats()")
    input("\nPress Carriage Return(Enter) to Continue >>> ")


def trip_duration_stats(df):
    print(10*"\n" + "*****Entering trip_duration_stats()")
    input("\nPress Carriage Return(Enter) to Continue >>> ")


    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    #print(df['Trip Duration'].sum())
    print("\nTotal \"Travel Time\", that is, sum() of the COLUMN 'Travel Time' is {} in Seconds.".format(df['Trip Duration'].sum()))

    # display mean travel time
    #print(df['Trip Duration'].mean())
    print("\nMean \"Travel Time\", that is, mean() of the COLUMN 'Travel Time' is {} in Seconds.".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("\n*****Leaving trip_duration_stats()")
    input("\nPress Carriage Return(Enter) to Continue >>> ")


def user_stats(df):
    print(10*"\n" + "*****Entering user_stats()")
    input("\nPress Carriage Return(Enter) to Continue >>> ")

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    #print(df['User Type'].value_counts())
    user_types = dict(df['User Type'].value_counts())
    #print(user_types)
    print("\nUser Types and Counts are:")
    for key,value in user_types.items():
        print(3*"\t" + "{} => {}".format(key, value))
        # Display counts of gender
    if 'Gender' in df.columns:
       #print(df['Gender'].value_counts())
       genders = dict(df['Gender'].value_counts())
       print("\nGender and Counts are:")
       for key,value in genders.items():
           print(2*"\t" + "{} => {}".format(key, value))
    else:
       print("\nNo COLUMN 'Gender'")

    # Display earliest, most recent, and most common year of birth
       #print(int(df['Birth Year'].min()))
    if 'Birth Year' in df.columns:
       print("\nEarliest Year of Birth is {}.".format(int(df['Birth Year'].min())))
       #print(int(df['Birth Year'].max()))
       print("\nMost Recent Year of Birth is {}.".format(int(df['Birth Year'].max())))

       #print(df['Birth Year'].value_counts().head(1))
       max_year = dict(df['Birth Year'].value_counts().head(1))
       #print(max_year)
       for key,value in max_year.items():
           print("\nMost Common Year of Birth is " + "{} with a Count of {}.".format(int(key), value))
    else:
       print("\nNo COLUMN 'Birth Year'")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print("\n*****Leaving user_stats()")
    input("\nPress Carriage Return(Enter) to Continue >>> ")

def data_display(df):
    print(5*"\n" + "*****Entering data_diplay().")
    input("\nPress Carriage Return(Enter) to Continue >>> ")
    ''' Tried to convert 'month' COLUMN from INT() to STR(), df['month'] = df['month'].astype(str), did not work. So, created another
         COLUMN 'month_by_name'. And the need for a copy of df as df_temp '''
    df_temp = df
    column_names = list(df_temp.columns.values)
    #print(column_names)
    for i in range(len(column_names)): ## A sanity check. Because 'washington.csv' has less COLUMNS.
        if column_names[i] == 'month':
           x = i
    df_temp.insert(x + 1, "month_by_name", '1')
    print("\n*****Created a copy of df as df_temp. And inserted a COLUMN named 'month_by_name'")
    print("\n*****Filling 'month_by_name' COLUMN with 'Jan', 'Feb', 'Mar', 'Apr', 'May' and 'Jun'")
    print("\n*****Please be patient. This will take some time. You may press key <Y> few times, so")
    print("*****that there will be few sets of data displayed after this period.")

    for i in range(len(df)):
        if df_temp['month'].values[i] == 1:
           df_temp['month_by_name'].values[i] = 'Jan'
        if df_temp['month'].values[i] == 2:
           df_temp['month_by_name'].values[i] = 'Feb'
        if df_temp['month'].values[i] == 3:
           df_temp['month_by_name'].values[i] = 'Mar'
        if df_temp['month'].values[i] == 4:
           df_temp['month_by_name'].values[i] = 'Apr'
        if df_temp['month'].values[i] == 5:
           df_temp['month_by_name'].values[i] = 'May'
        if df_temp['month'].values[i] == 6:
           df_temp['month_by_name'].values[i] = 'Jun'

    print("\n*****Raw Data from DataFrame will be displayed, 5 rows at a time.\n")
    #print(df_temp.head())
    row=0
    loop = 1
    while loop == 1:
        print()
        print(df_temp.iloc[row:row+5])
        print()
        keyboard_input =(input('\n*****Would you like to loop again for another set? Enter <Y> or <y> for YES or Press CARRIAGE RETURN to exit at the this PROMPT >>> ')).upper()
        if keyboard_input != 'Y':
           loop = 0
        else:
           row += 5

    print("\n*****Leaving data_display()\n")
    input("\nPress Carriage Return(Enter) to Continue >>> ")


###### main() Start ****************************
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        data_display(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
###### main() End ******************************
