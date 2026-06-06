import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    cond= df['sex']=='Male'
    average_age_men = round(df.loc[cond,'age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education']=='Bachelors').mean()*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # 1. On définit la population de référence (uniquement les études sup)
    etudes_sup = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # 2. On isole ce groupe dans un sous-tableau propre
    df_sup = df[etudes_sup]

    # 3. On applique la méthode .mean() DIRECTEMENT sur ce sous-tableau
    #resultat = (df_sup['salary'] == '>50K').mean() * 100

    # What percentage of people without advanced education make more than 50K?
    # Le symbole ~ inverse le résultat du .isin()
    cond_pas_etudes_sup = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    # on l'appliques ensuite normalement
    df_autres_etudes = df[cond_pas_etudes_sup]
    # 3. On applique la méthode .mean() DIRECTEMENT sur ce sous-tableau
    #resultat = (df_autres_etudes['salary'] == '>50K').mean() * 100

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = round((df_sup['salary'] == '>50K').mean() * 100,1)
    lower_education_rich = round((df_autres_etudes['salary'] == '>50K').mean() * 100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    cond_min = df['hours-per-week'] == df['hours-per-week'].min()
    num_min_workers = df[cond_min]

    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

    # What country has the highest percentage of people that earn >50K?
    df['is_rich'] = df['salary'] == '>50K'
    pays_pourcentages = df.groupby('native-country')['is_rich'].mean() * 100
    highest_earning_country = pays_pourcentages.idxmax()
    highest_earning_country_percentage = round(pays_pourcentages.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask=(df['native-country']=='India') & (df['salary']=='>50K')
    new_table=df[mask]
    top_IN_occupation = new_table['occupation'].value_counts().idxmax()

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
