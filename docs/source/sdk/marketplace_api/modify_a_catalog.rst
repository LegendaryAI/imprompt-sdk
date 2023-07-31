================================================
Modify a catalog
================================================



.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplaces/<MARKETPLACE_ID>/catalogs/<CATALOG_ID>
        Method: PUT
        Body: {
            "name":"My Catalog",
            "description":"desc",
            "at_stage":"dev",
            "is_published": true
        }
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location '<IMPROMPT_SERVER_URL>/marketplaces/<MARKETPLACE_ID>/catalogs/<CATALOG_ID>' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: <API_KEY>' \
        --data '{
            "name":"My Catalog",
            "description":"desc",
            "at_stage":"dev",
            "is_published": true
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
     - Name of the catalog.
   * - description
     - string
     - Description of the catalog.
   * - at_stage
     - string
     - Accepted values: dev, test, prod (default: dev)
   * - is_published
     - boolean
     - Accepted values: true, false (default: false)


Sample Response
===================
::

    {
        "at_stage": "dev",
        "created_at": "Mon, 31 Jul 2023 10:23:11 GMT",
        "description": null,
        "id": 1,
        "is_published": false,
        "marketplace_id": 1,
        "name": "My Catalog",
        "updated_at": "Mon, 31 Jul 2023 10:23:11 GMT"
    }