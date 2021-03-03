import sys
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QUrl, QDirIterator, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QFileDialog, QAction, QHBoxLayout, QVBoxLayout, QSlider
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent


class App(QMainWindow):

    def __init__(self, song):
        super().__init__()
        self.song_path = song
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.title = 'PyTunes'
        self.left = 300
        self.top = 300
        self.width = 300
        self.height = 150
        self.color = 0  # 0- toggle to dark 1- toggle to light
        self.userAction = -1  # 0- stopped, 1- playing 2-paused
        self.initUI()
        self.song = song

    def initUI(self):
        # Add file menu

        self.addControls()

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.toggleColors()
        self.show()

    def addControls(self):
        wid = QWidget(self)
        self.setCentralWidget(wid)
        # Add song controls
        volumeslider = QSlider(Qt.Horizontal, self)
        volumeslider.setFocusPolicy(Qt.NoFocus)
        volumeslider.valueChanged[int].connect(self.changeVolume)
        volumeslider.setValue(100)
        playBtn = QPushButton('Play')  # play button
        pauseBtn = QPushButton('Pause')  # pause button
        # Add button layouts
        controlArea = QVBoxLayout()  # centralWidget
        controls = QHBoxLayout()
        playlistCtrlLayout = QHBoxLayout()
        # Add buttons to song controls layout
        controls.addWidget(playBtn)
        controls.addWidget(pauseBtn)
        # Add buttons to playlist controls layout
        # Add to vertical layout
        controlArea.addWidget(volumeslider)
        controlArea.addLayout(controls)
        controlArea.addLayout(playlistCtrlLayout)
        wid.setLayout(controlArea)
        # Connect each signal to their appropriate function
        playBtn.clicked.connect(self.playhandler)
        pauseBtn.clicked.connect(self.pausehandler)

        self.statusBar()
        self.playlist.currentMediaChanged.connect(self.songChanged)

    def openFile(self):
       
        url = QUrl.fromLocalFile(self.song_path)
        
        self.playlist.addMedia(QMediaContent(url))
        self.player.setPlaylist(self.playlist)
        self.player.play()
        self.userAction = 1
    

    def addFiles(self):
        if self.playlist.mediaCount() != 0:
            self.folderIterator()
        else:
            self.folderIterator()
            self.player.setPlaylist(self.playlist)
            self.player.playlist().setCurrentIndex(0)
            self.player.play()
            self.userAction = 1
    
    def folderIterator(self):
        folderChosen = QFileDialog.getExistingDirectory(self, 'Open Music Folder', '~')
        if folderChosen != None:
            it = QDirIterator(folderChosen)
            it.next()
            while it.hasNext():
                if it.fileInfo().isDir() == False and it.filePath() != '.':
                    fInfo = it.fileInfo()
                    if fInfo.suffix() in ('mp3', 'ogg', 'wav', 'm4a'):
                        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(it.filePath())))
                it.next()
            if it.fileInfo().isDir() == False and it.filePath() != '.':
                fInfo = it.fileInfo()
                if fInfo.suffix() in ('mp3', 'ogg', 'wav', 'm4a'):
                    self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(it.filePath())))
    
    def playhandler(self):
        if self.playlist.mediaCount() == 0:
            self.openFile()
        elif self.playlist.mediaCount() != 0:
            self.player.play()
            self.userAction = 1

    def pausehandler(self):
        self.userAction = 2
        self.player.pause()

    def changeVolume(self, value):
        self.player.setVolume(value)
    
    def songChanged(self, media):
        if not media.isNull():
            url = media.canonicalUrl()
            self.statusBar().showMessage(url.fileName())

    def toggleColors(self):
        """ Fusion dark palette from https://gist.github.com/QuantumCD/6245215. Modified by me and J.J. """
        app.setStyle("Fusion")
        palette = QPalette()
        if self.color == 0:
            palette.setColor(QPalette.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.WindowText, Qt.white)
            palette.setColor(QPalette.Base, QColor(25, 25, 25))
            palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            palette.setColor(QPalette.ToolTipBase, Qt.white)
            palette.setColor(QPalette.ToolTipText, Qt.white)
            palette.setColor(QPalette.Text, Qt.white)
            palette.setColor(QPalette.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ButtonText, Qt.white)
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Link, QColor(235, 101, 54))
            palette.setColor(QPalette.Highlight, QColor(235, 101, 54))
            palette.setColor(QPalette.HighlightedText, Qt.black)
            app.setPalette(palette)
            self.color = 1
        elif self.color == 1:
            palette.setColor(QPalette.Window, Qt.white)
            palette.setColor(QPalette.WindowText, Qt.black)
            palette.setColor(QPalette.Base, QColor(240, 240, 240))
            palette.setColor(QPalette.AlternateBase, Qt.white)
            palette.setColor(QPalette.ToolTipBase, Qt.white)
            palette.setColor(QPalette.ToolTipText, Qt.white)
            palette.setColor(QPalette.Text, Qt.black)
            palette.setColor(QPalette.Button, Qt.white)
            palette.setColor(QPalette.ButtonText, Qt.black)
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Link, QColor(66, 155, 248))
            palette.setColor(QPalette.Highlight, QColor(66, 155, 248))
            palette.setColor(QPalette.HighlightedText, Qt.black)
            app.setPalette(palette)
            self.color = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App('/home/sami/Documents/Computer/server_and_client/client/recorded.wav')
    sys.exit(app.exec_())
