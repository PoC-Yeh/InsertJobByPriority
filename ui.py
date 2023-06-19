import sys
import core
from PySide2 import QtCore
from PySide2 import QtWidgets


HEADER = ['Job Name', 'Priority', 'Status', 'Note']


class MockJobWindow(QtWidgets.QWidget):
    def __init__(self, jobs):
        """ Initializing MonkJobWindow

        :param jobs: a list of jobs
                     Example:
                     [{'priority': 7, 'command': 'UviP_0'},
                     {'priority': 8, 'command': 'swTE_1'},
                     {'priority': 1, 'command': 'AXUe_2'}]
        :type jobs: list of dictionaries
        """
        super(MockJobWindow, self).__init__()

        self.currentJobList = core.sortTasksByPriority(jobs)
        self.newJob = core.generateTaskList(itemNum=1, commandTextCount=4)[0]
        self.addCount = 0
        self.initUi()
        self.setConnections()


    def initUi(self):
        """ Initializing ui
        """
        self.setWindowTitle('Job test')
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.jobLabel = QtWidgets.QLabel('Current Jobs')
        self.jobListTable = JobListTable(self, HEADER, self.currentJobList)
        self.submitJobLabel = QtWidgets.QLabel('Submit New Jobs')
        self.submitWidget = SubmitWidget(self)

        self.mainLayout.addWidget(self.jobLabel)
        self.mainLayout.addWidget(self.jobListTable)
        self.mainLayout.addWidget(self.submitJobLabel)
        self.mainLayout.addWidget(self.submitWidget)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.resize(self.jobListTable.sizeHint())
        self.generateNewJobForSubmit()

    def generateNewJobForSubmit(self):
        """ Generate new jobs to submit
        """
        self.submitWidget.nameLineEdit.setText(self.newJob.get('command'))
        self.submitWidget.priorityLineEdit.setText(str(self.newJob.get('priority')))

    def setConnections(self):
        """ Set connections to signals
        """
        self.submitWidget.submitJob.connect(self.insertNewJob)

    def insertNewJob(self, jobData):
        """ Insert newly submitted job to  the JobListTable

        :param jobData: Example: {'command': 'GvsK_0', 'priority': 1}
        :type jobData: dict
        :return:
        """
        insertIndex = core.getInsertIndex(jobData, self.currentJobList)
        self.jobListTable.insertJob(insertIndex, jobData, self.addCount)

        self.currentJobList.insert(insertIndex, self.newJob)
        self.newJob = core.generateTaskList(itemNum=1, commandTextCount=4)[0]
        self.generateNewJobForSubmit()
        self.addCount += 1



class JobListTable(QtWidgets.QTableWidget):
    def __init__(self, parent, header, jobList):
        """ Initializing JobListTable

        :param parent: parent of the widget
        :param header: the header of this QTableWidget
        :type header: list of string
        :param jobList: a list of jobs
                        Example:
                        [{'priority': 7, 'command': 'UviP_0'},
                        {'priority': 8, 'command': 'swTE_1'},
                        {'priority': 1, 'command': 'AXUe_2'}]
        :type jobList: list of dictionaries
        """
        super(JobListTable, self).__init__(parent=parent)

        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(header)
        self.header = self.horizontalHeader()
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.fillTable(jobList)
        self.setFixedSize(460, 300)

    def fillTable(self, jobList):
        """ fill JobListTable with a list of jobs

        :param jobList: a list of jobs
        :type jobList: list of dictionaries
        :return:
        """
        self.setRowCount(len(jobList))
        for index, job in enumerate(jobList):
            self.setItem(index, 0, QtWidgets.QTableWidgetItem(job.get('command')))
            self.setItem(index, 1, QtWidgets.QTableWidgetItem(str(job.get('priority'))))
            if index == 0:
                self.setItem(index, 2, QtWidgets.QTableWidgetItem('Running'))
                self.setItem(index, 3, QtWidgets.QTableWidgetItem('//I am running//'))
            else:
                self.setItem(index, 2, QtWidgets.QTableWidgetItem('Waiting'))

    def insertJob(self, insertIndex, jobData, newAddCount):
        """ Insert newly submitted job to the JobListTable

        :param insertIndex: the index for insert the newly submitted job
        :type insertIndex: int
        :param jobData: Example: {'command': 'GvsK_0', 'priority': 1}
        :type jobData: dict
        :param newAddCount: count of newly added jobs
        :type newAddCount: int
        :return:
        """
        self.insertRow(insertIndex)
        self.setItem(insertIndex, 0, QtWidgets.QTableWidgetItem(jobData.get('command')))
        self.setItem(insertIndex, 1, QtWidgets.QTableWidgetItem(str(jobData.get('priority'))))
        self.setItem(insertIndex, 2, QtWidgets.QTableWidgetItem('Waiting'))
        self.setItem(insertIndex, 3, QtWidgets.QTableWidgetItem('Newly submitted {}'.format(str(newAddCount))))



class SubmitWidget(QtWidgets.QWidget):
    submitJob = QtCore.Signal(dict)
    def __init__(self, parent):
        """ Initializing SubmitWidget
        """
        super(SubmitWidget, self).__init__(parent=parent)

        self.newJob = {'command': None, 'priority': None}

        self.initUi()
        self.setConnections()
        self.setSubmitButtonAvailability()

    def initUi(self):
        """ Initializing ui
        """
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.setLayout(self.mainLayout)

        self.nameLabel = QtWidgets.QLabel('Name:')
        self.nameLineEdit = QtWidgets.QLineEdit()
        self.priorityLabel = QtWidgets.QLabel('Priority:')
        self.priorityLineEdit = QtWidgets.QLineEdit()
        self.submitButton = QtWidgets.QPushButton('Submit')

        self.mainLayout.addWidget(self.nameLabel)
        self.mainLayout.addWidget(self.nameLineEdit)
        self.mainLayout.addWidget(self.priorityLabel)
        self.mainLayout.addWidget(self.priorityLineEdit)
        self.mainLayout.addWidget(self.submitButton)

    def setConnections(self):
        """ Set connections to signals
        """
        self.nameLineEdit.textChanged.connect(self.getJobName)
        self.priorityLineEdit.textChanged.connect(self.getJobPriority)
        self.submitButton.clicked.connect(self.emitSignal)


    def setSubmitButtonAvailability(self):
        """ Enable or disable the submit button.
        Enable only when all the values of a job are filled.
        """
        self.submitButton.setEnabled(all([value for value in self.newJob.values()]))

    def getJobName(self, name):
        """ Get the name of the job

        :param name: name of the job
        :type name: str
        :return:
        """
        self.newJob['command'] = name
        self.setSubmitButtonAvailability()

    def getJobPriority(self, priority):
        """ Get priority of the job

        :param priority: priority of the job
        :type priority: str
        """
        self.newJob['priority'] = int(priority) if priority.isdigit() else None
        self.setSubmitButtonAvailability()


    def emitSignal(self):
        """ emit signal
        """
        self.submitJob.emit(self.newJob)



if __name__ == '__main__':
    jobs = core.generateTaskList()
    app = QtWidgets.QApplication(sys.argv)

    window = MockJobWindow(jobs)
    window.show()

    app.exec_()

