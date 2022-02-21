import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    months = ["january", "february", "march", "april", "mai", "june"]
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    answers = ["yes", "no"]
    choices = ["month", "day", "both"]
    city = filter_answer = filter_choice = ""
    month = day = "all"
    while city not in cities:
        city = input("Please provide a city(chicago, new york city, washington): ").lower()
    print("\nThanks for choosing {}, if this is not correct please restart!".format(city))
    
    while filter_answer not in answers:
        filter_answer = input("Do you want to apply any filter? (yes/no): ").lower()
    if filter_answer == "yes":
        while filter_choice not in choices:
            filter_choice = input("Please set which kind of filter you need. (month, day, both): ").lower()

            if filter_choice == "both":
                # TO DO: get user input for month (all, january, february, ... , june)
                while month not in months:
                    month = input("Please provide a month (january, february, ... , june): ").lower()

                # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                while day not in days:
                    day = input("Please provide a day of week (monday, tuesday, ... sunday): ").lower()

            if filter_choice == "month":
                while month not in months:
                    month = input("Please provide a month (january, february, ... , june): ").lower()

            if filter_choice == "day":
                while day not in days:
                    day = input("Please provide a day of week (monday, tuesday, ... sunday): ").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #df['day_of_week'] = df['Start Time'].dt.weekday_name 

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index ( month ) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print ( '\nCalculating The Most Frequent Times of Travel...\n' )
    start_time = time.time()

    df['Start Time'] = pd.to_datetime (df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print ('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].mode()[0]
    print ('Most Popular Day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print ('Most Popular Start Hour:', popular_hour)
    
    print ('\nFinished Calculating Frequen Travel Times Statistics.\n')
    print ("\nThis took %s seconds." % (time.time() - start_time))
    print ('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print ( '\nCalculating the most popular stations and trip...\n' )
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts()
    print("The most popular Start Station is: ",start_station.index[0])

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts()
    print ("The most popular End Station: ", end_station.index[0])

    # TO DO: display most frequent combination of start station and end station trip
    most_common_station = df.groupby(['Start Station'])['End Station'].value_counts()
    print ("The most popular combination between start and end station is: ", most_common_station.index[0])
    print ('\nFinished calculating the most popular stations and trip.\n')
    print ("\nThis took %s seconds." % (time.time() - start_time))
    
    print ('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print ('\nCalculating Trip Duration Statistics...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ('Total travel time in s: ', total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print ('Mean travel time in s: ', mean_travel_time)

    print ('\nFinished Calculating Trip Duration Statistics.\n')
    print ("\nThis took %s seconds." % (time.time() - start_time))
    
    print ('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print ('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print("Display counts of user types:\n", count_user_type)
    
    # TO DO: Display counts of gender
    # In some Data files columns are not available, checking to avoid error (I could use this method in every function)
    if 'Gender' in df:
        count_gender = df['Gender'].value_counts()
        print("\nDisplay counts of gender:\n", count_gender)
    else:
        print("\n'Gender Data not found' skipping this...:")

    # TO DO: Display earliest, most recent, and most common year of birth
    # In some Data files columns are not available, checking to avoid error (I could use this method in every function)
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].value_counts()
        print("\nEarliest year of birth: ", earliest_birth)  
        print("Most recent year of birth: ", most_recent_birth)   
        print("Most common year of birth:", most_common_birth.index[0])
    else:
        print("\n'Birth Year Data not found' skipping this...:")
        
    print ('\nFinished Calculating Bikeshare Users Statistics.\n')
    print ("\nThis took %s seconds." % (time.time() - start_time))
    print ('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data (city, month, day)
        answer = ["yes", "no"]
        raw_data_answer = ""
        i=0
        k=5

        while k < len(df):
            raw_data_answer = input ("Please write 'yes' if you want to have a look at additional raw data, otherwise press enter                                        to continue: ".lower())
            if raw_data_answer == 'yes':
                print (df.iloc[i:k])
                i += 5
                k += 5
            else:
                break
                
        time_stats(df)
        input("Press Enter if you want to continue")
        station_stats(df)
        input("Press Enter if you want to continue")
        trip_duration_stats(df)
        input("Press Enter if you want to continue")
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
