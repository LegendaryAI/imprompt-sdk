================================================
Delete a catalog
================================================

.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplaces/<MARKETPLACE_ID>/catalogs/<CATALOG_ID>
        Method: DELETE
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location --request DELETE '<IMPROMPT_SERVER_URL>/marketplaces/<MARKETPLACE_ID>/catalogs/<CATALOG_ID>' \
        --header 'Authorization: API_KEY' \
        '


Sample Response
=================

::

    {
        "message": "MarketplaceCatalog deleted"
    }

