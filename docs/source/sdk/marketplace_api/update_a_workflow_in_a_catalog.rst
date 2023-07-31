=================================
Update a workflow in a catalog
=================================


.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplace-catalogs/<marketplace_catalog_id>/workflows/<workflow_id>
        Method: PUT
        Body:{
            "priority_ranking":10
        }
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location --request PUT '<IMPROMPT_SERVER_URL>/marketplace-catalogs/<marketplace_catalog_id>/workflows/<workflow_id>' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: API_KEY' \
        --data '{
            "priority_ranking":10
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
   * - priority_ranking
     - integer
     - The priority ranking of the plugin in the catalog. The lower the number, the higher the priority. If not provided, the plugin will be added to the end of the catalog.


Sample Response
===================
::

    {
        "added_by_user_id": 2,
        "created_at": "Mon, 31 Jul 2023 12:47:26 GMT",
        "marketplace_catalog_id": 2,
        "priority_ranking": 100,
        "updated_at": "Mon, 31 Jul 2023 12:47:26 GMT",
        "workflow_id": "6f37b1f7-6809-45a3-87a0-b257403affee"
    }