=================================
Add a plugin to a catalog
=================================


.. tabs::

  .. tab:: REST

    .. code-block:: sh

        API Endpoint: <IMPROMPT_SERVER_URL>/marketplace-catalogs/<MARKETPLACE_CATALOG_ID>/plugins
        Method: POST
        Body: {
            "plugin_external_id":"94c174594982989bd807dbbe0",
            "priority_ranking":100
        }
        X-Api-Key: API_KEY


  .. tab:: CURL

    .. code-block:: python

      curl --location '<IMPROMPT_SERVER_URL>/marketplace-catalogs/<MARKETPLACE_CATALOG_ID>/plugins' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: <API_KEY>' \
        --data '{
            "plugin_external_id":"94c174594982989bd807dbbe0",
            "priority_ranking":100
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
   * - plugin_external_id
     - string
     - The external id of the plugin to be added to the catalog.
   * - priority_ranking
     - integer
     - The priority ranking of the plugin in the catalog. The lower the number, the higher the priority. If not provided, the plugin will be added to the end of the catalog.


Sample Response
===================
::

    {
        "added_by_user_id": 2,
        "created_at": "Mon, 31 Jul 2023 11:02:44 GMT",
        "marketplace_catalog_id": 2,
        "plugin_external_id": "4c174594982989bd807dbbe0",
        "priority_ranking": 100,
        "updated_at": "Mon, 31 Jul 2023 11:02:44 GMT"
    }