=================================
Update a plugin in a catalog
=================================


.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplace-catalogs/<marketplace_catalog_id>/plugins/<plugin_id>
        Method: PUT
        Body:{
            "priority_ranking":10
        }
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location --request PUT '<IMPROMPT_SERVER_URL>/marketplace-catalogs/<marketplace_catalog_id>/plugins/<plugin_id>' \
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
        "created_at": "Mon, 31 Jul 2023 11:19:59 GMT",
        "marketplace_catalog_id": 2,
        "plugin_external_id": "25b20ad7307e4253a9ca7e41cbe3203d",
        "priority_ranking": 10,
        "updated_at": "Mon, 31 Jul 2023 12:15:58 GMT"
    }