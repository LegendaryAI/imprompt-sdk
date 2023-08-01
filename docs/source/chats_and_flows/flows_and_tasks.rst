============================
Flows & Tasks
============================

Every agent has capabilities to run workflows or tasks. A workflow is a set of tasks that are executed in a specific order. A task is an action that is executed using a LLM or a plugin.

The output of any task can be:

1. push to the next task
2. push to a blackboard
3. save it in a vector database

Each task can then accept these outputs as inputs alongwith it's own prompt.


Run a workflow
=======================================

.. image:: /_images/run_a_workflow.gif
   :alt: Run a workflow GIF
   :align: center