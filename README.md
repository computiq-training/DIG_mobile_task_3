## Task 3

Create the following endpoints in the corresponding controller module:

-----------

* `/api/categories`
* `/api/categories/{id}`

-----

* `/api/series`
* `/api/series/{id}`
* `/api/series/featured`
* `/api/series/{id}/seasons`
* `/api/series/{id}/seasons/{id}/episodes`
* `/api/series/{id}/seasons/{id}/episodes/{id}`

------

* `/api/news`
* `/api/news/{id}`

#### `Note`: your serial response should look like the following:

```python
{
    "id": "90fc257e-1d3e-49b4-b9e8-1ce651edae91",
    "title": "Dexter",
    "description": "This is a description of a specific serial that is intended only for demonstration purposes.",
    "image": "https://i.ibb.co/7pmwtgY/image.jpg",
    "release_date": "2022-10-04",
    "rating": "8.9",
    "categories": [
        {
            "id": "08bda9b0-4e35-45c7-9bee-b446e3c62b0b",
            "name": "Action"
        },
        {
            "id": "a589ead1-9ddb-4a5b-8eb8-c9d42c9b536c",
            "name": "Drama"
        }
    ],
    "actors": [
        {
            "id": "79c20360-0b04-42e8-8efa-feabd24da25f",
            "name": "Vin Diesel",
            "image": null
        }
    ]
},
```

Good Luck ! 🤞🏻✌🏻