============================
Assignments
============================

An agent can generate a workflow from an assignment.
The agent breaks the assignment into multiple tasks which runs in a sequential manner.
The agent decides the order of the tasks based on the dependencies between the tasks.
Each task can be completed by either using a LLM or a plugin.

**Example**

Assignment= "Generate a list of 10 dog breeds. Email the list to shrikant@brandops.io"

Workflow

+ Task 1: Generate a list of 10 dog breeds using a LLM
+ Task 2: Email the list to shrikant@brandops.io using Imprompt Email Plugin.


Generate a workflow from an assignment
=======================================

.. image:: /_images/generate_a_workflow.gif
   :alt: Generate a workflow GIF
   :align: center