================================
Create a new plugin from scratch
================================

Imprompt enables you to create new plugins, import them into an `OpenPlugin Manifest <https://openplugin.org/plugin_developers/openplugin_manifest.html>`_,
and use them in an LLM environment. This tutorial will help walk through those steps. The plugin we will be
creating is a text to image plugin that will take a string of text and convert it to an image and responding
with the URL. We will leverage the OpenAI Dalle2 model to do this.

Getting Started
===============

To get started, we will first need to understand the API docs for the OpenAI Dalle2 model. This will allow us
to understand what the model expects and returns.

.. image:: /_images/tutorial_new_plugin/understanding_docs.gif
   :alt: Understanding Docs GIF
   :align: center


Implement Plugin
================

Now that we understand the API docs, we can implement our plugin. Our plugin will wrap the Dalle2
model. We use `FastAPIs <https://swagger.io/specification>`_ to easily define the API and have it
documented for us in an `OpenAPI document <https://swagger.io/specification>`_. Once we have
implemented our plugin, we can test it locally and then deploy it publicly. You can deploy your
plugin to any cloud provider, but I used `AWS Lambda <https://aws.amazon.com/lambda/>`_ for this
example.

.. image:: /_images/tutorial_new_plugin/implement_plugin.gif
   :alt: Understanding Docs GIF
   :align: center


Import into Imprompt
====================

Now that we have our plugin implemented, we can import it into `Imprompt <https://app.imprompt.ai/plugins>`_.
All we need to get started is the `OpenAPI document <https://swagger.io/specification>`_ as seen below.

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
