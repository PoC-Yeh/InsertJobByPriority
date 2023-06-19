# Request
Implement a simple priority queue. Assume an incoming dictionary containing two keys; command to be executed and priority. Priority is an integer value [1, 10], where work items of the same priority are processed in the order they are received. 

# Launch the UI
The tool can be launched by executing ui.py

# What the UI does?
When the UI is first launched, it automatically generated a few jobs and sorted those jobs by their priorities. (High to low) In the upper section `Current Jobs`, you can see the first job is running and the others are waiting.
![alt text](/uiLaunch.png?raw=true)

We can submit new jobs on the lower section `Submit New Jobs`. The name and the priority of the job can be edited. After the job is submitted, it would appear on the `Current Jobs` section, with a note of `Newly submitted [number]`. The job would be inserted based on its priority. If there is jobs on the list having the same priority, the newly added job would be after the already existing one.
![alt text](/uiSubmit.png?raw=true)

# Details
## core.py
It is for generating lists of mock tasks and sorting tasks, finding where to insert a new task based on their priorities.
### Functions
1. `generateTaskList(itemNum=int, commandTextCount=int, priorityRange=(int, int))`: It is a function for generating a list of mock tasks. The list would look like:
```
[{'command': 'mnDO_0', 'priority': 2},
 {'command': 'KsEn_1', 'priority': 8},
 {'command': 'TpKE_2', 'priority': 10},
 {'command': 'vyLL_3', 'priority': 3},
 {'command': 'Gybo_4', 'priority': 9},
 {'command': 'cDIN_5', 'priority': 6}]
```
2. `sortTasksByPriority(list)`: Sort the whole list of tasks by priorites.
3. `getInsertIndex(dict, list)`: Get the index of where the dict should be inserted into the list.
4. `binarySearchInsertIndex(int, list, int, int)`: Use binary search to find where to insert the new value.
5. `getLargestSameValueIndex(int, list)`: Get the largest index of a certain value of a list.

### Testing core.py
The result of running `core.py` would be like the followings :
```
Tasks generated:
[{'command': 'ZqQf_0', 'priority': 3},
 {'command': 'kSlv_1', 'priority': 8},
 {'command': 'yFKF_2', 'priority': 8},
 {'command': 'RaTW_3', 'priority': 1},
 {'command': 'lQPI_4', 'priority': 4},
 {'command': 'Reey_5', 'priority': 8},
 {'command': 'BuPN_6', 'priority': 9},
 {'command': 'URFR_7', 'priority': 7},
 {'command': 'fctz_8', 'priority': 1},
 {'command': 'xJPt_9', 'priority': 2}]
--------------------------------------------------
Tasks sorted:
[{'command': 'BuPN_6', 'priority': 9},
 {'command': 'kSlv_1', 'priority': 8},
 {'command': 'yFKF_2', 'priority': 8},
 {'command': 'Reey_5', 'priority': 8},
 {'command': 'URFR_7', 'priority': 7},
 {'command': 'lQPI_4', 'priority': 4},
 {'command': 'ZqQf_0', 'priority': 3},
 {'command': 'xJPt_9', 'priority': 2},
 {'command': 'RaTW_3', 'priority': 1},
 {'command': 'fctz_8', 'priority': 1}]
--------------------------------------------------
insert task: {'command': 'GvsK_0', 'priority': 1}
--------------------------------------------------
Result:
[{'command': 'BuPN_6', 'priority': 9},
 {'command': 'kSlv_1', 'priority': 8},
 {'command': 'yFKF_2', 'priority': 8},
 {'command': 'Reey_5', 'priority': 8},
 {'command': 'URFR_7', 'priority': 7},
 {'command': 'lQPI_4', 'priority': 4},
 {'command': 'ZqQf_0', 'priority': 3},
 {'command': 'xJPt_9', 'priority': 2},
 {'command': 'RaTW_3', 'priority': 1},
 {'command': 'fctz_8', 'priority': 1},
 {'command': 'GvsK_0', 'priority': 1}]
```

## ui.py
The ui part of the tool.
### Widgets
1. `MockJobWindow()`: main tool widget
2. `JobListTable()`: the widget that shows the list of jobs
3. `SubmitWidget()`: the widget for submitting new job
