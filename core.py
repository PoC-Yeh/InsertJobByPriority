import random
import pprint
from string import ascii_letters


def generateTaskList(itemNum=6,
                     commandTextCount=4,
                     priorityRange=(1, 10)):
    """ Generate a list of mock tasks for the purpose of testing.

    :param itemNum: number of tasks that are going to be generated
    :type itemNum: int

    :param commandTextCount: number of the characters the random command
    :type commandTextCount: int

    :param priorityRange: the range of the priority
    :type priorityRange: tuple of integers

    :return: a list of dictionaries containing 2 keys 'command' and 'priority'
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


def sortTasksByPriority(taskList):
    """ Sort the tasks in the order of their priorities.

    :return: sorted taskList in the order of their priorities (descending)
    :rtype: list of dictionaries
    """
    return sorted(taskList, key=lambda task: task.get('priority'), reverse=True)


def getInsertIndex(task, sortedTaskList):
    """ Get the index of where the task should be inserted to the tasks list.

    :param task: a dictionary containing 2 keys 'command' and 'priority'.
                 Example: {'priority': 10, 'command': 'GASD_6'}
    :type task: dict
    :param sortedTaskList: A list of dictionaries containing 2 keys 'command' and 'priority'.
                           The list is sorted by priority in descending order.
                           Example:
                           [
            {'priority': 8, 'command': 'AFid_0'},
            {'priority': 7, 'command': 'SDas_1'},
            {'priority': 6, 'command': 'Avsd_2'},
            {'priority': 5, 'command': 'Btex_3'},
            {'priority': 5, 'command': 'lsdM_4'},
            {'priority': 1, 'command': 'OweP_5'},
            ]


    :type sortedTaskList: list of dictionaries
    :return: index of where the task should be inserted
    :rtype: int
    """
    priorityList = [task.get('priority') for task in sortedTaskList]
    highIndex, lowIndex = [0, len(priorityList) - 1]

    currentTaskPriority = task.get('priority')
    insertIndex = binarySearchInsertIndex(currentTaskPriority,
                                          priorityList,
                                          highIndex,
                                          lowIndex)

    return insertIndex


def binarySearchInsertIndex(number, listOfNumber, highIndex, lowIndex):
    """ Get the index of where the number should be inserted to the list.

    :param number:
    :param listOfNumber:
    :param highIndex:
    :type highIndex: int
    :param lowIndex:
    :type lowIndex: int
    :return: index of where the number should be inserted
    :rtype: int
    """
    middleIndex = round((lowIndex + highIndex) / 2)

    if number == listOfNumber[lowIndex]:
        return lowIndex + 1
    if number == listOfNumber[middleIndex]:
        return getLargestSameValueIndex(number, listOfNumber) + 1

    if number > listOfNumber[middleIndex]:
        lowIndex = middleIndex
    elif number < listOfNumber[middleIndex]:
        highIndex = middleIndex

    if highIndex + 1 == lowIndex:
        return lowIndex
    return binarySearchInsertIndex(number, listOfNumber, highIndex, lowIndex)


def getLargestSameValueIndex(value, wholeList):
    """ Get the largest index of a certain value of a list.
    Example:
    value is 10
    wholeList is [10, 10, 0, 8, 10, 2, 3]
    The largest index with the same value is 4

    :param value: assigned value
    :type value: int
    :param wholeList:
    :type wholeList: a list of integers
    :return: the largest index of a certain value of a list
    :rtype: int
    """
    largestIndex = wholeList.index(value)
    for index, number in enumerate(wholeList):
        if number == value:
            largestIndex = index
    return largestIndex


if __name__ == '__main__':
    taskList = generateTaskList(itemNum=10, commandTextCount=4)
    sortedTaskList = sortTasksByPriority(taskList)
    print('Tasks generated:')
    pprint.pprint(taskList)

    print('-' * 50)
    print('Tasks sorted:')
    pprint.pprint(sortedTaskList)

    newTask = generateTaskList(itemNum=1, commandTextCount=4)[0]
    print('-' * 50)
    print('insert task: {}'.format(newTask))

    insertIndex = getInsertIndex(newTask, sortedTaskList)
    sortedTaskList.insert(insertIndex, newTask)
    print('-' * 50)
    print('Result:')
    pprint.pprint(sortedTaskList)

