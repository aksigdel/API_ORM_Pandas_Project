# 7. Find whether there are more  male/female patients .
# takes dataframe as argument  and return  a new dataframe with counts
def group_by_gender(df):
    count_df = df.groupby('patient_gender').count(
    ).sort_values(by='patient_id', ascending=False)
    count_df = count_df[['patient_id']]
    return count_df.rename(columns={'patient_id': 'count'}).reset_index()


# 8. List patient born after (1985)


def after_1985(df):
    df.query('patient_dob> 1985')
    # create new df with only patient_name and patient_dob
    return df[['patient_name', 'patient_dob']]