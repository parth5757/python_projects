import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class TabbedBrowser(QTabWidget):
    def __init__(self):
        super(TabbedBrowser, self).__init__()

        self.add_new_tab(QUrl('http://bing.com'), 'Homepage')
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_current_tab)

    def add_new_tab(self, url, label):
        browser = QWebEngineView()
        browser.setUrl(url)
        index = self.addTab(browser, label)
        self.setCurrentIndex(index)

        # Update the URL bar when the tab's URL changes
        browser.urlChanged.connect(lambda q: self.update_url_bar(q, index))

    def close_current_tab(self, index):
        if self.count() > 1:  # Ensure there's at least one tab left
            self.removeTab(index)

    def update_url_bar(self, q, index):
        # You can update a separate URL bar for each tab here, if implemented
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.browser = TabbedBrowser()
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(lambda: self.browser.currentWidget().back())
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(lambda: self.browser.currentWidget().forward())
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(lambda: self.browser.currentWidget().reload())
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        new_tab_btn = QAction('New Tab', self)
        new_tab_btn.triggered.connect(self.add_new_tab)
        navbar.addAction(new_tab_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.currentChanged.connect(self.update_url_bar)

    def navigate_home(self):
        self.browser.currentWidget().setUrl(QUrl('http://bing.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.currentWidget().setUrl(QUrl(url))

    def add_new_tab(self):
        self.browser.add_new_tab(QUrl('http://bing.com'), 'New Tab')

    def update_url_bar(self):
        current_index = self.browser.currentIndex()
        current_browser = self.browser.widget(current_index)
        self.url_bar.setText(current_browser.url().toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('My Cool Browser')
window = MainWindow()
window.show()
app.exec_()
