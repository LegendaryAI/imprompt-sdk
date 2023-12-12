================================================
Get a marketplace
================================================

.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplaces/<marketplace_id>
        Method: GET
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location --request GET '<IMPROMPT_SERVER_URL>/marketplaces/<marketplace_id>' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: API_KEY' \
        '


Sample Response
================

::

    {
            "created_at": "Fri, 28 Jul 2023 15:04:19 GMT",
            "created_by_organization_id": 1,
            "description": "This is a test marketpalce",
            "id": 1,
            "name": "Test Marketplace",
            "publish_level": "internal_org",
            "updated_at": "Fri, 28 Jul 2023 15:04:19 GMT"
    }

