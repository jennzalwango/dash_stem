from django.shortcuts import render
from .dataCleaning import df
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def enrollment_rate_per_country(request):
    cols_used = ['Country', 'Female Enrollment (%)']
    enroll_rate_per_country = df[cols_used].groupby('Country')['Female Enrollment (%)'].mean().reset_index()

    return Response(
        enroll_rate_per_country.to_dict(orient='records')
    )

@api_view(['GET'])
def graduation_rate_per_country(request):
    #use graduation and country columns
    data_columns = ['Country', 'Female Graduation Rate (%)']
    #assign the colmn to hold new values
    grad_rate_per_country = df[data_columns].groupby('Country')['Female Graduation Rate (%)'].mean().reset_index()
    return Response(
        grad_rate_per_country.to_dict(orient='records')
    )


#get the rate of enrollment vs gradutaion per country per year
@api_view(['GET'])
def enrollment_vs_graduation_analysis(request):
    #uses the country, year enrollment and graudtaion columns
    columns_ratio = ['Country', 'Year', 'Female Enrollment (%)', 'Female Graduation Rate (%)']

    #create new df object to have the filtered columns
    new_filtered_cols = df[columns_ratio].copy()

    #group country and year
    country_year_avg = new_filtered_cols.groupby([
        'Country', 'Year'])[[
            'Female Enrollment (%)',
            'Female Graduation Rate (%)']
    ].mean().reset_index()

    #rename cols for better reading
    country_year_avg = country_year_avg.rename(columns={
        'Female Enrollment (%)': 'enrollmentRate',
        'Female Graduation Rate (%)': 'graduationRate'
    })
    
    return Response(
        country_year_avg.to_dict(orient='records')
    )


#countries thier with gender gap Index vs enrollment
@api_view(['GET'])
def gender_gap_vs_enrollment(request):
    columns = ['Country', 'Gender Gap Index', 'Female Enrollment (%)']
    
    #create copy of the df
    country_avg = df[columns].copy().groupby('Country')[
        ['Gender Gap Index', 'Female Enrollment (%)']
    ].mean().reset_index()

    #rename colmuns on copy 
    country_avg = country_avg.rename(columns={
        'Female Enrollment (%)': 'enrollmentRate',
    })

    return Response(country_avg.to_dict(orient='records'))


#gender gap Index per country per field.
@api_view(['GET'])
def gender_gap_analysis(request):
    columns = ['Country', 'STEM Fields', 'Gender Gap Index']
    filtered_cols = df[columns].copy()

    # the gender gap Index per country
    gap_index_per_country = filtered_cols.groupby('Country')['Gender Gap Index'].mean().reset_index()
    gap_index_per_country = gap_index_per_country.rename(columns={'Gender Gap Index': 'avgIndexPerCountry'})

    # the gender gap Index per STEM field
    gap_index_per_field = filtered_cols.groupby('STEM Fields')['Gender Gap Index'].mean().reset_index()
    gap_index_per_field = gap_index_per_field.rename(columns={'Gender Gap Index': 'avgIndexPerField'})

    #get the gender gap Index per country per STEM field (drill down)
    gap_per_country_field = filtered_cols.groupby(['Country', 'STEM Fields']).mean().reset_index()

    gap_per_country_field = gap_per_country_field.rename(columns={'Gender Gap Index':'avgIndexPerCountryField'})

    return Response({
        'gap_index_per_country': gap_index_per_country.to_dict(orient='records'),
        'gap_index_per_field': gap_index_per_field.to_dict(orient='records'),
        'gap_per_country_field':gap_per_country_field.to_dict(orient='records')
    })


#Statistical summary: Enrollement and Graduation Averages 
#calculate the average enrollements per country in each STEM Field.
@api_view(['GET'])
def average_enrollment_country_per_field(request):
    enrollment_avg_data = df.groupby(
        ['Country', 'STEM Fields']
    )['Female Enrollment (%)'].mean().reset_index()

    return Response(
        enrollment_avg_data.to_dict(orient='records')
    )


#calculate the average gradutaion per country in each STEM Field
@api_view(['GET'])
def average_graduation_country_per_field(request):
    graduation_avg_data = df.groupby(
        ['Country', 'STEM Fields']
    )['Female Graduation Rate (%)'].mean().reset_index()

    #print('This is the average garduation per Country In each STEM field:\n', graduation_avg_data)
    return Response(
        graduation_avg_data.to_dict(orient='records')
    )


#comparative analysis
@api_view(['GET'])
def enrollment_per_country_field(request):
    compared_enrollment_data = (
        df.pivot_table(
        values='Female Enrollment (%)',
        index='Country',
        columns='STEM Fields',
        aggfunc='sum'
    ).reset_index()
    )

    return Response(
        compared_enrollment_data.to_dict(orient='records')
    )

@api_view(['GET'])
def graduation_per_country_field(request):
    compared_graduation_data = (
        df.pivot_table(
        values='Female Graduation Rate (%)',
        index='Country',
        columns='STEM Fields',
        aggfunc='sum'
    ).reset_index()
    )

    return Response(
        compared_graduation_data.to_dict(orient='records')
    )


# STEM Field representation performance per country
@api_view(['GET'])
def fields_per_country_percent(request):

    field_counts = (
        df.groupby( ['Country', 'STEM Fields']).size().reset_index(name='Count')  
    )

    field_counts['Percentage']=(
        field_counts.groupby('Country')['Count']
                    .transform(lambda x: 100 * x / x.sum())
    )
    #print('These are the percentages of each STEM Field in each country:\n', field_counts)
    return Response(
        field_counts.to_dict(orient='records')
        )




