================================================
Remove user access from an internal marketplace
================================================

.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplaces/<MARKETPLACE_ID>/users/<USER_ID>/marketplace-private-access
        Method: DELETE
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location --request DELETE '<IMPROMPT_SERVER_URL>/marketplaces/<MARKETPLACE_ID>/users/<USER_ID>/marketplace-private-access' \
        --header 'Authorization: API_KEY' \
        '


Sample Response
=================

::

    {
        "message": "MarketplacePrivateAcces deleted"
    }

