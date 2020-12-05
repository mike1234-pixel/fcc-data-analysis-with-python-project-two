import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. ✓
    race_count = df.race.value_counts()

    # What is the average age of men? ✓
    average_age_both_sexes = df.groupby('sex').age.mean()
    average_age_men = round(average_age_both_sexes.Male, 1)

    # What is the percentage of people who have a Bachelor's degree? ✓
    raw_percentage_bachelors = df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100
    # rounded to 1 dcp
    percentage_bachelors = round(raw_percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K? ✓
    # What percentage of people without advanced education make more than 50K? ✓

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # select all entries in data where education is Bachelors, Masters and Doctorate (creates new dataframe)
    # select all entries in data where education is not Bachelors, Masters or Doctorate (creates new dataframe)
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    # from dataframe higher_education select those entries where 'salary' is '>50K'
    # df.shape[0] is the total number of entries in the df
    # select those in df where salary is >50K, count the total, divide it by the total number of entries and * 100 to get the percentage, round it to 1 dcp

    higher_education_rich = round(higher_education[higher_education['salary'] == '>50K']['salary'].count() / higher_education.shape[0] * 100, 1)

    lower_education_rich = round(lower_education[lower_education['salary'] == '>50K']['salary'].count() / lower_education.shape[0] * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)? ✓
    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K? ✓
    rich_percentage = round(num_min_workers[num_min_workers['salary'] == '>50K']['salary'].count() / num_min_workers.shape[0] * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    # filter df by data where salary >50K, split the data by native-country and count the values, turn it to a percentage, sort the values and select the id with the highest with using idmax()

    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts()/ df['native-country'].value_counts() * 100).idxmax()
    
   # highest_earning_country_percentage = (highest_earning_country / df.groupby('native-country')['native-country'].count()).max()
   # filter by salary >50k 
    highest_earning_country_percentage = round((df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')]['salary'].value_counts() / (df[(df['native-country'] == highest_earning_country)]['salary']).shape[0] * 100), 1)['>50K']

    # Identify the most popular occupation for those who earn >50K in India.
    # filter by salary >= '50K' then do a value count
    # groupby country then salary then value count then max value
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
