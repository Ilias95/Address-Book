#!/usr/bin/python3

# Copyright (C) 2012 Ilias Stamatis <stamatis.iliass@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __init__ import __version__

from PyQt4.QtCore import QSize
from PyQt4.QtGui import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                  QHBoxLayout, QLabel, QComboBox, QListWidget, QLineEdit,
                  QPushButton, QToolButton, QFrame, QIcon, QPixmap)

import sys
import pyqttools


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Address Book')
        self.resize(704, 459)

        categLabel = QLabel('Category:')
        self.categComboBox = QComboBox()
        cont_numLabel = QLabel('Contacts Number:')
        self.contactsListWidget = QListWidget()
        searchLabel = QLabel('Search')
        self.searchLineEdit = QLineEdit()

        widgets = ((categLabel, self.categComboBox),
                   (cont_numLabel, None),
                   (self.contactsListWidget,),
                   (searchLabel, self.searchLineEdit))
        vlayout1 = QVBoxLayout()

        for i in widgets:
            hlayout = pyqttools.add_to_layout(QHBoxLayout(), i)
            vlayout1.addLayout(hlayout)

        addToolButton = QToolButton()
        addToolButton.setMinimumSize(QSize(50, 50))
#        icon = QIcon()
#        icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
#        addToolButton.setIcon(icon)
#        addToolButton.setIconSize(QSize(45, 45))
        self.showLabel = QLabel()
        self.showLabel.setFrameShape(QFrame.StyledPanel)
        editButton = QPushButton('Edit')
        convertButton = QPushButton('Convert')

        widgets = ((None, addToolButton, None),
                   (self.showLabel,),
                   (None, editButton, convertButton))
        vlayout2 = QVBoxLayout()

        for i in widgets:
            hlayout = pyqttools.add_to_layout(QHBoxLayout(), i)
            vlayout2.addLayout(hlayout)

        f_layout = pyqttools.add_to_layout(QHBoxLayout(), (vlayout1, vlayout2))

        Widget = QWidget()
        Widget.setLayout(f_layout)
        self.setCentralWidget(Widget)

        self.statusBar = self.statusBar()
        self.userLabel = QLabel()
        self.statusBar.addPermanentWidget(self.userLabel)

        panelAction = pyqttools.create_action(self, 'User panel',
                                                     triggered=self.user_panel)
        quitAction = pyqttools.create_action(self, 'Quit', 'Ctrl+Q',
                                                          triggered=self.close)
        add_contactAction = pyqttools.create_action(self, 'Add contact',
                                          'Ctrl+N', triggered=self.add_contact)
        delete_allAction = pyqttools.create_action(self,
                              'Delete all contacts', triggered=self.delete_all)
        delete_categAction = pyqttools.create_action(self, 'Delete '
                                'categories', triggered=self.delete_categories)
        aboutAction = pyqttools.create_action(self, 'About', 'Ctrl+?',
                                                          triggered=self.about)

        fileMenu = self.menuBar().addMenu('File')
        contactsMenu = self.menuBar().addMenu('Contacts')
        deleteMenu = self.menuBar().addMenu(self.tr('Delete'))
        helpMenu = self.menuBar().addMenu('Help')

        pyqttools.add_actions(fileMenu, [panelAction, None, quitAction])
        pyqttools.add_actions(contactsMenu, [add_contactAction])
        pyqttools.add_actions(deleteMenu,[delete_allAction,delete_categAction])
        pyqttools.add_actions(helpMenu, [aboutAction])

    def user_panel(self):
        pass

    def add_contact(self):
        pass

    def delete_all(self):
        pass

    def delete_categories(self):
        pass

    def about(self):
        pass


def main():
    app = QApplication(sys.argv)
    address_book = MainWindow()
    address_book.show()
    app.exec_()

if __name__ == '__main__':
    main()