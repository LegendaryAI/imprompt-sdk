==================================
Create a Plugin from 3rd Party API
==================================

Imprompt enables you to create new plugins, import them into an `OpenPlugin Manifest <https://openplugin.org/plugin_developers/openplugin_manifest.html>`_,
and use them in an LLM environment. This tutorial will help walk through those steps. The plugin we will be
creating is OpenAI `Dalle2 <https://openai.com/dall-e-2>`_ plugin that will take a string of text and convert it to an image and responding
with the URL.

Getting Started
===============

To get started, we will first need to understand the API docs for the OpenAI Dalle2 model. This will allow us
to understand what the model expects and returns.

.. image:: /_images/tutorial_new_plugin/understanding_docs.gif
   :alt: Understanding Docs GIF
   :align: center


Create OpenAPI Document
=======================

Now that we understand the API docs, we can create an `OpenAPI document <https://swagger.io/specification>`_.
If you are familiar with creating this yourself, you can use `Swagger Editor <https://swagger.io/tools/swagger-editor/>`_.
I will instead create a `Postman <https://www.postman.com/>`_ Collection so I can first test the API.

.. image:: /_images/tutorial_new_plugin/create_postman_collection.png
   :alt: Create Postman Collection
   :align: center


.. raw:: html

   <br/>

Next, I will import it into `Stoplight <https://stoplight.io/>`_ for the ease of modifying & creating the OpenAPI
document. When I am happy with the OpenAPI document, I will export it as a JSON file.

.. image:: /_images/tutorial_new_plugin/stoplight_edit_openapi_doc.gif
   :alt: Stoplight Edit OpenAPI Doc
   :align: center


Import into Imprompt
====================

Now that we have our OpenAPI document, we can import it into `Imprompt <https://app.imprompt.ai/plugins>`_.

.. image:: /_images/tutorial_new_plugin/import_plugin_to_imprompt.gif
   :alt: Import Plugin to Imprompt
   :align: center

.. raw:: html

   <br/>

You have the option to enable/disable operations from your OpenAPI document. In this case, we only have one
operation, so we will enable it.

Edit & Save OpenPlugin Manifest
===============================

After we have imported our plugin, it will produce us with a starter `OpenPlugin Manifest <https://openplugin.org/plugin_developers/openplugin_manifest.html>`_.
We will need to edit this manifest to include more information about our plugin, such a description, logo, operation examples,
and operation helpers.

.. image:: /_images/tutorial_new_plugin/edit_manifest.gif
   :alt: Edit OpenPlugin Manifest
   :align: center


Try Plugin
==========

Now we can try our plugin in `Imprompt <https://app.imprompt.ai/plugins>`_!

.. image:: /_images/tutorial_new_plugin/try_plugin.gif
   :alt: Try Plugin
   :align: center
