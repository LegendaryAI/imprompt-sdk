================================================
Remove a plugin from catalog
================================================


.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplace-catalogs/<marketplace_catalog_id>/plugins/<plugin_id>
        Method: DELETE
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location --request DELETE '<IMPROMPT_SERVER_URL>/marketplace-catalogs/<marketplace_catalog_id>/plugins/<plugin_id>' \
        --header 'Authorization: API_KEY' \
        '


Sample Response
=================

::

    {
        "message": "MarketplaceCatalogPlugin deleted"
    }
