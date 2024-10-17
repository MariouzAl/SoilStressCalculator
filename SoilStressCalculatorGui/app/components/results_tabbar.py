from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QTabBar
from soil_vertical_stress_increment.models.vertical_stress_increment_result import (
    VerticalStressIncrementResults,
)


class ResultsTabBar(QTabBar):
    on_deleted_tab: pyqtSignal = pyqtSignal(int)
    currentTabChanged: pyqtSignal = pyqtSignal(tuple)
    data: list[VerticalStressIncrementResults] = []
    on_double_click: pyqtSignal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setTabsClosable(True)
        self.setMovable(True)
        print("TABS currentIndex", self.currentIndex())
        self.tabCloseRequested.connect(self.handle_close_request_slot)
        self.currentChanged.connect(self.handle_current_changed_slot)

    def addTab(self, item: VerticalStressIncrementResults, label: str):
        self.data.append(item)
        super().addTab(label)

    def setTabs(self, items: list[VerticalStressIncrementResults]):
        for item in items:
            self.addTab(item)

    def removeAll(self):
        tab_count = self.count()
        if tab_count > 0:
            i = 0
            while True:
                self.removeTab(i)
                i = i + 1
                tab_count = self.count()
                if tab_count == 0:
                    break

    def mouseDoubleClickEvent(self, event):
        index = self.tabAt(event.pos())
        self.on_double_click.emit(index)

    def handle_close_request_slot(self, index: int):
        self.on_deleted_tab.emit(index)
        self.removeTab(index)
        self.data.remove(self.data[index])

    def handle_current_changed_slot(self, index):
        self.currentTabChanged.emit((index, self.data[index]))

    def renameTab(self, rename_item:tuple[int , str]):
        index, new_name=rename_item
        self.setTabText(index, new_name)
        