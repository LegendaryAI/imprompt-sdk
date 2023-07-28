================================================
Get all users in an internal marketplace
================================================


.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplace-private-access?marketplace_id=<MARKETPLACE_ID>
        Method: GET
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location --request GET '<IMPROMPT_SERVER_URL>/marketplace-private-access?marketplace_id=<MARKETPLACE_ID>' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: API_KEY' \
        '


Sample Response
=================

::

    [
        {
            "created_at": "Fri, 28 Jul 2023 15:38:28 GMT",
            "marketplace_id": 1,
            "role": "admin",
            "updated_at": "Fri, 28 Jul 2023 15:38:28 GMT",
            "user_id": 2
        }
    ]

