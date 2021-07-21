import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago','new york','washington']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ]

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
    
    
    
   
       
    while True:
        city = input('would you choose the city you want to display ? (chicago, new york city, washington)').lower()
        if city in CITIES:
            break
           
        # TO DO: get user input for month (all, january, february, ... , june)
    
        month = input('would you choose the month you want to display ? say \"all\" if you want to display all months data').lower()
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day=input('would you choose the day you want to display ? say \"all\" if you want to display all days data').lower()

    
        print('-'*40)
    return city.lower(), month.lower(), day.lower()


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

        
    df =pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    
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
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mode_month =  df['month'].mode()[0]
    print('most common month is :',mode_month)
    # TO DO: display the most common day of week
    mode_day =  df['day_of_week'].mode()[0]
    print('most common day is :',mode_day)
    # TO DO: display the most common start hour
    mode_hour = df['hour'].mode()[0]
    print('most common hour is :',mode_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_station_start = df['Start Station'].mode()[0]
    print('most commonly used start station is :',mode_station_start)
    # TO DO: display most commonly used end station
    mode_station_end = df['End Station'].mode()[0]
    print('most commonly used end station is :',mode_station_end)
    # TO DO: display most frequent combination of start station and end station trip
    mode_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print(' most commonly used start station and end station : {}, {}'.format(mode_start_end_station[0],mode_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is :", total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("Mean of travel time is :", avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
  
    user_typs = df['User Type'].value_counts()
    print('Counts of user types:',user_typs )
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Counts of user types:',gender )
    else:print("There is no gender information in this city.")

   
    

    # TO DO: Display earliest, most recent, and most common year of birth
  
               
    mode_earliest = df['Birth Year'].min()
    print("The most earliest birth year:", mode_earliest)
    
    
    mode_recent = df['Birth Year'].max()
    print("The most recent birth year:", mode_recent)


    mode_birthy = df['Birth Year'].mode()[0]
    print('most common year of birth is :', mode_birthy)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw bikeshare data."""
    rows = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5
    for i in range(0, rows, 5):
        n=i
        yes = input('\nWould you like to continue? Type \'yes\' or \'no\'\n> ').lower()
        if yes != 'yes':
            break
        
        # retrieve and convert data to json format
        # split each json row data 
        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            # pretty print each user data
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(df.heaser(n))    
    
    
    
    
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
   
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
