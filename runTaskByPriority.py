import random
import pprint
from string import ascii_letters


def generateTaskList(itemNum=6,
                     commandTextCount=4,
                     priorityRange=(0, 10)):
    """ Generate a list of mock tasks for the purpose of testing.

    :param itemNum: number of tasks that are going to be generated
    :type itemNum: int

    :param commandTextCount: number of the characters the random command
    :type commandTextCount: int

    :param priorityRange: the range of the priority
    :type priorityRange: tuple of integers

    :return: a list of dictionaries containing 2 keys 'priority' and 'command'
            Example:
            [
            {'priority': 7, 'command': 'UviP_0'},
            {'priority': 8, 'command': 'swTE_1'},
            {'priority': 1, 'command': 'AXUe_2'},
            {'priority': 6, 'command': 'rukr_3'},
            {'priority': 5, 'command': 'bxdJ_4'},
            {'priority': 5, 'command': 'onKy_5'},
            ]

    :rtype: list of dictionary
    """
    taskList = list()
    for index in range(itemNum):
        randomString = ''.join(random.choice(ascii_letters) for count in range(commandTextCount))
        command = '_'.join([randomString, str(index)])
        taskList.append(
            {'command': command,
             'priority':random.randint(priorityRange[0], priorityRange[1])
            }
        )

    return taskList



def sortTaskByPriority(taskList, largeToSmall=True):
    """ Sort a list of tasks by their priority numbers.

    :param taskList: list of tasks
                     Each task is a dictionary containing 2 keys 'priority' and 'command'
    :type taskList: list of dictionaries

    :param largeToSmall: if sorting the list by larger priority numbers to smaller priority numbers.
    :type largeToSmall: bool

    :return: a list of sorted tasks
    :rtype: list
    """
    return sorted(taskList, key=lambda task: task.get('priority'), reverse=largeToSmall)


def runTasks(tasks):
    """ A mock of running the command of the task.

    :param tasks: list of tasks
                  Each task is a dictionary containing 2 keys 'priority' and 'command'
    :type tasks: list

    :return:
    """
    for task in tasks:
        print('run command: {}, task priority: {}'.format(task.get('command'),
                                                          task.get('priority')))



def execute(priorityLagerToSmall=True):
    """

    :return:
    """
    taskList = generateTaskList(itemNum=10, commandTextCount=4)
    sortedTaskList = sortTaskByPriority(taskList, largeToSmall=priorityLagerToSmall)

    print('Tasks generated:')
    pprint.pprint(taskList)
    print('\n[Run tasks]', '-' * 20)

    runTasks(sortedTaskList)


if __name__ == '__main__':
    execute()

"""
result would be like:

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

"""
