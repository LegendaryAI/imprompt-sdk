================================================
Add user access to an internal marketplace
================================================


.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplace-private-access
        Method: POST
        Body: {
            "marketplace_id":1,
            "user_id":2,
            "role":"admin"
        }
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location '<IMPROMPT_SERVER_URL>/marketplace-private-access' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: <API_KEY>' \
        --data '{
            "marketplace_id":1,
            "user_id":2,
            "role":"admin"
        }'



API Body Parameters
===================
These parameters are used to configure the API request. The API request body is a JSON object with the following fields:

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - marketplace_id
     - integer
     - Marketplace id of the marketplace to which the user is to be added.
   * - user_id
     - integer
     - User id of the user to be added to the marketplace.
   * - role
     - string
     - Accepted values: admin, user, developer


Sample Response
===================
::

    {
        "created_at": "Fri, 28 Jul 2023 15:38:28 GMT",
        "marketplace_id": 1,
        "role": "admin",
        "updated_at": "Fri, 28 Jul 2023 15:38:28 GMT",
        "user_id": 2
    }