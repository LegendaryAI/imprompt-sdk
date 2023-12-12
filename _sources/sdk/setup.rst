=================
Setup
=================

**Imprompt Server Endpoint** = https://api.imprompt.ai/app/

Get an API key
=================


Marketplace API needs bearer token in the header to authenticate the API call:
You can get the bearer token from the Imprompt team.

Authorization=Bearer <BEARER-TOKEN>

**Sample API call**

.. tabs::

  .. tab:: REST

    .. code-block:: sh

        GET /marketplaces/2 HTTP/1.1
        Host: <SERVER_ENDPOINT>
        Authorization: Bearer <BEARER_TOKEN>


  .. tab:: CURL

    .. code-block:: python

      curl --location '<API_ENDPOINT>' \
        --header 'Authorization: Bearer <BEARER_TOKEN>'

  .. tab:: Python

    .. code-block:: python

      import requests

      url = "<API_ENDPOINT>"
      payload = {}
      headers = {
          'Authorization': 'Bearer <BEARER_TOKEN>'
      }
      response = requests.request("GET", url, headers=headers, data=payload)
      print(response.text)




