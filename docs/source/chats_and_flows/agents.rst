============================
Agents
============================

An Imprompt agent leverages large language models(LLMs) to generate workflows from assignment statements and able to run a workflow to complete the assignment.

Its primary function is to understand assignment statements and transform them into actionable workflows. Whether it's a simple to-do list, a complex project plan, or a multi-step business process, the Imprompt Agent can turn it into a seamless and efficient set of tasks.

You can increase your agent's capabilities by:

1. Installing plugins
2. Uploading files

Your can use your personal agent to perform following tasks:

1. Design a workflow from an assignment.
2. Run a task.
3. Run a workflow.





Create a new agent in Imprompt
===================================

Imprompt users can create a personal agent or an organization agent. The organization agent can be used by all the members of the organization.


.. image:: /_images/create_an_agent.gif
   :alt: Create an agent GIF
   :align: center

Install a plugin to an agent
===================================

You can increase capabilities of your agent by installing plugins. You can install plugins from the Imprompt plugin marketplace.
Every agent comes default with these systems plugins:

1. Imprompt Email
2. Imprompt Web Scraper
3. Imprompt Web Search
4. Imprompt File Manager

.. image:: /_images/install_a_plugin.gif
   :alt: Installing a plugin GIF
   :align: center


Upload a file to an agent
===================================

You can provide your agent with text files to use as a data source. You can upload a file from your local machine or from a URL.

We support the various input formats: txt, pdf, odt, doc, docx, rtf, url, mp3.

Data preprocessing pipeline: Documents are broken into chunks, passed through the OpenAI embedding model, then stored in pinecone vector database.



.. image:: /_images/upload_a_file_to_agent.gif
   :alt: Upload a file GIF
   :align: center



