# Request
Implement a simple priority queue. Assume an incoming dictionary containing two keys; command to be executed and priority. Priority is an integer value [1, 10], where work items of the same priority are processed in the order they are received. 

# UI
When the UI is first launched, it automatically generated a few jobs and sorted those jobs by their priorities. (High to low) In the upper section `Current Jobs`, you can see the first job is running and the others are waiting.
![alt text](/uiLaunch.png?raw=true)

We can submit new jobs on the lower section `Submit New Jobs`. The name and the priority of the job can be edited. After the job is submitted, it would appear on the `Current Jobs` section, with a note of `Newly submitted [number]`
![alt text](/uiSubmit.png?raw=true)


# What it does?


# Details
1. `generateTaskList(itemNum=int, commandTextCount=int, priorityRange=(int, int))`: 
It is a function for generating a list of mock tasks.  Each element in the list is a dictionary containing 2 keys `command` and `priority`. The values of `command` consist of a few random alphabet characters, underline and a number (the number would be the index of the task in the list). The values of `priority` are interger in a range from 1 to 10.
   - `itemNum`:  Decide the amonut of tasks in the list. Default is 6.
   - `commandTextCount`: The amount of ramdom alphabet characters in `command`. Default is 4.
   - `priorityRange`: For setting the range of priority. Default is (1, 10) 
```
[{'command': 'mnDO_0', 'priority': 2},
 {'command': 'KsEn_1', 'priority': 8},
 {'command': 'TpKE_2', 'priority': 10},
 {'command': 'vyLL_3', 'priority': 3},
 {'command': 'Gybo_4', 'priority': 9},
 {'command': 'cDIN_5', 'priority': 6}]
```



# Result
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
