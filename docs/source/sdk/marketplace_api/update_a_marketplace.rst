========================
Update a marketplace
========================

.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplaces/<marketplace_id>
        Method: PUT
        Body: {
            "description":"description"
        }
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location --request PUT '<IMPROMPT_SERVER_URL>/marketplaces/<marketplace_id>' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: <API_KEY>' \
        --data '{
            "description": "description"
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
   * - name
     - string
     - The name of the marketplace.
   * - publish_level
     - string
     - Accepted values: internal_org, external_org
   * - description
     - string
     - The description of the marketplace.


Sample Response
===================
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