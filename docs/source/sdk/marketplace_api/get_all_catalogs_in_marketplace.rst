================================================
Get all catalogs from a marketplace
================================================


.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplaces/<MARKETPLACE_ID>/catalogs
        Method: GET
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location --request GET '<IMPROMPT_SERVER_URL>/marketplaces/<MARKETPLACE_ID>/catalogs' \
           --header 'Authorization: API_KEY' \
        '


Sample Response
=================

::

    [
        {
            "at_stage": "dev",
            "created_at": "Mon, 31 Jul 2023 10:23:11 GMT",
            "description": null,
            "id": 1,
            "is_published": false,
            "marketplace_id": 1,
            "name": "My Catalog",
            "updated_at": "Mon, 31 Jul 2023 10:23:11 GMT"
        }
    ]

