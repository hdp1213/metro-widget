import sys
from PyQt4 import QtGui


class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, parent=None):
        super(SystemTrayIcon, self).__init__(QtGui.QIcon('/usr/share/icons/gnome/16x16/emotes/face-cool.png'), parent)
        self.parent = parent

        self.contextMenu = QtGui.QMenu(self.parent)

        self.optionAction = self.contextMenu.addAction('Options')

        self.contextMenu.addSeparator()

        self.exitAction = self.contextMenu.addAction('&Exit')
        self.exitAction.triggered.connect(QtGui.qApp.quit)

        self.setContextMenu(self.contextMenu)
        self.setToolTip('Metro')

        self.activated.connect(self.displayWidget)

    def displayWidget(self, activationReason, *args):
        if activationReason == QtGui.QSystemTrayIcon.Trigger:
            # message = QtGui.QMessageBox.information(self.parent, 'Hello World', 'Hey there')
            menu = QtGui.QMenu('My Menu!', self.parent)
            menu.addAction('test')
            # menu.geomo
            menu.show()
        else:
            pass


def main():
    app = QtGui.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    w = QtGui.QWidget()

    trayIcon = SystemTrayIcon(w)
    trayIcon.show()

    return app.exec_()

if __name__ == '__main__':
    exit(main())
