from django.urls import path
from .views import enrollment_rate_per_country, graduation_rate_per_country, enrollment_vs_graduation_analysis, gender_gap_vs_enrollment, gender_gap_analysis, average_enrollment_country_per_field,average_graduation_country_per_field,enrollment_per_country_field,graduation_per_country_field, fields_per_country_percent    
urlpatterns = [
    path(
        'enrollment_rate_per_country/',
        enrollment_rate_per_country
    ),

    path(
        'graduation_rate_per_country/',
        graduation_rate_per_country
    ),

    path(
        'enrollment_vs_graduation_analysis/',
        enrollment_vs_graduation_analysis
    ),
    path(
        'gender_gap_vs_enrollment/',
        gender_gap_vs_enrollment
    ),

    path(
        'gender_gap_analysis/',
        gender_gap_analysis
    ),

    path('average_enrollment_country_per_field/',
         average_enrollment_country_per_field
    ),

    path('average_graduation_country_per_field/',
         average_graduation_country_per_field
         ),

    path('enrollment_per_country_field/',
         enrollment_per_country_field
         ),

    path('graduation_per_country_field/',
         graduation_per_country_field
        ),

    path(
        'fields_per_country_percent/',
        fields_per_country_percent
    ),
 
]

