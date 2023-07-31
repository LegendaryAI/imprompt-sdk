================================================
List all plugins in a catalog
================================================


.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplace-catalogs/<MARKETPLACE_CATALOG_ID>/plugins
        Method: GET
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location --request GET '<IMPROMPT_SERVER_URL>/marketplace-catalogs/<MARKETPLACE_CATALOG_ID>/plugins' \
           --header 'Authorization: API_KEY' \
        '


Sample Response
=================

::

    [
        {
            "added_by_user_id": 2,
            "created_at": "Mon, 31 Jul 2023 11:02:44 GMT",
            "marketplace_catalog_id": 2,
            "plugin_external_id": "8ad773c94c174594982989bd807dbbe0",
            "priority_ranking": 100,
            "updated_at": "Mon, 31 Jul 2023 11:02:44 GMT"
        }
    ]

