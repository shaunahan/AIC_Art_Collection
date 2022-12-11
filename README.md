# aic_art_collection

This python package retrieves artwork collections from the Art Institute of Chicago API in an efficient, user-friendly way. 
It helps users to find information about the art collections of their interest with visualizations. 

## Installation

```bash
$ pip install aic_art_collection
```

## Usage

1. Usage of `get_search_artwork()` function:
```python
# Retrieve art collection data by Monet.
>>> from aic_art_collection import get_search_artwork
>>> get_search_artwork("Monet")
```
<p align="center">
<img src="https://github.com/shaunahan/aic_art_collection/blob/main/img/get_search_artwork.png" style="zoom:70%;" />
</p>
<br>

2. Usage of `get_museum_tour` function:
```python
# Retreive a tour program information at the Art Institute of Chicago.
>>> from aic_art_collection import get_museum_tour
>>> get_museum_tour('Tour')
```

<p align="center">
<img src="https://github.com/shaunahan/aic_art_collection/blob/main/img/get_museum_tour.png" style="zoom:70%;" />
</p>

3. Usage of `post_popularity_stat` function:
```python
# This function counts the frequency of the keyword over time.
>>> from aic_art_collection import post_popularity_stat
>>> post_popularity_stat('Monet')
```
<p align="center">
<img src="https://github.com/shaunahan/aic_art_collection/blob/main/img/post_popularity_stat.png" style="zoom:70%;" />
</p>

4. Usage of `get_image` function:
```python
# This function retrieves an artwork collection of the queried keyword.
>>> from aic_art_collection import get_image
>>> get_image('Monet')
```
<p align="center">
<img src="https://github.com/shaunahan/aic_art_collection/blob/main/img/get_image.png" style="zoom:70%;" />
</p>

- For more information, please refer to the [`vignette`](https://github.com/shaunahan/aic_art_collection/blob/main/vignette.ipynb) for more guidance. 

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`aic_art_collection` was created by Shauna Han. It is licensed under the terms of the MIT license.

## Credits

`aic_art_collection` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
