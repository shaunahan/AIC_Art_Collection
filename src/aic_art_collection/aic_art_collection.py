import os
import pandas as pd
import numpy as np
import json
import requests
from ivpy import attach,show
import altair as alt
from PIL import Image
from io import BytesIO
from IPython.display import display, HTML

'''
This python package retrives information about collections at the Art Institute of Chicago. 
A user can query any keyword, whether it be the name of an artist, an artwork or an art category. 
This package will generate queried inforamtion along with related information for the artwork, such as: 
the date of the artwork, the place of origin, materials used, and the descriptions of the artwork.
'''

def get_search_artwork(artwork):
    '''
    Retrieve the information about collections in the Art Institute of Chicago
    
    Parameters:
    -------------
    artwork: Write any key word to query. It can be the name of an artist, an artwork, the place where an artwork was created, date, or the type of the work.
    
    Returns:
    -------------
    Status code: str
        Status code is issued by a server in response to a client's request made to the server.
        
    Dataframe: df
        Includes the detailed information about artworks that were queried.
        
    Example: 
    -------------
    >>> get_search_artwork('1984')
        200 OK success response code. The request has succeeded. 
            id  ...                                    category_titles
        0  189594  ...                              [Prints and Drawings]
        1  121115  ...            [Photography and Media, Latin American]
        2  103026  ...                          [Architecture and Design]
        3  102229  ...  [Contemporary Art, Chicago Artists, SAIC Alumn...
        4  185062  ...                            [Photography and Media]
        5  151231  ...                              [Prints and Drawings]
        6   76934  ...                            [Photography and Media]
        7  187165  ...      [Contemporary Art, Essentials, Women artists]
        8  131385  ...   [Prints and Drawings, Essentials, Women artists]
        9  212224  ...                            [Photography and Media]
        [10 rows x 7 columns]
    '''
    params_search = {'q': artwork} 
    r = requests.get("https://api.artic.edu/api/v1/artworks/search?fields=id,title,date_start,date_end,artist_display,place_of_origin,medium_display,category_titles", params = params_search)        
    
    try:
        status = r.status_code
    except HTTPError as http_err:
        print(f'An HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occured: {err}')
    if r.status_code == 404:
        print('404 Not Found. Website content may have been removed or moved to another URL.')
    elif r.status_code == 200:
        print('200 OK success response code. The request has succeeded.')
        r1 = json.dumps(r.json(), indent = 2)
        artsearch = json.loads(r1)
        artworks = pd.DataFrame(artsearch['data'])
        artworks_info = artworks[['id', 'title','artist_display','place_of_origin','date_start','date_end','medium_display','category_titles']]
        
        return artworks_info


def get_museum_tour(tour):
    '''
    Function to retrieve the information about current tours at the Art institute of Chicago.

    Parameters:
    -------------
    tour: str
        A keyword to query; keyword can be any string that indicates a tour name, title of artwork, an exhibition name, or an artist's name. 

    Returns:
    -------------
    tour_info

    Example:
    -------------
    >>> get_museum_tour('cezanne tour')
        no error (successfully made request)
            id  ...                                      artist_titles
        0  4999  ...  [Paul Cezanne, Paul Cezanne, Paul Cezanne, Pau...
        1  4989  ...  [Paul Cezanne, Paul Cezanne, Paul Cezanne, Pau...
        2  2193  ...  [Archibald John Motley Jr., Grant Wood, Olowe ...
        3  1023  ...                     [Adler & Sullivan, Architects]
        4  4197  ...  [Archibald John Motley Jr., Felix Gonzalez-Tor...
        5  5155  ...                                                 []
        6  3246  ...  [Grant Wood, Olowe of Ise, Yoruba, Aztec (Mexi...
        7  4551  ...  [Ancient Roman, Ancient Roman, Ancient Mesopot...
        8  5164  ...                                                 []
        9  4671  ...  [René Magritte, Max Ernst, Joan Miró, Claude C...
        [10 rows x 7 columns]
    '''
    
    params_search_tour = {'q': tour} 
    rt = requests.get("https://api.artic.edu/api/v1/tours/search?fields=id,image,title,description,intro,artwork_titles,artist_titles", params = params_search_tour)
    try:
        status = rt.status_code
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('no error (successfully made request)')
        rt1 = json.dumps(rt.json(), indent = 2)
        toursearch = json.loads(rt1)
        ntour = pd.DataFrame(toursearch['data'])
        tour_info = ntour[['id','title','image','description','intro','artwork_titles','artist_titles']]
        return tour_info


def post_popularity_stat(query):
    '''
    Objects mentioning the queried keyword accessioned to the Art Institute of Chicago
    This function counts the frequency of the keyword over time.

    Parameters:
    -------------
    query: str
        A keyword to query; keyword can be any string that indicates a tour name, title of artwork, an exhibition name, or an artist's name. 

    Returns:
    -------------
    chart: a visualization of the frequency of the queried word appeared over time at the Art Institute of Chicago. 

    Example:
    -------------
    >>> a visualization of the queried word appeared over time at the Art Institute of Chicago.
    '''

    data = {
      "q": query,
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
    aic_water_lilies = aic_response.json()["aggregations"]["years"]["buckets"]
    aic_water_lilies_df = pd.DataFrame(aic_water_lilies)
    aic_water_lilies_df['institution'] = 'Art Institute of Chicago'
    
    aic_water_lilies_df.rename(columns={'doc_count': 'count', 'key': 'year'}, inplace=True)

    chart = alt.Chart(aic_water_lilies_df).mark_bar().encode(
        y='count:Q',
        x='year:O',
        color='institution:N')

    return chart 
#     return aic_response, aic_water_lilies_df
# def vis(aic_water_lilies_df):


"""
def get_image(image):
    '''
    A function to print the quried keyword. A user can query artworks by the name of an aritst or by the name of an artwork.

    Parameters:
    -------------
    query: str
        A keyword to query.

    Returns:
    -------------
    viz: a collection of images on the queried by a user.

    Example:
    -------------
    >>> a visualization of the queried word appeared over time at the Art Institute of Chicago.
    '''
    params_search_image = {'q': image} 
    
    aic_response = requests.get('https://api.artic.edu/api/v1/artworks/search/?fields=title,image_id&limit=27', params = params_search_image)
    aic_waterlilies_all = aic_response.json()['data']
    aic_waterlilies_all_df = pd.DataFrame(aic_waterlilies_all)
    aic_waterlilies_all_df.head()
    
    IIIF_IMAGE_URL = "https://www.artic.edu/iiif/2/%s/full/100,100/0/default.jpg"
    aic_waterlilies_all_df.image_id = [IIIF_IMAGE_URL % item for item in aic_waterlilies_all_df.image_id]
    
    attach(aic_waterlilies_all_df, "image_id")
    viz = show()
    return viz
    """




