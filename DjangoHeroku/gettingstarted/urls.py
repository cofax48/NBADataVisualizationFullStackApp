from django.conf.urls import include, url
from django.urls import path

import hello.views

#My Url PAtterns
urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    #apis
    url(r'^all_column_names', hello.views.all_column_names, name='all_column_names'),
    url(r'^category_over_player_career', hello.views.category_over_player_career, name='category_over_player_career'),
    url(r'^category_over_team_existence', hello.views.category_over_team_existence, name='category_over_team_existence'),
    url(r'^top_20_players_in_category_for_year', hello.views.top_20_players_in_category_for_year, name='top_20_players_in_category_for_year'),
    url(r'^get_individual_column', hello.views.get_individual_column, name='get_individual_column'),
    url(r'^one_paramter_query', hello.views.one_paramter_query, name='one_paramter_query'),
    url(r'^two_parameter_query', hello.views.two_parameter_query, name='two_parameter_query'),
    url(r'^three_parameter_query', hello.views.three_parameter_query, name='three_parameter_query'),

]
