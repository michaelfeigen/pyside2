"""
This module is an example script for PySide2

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from PySide2 import QtCore, QtGui, QtWidgets


class FarmDeployer(QtWidgets.QDialog):
    """
    An instance of this class is a GUI that has the potential to
    install standard packages, delete specified paths and deliver custom files.
    It currently has no functionality, but functionality can be added where it
    says #add functionality HERE to make it fully functional.
    """

    def __init__(self):
        super().__init__()

        #create the widgets for the window
        self.createVerticalLabels("img\\logo.jpg")
        self.createFormGroupBox()
        self.installStandardPackages()
        self.deliverCustomFiles()
        self.createHBox()

        #create the main layout
        mainLayout = QtWidgets.QVBoxLayout()
	    
        #add the widgets to the main layout
        mainLayout.addWidget(self.verticalLabels)
        self.createVerticalLabels("img\\selectMachines.jpg")
        mainLayout.addWidget(self.verticalLabels)
        mainLayout.addWidget(self.formGroupBox)
        self.createVerticalLabels("img\\installPackages.jpg")
        mainLayout.addWidget(self.verticalLabels)
        mainLayout.addWidget(self.gridGroupBox)
        self.createVerticalLabels("img\\deliverCustomFiles.jpg")
        mainLayout.addWidget(self.verticalLabels)
        mainLayout.addWidget(self.deliverCustomFiles)
        mainLayout.addWidget(self.hBoxs)

        #set the layout
        self.setLayout(mainLayout)

        #set the window title and image in the upper left corner
        self.setWindowTitle('Carbon Farm Deployer')
        self.setWindowIcon(QtGui.QIcon('img\\0.png')) 
       

    def createVerticalLabels(self, image):
        """
        Creates a Vertical Box and fills it will the given image

        Parameter image: The relative path to the image
        Precondition: image is a string
        """
        #set the layout to Vertical Box Layout
        vbox = QtWidgets.QVBoxLayout(self)
        self.verticalLabels = QtWidgets.QGroupBox("")

        #add the picture to the window
        pixmap = QtGui.QPixmap(image)
        pixmap = pixmap.scaled(1100, 1200, QtCore.Qt.KeepAspectRatio)
        lbl = QtWidgets.QLabel(self)
        lbl.setAlignment(QtCore.Qt.AlignHCenter)
        lbl.setPixmap(pixmap)
        vbox.addWidget(lbl)

        #set the layout
        self.verticalLabels.setLayout(vbox)

    
    def createHBox(self):
        """
        Creates the Delete Specific Path and Deliver Custom Files 
        buttons. It does this utilizing a horizontal box layout 
        and adding Push Buttons to it.
        """
        #set the layout to Horizontal Box Layout
        hbox = QtWidgets.QHBoxLayout(self)
        self.hBoxs = QtWidgets.QGroupBox("")

        #create the Delete Specific Path and Deliver Custom Files buttons
        btn = QtWidgets.QPushButton("Delete Specific Path", self)
        btn.clicked.connect(self.deletePopUp)
        btn2 = QtWidgets.QPushButton("Deliver Custom Files", self)

        #add functionality HERE

        hbox.addWidget(btn)
        hbox.addWidget(btn2)

        #set the layout
        self.hBoxs.setLayout(hbox)


    def createFormGroupBox(self):
        """
        Creates the text box's to fill in Machine Name,
        User Name, Deadline Pool Name, Deadline Version
        """
        #set the layout to Form Layout
        self.formGroupBox = QtWidgets.QGroupBox("")
        layout = QtWidgets.QFormLayout()

        #create the field for Machine Name
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setPlaceholderText("Comma Seperated List")
        layout.addRow(QtWidgets.QLabel("           Machine Name:"), self.lineEdit)

        #create the field for User Name
        self.lineEdit1 = QtWidgets.QLineEdit(self)
        self.lineEdit1.setPlaceholderText("Comma Seperated List")
        layout.addRow(QtWidgets.QLabel("           User Name: "), self.lineEdit1)
		
        #create the field for Deadline Pool Name
        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.setPlaceholderText("Leave Blank if Specifying Machine Names")
        layout.addRow(QtWidgets.QLabel("           Deadline Pool Name:            "), self.lineEdit2)

        #create the field for Deadline Version
        self.lineEdit3 = QtWidgets.QLineEdit(self)
        self.lineEdit3.setText("deadline10")
        layout.addRow(QtWidgets.QLabel("           Deadline Version:"), self.lineEdit3)

        #set the layout
        self.formGroupBox.setLayout(layout)


    def installStandardPackages(self):
        """                               
        Creates the checkbox's, combobox's and Install Standard Packages
        Button seen under the Install Standard Packages Label.
        """
        #set layout to Grid Layout
        self.gridGroupBox = QtWidgets.QGroupBox("")
        layout = QtWidgets.QGridLayout()

        #set the Horizontal and Vertical spacing for the grid
        layout.setHorizontalSpacing(4)
        layout.setVerticalSpacing(14)

        #create the 3ds Max, Maya, C4D, Nuke, Fusion and AE checkbox's 
        self.checkbox = QtWidgets.QCheckBox('3ds Max',self)
        layout.addWidget(self.checkbox, 0, 1)
        self.checkbox1 = QtWidgets.QCheckBox('Maya',self)
        layout.addWidget(self.checkbox1, 0, 3)
        self.checkbox2 = QtWidgets.QCheckBox('C4D',self)
        layout.addWidget(self.checkbox2, 0, 5)
        self.checkbox3 = QtWidgets.QCheckBox('Nuke',self)
        layout.addWidget(self.checkbox3, 0, 7)
        self.checkbox4 = QtWidgets.QCheckBox('Fusion',self)
        layout.addWidget(self.checkbox4, 0, 9)
        self.checkbox5 = QtWidgets.QCheckBox('AE',self)
        layout.addWidget(self.checkbox5, 0, 11)

        #create variables for the different versions 
        Max = ('2018', '2013', '2014', '2015', '2016', '2017', '2018', '2019')
        Maya = ('2018', '2013', '2014', '2015', '2016', '2016.5', '2017', '2018', '2019')
        C4D = ('R19', 'R18', 'R17', 'R16')
        Nuke = ('11.3','10.5')
        Fusion = ('9.0', '8.0', '7.8', '7.7', '7.5', '7.0', '6.4', '6.3', '6.2', '6.1')
        AE = ('CC 2018', 'CC 2017', 'CC 2015.4', 'CC 2015', 'CC 2014', 'CC', 'CS6' )

        versions = [Max, Maya, C4D, Nuke, Fusion, AE]

        #create the combo box's for the different versions 
        self.combo = QtWidgets.QComboBox(self)
        self.combo.addItems(versions[0])
        layout.addWidget(self.combo, 0, 2)
        self.combo1 = QtWidgets.QComboBox(self)
        self.combo1.addItems(versions[1])
        layout.addWidget(self.combo1, 0, 4) 
        self.combo2 = QtWidgets.QComboBox(self)
        self.combo2.addItems(versions[2])
        layout.addWidget(self.combo2, 0, 6)
        self.combo3 = QtWidgets.QComboBox(self)
        self.combo3.addItems(versions[3])
        layout.addWidget(self.combo3, 0, 8)
        self.combo4 = QtWidgets.QComboBox(self)
        self.combo4.addItems(versions[4])
        layout.addWidget(self.combo4, 0, 10)
        self.combo5 = QtWidgets.QComboBox(self)
        self.combo5.addItems(versions[5])
        layout.addWidget(self.combo5, 0, 12)

        #create the check box's to Skip Plugins and Skip MCG
        self.checkbox6 = QtWidgets.QCheckBox('Skip Plugins', self)
        layout.addWidget(self.checkbox6, 0, 16)
        self.checkbox7 = QtWidgets.QCheckBox('Skip MCG', self)
        self.checkbox7.setCheckState(QtCore.Qt.Checked)
        layout.addWidget(self.checkbox7, 0, 17)

        #create the Install Standard Packages Push Button 
        btn = QtWidgets.QPushButton('Install Standard Packages', self)

        #add functionality HERE

        layout.addWidget(btn, 0, 18)

        #set the layout
        self.gridGroupBox.setLayout(layout)


    def deliverCustomFiles(self):
        """
        Creates the text box's to fill in the Source Folder 
        and Destination Folder under the Deliver Custom Files label.
        """
        #set the layout to Form Layout
        self.deliverCustomFiles = QtWidgets.QGroupBox("")
        layout = QtWidgets.QFormLayout()

        #create the Enter Source Folder to Transport text field
        self.lineEdit4 = QtWidgets.QLineEdit(self)
        self.lineEdit4.setText("Transporter")
        transportMessage = "           Enter Source Folder to Transport:"
        layout.addRow(QtWidgets.QLabel(transportMessage), self.lineEdit4)
		
        #create the Enter Destination Folder text field
        self.lineEdit5 = QtWidgets.QLineEdit(self)
        self.lineEdit5.setText("\\C$\\")
        destinationMessage = "           Enter Destination Folder:"
        layout.addRow(QtWidgets.QLabel(destinationMessage), self.lineEdit5)
	    
        #set the layout
        self.deliverCustomFiles.setLayout(layout)


    def deletePopUp(self):
        """
        Creates the window that pops up when the Delete 
        Specific Path Button is pressed
        """
        #create the pop up window
        message = "         Are you sure? \nDon't Delete the C Drive! "
        choice = QtWidgets.QMessageBox.warning(self, 'Farm Destroyer', message, 
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		
        #add functionality HERE


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = FarmDeployer()
    sys.exit(dialog.exec_())

