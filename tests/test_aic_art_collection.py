from aic_art_collection import aic_art_collection
import pandas as pd
import numpy as np
import json
import requests
import pytest

def test_search_artwork():
    # test case 1 
    expected = '1984'
    actual = aic_art_collection.get_search_artwork(expected) 
    assert not actual.empty
    assert isinstance(actual, pd.DataFrame)
    assert aic_art_collection.get_search_artwork(expected).shape==(10, 8)

    # # test case 2 
    col = ['id', 'title', 'artist_display', 'place_of_origin', 'date_start',
       'date_end', 'medium_display', 'category_titles']
    for c in actual.columns:
        if c not in col:
            raise ValueError("Column name not found")
        
    # test case 3: status code
    response = requests.get("https://api.artic.edu/api/v1/artworks/search?fields=id,title,date_start,date_end,artist_display,place_of_origin,medium_display,category_titles")        
    assert response.status_code == 200


def test_museum_tour():

    expected = 'Cezanne Tour'
    actual = aic_art_collection.get_museum_tour(expected)
    assert type(actual) == pd.DataFrame
    assert not actual.empty

    response = aic_art_collection.get_museum_tour('Cezanne Tour')  
    assert len(response)== 10 
    assert type(response) == pd.DataFrame


def test_post_popularity_stat():

    data = {
      "q": "query",
      "limit": 0, 
      "aggs": {
        "years": {
          "terms": {
            "size": 100,
            "field": "fiscal_year"
          }
        }
      }
    }
    aic_response = requests.post("https://api.artic.edu/api/v1/artworks/search", json=data)
    assert aic_response.status_code == 200
    
    aic_water_lilies = aic_response.json()
    assert type(aic_water_lilies) == dict 
    

