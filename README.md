# runTaskByPriority
Implement a simple priority queue. Assume an incoming stream of dictionaries containing two keys; command to be executed and priority. Priority is an integer value [0, 10], where work items of the same priority are processed in the order they are received. 

# Details
1. `generateTaskList(itemNum=int, commandTextCount=int, priorityRange=(int, int))` 
It is a function for generating a list of mock tasks.  Each element in the list is a dictionary containing 2 keys `command` and `priority`. The values of `command` consist of a few random alphabet characters, underline and a number. The values of `priority` are interger in a range from 0 to 10.
   - `itemNum`:  Decide the amonut of tasks in the list. Default is 6.
   - `commandTextCount`: The amount of ramdom alphabet characters in `command`. Default is 4.
   - `priorityRange`: For setting the range of priority. Default is (0, 10) 
```
[{'command': 'mnDO_0', 'priority': 2},
 {'command': 'KsEn_1', 'priority': 8},
 {'command': 'TpKE_2', 'priority': 10},
 {'command': 'vyLL_3', 'priority': 3},
 {'command': 'Gybo_4', 'priority': 9},
 {'command': 'cDIN_5', 'priority': 6},
 {'command': 'IObN_6', 'priority': 3},
 {'command': 'HglU_7', 'priority': 5},
 {'command': 'ERRH_8', 'priority': 7},
 {'command': 'Yzvb_9', 'priority': 9}]
```

2. `runTaskCommand(dict)`: Run the command of the task. (In this case, it is printing out string like: `run command: TpKE_2, task priority: 10`.
3. `execute()`: The actaul function of running the input task list in an order of task priorites.

# Result
When run runTaskByPriority.py, the result would be like the followings :
```
Tasks generated:
[{'command': 'mnDO_0', 'priority': 2},
 {'command': 'KsEn_1', 'priority': 8},
 {'command': 'TpKE_2', 'priority': 10},
 {'command': 'vyLL_3', 'priority': 3},
 {'command': 'Gybo_4', 'priority': 9},
 {'command': 'cDIN_5', 'priority': 6},
 {'command': 'IObN_6', 'priority': 3},
 {'command': 'HglU_7', 'priority': 5},
 {'command': 'ERRH_8', 'priority': 7},
 {'command': 'Yzvb_9', 'priority': 9}]

[Run tasks] --------------------
run command: TpKE_2, task priority: 10
run command: Gybo_4, task priority: 9
run command: Yzvb_9, task priority: 9
run command: KsEn_1, task priority: 8
run command: ERRH_8, task priority: 7
run command: cDIN_5, task priority: 6
run command: HglU_7, task priority: 5
run command: vyLL_3, task priority: 3
run command: IObN_6, task priority: 3
run command: mnDO_0, task priority: 2
```
