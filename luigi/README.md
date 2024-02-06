
# Building workflows with [luigi](https://luigi.readthedocs.io/en/stable/index.html)

## Tutorial
There are two fundamental building blocks of Luigi - the Task class and the Target class.
Both are abstract classes and expect a few methods to be implemented. 
In addition to those two concepts, the Parameter class is an important concept that governs how a Task is run.

### Task

The Task class is a bit more conceptually interesting because this is where computation is done. There are a few methods that can be implemented to alter its behavior, most notably run(), output() and requires().

![](https://luigi.readthedocs.io/en/stable/_images/tasks_input_output_requires.png)

### Parameter
if your Task class runs a Hadoop job to create a report every night, you probably want to make the date a parameter of the class

![](https://luigi.readthedocs.io/en/stable/_images/task_parameters.png)

### Dependencies
Using tasks, targets, and parameters, Luigi lets you express arbitrary dependencies in code, rather than using some kind of awkward config DSL. This is really useful because in the real world, dependencies are often very messy

## Luigi Task Status

If you want to visualize the tasks , use the following command to see http://localhost:8082/static/visualiser/index.html

$ luigid

## Running from the Command Line
$cd basic
$python -m luigi --module hello-world HelloLuigi --local-scheduler

## Running from Python code
Another way to start tasks from Python code is using luigi.build(tasks, worker_scheduler_factory=None, **env_params) 
from luigi.interface module. 
Also, it is possible to pass additional parameters to build such as host, port, workers and local_scheduler.






