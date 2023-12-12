================================================
Modify a user role in an internal marketplace
================================================

.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplaces/<MARKETPLACE_ID>/users/<USER_ID>/marketplace-private-access
        Method: PUT
        Body: {
            "role":"user"
        }
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location '<IMPROMPT_SERVER_URL>/marketplaces/<MARKETPLACE_ID>/users/<USER_ID>/marketplace-private-access' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: <API_KEY>' \
        --data '{
            "role":"user"
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
   * - role
     - string
     - Accepted values: admin, user, developer


Sample Response
===================
::

    {
        "created_at": "Mon, 31 Jul 2023 09:28:36 GMT",
        "marketplace_id": 1,
        "role": "user",
        "updated_at": "Mon, 31 Jul 2023 09:31:41 GMT",
        "user_id": 2
    }