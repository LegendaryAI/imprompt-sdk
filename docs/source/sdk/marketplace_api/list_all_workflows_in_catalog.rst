================================================
List all workflows in a catalog
================================================


.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplace-catalogs/<MARKETPLACE_CATALOG_ID>/catalogs
        Method: GET
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location --request GET '<IMPROMPT_SERVER_URL>/marketplace-catalogs/<MARKETPLACE_CATALOG_ID>/catalogs' \
           --header 'Authorization: API_KEY' \
        '


Sample Response
=================

::

    [
        {
            "added_by_user_id": 2,
            "created_at": "Mon, 31 Jul 2023 12:47:26 GMT",
            "marketplace_catalog_id": 2,
            "priority_ranking": 100,
            "updated_at": "Mon, 31 Jul 2023 12:47:26 GMT",
            "workflow_id": "6f37b1f7-6809-45a3-87a0-b257403affee"
        }
    ]

