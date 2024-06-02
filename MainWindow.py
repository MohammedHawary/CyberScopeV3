from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QFrame, QSizePolicy,QToolTip, QSpacerItem, QMessageBox, QCheckBox, QRadioButton, QScrollArea, QComboBox, QToolButton, QTextEdit, QTabWidget, QDialog, QHBoxLayout, QMainWindow, QWidget, QLineEdit, QAction, QPushButton, QLabel, QVBoxLayout, QStackedWidget, QDesktopWidget, QGridLayout, QMenu, QPlainTextEdit, QTextBrowser
from PyQt5.QtCore import QFile, QTextStream, Qt, QTimer, QCoreApplication, QMargins ,QSize, QEvent
from PyQt5.QtGui import QIcon, QFont, QPainter, QColor, QPen, QTextCursor, QCursor
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QBarSet, QBarSeries, QLegend
import re
import DB_V2
from datetime import datetime
import webbrowser
import winreg



class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent=None)
        self.setFixedSize(613, 200)  # Set fixed size
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove title bar
        uic.loadUi('Dialog.ui', self)

        self.frame          = self.findChild(QFrame,        "frame"         )
        self.frame_2        = self.findChild(QFrame,        "frame_2"       )
        self.frame_3        = self.findChild(QFrame,        "frame_3"       )
        self.label          = self.findChild(QLabel,        "label"         )
        self.label_2        = self.findChild(QLabel,        "label_2"       )
        self.Cancel_btn2    = self.findChild(QPushButton,   "Cancel_btn2"   )
        self.Cancel_btn     = self.findChild(QPushButton,   "Cancel_btn"    )
        self.line_edit      = self.findChild(QLineEdit,     "line_edit"     )
        self.ok_button      = self.findChild(QPushButton,   "ok_button"     )
        self.light_theme    = "Light"
        if parent:
            self.move(parent.geometry().center() - self.rect().center())

        self.Cancel_btn2.clicked.connect(self.close)
        self.Cancel_btn.clicked.connect(self.close)
        self.ok_button.clicked.connect(self.validate_and_accept)
        self.line_edit.returnPressed.connect(self.validate_and_accept)


    def mode(self,light_theme="Light"):
        if light_theme == "Light":
            self.light_theme = "Light"
            self.frame.setStyleSheet('background-color: rgb(245, 245, 245);border-top: 5px solid rgb(38, 55, 70);border-bottom: 2px dotted rgb(221, 221, 221);')
            self.frame_2.setStyleSheet('background-color: rgb(245, 245, 245);border-bottom: 2px dotted rgb(221, 221, 221);')
            self.frame_3.setStyleSheet('background-color: rgb(245, 245, 245);')
            self.label.setStyleSheet('color: black; font-size: 20px;border: none;')
            self.label_2.setStyleSheet('color: black; font-size: 15px;border: none;')
            self.Cancel_btn2.setStyleSheet('QPushButton{border: none; font-size: 20px;color: rgb(221, 221, 221);font-weight: bold;} QPushButton:hover{color:rgb(51, 51, 51);}')
            self.line_edit.setStyleSheet('QLineEdit{height: 30px; font-size: 15px; border: 1px solid rgb(200, 200, 200); color: black;padding-left: 10px;} QLineEdit:focus{border: 1px solid rgb(166, 166, 166)};')
            self.ok_button.setStyleSheet('QPushButton{height:29px; width: 75px; background-color:rgb(0, 113, 185); color: white;border: none;font-size: 12px;}QPushButton:hover{background-color:rgb(42, 99, 149);}')
            self.Cancel_btn.setStyleSheet('QPushButton{height:29px; width: 75px;background-color:rgb(245, 245, 245); color: black;border: none;font-size: 12px;}QPushButton:hover{background-color:rgb(197, 197, 197); color:rgb(0, 113, 185);}')
        else:
            self.light_theme = "Dark"
            self.frame.setStyleSheet('background-color: rgb(59, 74, 97);border-top: 5px solid rgb(38, 55, 70);border-bottom: 2px dotted rgb(49, 58, 70);')
            self.frame_2.setStyleSheet('background-color: rgb(59, 74, 97);border-bottom: 2px dotted rgb(49, 58, 70);')
            self.frame_3.setStyleSheet('background-color: rgb(59, 74, 97);')
            self.label.setStyleSheet('color: white; font-size: 20px;border: none;')
            self.label_2.setStyleSheet('color: white; font-size: 15px;border: none;')
            self.Cancel_btn2.setStyleSheet('QPushButton{border: none; font-size: 20px;color: rgb(255, 89, 89);font-weight: bold;} QPushButton:hover{color:rgb(153, 0, 0);}')
            self.line_edit.setStyleSheet('QLineEdit{height: 30px; font-size: 15px; border: 1px solid rgb(110, 126, 149); padding-left: 10px; color: white;} QLineEdit:focus{border: 1px solid rgb(0, 165, 181)};')
            self.ok_button.setStyleSheet('QPushButton{height:29px; width: 75px; background-color:rgb(19, 114, 129); color: white;border-radius: 2px; border: 1px solid rgb(0, 165, 182);font-size: 12px;}QPushButton:hover{background-color:rgb(0, 165, 182);}')
            self.Cancel_btn.setStyleSheet('QPushButton{height:29px; width: 75px;background-color:rgb(90, 93, 101); color: white;border-radius: 2px;border: none;font-size: 12px;}QPushButton:hover{background-color:rgb(72, 83, 98);}')

    def validate_and_accept(self):
        new_name = self.line_edit.text().strip()
        if not new_name:
            self.line_edit.setToolTip("Field cannot be empty!")
            if self.light_theme == "Light":
                self.line_edit.setStyleSheet('QLineEdit{height: 30px; font-size: 15px; border: 1px solid red; padding-left: 10px; color: black;} QLineEdit:focus{border: 1px solid red};')
            else:
                self.line_edit.setStyleSheet('QLineEdit{height: 30px; font-size: 15px; border: 1px solid red; padding-left: 10px; color: white;} QLineEdit:focus{border: 1px solid red};')
            return
        elif len(new_name) > 20:
            self.line_edit.setToolTip("Please Enter folder name between (_1 and 19_) charcter!")
            if self.light_theme == "Light":
                self.line_edit.setStyleSheet('QLineEdit{height: 30px; font-size: 15px; border: 1px solid red; padding-left: 10px; color: black;} QLineEdit:focus{border: 1px solid red};')
            else:
                self.line_edit.setStyleSheet('QLineEdit{height: 30px; font-size: 15px; border: 1px solid red; padding-left: 10px; color: white;} QLineEdit:focus{border: 1px solid red};')
            return
        elif DB_V2.check_folder_exist_in_folderNames_table(new_name):
            self.line_edit.setToolTip("Folder name already exists try another name!")
            if self.light_theme == "Light":
                self.line_edit.setStyleSheet('QLineEdit{height: 30px; font-size: 15px; border: 1px solid red; padding-left: 10px; color: black;} QLineEdit:focus{border: 1px solid red};')
            else:
                self.line_edit.setStyleSheet('QLineEdit{height: 30px; font-size: 15px; border: 1px solid red; padding-left: 10px; color: white;} QLineEdit:focus{border: 1px solid red};')
            return
        self.accept()

    def create_folder(self):
        self.label.setText("Create Folder")
        self.ok_button.setText("Create")

    def rename_folder(self):
        self.label.setText("Rename Folder")
        self.ok_button.setText("Rename")

    def load_stylesheet(self, filename):
        print(filename)
        # self.clear_widget_styles(self)
        style_file = QFile(filename)
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            content = stream.readAll()
            style_file.close()
            self.setStyleSheet(content)
        else:
            print(f"Failed to open {filename}")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('MainWindow.ui', self)
        self.setGeometry(700, 500, 500, 200)
                            # QWidget
        self.SideBar                   = self.findChild(QWidget,        "SideBar"                   )
        self.TopBar                    = self.findChild(QWidget,        "TopBar"                    )
        self.Body                      = self.findChild(QWidget,        "Body"                      )
        self.UnderTopBar               = self.findChild(QWidget,        "UnderTopBar"               )
        self.ChartBar                  = self.findChild(QWidget,        "ChartBar"                  )
        self.ChartBar_2                = self.findChild(QWidget,        "ChartBar_2"                )
        self.HostInDesailsTopWidget    = self.findChild(QWidget,        "HostInDesailsTopWidget"    )
        self.HostInDesailsBottomWidget = self.findChild(QWidget,        "HostInDesailsBottomWidget" )
        self.VulnsWidget               = self.findChild(QWidget,        "VulnsWidget"               )
        self.tab_5                     = self.findChild(QWidget,        "tab_5"                     )
                            # QStackedWidget
        self.stackedWidget             = self.findChild(QStackedWidget, "stackedWidget"             )
                                    # QLabel
        self.FoldersLabel              = self.findChild(QLabel,          "FoldersLabel"             )
        self.MyScansLabel              = self.findChild(QLabel,          "MyScansLabel"             )
        self.EmptyFolderLabel          = self.findChild(QLabel,          "EmptyFolderLabel"         )
                            # QPushButton
        self.MyScansBtn                = self.findChild(QPushButton,     "MyScansBtn"               )
        self.AllScansBtn               = self.findChild(QPushButton,     "AllScansBtn"              )
        self.TrashBtn                  = self.findChild(QPushButton,     "TrashBtn"                 )
        self.MyAccountBtn              = self.findChild(QPushButton,     "MyAccountBtn"             )
        self.ThemeBtn                  = self.findChild(QPushButton,     "ThemeBtn"                 )
        self.AboutBtn                  = self.findChild(QPushButton,     "AboutBtn"                 )
        self.ScansTopBarBtn            = self.findChild(QPushButton,     "ScansTopBarBtn"           )
        self.SettingsTopBarBtn         = self.findChild(QPushButton,     "SettingsTopBarBtn"        )
        self.LogedInUserBtn            = self.findChild(QPushButton,     "LogedInUserBtn"           )
        self.LogedUserBtn              = self.findChild(QPushButton,     "LogedUserBtn"             )
        self.NewFolderBtn              = self.findChild(QPushButton,     "NewFolderBtn"             )
        self.NewScanBtn                = self.findChild(QPushButton,     "NewScanBtn"               )
        self.CreateNewScanBtn          = self.findChild(QPushButton,     "CreateNewScanBtn"         )
        self.BackBtn                   = self.findChild(QPushButton,     "BackBtn"                  )
        self.DeleteBtn                 = self.findChild(QPushButton,     "DeleteBtn"                )
        self.VulnBtn                   = self.findChild(QPushButton,     "VulnBtn"                  )
        self.SaveInputsBtn             = self.findChild(QPushButton,     "SaveInputsBtn"            )
        self.CanceInputsBtn            = self.findChild(QPushButton,     "CanceInputsBtn"           )
                            # QGridLayout
        self.gridLayout_2              = self.findChild(QGridLayout,     "gridLayout_2"             )
        self.gridLayout_48             = self.findChild(QGridLayout,     "gridLayout_48"            )
        self.gridLayout_64             = self.findChild(QGridLayout,     "gridLayout_64"            )
        self.gridLayout_102            = self.findChild(QGridLayout,     "gridLayout_102"           )
        self.gridLayout_103            = self.findChild(QGridLayout,     "gridLayout_103"           )
                            # QScrollArea
        self.ScrollArea                = self.findChild(QScrollArea,     "ScrollArea"               )
                            # QRadioButton
        self.DarkThemeRadioButton     = self.findChild(QRadioButton,     "DarkThemeRadioButton"     )
        self.Last_back_and_text       = [] 

                            # ####################
                            #   Buttons Section  #
                            # ####################

        self.MyScansBtn.clicked.connect(self.ClickedBtn)
        self.AllScansBtn.clicked.connect(self.ClickedBtn)
        self.ScansTopBarBtn.clicked.connect(self.ScansTopBar)
        self.SettingsTopBarBtn.clicked.connect(self.SettingPage)
        self.LogedInUserBtn.clicked.connect(self.SettingPage)
        self.LogedUserBtn.clicked.connect(self.SettingPage)

        self.MyAccountBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.ThemeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.AboutBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))



        self.stackedWidget.currentChanged.connect(self.print_current_index)

        self.CreateNewScanBtn.clicked.connect(self.BackFunc)
        self.NewFolderBtn.clicked.connect(self.AddNewFolderWindow)
        self.NewScanBtn.clicked.connect(self.BackFunc)

        self.OWASPBtn1.clicked.connect(self.BackFromOWASPBtn)
        self.OWASPBtn2.clicked.connect(self.BackFromOWASPBtn)
        self.OWASPBtn3.clicked.connect(self.BackFromOWASPBtn)

        self.SaveInputsBtn.clicked.connect(self.SaveScanInput)
        self.CanceInputsBtn.clicked.connect(self.CancelScanInput)

##################################################################################################################
                            # Dark Mode Section

        self.system_theme = self.DarkMode()
        self.DarkThemeRadioButton.clicked.connect(lambda: self.DarkMode(self.DarkThemeRadioButton))
##################################################################################################################
##################################################################################################################
                            # Chart section
        self.circleChart(self.gridLayout_102, 25,10, 0, 0, 1)

        self.circleChart(self.gridLayout_103, 25,10, 0, 0, 1)

        self.lineChart(25,10,0,0,1)

##################################################################################################################
                            # called Func Section
        DB_V2.create_table()
        DB_V2.craet_all_tables()
        self.addBtns(DB_V2.select_all_data())
        # self.HostInDesailsWidget.currentChanged.connect(self.create_table_scans_for_vulnerability)
        self.create_table_scans_for_vulnerability()
        self.tab_5.installEventFilter(self)

        self.MyScansBtn.click()
        # self.stackedWidget.setCurrentIndex(2)
        self.show()
        self.showMaximized()

    def print_current_index(self, index):
        all_buttons = self.SideBar.findChildren(QPushButton)
        if index == 4:
            for button in all_buttons:
                if button.isChecked():
                    self.BackBtn.setText(f'< Back to {button.text()}')
                    self.BackBtn.clicked.connect(button.click)
        if index == 8:
            self.BackBtn.setText('< Back to Vulnerabilites')
            self.BackBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))


    def DarkMode(self,btn=None):
        all_buttons = self.VulnsWidget.findChildren(QPushButton)
        all_label = self.VulnsWidget.findChildren(QLabel)
        all_Widgets = self.VulnsWidget.findChildren(QWidget)
        all_CheckBoxs = self.VulnsWidget.findChildren(QCheckBox)

        if btn:
            if btn.isChecked():
                self.load_stylesheet("dark_theme.qss")
                system_theme = "Dark"
                DB_V2.insert_theme_data("Dark")
                print("btn from Dark")
                self.system_theme = system_theme
                self.addBtns(DB_V2.select_all_data(),"Dark")

                self.access_grid_layout_elements(self.gridLayout_102)
                self.access_grid_layout_elements(self.gridLayout_103)

                self.NameInput.setStyleSheet('QLineEdit{border: 1px solid rgb(109, 125, 148);background-color: rgb(36, 45, 59);color: white;height: 30px;}QLineEdit:focus{border: 1px solid rgb(28, 210, 227);}')
                self.TargetInput.setStyleSheet('border: 1px solid rgb(109, 125, 148);background-color: rgb(36, 45, 59);color: white;height: 30px;')

# #################################################################
                for widget in all_Widgets:
                    if widget.objectName() == "TopWidget":
                        widget.setStyleSheet('background-color: rgb(72, 83, 98); border: 1px solid rgb(72, 73, 80);')
                        continue
                    if widget.objectName() == "DownWidget":
                        widget.setStyleSheet('background-color: rgb(49, 58, 70); border: 1px solid rgb(72, 73, 80); font-size: 13px; font-weight: bold')
                        continue
                    widget.setStyleSheet('background-color: rgb(36, 45, 59);font-size: 13px; font-weight: bold')

                for button in all_buttons:
                    if button.objectName() == "EditBtn":
                        button.setStyleSheet('''
                            QPushButton{
                                border: none;
                                background-color: rgb(72, 83, 98);
                                font-size: 12px;
                                color: white;
                                text-align: left;
                                }
                            ''')
                        continue
                    button.setStyleSheet('''
                    QPushButton{
                        border: none;
                        background-color: rgb(49, 58, 70);
                        font-size: 12px;
                        color: white;
                        text-align: left;
                        }
                    QPushButton:hover{
                        text-decoration: underline;
                        color: rgb(37, 210, 227);
                        }

                        ''')

                for CheckBox in all_CheckBoxs:
                    CheckBox.setStyleSheet('border: none;')

                for label in all_label:
                    if label.objectName() == 'SevLabel':
                        label.setStyleSheet('color: black;border: none;background-color: rgb(145, 36, 62); color: white; border-radius: 4px; font-size: 10px; font-weight: normal;')
                        continue

                    label.setStyleSheet('color: white; border: none;font-size: 13px; font-weight: bold;')
                return
            else:
                self.load_stylesheet("light_theme.qss")
                system_theme = "Light"
                DB_V2.insert_theme_data("Light")
                print("btn from Light")
                self.system_theme = system_theme
                self.addBtns(DB_V2.select_all_data(),"Light")

                self.access_grid_layout_elements(self.gridLayout_102)
                self.access_grid_layout_elements(self.gridLayout_103)

                self.NameInput.setStyleSheet('QLineEdit{border: 1px solid rgb(204, 204, 204);background-color: rgb(255,255,255);color: black;height: 30px;} QLineEdit:focus{border: 1px solid rgb(170, 170, 170);}')
                self.TargetInput.setStyleSheet('QLineEdit{border: 1px solid rgb(204, 204, 204);background-color: white;color: black;height: 30px;} QLineEdit:focus{border: 1px solid rgb(170, 170, 170);}')

# #################################################################
                for widget in all_Widgets:
                    if widget.objectName() == "TopWidget":
                        widget.setStyleSheet('background-color: rgb(245, 245, 245); border: 1px solid rgb(221, 221, 221);')
                        continue
                    if widget.objectName() == "DownWidget":
                        widget.setStyleSheet('background-color: white; border: 1px solid rgb(221, 221, 221);font-size: 13px; font-weight: normal;')
                        continue
                    widget.setStyleSheet('background-color: white;font-size: 13px; font-weight: bold;')

                for button in all_buttons:
                    if button.objectName() == "EditVulnBtn":
                        button.setStyleSheet('''
                            QPushButton{
                                border: none;
                                background-color: rgb(245, 245, 245);
                                font-size: 12px;
                                color: rgb(245, 245, 245);
                                text-align: left;
                                }
                            ''')
                        continue
                    button.setStyleSheet('QPushButton{border:none; text-align: left;background-color white; color: black;} QPushButton:hover{text-decoration: underline; color: rgb(56, 109, 156);}')


                for CheckBox in all_CheckBoxs:
                    CheckBox.setStyleSheet('border: none;')


                for label in all_label:
                    if label.objectName() == 'SevLabel':
                        label.setStyleSheet('color: black;border: none;background-color: rgb(145, 36, 62); color: white; border-radius: 4px; font-size: 10px; font-weight: normal;')
                        continue
                    label.setStyleSheet('color: black; border: none;font-size: 13px;')
                return

        system_theme = self.get_windows_theme()
        Theme = DB_V2.get_theme_data()
        if Theme:
            if Theme == "Light":
                self.load_stylesheet("light_theme.qss")
                system_theme = Theme
                print("Light From DB")

                self.access_grid_layout_elements(self.gridLayout_102)
                self.access_grid_layout_elements(self.gridLayout_103)

                return system_theme
            else:
                self.load_stylesheet("dark_theme.qss")
                self.DarkThemeRadioButton.setChecked(1)
                system_theme = Theme
                print("Dark From DB")

                self.access_grid_layout_elements(self.gridLayout_102)
                self.access_grid_layout_elements(self.gridLayout_103)

                return system_theme

        if system_theme == "Light":
            self.load_stylesheet("light_theme.qss")

            self.access_grid_layout_elements(self.gridLayout_102)
            self.access_grid_layout_elements(self.gridLayout_103)

            return system_theme
        else:
            self.load_stylesheet("dark_theme.qss")
            self.DarkThemeRadioButton.setChecked(1)

            self.access_grid_layout_elements(self.gridLayout_102)
            self.access_grid_layout_elements(self.gridLayout_103)

            return system_theme

    def BackFunc(self):
        all_buttons = self.SideBar.findChildren(QPushButton)
        for button in all_buttons:
            if button.isChecked():
                if button.objectName() == "MyScansBtn":
                    self.BackBtn.setText(f'< Back To My Scans')

                if button.objectName() == "AllScansBtn":
                    self.BackBtn.setText(f'< Back To All Scans')


                if button.objectName() != "AllScansBtn" and button.objectName() != "MyScansBtn":
                    self.BackBtn.setText(f'< Back To {button.objectName()}')

                self.stackedWidget.setCurrentIndex(1)
                self.FolderInput.clear()
                self.MyScansLabel.setText("Scan Templates")
                self.BackBtn.clicked.connect(button.click)

    def BackFromOWASPBtn(self):
        data = DB_V2.select_all_data()
        self.FolderInput.addItem('My Scans')
        for i in data:
            self.FolderInput.addItem(i[1])

        self.stackedWidget.setCurrentIndex(2)
        self.BackBtn.setText('< Back to Scan Templates')
        self.MyScansLabel.setText("New Scan / Web Application Tests")
        self.BackBtn.clicked.connect(self.CreateNewScanBtn.click)

    def lineChart(self, info, low, medium, high, critical):
        self.InfoLabel.setMaximumSize      (1006,16)
        self.LowLabel.setMaximumSize       (1006,16)
        self.MediumLabel.setMaximumSize    (1006,16)
        self.HighLabel.setMaximumSize      (1006,16)
        self.CriticalLabel.setMaximumSize  (1006,16)

        self.CriticalLabel.setText(f"{critical}")
        self.HighLabel.setText(f"{high}")
        self.MediumLabel.setText(f"{medium}")
        self.LowLabel.setText(f"{low}")
        self.InfoLabel.setText(f"{info}")

        self.hide_if_zero(self.CriticalLabel, critical)
        self.hide_if_zero(self.HighLabel, high)
        self.hide_if_zero(self.MediumLabel, medium)
        self.hide_if_zero(self.LowLabel, low)
        self.hide_if_zero(self.InfoLabel, info)

        self.gridLayout_48.setColumnStretch(0,critical)
        self.gridLayout_48.setColumnStretch(1,high)
        self.gridLayout_48.setColumnStretch(2,medium)  
        self.gridLayout_48.setColumnStretch(3,low)
        self.gridLayout_48.setColumnStretch(4,info)

    def get_pie_series(self, chart):
        for series in chart.series():
            if isinstance(series, QPieSeries):
                if series.objectName() == 'center_slice':
                    return series.slices()
        return None

    def access_grid_layout_elements(self, target_layout):
        rows = target_layout.rowCount()
        cols = target_layout.columnCount()

        for row in range(rows):
            for col in range(cols):
                item = target_layout.itemAtPosition(row, col)
                if item is not None:
                    widget = item.widget()
                    if isinstance(widget, QChartView):
                        chart = widget.chart()
                        center_slice = self.get_pie_series(chart)

                        if self.system_theme == "Light":
                            center_slice[0].setBrush(QColor(255,255,255))
                            center_slice[0].setBorderColor(QColor(255,255,255))

                            widget.setStyleSheet('background-color: white;')
                            chart.setBackgroundBrush(QColor(255,255,255))
                        else:
                            center_slice[0].setBrush(QColor(36, 45, 59))
                            center_slice[0].setBorderColor(QColor(36, 45, 59))
                            widget.setStyleSheet('background-color: rgb(36, 45, 59); color: red;')
                            chart.setBackgroundBrush(QColor(36, 45, 59))
                    elif widget:
                        if hasattr(widget, 'text'):
                            print(f"Widget at ({row}, {col}): {widget.text()}")

    def circleChart(self, target_layout, info, low, medium, high, critical):
        self.series = QPieSeries()
        self.slice1 = self.series.append("Critical", critical)
        self.slice2 = self.series.append("High", high)
        self.slice3 = self.series.append("Medium", medium)
        self.slice4 = self.series.append("Low", low)
        self.slice5 = self.series.append("Info", info)

        self.slice1.setBrush(QColor(145, 36, 62))
        self.slice2.setBrush(QColor(221, 75, 80))
        self.slice3.setBrush(QColor(241, 140, 67))
        self.slice4.setBrush(QColor(248, 200, 81))
        self.slice5.setBrush(QColor(103, 172, 225))

        self.slice1.setBorderWidth(2)  # Remove the border
        self.slice2.setBorderWidth(2)  # Remove the border
        self.slice3.setBorderWidth(2)  # Remove the border
        self.slice4.setBorderWidth(2)  # Remove the border
        self.slice5.setBorderWidth(2)  # Remove the border


        self.slice1.setBorderColor(QColor(145, 36, 62))
        self.slice2.setBorderColor(QColor(221, 75, 80))
        self.slice3.setBorderColor(QColor(241, 140, 67))
        self.slice4.setBorderColor(QColor(248, 200, 81))
        self.slice5.setBorderColor(QColor(103, 172, 225))

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.legend().setAlignment(Qt.AlignRight)

        font = self.chart.legend().font()
        font.setPointSize(12)
        self.chart.legend().setFont(font)


        self.chart.legend().setMarkerShape(QLegend.MarkerShapeCircle)


        # Center series (inner circle)
        self.center_series = QPieSeries()
        self.center_series.setObjectName('center_slice')
        self.center_slice = self.center_series.append('', 100)
        self.center_slice.setBrush(QColor(255,255,255))
        self.center_slice.setBorderWidth(2)  # Remove the border
        self.center_slice.setBorderColor(QColor(255,255,255))  # Set the border color to red

        # Adjust pie size to ensure proper coverage
        self.center_series.setPieSize(0.38)

        self.chart.addSeries(self.center_series)
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.chart.setMargins(QMargins(0, 0, 0, 0))

        self.chartview.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.chartview.setMaximumSize(350, 250)
        self.chartview.setMinimumSize(350, 250)

        self.chartview.setStyleSheet('background-color: white;')

        target_layout.addWidget(self.chartview)

        self.DarkMode()

        self.series.hovered.connect(self.showPercentage)

    def showPercentage(self, slice, state):
        if state:  # If hovered
            total = sum([s.value() for s in self.series.slices()])
            percentage = (slice.value() / total) * 100
            QToolTip.showText(QCursor.pos(), f'{percentage:.2f}%')

    def hide_if_zero(self, label, num):
        if num == 0:
            label.setVisible(False)

    def addBtns(self, folderNames, theme=None):
        if theme == "Dark":
            all_buttons = self.SideBar.findChildren(QPushButton)
            for button in all_buttons:
                if button.objectName() == "TrashBtn":
                    button.setStyleSheet('''
                    QPushButton{    
                        height: 40px;
                        font-size: 15px;
                        text-align: left;
                        border: none;
                        color: rgb(29, 210, 227);;
                        background-image: url('png/trash_dark.png');
                        background-position: left center;
                        background-repeat: no-repeat;
                        padding-left: 40px;
                        }
                    QPushButton:checked{ 
                        border-left: 5px solid rgb(0, 131, 155);
                        background-color: rgb(72, 76, 86);
                        color: rgb(29, 212, 228);
                        height: 40px;
                        font-size: 15px;
                        text-align: left;
                        background-image: url('png/trash_dark.png');
                        background-position: left center;
                        background-repeat: no-repeat;
                        padding-left: 40px;
                    }
                    QPushButton:pressed{    
                        text-align: left;
                        text-decoration: underline;
                    }
                    QPushButton:hover {
                        background-color: rgb(72, 83, 98);
                    }
                        ''')
                    continue                    
                button.setStyleSheet('''
                QPushButton{    
                    height: 40px;
                    font-size: 15px;
                    text-align: left;
                    border: none;
                    color: rgb(29, 210, 227);;
                    background-image: url('png/folder_dark.png');
                    background-position: left center;
                    background-repeat: no-repeat;
                    padding-left: 40px;
                    }
                QPushButton:checked{ 
                    border-left: 5px solid rgb(0, 131, 155);
                    background-color: rgb(72, 76, 86);
                    color: rgb(29, 212, 228);
                    height: 40px;
                    font-size: 15px;
                    text-align: left;
                    background-image: url('png/open_folder_dark.png');
                    background-position: left center;
                    background-repeat: no-repeat;
                    padding-left: 40px;
                }
                QPushButton:pressed{    
                    text-align: left;
                    text-decoration: underline;
                }
                QPushButton:hover {
                    background-color: rgb(72, 83, 98);
                }
                    ''')
            return
        if theme == "Light":
            all_buttons = self.SideBar.findChildren(QPushButton)
            for button in all_buttons:
                if button.objectName() == "TrashBtn":
                    button.setStyleSheet('''
                    QPushButton{    
                        height: 40px;
                        font-size: 15px;
                        text-align: left;
                        border: none;
                        color: black;
                        background-image: url('png/trash.png');
                        background-position: left center;
                        background-repeat: no-repeat;
                        padding-left: 40px;
                        }
                    QPushButton:checked{ 
                        border-left: 5px solid rgb(63, 174, 73);
                        background-color: rgb(222, 222, 222);
                        color: black;
                        height: 40px;
                        font-size: 15px;
                        text-align: left;
                        background-image: url('png/trash.png');
                        background-position: left center;
                        background-repeat: no-repeat;
                        padding-left: 40px;
                    }
                    QPushButton:pressed{    
                        text-align: left;
                        text-decoration: underline;
                    }
                    QPushButton:hover {
                        background-color: rgb(38, 55, 70);
                        color: rgb(255, 255, 255);
                    }
                        ''')
                    continue                    
                button.setStyleSheet('''
                QPushButton{    
                    height: 40px;
                    font-size: 15px;
                    text-align: left;
                    border: none;
                    color: black;
                    background-image: url('png/folder.png');
                    background-position: left center;
                    background-repeat: no-repeat;
                    padding-left: 40px;
                    }
                QPushButton:checked{ 
                    border-left: 5px solid rgb(63, 174, 73);
                    background-color: rgb(222, 222, 222);
                    color: black;
                    height: 40px;
                    font-size: 15px;
                    text-align: left;
                    background-image: url('png/open-folder.png');
                    background-position: left center;
                    background-repeat: no-repeat;
                    padding-left: 40px;
                }
                QPushButton:pressed{    
                    text-align: left;
                    text-decoration: underline;
                }
                QPushButton:hover {
                    background-color: rgb(38, 55, 70);
                    color: rgb(255, 255, 255);
                }
                    ''')
            return
        else:
            for i in folderNames:
                self.new_btn = QPushButton(f"{i[1]}", self)
                self.new_btn.setObjectName(i[1])
                self.new_btn.setCheckable(True)
                self.new_btn.setAutoExclusive(True)

                context_menu = QMenu(self)
                delete_action = QAction("Delete", self)
                delete_action.triggered.connect(lambda _, button=self.new_btn: self.deleteButton(button))
                context_menu.addAction(delete_action)
                Rename_action = QAction("Rename", self)
                Rename_action.triggered.connect(lambda _, button=self.new_btn: self.renameButton(button))
                context_menu.addAction(Rename_action)
                self.new_btn.setContextMenuPolicy(3)
                self.new_btn.customContextMenuRequested.connect(
                    lambda pos, button=self.new_btn, menu=context_menu: self.showContextMenu(pos, button, menu)
                )
                if self.system_theme == "Light":
                    self.new_btn.setStyleSheet('''
                    QPushButton{    
                        height: 40px;
                        font-size: 15px;
                        text-align: left;
                        border: none;
                        color: black;
                        background-image: url('png/folder.png');
                        background-position: left center;
                        background-repeat: no-repeat;
                        padding-left: 40px;
                        }
                    QPushButton:checked{ 
                        border-left: 5px solid rgb(63, 174, 73);
                        background-color: rgb(222, 222, 222);
                        color: black;
                        height: 40px;
                        font-size: 15px;
                        text-align: left;
                        background-image: url('png/open-folder.png');
                        background-position: left center;
                        background-repeat: no-repeat;
                        padding-left: 40px;
                    }
                    QPushButton:pressed{    
                        text-align: left;
                        text-decoration: underline;
                    }
                    QPushButton:hover {
                        background-color: rgb(38, 55, 70);
                        color: rgb(255, 255, 255);
                    }
                        ''')
                else:
                    self.new_btn.setStyleSheet('''
                    QPushButton{    
                        height: 40px;
                        font-size: 15px;
                        text-align: left;
                        border: none;
                        color: rgb(29, 210, 227);;
                        background-image: url('png/folder_dark.png');
                        background-position: left center;
                        background-repeat: no-repeat;
                        padding-left: 40px;
                        }
                    QPushButton:checked{ 
                        border-left: 5px solid rgb(0, 131, 155);
                        background-color: rgb(72, 76, 86);
                        color: rgb(29, 212, 228);
                        height: 40px;
                        font-size: 15px;
                        text-align: left;
                        background-image: url('png/open_folder_dark.png');
                        background-position: left center;
                        background-repeat: no-repeat;
                        padding-left: 40px;
                    }
                    QPushButton:pressed{    
                        text-align: left;
                        text-decoration: underline;
                    }
                    QPushButton:hover {
                        background-color: rgb(72, 83, 98);
                    }
                        ''')
                self.new_btn.clicked.connect(self.ClickedBtn)

                index = self.gridLayout_2.indexOf(self.AllScansBtn)
                self.gridLayout_2.addWidget(self.new_btn, self.gridLayout_2.rowCount() , 0)
                self.gridLayout_2.addWidget(self.TrashBtn, self.gridLayout_2.rowCount() + 1, 0)

    def ClickedBtn(self):
        btn = self.sender()
        self.MyScansLabel.setText(btn.text().strip())
        self.ScansTopBarBtn.setChecked(True)
        self.MyAccountBtn.hide()
        self.AboutBtn.hide()
        self.ThemeBtn.hide()
        if btn.objectName() == "AllScansBtn":
            self.stackedWidget.setCurrentIndex(3)
            if DB_V2.check_if_scans_exist():
                self.create_table_scans("All")
            else:
                self.stackedWidget.setCurrentIndex(0)             # if not find any scan for this folder
        elif btn.objectName() == "MyScansBtn": # if find any scan for this folder
            self.stackedWidget.setCurrentIndex(3)
            self.create_table_scans('My Scans')
            self.BackBtn.setText("")

        elif DB_V2.get_data_by_folder_name(btn.objectName()): # if find any scan for this folder
            self.stackedWidget.setCurrentIndex(3)
            self.create_table_scans(btn.objectName())
            self.BackBtn.setText("")
        else:
            self.stackedWidget.setCurrentIndex(0)             # if not find any scan for this folder
            self.BackBtn.setText("")

    def clear_grid_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                    widget.deleteLater()
                else:
                    # If it's a layout, recursively clear it
                    sub_layout = item.layout()
                    if sub_layout is not None:
                        self.clear_grid_layout(sub_layout)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Show and source is self.tab_5:
            # self.create_table_scans_for_vulnerability()
            pass
        return super().eventFilter(source, event)

    def create_table_scans_for_vulnerability(self):
        spacer = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        ParentLayout = QGridLayout()         #######> this is the main layout that all windget inside it 
        MainVLayout = QVBoxLayout()  # create virtival layout to add all widget virticaly and set it as main layout for main widget 
        MainVLayout.setSpacing(0)
        ParentLayout.setContentsMargins(70, 2, 0, 0)

        HLayout = QHBoxLayout()
        CheckBox = QCheckBox()
        SevLabel = QLabel("Sev")
        SevLabel.setFixedSize(57, 22)
        SevLabel.setAlignment(Qt.AlignCenter)

        SevLabel.setStyleSheet('border: none; ')
        CheckBox.setStyleSheet('border: none; ')

        HLayout.addWidget(CheckBox)
        HLayout.addWidget(SevLabel)

        HLayout.addItem(spacer)
        HLayout.setStretch(0,0)
        HLayout.setStretch(1,1)
        HLayout.setSpacing(20)




        HLayout2 = QHBoxLayout()
        NameLabel = QLabel("Name")
        NameLabel.setStyleSheet('border: none; ')
        HLayout2.addWidget(NameLabel)


        HLayout3 = QHBoxLayout()
        FamilyLabel = QLabel("Family")
        FamilyLabel.setStyleSheet('border: none; ')
        HLayout3.addWidget(FamilyLabel)

        HLayout4 = QHBoxLayout()
        CountLabel = QLabel("Count")
        CountLabel.setStyleSheet('border: none; ')
        HLayout4.addWidget(CountLabel)


        HLayout5 = QHBoxLayout()
        EditBtn  = QPushButton()
        EditBtn.setObjectName('EditBtn')
        EditBtn.setIcon(QIcon('png/cogwheel.png'))
        EditBtn.setIconSize(QSize(18, 18))

        EditBtn.setStyleSheet('border: none;')
        HLayout5.addWidget(EditBtn)

        EditBtn.setStyleSheet('''
            QPushButton:hover{border:none; font-size: 25px; margin-left: 40px;color: rgb(165, 165, 165);}
            QPushButton{border:none; font-size: 25px; margin-left: 40px;color: rgb(217, 217, 217);}
            ''')


        MainLayout = QGridLayout()
        # MainLayout.setContentsMargins(10, 0, 20, 0)

        MainLayout.addLayout(HLayout , 0, 0)
        MainLayout.addLayout(HLayout2, 0, 1)
        MainLayout.addLayout(HLayout3, 0, 2)
        MainLayout.addLayout(HLayout4, 0, 3)
        MainLayout.addLayout(HLayout5, 0, 4)

        MainLayout.setColumnStretch(0, 5)
        MainLayout.setColumnStretch(1, 12)
        MainLayout.setColumnStretch(2, 13)
        MainLayout.setColumnStretch(3, 4)
        MainLayout.setColumnStretch(4, 1)


        self.Widget1 = QWidget(self)
        self.Widget1.setObjectName("TopWidget")
        if self.system_theme == "Light":
            self.Widget1.setStyleSheet("border: 1px solid rgb(221, 221, 221); background-color: rgb(245, 245, 245);font-size: 13px; font-weight: bold;")
            SevLabel.setStyleSheet('color: black;border: none;')
            NameLabel.setStyleSheet('color: black;border: none;')
            FamilyLabel.setStyleSheet('color: black;border: none;')
            CountLabel.setStyleSheet('color: black;border: none;')
        else:
            SevLabel.setStyleSheet('color: white;border: none;')
            NameLabel.setStyleSheet('color: white;border: none;')
            FamilyLabel.setStyleSheet('color: white;border: none;')
            CountLabel.setStyleSheet('color: white;border: none;')
            self.Widget1.setStyleSheet("border: 1px solid rgb(72, 73, 80); background-color: rgb(72, 83, 98);font-size: 13px; font-weight: bold;")

        self.Widget1.setMinimumHeight(37)
        self.Widget1.setMaximumHeight(37)

        self.Widget1.setLayout(MainLayout)  # set layout of Widget1 with his elements

        MainVLayout.addLayout(ParentLayout)
        MainVLayout.addWidget(self.Widget1)
        MainVLayout.setContentsMargins(0,9,0,0)

        for i in range(2):
            SevLayout = QHBoxLayout()
            ChildCheckBox = QCheckBox()
            SevLabel = QLabel(f"CRETICAL")
            SevLabel.setObjectName('SevLabel')
            SevLabel.setFixedSize(57, 22)
            ChildCheckBox.setStyleSheet('border: none; ')
            SevLabel.setAlignment(Qt.AlignCenter)


            SevLayout.addWidget(ChildCheckBox)
            SevLayout.addWidget(SevLabel)
            SevLayout.addItem(spacer)
            SevLayout.setStretch(0,0)
            SevLayout.setStretch(1,1)
            SevLayout.setSpacing(20)


            VulNameLayout = QHBoxLayout()
            VulnNameBtn = QPushButton(f"Reflected XSS")
            VulNameLayout.addWidget(VulnNameBtn)


            VulnNameBtn.clicked.connect(lambda: self.show_vuln_info("Reflected XSS"))

            VulnFamilyLayout = QHBoxLayout()
            VulnFamilyLabel = QLabel(f"Cross Site Scripting")
            VulnFamilyLayout.addWidget(VulnFamilyLabel)


            VulnCountLayout = QHBoxLayout()
            VulnCountLabel = QLabel(f"1")
            VulnCountLayout.addWidget(VulnCountLabel)


            BtnsLayout = QHBoxLayout()

            EditVulnBtn = QPushButton()
            EditVulnBtn.setObjectName('EditVulnBtn')
            EditVulnBtn.setIcon(QIcon('png/pen.png'))
            EditVulnBtn.setIconSize(QSize(18, 18))  # Set the size of the icon (optional)

            EditVulnBtn.setStyleSheet('''
                QPushButton:hover{border:none; font-size: 25px; margin-left: 40px;color: rgb(165, 165, 165);}
                QPushButton{border:none; font-size: 25px; margin-left: 40px;color: rgb(217, 217, 217);}
                ''')
            font = QFont("Sitka Subheading Semibold")
            EditVulnBtn.setFont(font)
            EditVulnBtn.setObjectName(f"test5")

            # EditVulnBtn.clicked.connect(self.CancelScan)

            BtnsLayout.addWidget(EditVulnBtn)


            MainLayout = QGridLayout()
            # MainLayout.setContentsMargins(10, 0, 20, 0)



            MainLayout.addLayout(SevLayout       ,0, 0)
            MainLayout.addLayout(VulNameLayout   ,0, 1)
            MainLayout.addLayout(VulnFamilyLayout,0, 2)
            MainLayout.addLayout(VulnCountLayout ,0, 3)
            MainLayout.addLayout(BtnsLayout      ,0, 4)


            MainLayout.setColumnStretch(0, 5)
            MainLayout.setColumnStretch(1, 12)
            MainLayout.setColumnStretch(2, 13)
            MainLayout.setColumnStretch(3, 4)
            MainLayout.setColumnStretch(4, 1)

            self.Widget2 = QWidget(self)
            self.Widget2.setObjectName("DownWidget")
            if self.system_theme == "Light":
                VulnNameBtn.setStyleSheet('QPushButton{border:none; text-align: left;background-color white; color: black;} QPushButton:hover{text-decoration: underline; color: rgb(56, 109, 156);}')
                SevLabel.setStyleSheet('color: black;border: none;background-color: rgb(145, 36, 62); color: white; border-radius: 4px; font-size: 10px; font-weight: normal;')
                VulnFamilyLabel.setStyleSheet('color: black;border: none;font-weight: normal;')
                VulnCountLabel.setStyleSheet('color: black;border: none; text-align: center;')
                self.Widget2.setStyleSheet("border: 1px solid rgb(221, 221, 221); background-color: white;font-size: 13px;")
            else:
                VulnNameBtn.setStyleSheet('QPushButton{border:none; text-align: left;background-color rgb(48, 57, 69); color: white;} QPushButton:hover{text-decoration: underline; color: rgb(56, 109, 156);}')
                SevLabel.setStyleSheet('color: black;border: none;background-color: rgb(145, 36, 62); color: white; border-radius: 4px; font-size: 10px; font-weight: normal;')
                VulnFamilyLabel.setStyleSheet('color: white;border: none;')
                VulnCountLabel.setStyleSheet('color: white;border: none; text-align: center;')
                self.Widget2.setStyleSheet("border: 1px solid rgb(72, 73, 80); background-color: rgb(48, 57, 69);font-size: 13px;")


            self.Widget2.setMinimumHeight(48)
            self.Widget2.setMaximumHeight(48)

            self.Widget2.setLayout(MainLayout)  # set layout of Widget2 with his elements
            MainVLayout.addWidget(self.Widget2)


        self.MainWidget = QWidget(self) # Create Main widget 
        spacer = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        MainVLayout.addItem(spacer)
        self.MainWidget.setLayout(MainVLayout) # add the main Virtical layout that contain all widget with his elements 


        self.gridLayout_64.addWidget(self.MainWidget)  # Add button to row 0, column 0

    def create_table_scans(self, FolderName):
        ParentLayout = QGridLayout()         #######> this is the main layout that all windget inside it 
        MainVLayout = QVBoxLayout()  # create virtival layout to add all widget virticaly and set it as main layout for main widget 
        MainVLayout.setSpacing(0)
        ParentLayout.setContentsMargins(0, 0, 0, 0)

        HLayout = QHBoxLayout()
        self.CheckBox = QCheckBox()
        self.NameLabel = QLabel("Name")

        HLayout.addWidget(self.CheckBox)
        HLayout.addWidget(self.NameLabel)
        HLayout.setStretch(0,0)
        HLayout.setStretch(1,1)
        HLayout.setSpacing(20)


        HLayout2 = QHBoxLayout()
        self.LastModifyLabel = QLabel("        Last Modify")
        HLayout2.addWidget(self.LastModifyLabel)


        HLayout3 = QHBoxLayout()
        self.ScheduleLabel = QLabel("Schedule")
        HLayout3.addWidget(self.ScheduleLabel)


        BtnsLayout = QHBoxLayout()

        self.RunScanBtn = QPushButton("►")
        self.CancelScanBtn = QPushButton("X")
        font = QFont("Sitka Subheading Semibold")
        self.CancelScanBtn.setFont(font)

        BtnsLayout.addWidget(self.RunScanBtn)
        BtnsLayout.addWidget(self.CancelScanBtn)



        MainLayout = QGridLayout()
        MainLayout.setContentsMargins(10, 0, 20, 0)

        MainLayout.addLayout(HLayout,    0, 0)
        MainLayout.addLayout(HLayout3,   0, 1)
        MainLayout.addLayout(HLayout2,   0, 2)
        MainLayout.addLayout(BtnsLayout, 0, 3)

        MainLayout.setColumnStretch(0, 4)
        MainLayout.setColumnStretch(1, 4)
        MainLayout.setColumnStretch(2, 2)

        self.Widget2 = QWidget(self)
        self.Widget2.setMinimumHeight(37)
        self.Widget2.setMaximumHeight(37)

        if self.system_theme == "Light":
            self.Widget2.setStyleSheet(f'background-color: rgb(30,50,30);color; black;')
            self.Widget2.setStyleSheet("border: 1px solid rgb(221, 221, 221); height: 35px; background-color: rgb(245, 245, 245);font-size: 13px; font-weight: bold;color; black;")
            self.CheckBox.setStyleSheet('border-left: none;border-right: none; color; black;')
            self.NameLabel.setStyleSheet('border-left: none;border-right: none;color; black; ')
            self.LastModifyLabel.setStyleSheet('border-left: none;border-right: none;color; black; ')
            self.ScheduleLabel.setStyleSheet('border-left: none;border-right: none;color; black; ')
            self.CancelScanBtn.setStyleSheet('''
                QPushButton{border-left: none;border-right: none; font-size: 25px; margin-left: 40px;color: rgb(245, 245, 245);}
                ''')
            self.RunScanBtn.setStyleSheet("""
                QPushButton {border-left: none;border-right: none; font-size: 17px;color: rgb(245, 245, 245); margin-left: 52px;width: 40px;}
                """)

        else:
            self.Widget2.setStyleSheet(f'background-color: rgb(72, 83, 98); color: rgb(216, 222, 233);')
            self.Widget2.setStyleSheet("border: 1px solid rgb(74, 78, 88); height: 35px; background-color: rgb(72, 83, 98);font-size: 13px; font-weight: bold;")
            self.CheckBox.setStyleSheet('border-left: none;border-right: none; color; black;')

            self.NameLabel.setStyleSheet('QLabel{border-left: none;border-right: none;color: rgb(216, 222, 233);} ')
            self.LastModifyLabel.setStyleSheet('border-left: none;border-right: none; color: rgb(216, 222, 233); ')
            self.ScheduleLabel.setStyleSheet('border-left: none;border-right: none; color: rgb(216, 222, 233);')
            self.CancelScanBtn.setStyleSheet('''
                QPushButton{border-left: none;border-right: none; font-size: 25px; margin-left: 40px;color: rgb(72, 83, 98);}
                ''')
            self.RunScanBtn.setStyleSheet("""
                QPushButton {border-left: none;border-right: none; font-size: 17px;color: rgb(72, 83, 98); margin-left: 52px;width: 40px;}
                """)


        self.Widget2.setLayout(MainLayout)  # set layout of Widget2 with his elements

        MainVLayout.addLayout(ParentLayout)
        MainVLayout.addWidget(self.Widget2)
        
        if FolderName == "All":
            data = DB_V2.get_all_data()
        else:
            data = DB_V2.get_data_by_folder_name(FolderName)
        self.ChildCheckBoxes = []
        for i in data:
            NameLayout = QHBoxLayout()
            self.ChildCheckBox = QCheckBox()
            self.NameBtn = QPushButton(f"{i[1]}")

            NameLayout.addWidget(self.ChildCheckBox)
            NameLayout.addWidget(self.NameBtn)
            NameLayout.setStretch(0,0)
            NameLayout.setStretch(1,1)
            NameLayout.setSpacing(20)

            self.ChildCheckBoxes.append(self.ChildCheckBox)

            self.NameBtn.setObjectName(f"{i[1]}")

            self.NameBtn.clicked.connect(self.host_in_details)


            LastModifyLayout = QHBoxLayout()
            self.LabelText = f'<span style=" display:inline-block; white-space:nowrap;font-size: 20px; ">🗸</span>&nbsp;&nbsp;&nbsp;&nbsp;<span style=" font-size: 13px;">{i[3]}</span>'
            self.LastModifyLabel = QLabel(f"{self.LabelText}")
            LastModifyLayout.addWidget(self.LastModifyLabel)


            ScheduleLayout = QHBoxLayout()
            self.ScheduleLabel = QLabel(f"{i[2]}")
            ScheduleLayout.addWidget(self.ScheduleLabel)


            BtnsLayout = QHBoxLayout()

            self.RunScanBtn = QPushButton("►")
            self.CancelScanBtn = QPushButton("X")
            font = QFont("Sitka Subheading Semibold")
            self.CancelScanBtn.setFont(font)
            self.CancelScanBtn.setObjectName(f"{i[1]}")
            self.RunScanBtn.setObjectName(f"{i[1]}")

            self.RunScanBtn.clicked.connect(self.RunScan)
            self.CancelScanBtn.clicked.connect(self.CancelScan)

            BtnsLayout.addWidget(self.RunScanBtn)
            BtnsLayout.addWidget(self.CancelScanBtn)


            MainLayout = QGridLayout()
            MainLayout.setContentsMargins(10, 0, 20, 0)



            MainLayout.addLayout(NameLayout      , 0, 0)
            MainLayout.addLayout(ScheduleLayout  , 0, 1)
            MainLayout.addLayout(LastModifyLayout, 0, 2)
            MainLayout.addLayout(BtnsLayout      , 0, 3)


            MainLayout.setColumnStretch(0, 4)
            MainLayout.setColumnStretch(1, 4)
            MainLayout.setColumnStretch(2, 2)


            self.Widget2 = QWidget(self)


            if self.system_theme == "Light":
                self.ChildCheckBox.setStyleSheet('border-left: none;border-right: none; ')
                self.NameBtn.setStyleSheet('''
                    QPushButton{border-left: none;border-right: none;text-align: left; color: black;}
                    QPushButton:hover{text-decoration: underline; color: rgb(56, 109, 156);}
                    ''')
                self.LastModifyLabel.setStyleSheet('border-left: none;border-right: none; color: black;')
                self.ScheduleLabel.setStyleSheet('border-left: none;border-right: none;color: black; ')
                self.CancelScanBtn.setStyleSheet('''
                    QPushButton:hover{border-left: none;border-right: none; font-size: 25px; margin-left: 40px;color: rgb(165, 165, 165);}
                    QPushButton{border-left: none;border-right: none; font-size: 25px; margin-left: 40px;color: rgb(217, 217, 217);}
                    ''')
                self.RunScanBtn.setStyleSheet("""
                    QPushButton:hover{border-left: none;border-right: none; font-size: 17px;color: rgb(165, 165, 165); margin-left: 52px;}
                    QPushButton {border-left: none;border-right: none; font-size: 17px;color: rgb(217, 217, 217); margin-left: 52px;width: 40px;}
                    """)
                self.Widget2.setStyleSheet("background-color: white;border: 1px solid rgb(221, 221, 221); height: 60px; font-size: 12px; ")
            else:
                self.ChildCheckBox.setStyleSheet('border-left: none;border-right: none; ')
                self.NameBtn.setStyleSheet('''
                    QPushButton{border-left: none;border-right: none;text-align: left; color: White;}
                    QPushButton:hover{text-decoration: underline; color: rgb(37, 210, 227);}
                    ''')
                self.LastModifyLabel.setStyleSheet('border-left: none;border-right: none;  color:  White;')
                self.ScheduleLabel.setStyleSheet('border-left: none;border-right: none;  color:  White;')
                self.CancelScanBtn.setStyleSheet('''
                    QPushButton{border-left: none;border-right: none; font-size: 25px; margin-left: 40px;color: rgb(255, 89, 89);}
                    QPushButton:hover{color:rgb(153, 0, 0);}

                    ''')
                self.RunScanBtn.setStyleSheet("""
                    QPushButton {border-left: none;border-right: none; font-size: 17px;color: rgb(217, 217, 217); margin-left: 52px;width: 40px;}
                    """)
                self.Widget2.setStyleSheet("background-color: rgb(49, 58, 70);border: 1px solid rgb(77, 80, 90); height: 60px; font-size: 12px; ")



            self.Widget2.setLayout(MainLayout)  # set layout of Widget2 with his elements
            self.Widget2.setMinimumHeight(48)
            self.Widget2.setMaximumHeight(48)
            MainVLayout.addWidget(self.Widget2)



        self.MainWidget = QWidget(self) # Create Main widget 
        spacer = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        MainVLayout.addItem(spacer)
        MainVLayout.setContentsMargins(0,0,20,0)

        self.MainWidget.setLayout(MainVLayout) # add the main Virtical layout that contain all widget with his elements 

        self.ScrollArea.setWidget(self.MainWidget)
        if self.system_theme == "Light":
            self.ScrollArea.setStyleSheet("background-color: white;border: none;")
        else:
            self.ScrollArea.setStyleSheet("background-color: rgb(36, 45, 59);border: none;")
        # self.SearchFindLabel.setText(f"{len(self.child_checkboxes)} Scans")
        # self.SearchFindLabel2.setText(f"{len(self.child_checkboxes)} Scans")
        # self.SearchFindLabel3.setText(f"{len(self.child_checkboxes)} Scans")
        # self.checkbox.stateChanged.connect(self.mark_all_checkBoxes)

    def host_in_details(self):
        self.HostInDesailsTopWidget.setMinimumHeight(37)
        self.HostInDesailsTopWidget.setMaximumHeight(37)
        self.HostInDesailsBottomWidget.setMinimumHeight(48)
        self.HostInDesailsBottomWidget.setMaximumHeight(48)
        self.stackedWidget.setCurrentIndex(4)
        btn = self.sender()
        domain_name = self.extract_domain(DB_V2.get_scan_by_name(btn.objectName())[6])
        self.VulnBtn.setText(f"{domain_name}")
        self.VulnBtn.clicked.connect(lambda: self.HostInDesailsWidget.setCurrentIndex(1))
        all_buttons = self.SideBar.findChildren(QPushButton)
        for button in all_buttons:
            if button.isChecked():
                if button.objectName() == "MyScansBtn":
                    self.BackBtn.setText(f'< Back To My Scans')
                if button.objectName() == "AllScansBtn":
                    self.BackBtn.setText(f'< Back To All Scans')
                if button.objectName() != "AllScansBtn" and button.objectName() != "MyScansBtn":
                    self.BackBtn.setText(f'< Back To {button.objectName()}')

                self.BackBtn.clicked.connect(button.click)

    def show_vuln_info(self, VulnName):
        self.stackedWidget.setCurrentIndex(8)
        self.SeeAlLabel.setText("&nbsp;&nbsp;&nbsp;<a href='http://www.example.com'>Click me to open link</a>")
        self.SeeAlLabel.setOpenExternalLinks(True)

        import Forms_of_vuln

        VulnName, VulnSev, VulnDescriptionForm, VulnImpactesForm, VulnSoluationForm, VulnSeeAlsoForm, VulnOutputForm = Forms_of_vuln.PUT_DELETE_Mathod_Form()

        if VulnSev.strip().lower() == "info":
            self.SevBtn.setStyleSheet('''
                border-radius: 3px;
                font-size: 12px;
                width: 77px;
                height: 22;
                background-color: rgb(103, 172, 225);
                color: white;
                ''')
        elif VulnSev.strip().lower() == "low":
            self.SevBtn.setStyleSheet('''
                border-radius: 3px;
                font-size: 12px;
                width: 77px;
                height: 22;
                background-color: rgb(248, 200, 81);
                color: white;
                ''')
        elif VulnSev.strip().lower() == "medium":
            self.SevBtn.setStyleSheet('''
                border-radius: 3px;
                font-size: 12px;
                width: 77px;
                height: 22;
                background-color: rgb(241, 140, 67);
                color: white;
                ''')
        elif VulnSev.strip().lower() == "high":
            self.SevBtn.setStyleSheet('''
                border-radius: 3px;
                font-size: 12px;
                width: 77px;
                height: 22;
                background-color: rgb(221, 75, 80);
                color: white;
                ''')
        elif VulnSev.strip().lower() == "critical":
            self.SevBtn.setStyleSheet('''
                border-radius: 3px;
                font-size: 12px;
                width: 77px;
                height: 22;
                background-color: rgb(145, 36, 62);
                color: white;
                ''')

        self.DescPlainTextEdit.setText(VulnDescriptionForm.strip())
        self.DescPlainTextEdit.setStyleSheet("font-size: 16px; border: none;")


        self.SoluPlainTextEdit.setText(VulnSoluationForm.strip())
        self.SoluPlainTextEdit.setStyleSheet("font-size: 16px; border: none;")

        self.ImpactsPlainTextEdit.setText(VulnImpactesForm.strip())
        self.ImpactsPlainTextEdit.setStyleSheet("font-size: 16px; border: none;")

        self.SeeAlLabel.setText(VulnSeeAlsoForm.strip())
        self.SeeAlLabel.setStyleSheet("font-size: 16px; height: 70px; border: none;")

        self.OutputPlainTextEdit.setText("""
    CyberScope was able to identify the following PHP version information :

      Version : 5.6.40-38+ubuntu20.04.1+deb.sury.org+1
      Source  : X-Powered-By: PHP/5.6.40-38+ubuntu20.04.1+deb.sury.org+1
            """)
        self.OutputPlainTextEdit.setStyleSheet("font-size: 16px; border: none;")

        desc_hight   = int(self.DescPlainTextEdit.document().size().height())
        solu_hight   = int(self.SoluPlainTextEdit.document().size().height())
        output_hight = int(self.OutputPlainTextEdit.document().size().height())
        impa_hight   = int(self.ImpactsPlainTextEdit.document().size().height())

        self.DescPlainTextEdit.setMaximumSize(16777215 ,desc_hight)
        self.SoluPlainTextEdit.setMaximumSize(16777215 ,solu_hight)
        self.OutputPlainTextEdit.setMaximumSize(16777215 ,output_hight)
        self.ImpactsPlainTextEdit.setMaximumSize(16777215 ,impa_hight)

        self.DescPlainTextEdit.setMinimumSize(16777215 ,desc_hight)
        self.SoluPlainTextEdit.setMinimumSize(16777215 ,solu_hight)
        self.OutputPlainTextEdit.setMinimumSize(16777215 ,output_hight)
        self.ImpactsPlainTextEdit.setMinimumSize(16777215 ,impa_hight)



        self.VulnNameLabel.setText(VulnName.strip())
        self.SevBtn.setText(VulnSev.strip())

    def AddNewFolderWindow(self):

        dialog = Dialog(self)

        # Center the dialog on the screen
        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - dialog.width()) / 2
        y = (screen_geometry.height() - dialog.height()) / 2
        dialog.move(int(x), int(y))

        dialog.mode(self.system_theme)
        dialog.create_folder()
        result = dialog.exec_()
        if result == QDialog.Accepted:
            # new_name = dialog.line_edit.text()
            DB_V2.insert_folder_name(dialog.line_edit.text().strip())
            self.addBtns([(1,dialog.line_edit.text().strip())])
            self.FolderInput.addItem(dialog.line_edit.text().strip())

    def SaveScanInput(self):
        ValidateNameInput  = False
        ValidateTargetInput = False
        if len(self.NameInput.text().strip()) == 0:
            self.NameInput.setToolTip("Field cannot be empty!") 
            if self.system_theme == "Light":
                self.NameInput.setStyleSheet('QLineEdit{border: 1px solid rgb(255, 94, 92);background-color: rgb(255,255,255);color: black;height: 30px; } QLineEdit:focus{border: 1px solid rgb(170, 170, 170);}')
            else:
                self.NameInput.setStyleSheet('border: 1px solid rgb(255, 94, 93);background-color: rgb(36, 45, 59);color: white;height: 30px;')

        elif DB_V2.check_name_exist(self.NameInput.text().strip()):
            self.NameInput.setToolTip("Scan name already exists try another name!")
            if self.system_theme == "Light":
                self.NameInput.setStyleSheet('QLineEdit{border: 1px solid rgb(255, 94, 92);background-color: rgb(255,255,255);color: black;height: 30px;} QLineEdit:focus{border: 1px solid rgb(170, 170, 170);}')
            else:
                self.NameInput.setStyleSheet('border: 1px solid rgb(255, 94, 93);background-color: rgb(36, 45, 59);color: white;height: 30px;')
        else:
            if self.system_theme == "Light":
                self.NameInput.setStyleSheet('QLineEdit{border: 1px solid rgb(204, 204, 204);background-color: rgb(255,255,255);color: black;height: 30px;} QLineEdit:focus{border: 1px solid rgb(170, 170, 170);}')
            else:
                self.NameInput.setStyleSheet('QLineEdit{border: 1px solid rgb(109, 125, 148);background-color: rgb(36, 45, 59);color: white;height: 30px;}QLineEdit:focus{border: 1px solid rgb(28, 210, 227);}')

            ValidateNameInput = True

        if self.is_valid_input(self.TargetInput.text()) and len(self.TargetInput.text().strip()) != 0:
            if self.system_theme == "Light":
                self.TargetInput.setStyleSheet('QLineEdit{border: 1px solid rgb(204, 204, 204);background-color: white;color: black;height: 30px;} QLineEdit:focus{border: 1px solid rgb(170, 170, 170);}')
            else:
                self.TargetInput.setStyleSheet('QLineEdit{border: 1px solid rgb(109, 125, 148);background-color: rgb(36, 45, 59);color: white;height: 30px;}QLineEdit:focus{border: 1px solid rgb(28, 210, 227);}')
            ValidateTargetInput = True
        else:
            self.TargetInput.setToolTip("Please Enter Valid Target Like : 192.168.1.3 or URL or Link or example.com") 
            if self.system_theme == "Light":
                self.TargetInput.setStyleSheet('QLineEdit{border: 1px solid rgb(255, 94, 92);background-color: white;color: black;height: 30px;} QLineEdit:focus{border: 1px solid rgb(170, 170, 170);}')
            else:
                self.TargetInput.setStyleSheet('border: 1px solid rgb(255, 94, 92);background-color: rgb(36, 45, 59);color: white;height: 30px;')

        if ValidateNameInput and ValidateTargetInput:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
            DB_V2.insert_data(self.NameInput.text(), "On Demand", current_datetime, self.FolderInput.currentText(), self.DescriptionInput.toPlainText(), self.TargetInput.text())

            btn = self.find_button_by_text(self.FolderInput.currentText())
            self.NameInput.setText('')
            self.DescriptionInput.setPlainText('')
            self.FolderInput.setCurrentText('')
            self.TargetInput.setText('')
            btn.click()

    def CancelScanInput(self):
        if self.system_theme == "Light":
            self.NameInput.setStyleSheet('QLineEdit{border: 1px solid rgb(204, 204, 204);background-color: rgb(255,255,255);color: black;height: 30px;} QLineEdit:focus{border: 1px solid rgb(170, 170, 170);}')
        else:
            self.NameInput.setStyleSheet('QLineEdit{border: 1px solid rgb(109, 125, 148);background-color: rgb(36, 45, 59);color: white;height: 30px;}QLineEdit:focus{border: 1px solid rgb(28, 210, 227);}')

        if self.system_theme == "Light":
            self.TargetInput.setStyleSheet('QLineEdit{border: 1px solid rgb(204, 204, 204);background-color: rgb(255,255,255);color: black;height: 30px;} QLineEdit:focus{border: 1px solid rgb(170, 170, 170);}')
        else:
            self.TargetInput.setStyleSheet('QLineEdit{border: 1px solid rgb(109, 125, 148);background-color: rgb(36, 45, 59);color: white;height: 30px;}QLineEdit:focus{border: 1px solid rgb(28, 210, 227);}')

        self.NameInput.setText('')
        self.DescriptionInput.setPlainText('')
        self.FolderInput.setCurrentText('')
        self.TargetInput.setText('')
        self.CreateNewScanBtn.click()

    def ScansTopBar(self):
        self.MyScansBtn.click()
        self.ScansTopBarBtn.setChecked(True)
        all_buttons = self.SideBar.findChildren(QPushButton)
        for button in all_buttons:
            button.show()
        self.NewFolderBtn.show()
        self.NewScanBtn.show()
        self.FoldersLabel.setText("FOLDERS")
        self.MyAccountBtn.hide()
        self.AboutBtn.hide()
        self.ThemeBtn.hide()

        font_1 = self.SettingsTopBarBtn.font()
        font_2 = self.ScansTopBarBtn.font()
        font_1.setBold(False)
        font_2.setBold(True)
        self.SettingsTopBarBtn.setFont(font_1)
        self.ScansTopBarBtn.setFont(font_2)

    def find_button_by_text(self, target_text):
        for child in self.SideBar.findChildren(QPushButton):
            if child.text().strip() == target_text:
                return child
        return None

    def SettingPage(self):
        sender_button = self.sender()
        self.stackedWidget.setCurrentIndex(5)
        all_buttons = self.SideBar.findChildren(QPushButton)
        for button in all_buttons:
            button.hide()
        self.NewFolderBtn.hide()
        self.NewScanBtn.hide()
        self.FoldersLabel.setText("SETTINGS")
        self.MyAccountBtn.show()
        self.AboutBtn.show()
        self.ThemeBtn.show()
        self.BackBtn.setText('')
        self.MyAccountBtn.click()
        self.SettingsTopBarBtn.setChecked(True)

        font_1 = self.SettingsTopBarBtn.font()
        font_2 = self.ScansTopBarBtn.font()
        font_1.setBold(True)
        font_2.setBold(False)
        self.SettingsTopBarBtn.setFont(font_1)
        self.ScansTopBarBtn.setFont(font_2)

    def is_valid_ip(self, ip):
        # Define a strong regular expression pattern for a valid IPv4 address
        ip_pattern = re.compile(r'''
            ^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
            (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
        ''', re.VERBOSE)

        return bool(ip_pattern.match(ip))

    def is_valid_url(self, url):
        # Define a regular expression pattern for a valid URL
        url_pattern = re.compile(r'''
            ^(https?|ftp):\/\/   # Protocol (http, https, or ftp)
            (www\.)?              # Optional "www." prefix
            [a-zA-Z0-9_-]+        # Domain name
            (\.[a-zA-Z]{2,})+     # Top-level domain (TLD)
            (:[0-9]+)?            # Optional port number
            (\/[a-zA-Z0-9_.-]*)*  # Path (optional)
            (\?[a-zA-Z0-9_=-]*)*  # Query string (optional)
            (\#[a-zA-Z0-9_]*)*$   # Fragment identifier (optional)
        ''', re.VERBOSE)

        return bool(url_pattern.match(url))

    def is_valid_domain(self, input_str):
        # Define a regular expression pattern for a valid domain
        domain_pattern = re.compile(r'''
            ^(www\.)?              # Optional "www." prefix
            [a-zA-Z0-9_-]+        # Domain name
            (\.[a-zA-Z]{2,})+$     # Top-level domain (TLD)
        ''', re.VERBOSE)

        # Check if the given string matches the domain pattern
        return bool(domain_pattern.match(input_str))

    def is_valid_input(self, input_str):
        is_valid = self.is_valid_ip(input_str)
        if is_valid:
            return input_str

        is_valid = self.is_valid_url(input_str)
        if is_valid:
            return input_str

        is_valid = self.is_valid_domain(input_str)
        if is_valid:
            return input_str

        return False

    def extract_domain(self, url):
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if not domain:
            # If netloc is empty, it's likely an IP address
            domain = parsed_url.path.split('/')[0]  # Extract IP from path
        if domain.startswith('www.'):
            domain = domain[4:]  # Remove 'www.' if present
        return domain

    def RunScan(self):
        btn = self.sender()
        if btn.text() == "►":
            btn.setText("||")
        else:
            btn.setText("►")

    def CancelScan(self):
        btn = self.sender()
        print(btn.objectName())
        reply = QMessageBox.question(self, 'Confirmation', 'Do you want to remove this Scan ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            DB_V2.remove_scan_by_name(btn.objectName())
            print(self.findClickedButton().click())

    def findClickedButton(self):
        for child in self.SideBar.children():
            if isinstance(child, QPushButton) and child.isChecked():
                return child

    def deleteButton(self, button):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure if you delete this folder, all the scans inside it will be deleted as well !', 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            value_to_delete = button.objectName()
            index = self.FolderInput.findText(value_to_delete)
            if index != -1:
                self.FolderInput.removeItem(index)            
            DB_V2.remove_scan_by_folder_name(button.objectName())
            DB_V2.delete_row_by_foldername(button.objectName())

            button.deleteLater()
            self.MyScansBtn.click()

    def renameButton(self, button):
        dialog = Dialog(self)
        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - dialog.width()) / 2
        y = (screen_geometry.height() - dialog.height()) / 2
        dialog.move(int(x), int(y))

        dialog.mode(self.system_theme)
        dialog.rename_folder()
        result = dialog.exec_()
        if result == QDialog.Accepted:
            value_to_delete = button.objectName()
            index = self.FolderInput.findText(value_to_delete)
            if index != -1:
                self.FolderInput.removeItem(index)
            self.FolderInput.addItem(dialog.line_edit.text().strip())      

            DB_V2.rename_folder(button.objectName(),dialog.line_edit.text().strip())

            button.setObjectName(dialog.line_edit.text().strip())
            button.setText(f"{dialog.line_edit.text().strip()}")

    def showContextMenu(self, pos, button, menu):
        global_pos = button.mapToGlobal(pos)
        menu.exec_(global_pos)

    def get_windows_theme(self):
        key_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
        value_name = 'AppsUseLightTheme'

        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
                value, _ = winreg.QueryValueEx(key, value_name)
                return "Light" if value == 1 else "Dark"
        except FileNotFoundError:
            return "Light"

    def load_stylesheet(self, filename):
        # self.clear_widget_styles(self)
        style_file = QFile(filename)
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            content = stream.readAll()
            style_file.close()
            self.setStyleSheet(content)
        else:
            print(f"Failed to open {filename}")

app = QApplication([])
UiWindow = MainWindow()
app.exec_()