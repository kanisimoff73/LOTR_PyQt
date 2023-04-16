from PyQt5 import QtCore, QtGui, QtWidgets
from transliterate import translit
import main
from random import shuffle


class Ui_LOTR(object):
    active_weapon = 0
    active_item = 0
    deck = []
    fear_deck = main.Fear
    shuffle(fear_deck)
    damage_deck = main.Damage
    shuffle(damage_deck)
    discarding_deck = []
    choice_skill_check_deck = [0, 0, 0, 0]
    active_skill_deck = [0, 0, 0, 0]

    def setupUi(self, LOTR):
        LOTR.setObjectName("LOTR")
        LOTR.resize(1818, 1018)
        LOTR.setWindowOpacity(1.0)
        LOTR.setStyleSheet("")
        LOTR.setIconSize(QtCore.QSize(20, 20))
        self.centralwidget = QtWidgets.QWidget(LOTR)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMaximumSize(QtCore.QSize(9999999, 999999))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Table = QtWidgets.QTabWidget(self.centralwidget)
        self.Table.setMinimumSize(QtCore.QSize(1800, 1000))
        self.Table.setObjectName("Table")
        self.Main_table = QtWidgets.QWidget()
        self.Main_table.setObjectName("Main_table")
        self.label = QtWidgets.QLabel(self.Main_table)
        self.label.setGeometry(QtCore.QRect(0, 0, 1800, 1000))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(999999, 1000))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setMouseTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Cards/Planshetka_V2.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.weapon_2 = QtWidgets.QPushButton(self.Main_table)
        self.weapon_2.setEnabled(False)
        self.weapon_2.setGeometry(QtCore.QRect(1202, 510, 161, 228))
        self.weapon_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Cards/Оружие.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weapon_2.setIcon(icon)
        self.weapon_2.setIconSize(QtCore.QSize(160, 240))
        self.weapon_2.setObjectName("weapon_2")
        self.Hero_card = QtWidgets.QLabel(self.Main_table)
        self.Hero_card.setGeometry(QtCore.QRect(555, 500, 451, 247))
        self.Hero_card.setText("")
        self.Hero_card.setPixmap(QtGui.QPixmap("Cards/Карты персонажей/Стандарт.JPG"))
        self.Hero_card.setScaledContents(True)
        self.Hero_card.setObjectName("Hero_card")
        self.item_1 = QtWidgets.QPushButton(self.Main_table)
        self.item_1.setEnabled(False)
        self.item_1.setGeometry(QtCore.QRect(1314, 750, 161, 228))
        self.item_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Cards/Предмет.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.item_1.setIcon(icon1)
        self.item_1.setIconSize(QtCore.QSize(160, 240))
        self.item_1.setObjectName("item_1")
        self.skill_2_activate = QtWidgets.QPushButton(self.Main_table)
        self.skill_2_activate.setEnabled(False)
        self.skill_2_activate.setGeometry(QtCore.QRect(610, 750, 161, 228))
        self.skill_2_activate.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Cards/Подготовленный навык.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skill_2_activate.setIcon(icon2)
        self.skill_2_activate.setIconSize(QtCore.QSize(160, 240))
        self.skill_2_activate.setObjectName("skill_2_activate")
        self.drop_btn = QtWidgets.QPushButton(self.Main_table)
        self.drop_btn.setEnabled(False)
        self.drop_btn.setGeometry(QtCore.QRect(204, 510, 160, 228))
        self.drop_btn.setMaximumSize(QtCore.QSize(999999, 999999))
        self.drop_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Cards/Сброс.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drop_btn.setIcon(icon3)
        self.drop_btn.setIconSize(QtCore.QSize(160, 240))
        self.drop_btn.setObjectName("drop_btn")
        self.armor = QtWidgets.QPushButton(self.Main_table)
        self.armor.setEnabled(False)
        self.armor.setGeometry(QtCore.QRect(1140, 750, 161, 228))
        self.armor.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Cards/Броня.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.armor.setIcon(icon4)
        self.armor.setIconSize(QtCore.QSize(160, 240))
        self.armor.setObjectName("armor")
        self.skill_deck = QtWidgets.QPushButton(self.Main_table)
        self.skill_deck.setEnabled(False)
        self.skill_deck.setGeometry(QtCore.QRect(380, 510, 161, 228))
        self.skill_deck.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Cards/Колода навыков.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skill_deck.setIcon(icon5)
        self.skill_deck.setIconSize(QtCore.QSize(160, 240))
        self.skill_deck.setObjectName("skill_deck")
        self.weapon_1 = QtWidgets.QPushButton(self.Main_table)
        self.weapon_1.setEnabled(False)
        self.weapon_1.setGeometry(QtCore.QRect(1022, 510, 161, 228))
        self.weapon_1.setText("")
        self.weapon_1.setIcon(icon)
        self.weapon_1.setIconSize(QtCore.QSize(160, 240))
        self.weapon_1.setObjectName("weapon_1")
        self.skill_3_activate = QtWidgets.QPushButton(self.Main_table)
        self.skill_3_activate.setEnabled(False)
        self.skill_3_activate.setGeometry(QtCore.QRect(785, 750, 161, 228))
        self.skill_3_activate.setAutoFillBackground(False)
        self.skill_3_activate.setText("")
        self.skill_3_activate.setIcon(icon2)
        self.skill_3_activate.setIconSize(QtCore.QSize(160, 240))
        self.skill_3_activate.setObjectName("skill_3_activate")
        self.choice_skill_3 = QtWidgets.QPushButton(self.Main_table)
        self.choice_skill_3.setEnabled(False)
        self.choice_skill_3.setGeometry(QtCore.QRect(1392, 360, 155, 241))
        self.choice_skill_3.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Cards/Обратная_сторона_навыка.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.choice_skill_3.setIcon(icon6)
        self.choice_skill_3.setIconSize(QtCore.QSize(160, 240))
        self.choice_skill_3.setObjectName("choice_skill_3")
        self.card_down_btn_1 = QtWidgets.QPushButton(self.Main_table)
        self.card_down_btn_1.setEnabled(False)
        self.card_down_btn_1.setGeometry(QtCore.QRect(1392, 310, 155, 23))
        self.card_down_btn_1.setObjectName("card_down_btn_1")
        self.choice_skill_2 = QtWidgets.QPushButton(self.Main_table)
        self.choice_skill_2.setEnabled(False)
        self.choice_skill_2.setGeometry(QtCore.QRect(1574, 70, 155, 241))
        self.choice_skill_2.setText("")
        self.choice_skill_2.setIcon(icon6)
        self.choice_skill_2.setIconSize(QtCore.QSize(160, 240))
        self.choice_skill_2.setObjectName("choice_skill_2")
        self.choice_skill_1 = QtWidgets.QPushButton(self.Main_table)
        self.choice_skill_1.setEnabled(False)
        self.choice_skill_1.setGeometry(QtCore.QRect(1392, 70, 155, 241))
        self.choice_skill_1.setText("")
        self.choice_skill_1.setIcon(icon6)
        self.choice_skill_1.setIconSize(QtCore.QSize(160, 240))
        self.choice_skill_1.setObjectName("choice_skill_1")
        self.choice_skill_4 = QtWidgets.QPushButton(self.Main_table)
        self.choice_skill_4.setEnabled(False)
        self.choice_skill_4.setGeometry(QtCore.QRect(1574, 360, 155, 241))
        self.choice_skill_4.setText("")
        self.choice_skill_4.setIcon(icon6)
        self.choice_skill_4.setIconSize(QtCore.QSize(160, 240))
        self.choice_skill_4.setObjectName("choice_skill_4")
        self.skill_4_activate = QtWidgets.QPushButton(self.Main_table)
        self.skill_4_activate.setEnabled(False)
        self.skill_4_activate.setGeometry(QtCore.QRect(965, 750, 161, 228))
        self.skill_4_activate.setAcceptDrops(False)
        self.skill_4_activate.setAutoFillBackground(False)
        self.skill_4_activate.setText("")
        self.skill_4_activate.setIcon(icon2)
        self.skill_4_activate.setIconSize(QtCore.QSize(160, 240))
        self.skill_4_activate.setCheckable(False)
        self.skill_4_activate.setObjectName("skill_4_activate")
        self.skill_1_activate = QtWidgets.QPushButton(self.Main_table)
        self.skill_1_activate.setEnabled(False)
        self.skill_1_activate.setGeometry(QtCore.QRect(430, 750, 161, 228))
        self.skill_1_activate.setMinimumSize(QtCore.QSize(0, 0))
        self.skill_1_activate.setText("")
        self.skill_1_activate.setIcon(icon2)
        self.skill_1_activate.setIconSize(QtCore.QSize(160, 240))
        self.skill_1_activate.setObjectName("skill_1_activate")
        self.Fear_botton_7 = QtWidgets.QPushButton(self.Main_table)
        self.Fear_botton_7.setEnabled(False)
        self.Fear_botton_7.setGeometry(QtCore.QRect(1150, 260, 160, 228))
        self.Fear_botton_7.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Cards/Обратная_сторона_страха.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Fear_botton_7.setIcon(icon7)
        self.Fear_botton_7.setIconSize(QtCore.QSize(160, 240))
        self.Fear_botton_7.setCheckable(True)
        self.Fear_botton_7.setObjectName("Fear_botton_7")
        self.Damage_botton_2 = QtWidgets.QPushButton(self.Main_table)
        self.Damage_botton_2.setEnabled(False)
        self.Damage_botton_2.setGeometry(QtCore.QRect(348, 20, 160, 228))
        self.Damage_botton_2.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Cards/Обратная_сторона_урона.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Damage_botton_2.setIcon(icon8)
        self.Damage_botton_2.setIconSize(QtCore.QSize(160, 240))
        self.Damage_botton_2.setCheckable(True)
        self.Damage_botton_2.setObjectName("Damage_botton_2")
        self.Damage_botton_6 = QtWidgets.QPushButton(self.Main_table)
        self.Damage_botton_6.setEnabled(False)
        self.Damage_botton_6.setGeometry(QtCore.QRect(1073, 20, 160, 228))
        self.Damage_botton_6.setText("")
        self.Damage_botton_6.setIcon(icon8)
        self.Damage_botton_6.setIconSize(QtCore.QSize(160, 240))
        self.Damage_botton_6.setCheckable(True)
        self.Damage_botton_6.setObjectName("Damage_botton_6")
        self.Damage_botton_5 = QtWidgets.QPushButton(self.Main_table)
        self.Damage_botton_5.setEnabled(False)
        self.Damage_botton_5.setGeometry(QtCore.QRect(890, 20, 160, 228))
        self.Damage_botton_5.setText("")
        self.Damage_botton_5.setIcon(icon8)
        self.Damage_botton_5.setIconSize(QtCore.QSize(160, 240))
        self.Damage_botton_5.setCheckable(True)
        self.Damage_botton_5.setObjectName("Damage_botton_5")
        self.Fear_botton_3 = QtWidgets.QPushButton(self.Main_table)
        self.Fear_botton_3.setEnabled(False)
        self.Fear_botton_3.setGeometry(QtCore.QRect(434, 260, 160, 228))
        self.Fear_botton_3.setText("")
        self.Fear_botton_3.setIcon(icon7)
        self.Fear_botton_3.setIconSize(QtCore.QSize(160, 240))
        self.Fear_botton_3.setCheckable(True)
        self.Fear_botton_3.setObjectName("Fear_botton_3")
        self.Fear_botton_2 = QtWidgets.QPushButton(self.Main_table)
        self.Fear_botton_2.setEnabled(False)
        self.Fear_botton_2.setGeometry(QtCore.QRect(255, 260, 160, 228))
        self.Fear_botton_2.setText("")
        self.Fear_botton_2.setIcon(icon7)
        self.Fear_botton_2.setIconSize(QtCore.QSize(160, 240))
        self.Fear_botton_2.setCheckable(True)
        self.Fear_botton_2.setObjectName("Fear_botton_2")
        self.Damage_counter = QtWidgets.QSpinBox(self.Main_table)
        self.Damage_counter.setEnabled(False)
        self.Damage_counter.setGeometry(QtCore.QRect(120, 100, 42, 61))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(24)
        font.setItalic(True)
        self.Damage_counter.setFont(font)
        self.Damage_counter.setStyleSheet("color: rgb(184, 73, 56);\n"
"background-color: rgb(44, 40, 37);")
        self.Damage_counter.setObjectName("Damage_counter")
        self.Fear_botton_4 = QtWidgets.QPushButton(self.Main_table)
        self.Fear_botton_4.setEnabled(False)
        self.Fear_botton_4.setGeometry(QtCore.QRect(613, 260, 160, 228))
        self.Fear_botton_4.setText("")
        self.Fear_botton_4.setIcon(icon7)
        self.Fear_botton_4.setIconSize(QtCore.QSize(160, 240))
        self.Fear_botton_4.setCheckable(True)
        self.Fear_botton_4.setObjectName("Fear_botton_4")
        self.Fear_botton_1 = QtWidgets.QPushButton(self.Main_table)
        self.Fear_botton_1.setEnabled(False)
        self.Fear_botton_1.setGeometry(QtCore.QRect(76, 260, 160, 228))
        self.Fear_botton_1.setText("")
        self.Fear_botton_1.setIcon(icon7)
        self.Fear_botton_1.setIconSize(QtCore.QSize(160, 240))
        self.Fear_botton_1.setCheckable(True)
        self.Fear_botton_1.setObjectName("Fear_botton_1")
        self.Damage_botton_3 = QtWidgets.QPushButton(self.Main_table)
        self.Damage_botton_3.setEnabled(False)
        self.Damage_botton_3.setGeometry(QtCore.QRect(526, 20, 160, 228))
        self.Damage_botton_3.setText("")
        self.Damage_botton_3.setIcon(icon8)
        self.Damage_botton_3.setIconSize(QtCore.QSize(160, 240))
        self.Damage_botton_3.setCheckable(True)
        self.Damage_botton_3.setObjectName("Damage_botton_3")
        self.Fear_counter = QtWidgets.QSpinBox(self.Main_table)
        self.Fear_counter.setEnabled(False)
        self.Fear_counter.setGeometry(QtCore.QRect(30, 330, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(28)
        font.setItalic(True)
        self.Fear_counter.setFont(font)
        self.Fear_counter.setStyleSheet("background-color: rgb(44, 40, 37);\n"
"color: rgb(46, 137, 123);")
        self.Fear_counter.setObjectName("Fear_counter")
        self.Fear_botton_6 = QtWidgets.QPushButton(self.Main_table)
        self.Fear_botton_6.setEnabled(False)
        self.Fear_botton_6.setGeometry(QtCore.QRect(970, 260, 160, 228))
        self.Fear_botton_6.setText("")
        self.Fear_botton_6.setIcon(icon7)
        self.Fear_botton_6.setIconSize(QtCore.QSize(160, 240))
        self.Fear_botton_6.setCheckable(True)
        self.Fear_botton_6.setObjectName("Fear_botton_6")
        self.Damage_botton_1 = QtWidgets.QPushButton(self.Main_table)
        self.Damage_botton_1.setEnabled(False)
        self.Damage_botton_1.setGeometry(QtCore.QRect(166, 20, 160, 228))
        self.Damage_botton_1.setText("")
        self.Damage_botton_1.setIcon(icon8)
        self.Damage_botton_1.setIconSize(QtCore.QSize(160, 240))
        self.Damage_botton_1.setCheckable(True)
        self.Damage_botton_1.setObjectName("Damage_botton_1")
        self.Fear_botton_5 = QtWidgets.QPushButton(self.Main_table)
        self.Fear_botton_5.setEnabled(False)
        self.Fear_botton_5.setGeometry(QtCore.QRect(790, 260, 160, 228))
        self.Fear_botton_5.setText("")
        self.Fear_botton_5.setIcon(icon7)
        self.Fear_botton_5.setIconSize(QtCore.QSize(160, 240))
        self.Fear_botton_5.setCheckable(True)
        self.Fear_botton_5.setObjectName("Fear_botton_5")
        self.Damage_botton_4 = QtWidgets.QPushButton(self.Main_table)
        self.Damage_botton_4.setEnabled(False)
        self.Damage_botton_4.setGeometry(QtCore.QRect(710, 20, 160, 228))
        self.Damage_botton_4.setText("")
        self.Damage_botton_4.setIcon(icon8)
        self.Damage_botton_4.setIconSize(QtCore.QSize(160, 240))
        self.Damage_botton_4.setCheckable(True)
        self.Damage_botton_4.setObjectName("Damage_botton_4")
        self.item_2 = QtWidgets.QPushButton(self.Main_table)
        self.item_2.setEnabled(False)
        self.item_2.setGeometry(QtCore.QRect(1496, 750, 161, 228))
        self.item_2.setText("")
        self.item_2.setIcon(icon1)
        self.item_2.setIconSize(QtCore.QSize(160, 240))
        self.item_2.setObjectName("item_2")
        self.card_up_btn_3 = QtWidgets.QPushButton(self.Main_table)
        self.card_up_btn_3.setEnabled(False)
        self.card_up_btn_3.setGeometry(QtCore.QRect(1392, 340, 155, 23))
        self.card_up_btn_3.setObjectName("card_up_btn_3")
        self.card_up_btn_4 = QtWidgets.QPushButton(self.Main_table)
        self.card_up_btn_4.setEnabled(False)
        self.card_up_btn_4.setGeometry(QtCore.QRect(1574, 340, 155, 23))
        self.card_up_btn_4.setObjectName("card_up_btn_4")
        self.card_down_btn_2 = QtWidgets.QPushButton(self.Main_table)
        self.card_down_btn_2.setEnabled(False)
        self.card_down_btn_2.setGeometry(QtCore.QRect(1574, 310, 155, 23))
        self.card_down_btn_2.setObjectName("card_down_btn_2")
        self.card_up_btn_2 = QtWidgets.QPushButton(self.Main_table)
        self.card_up_btn_2.setEnabled(False)
        self.card_up_btn_2.setGeometry(QtCore.QRect(1574, 50, 155, 23))
        self.card_up_btn_2.setObjectName("card_up_btn_2")
        self.card_down_btn_4 = QtWidgets.QPushButton(self.Main_table)
        self.card_down_btn_4.setEnabled(False)
        self.card_down_btn_4.setGeometry(QtCore.QRect(1574, 600, 155, 23))
        self.card_down_btn_4.setObjectName("card_down_btn_4")
        self.card_up_btn_1 = QtWidgets.QPushButton(self.Main_table)
        self.card_up_btn_1.setEnabled(False)
        self.card_up_btn_1.setGeometry(QtCore.QRect(1392, 50, 155, 23))
        self.card_up_btn_1.setObjectName("card_up_btn_1")
        self.card_down_btn_3 = QtWidgets.QPushButton(self.Main_table)
        self.card_down_btn_3.setEnabled(False)
        self.card_down_btn_3.setGeometry(QtCore.QRect(1392, 600, 155, 23))
        self.card_down_btn_3.setObjectName("card_down_btn_3")
        self.secrecy = QtWidgets.QPushButton(self.Main_table)
        self.secrecy.setEnabled(False)
        self.secrecy.setGeometry(QtCore.QRect(231, 750, 161, 228))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secrecy.sizePolicy().hasHeightForWidth())
        self.secrecy.setSizePolicy(sizePolicy)
        self.secrecy.setMinimumSize(QtCore.QSize(0, 0))
        self.secrecy.setAutoFillBackground(False)
        self.secrecy.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Cards/Скрытность/Скрытность_рубашка.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.secrecy.setIcon(icon9)
        self.secrecy.setIconSize(QtCore.QSize(171, 243))
        self.secrecy.setShortcut("")
        self.secrecy.setCheckable(True)
        self.secrecy.setObjectName("secrecy")
        self.determination = QtWidgets.QPushButton(self.Main_table)
        self.determination.setEnabled(False)
        self.determination.setGeometry(QtCore.QRect(28, 746, 161, 228))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.determination.sizePolicy().hasHeightForWidth())
        self.determination.setSizePolicy(sizePolicy)
        self.determination.setMinimumSize(QtCore.QSize(0, 0))
        self.determination.setAutoFillBackground(False)
        self.determination.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Cards/Решительность/Решительность_рубашка.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.determination.setIcon(icon10)
        self.determination.setIconSize(QtCore.QSize(171, 243))
        self.determination.setShortcut("")
        self.determination.setCheckable(True)
        self.determination.setObjectName("determination")
        self.courage = QtWidgets.QPushButton(self.Main_table)
        self.courage.setEnabled(False)
        self.courage.setGeometry(QtCore.QRect(30, 510, 161, 228))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.courage.sizePolicy().hasHeightForWidth())
        self.courage.setSizePolicy(sizePolicy)
        self.courage.setMinimumSize(QtCore.QSize(0, 0))
        self.courage.setAutoFillBackground(False)
        self.courage.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Cards/Смелость/Смелость_рубашка.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.courage.setIcon(icon11)
        self.courage.setIconSize(QtCore.QSize(171, 243))
        self.courage.setShortcut("")
        self.courage.setCheckable(True)
        self.courage.setObjectName("courage")
        self.Select_hero_btn = QtWidgets.QPushButton(self.Main_table)
        self.Select_hero_btn.setGeometry(QtCore.QRect(660, 710, 251, 31))
        self.Select_hero_btn.setStyleSheet("background-color: rgb(3, 35, 46);\n"
"color: rgb(182, 155, 9);\n"
"font: 16pt \"Segoe Print\";")
        self.Select_hero_btn.setObjectName("Select_hero_btn")

        self.shuffle_card_btn = QtWidgets.QPushButton(self.Main_table)
        self.shuffle_card_btn.setGeometry(QtCore.QRect(1430, 650, 281, 41))
        self.shuffle_card_btn.setStyleSheet("background-color: rgb(3, 35, 46);\n"
"color: rgb(182, 155, 9);\n"
"font: 16pt \"Segoe Print\";")
        self.shuffle_card_btn.setObjectName("shuffle_card_btn")
        self.shuffle_card_btn.setEnabled(False)

        self.discarding_btn = QtWidgets.QPushButton(self.Main_table)
        self.discarding_btn.setGeometry(QtCore.QRect(1250, 150, 131, 41))
        self.discarding_btn.setStyleSheet("background-color: rgb(3, 35, 46);\n"
"color: rgb(182, 155, 9);\n"
"font: 16pt \"Segoe Print\";")
        self.discarding_btn.setObjectName("discarding_btn")
        self.discarding_btn.setEnabled(False)

        self.Select_hero = QtWidgets.QComboBox(self.Main_table)
        self.Select_hero.setGeometry(QtCore.QRect(695, 504, 171, 31))
        self.Select_hero.setStyleSheet("background-color: rgb(0, 33, 43);\n"
"color: rgb(185, 161, 24);\n"
"font: 22pt \"Segoe Print\";")
        self.Select_hero.setObjectName("Select_hero")
        self.Select_hero.addItem("")
        self.Select_hero.addItem("")
        self.Select_hero.addItem("")
        self.Select_hero.addItem("")
        self.Select_hero.addItem("")
        self.Select_hero.addItem("")
        self.label.raise_()
        self.weapon_2.raise_()
        self.Hero_card.raise_()
        self.item_1.raise_()
        self.skill_2_activate.raise_()
        self.drop_btn.raise_()
        self.armor.raise_()
        self.skill_deck.raise_()
        self.weapon_1.raise_()
        self.skill_3_activate.raise_()
        self.choice_skill_1.raise_()
        self.card_down_btn_3.raise_()
        self.choice_skill_4.raise_()
        self.choice_skill_3.raise_()
        self.choice_skill_2.raise_()
        self.skill_4_activate.raise_()
        self.skill_1_activate.raise_()
        self.Fear_botton_7.raise_()
        self.Damage_botton_2.raise_()
        self.Damage_botton_6.raise_()
        self.Damage_botton_5.raise_()
        self.Fear_botton_3.raise_()
        self.Fear_botton_2.raise_()
        self.Fear_botton_4.raise_()
        self.Fear_botton_1.raise_()
        self.Damage_botton_3.raise_()
        self.Fear_counter.raise_()
        self.Fear_botton_6.raise_()
        self.Damage_botton_1.raise_()
        self.Fear_botton_5.raise_()
        self.Damage_botton_4.raise_()
        self.item_2.raise_()
        self.card_up_btn_3.raise_()
        self.card_up_btn_4.raise_()
        self.card_down_btn_4.raise_()
        self.card_up_btn_2.raise_()
        self.card_down_btn_2.raise_()
        self.card_up_btn_1.raise_()
        self.card_down_btn_1.raise_()
        self.Damage_counter.raise_()
        self.secrecy.raise_()
        self.determination.raise_()
        self.courage.raise_()
        self.Select_hero_btn.raise_()
        self.shuffle_card_btn.raise_()
        self.discarding_btn.raise_()
        self.Select_hero.raise_()
        self.Table.addTab(self.Main_table, "")
        self.Weapon = QtWidgets.QWidget()
        self.Weapon.setObjectName("Weapon")
        self.Table.addTab(self.Weapon, "")
        self.Armor = QtWidgets.QWidget()
        self.Armor.setObjectName("Armor")
        self.Table.addTab(self.Armor, "")
        self.Items = QtWidgets.QWidget()
        self.Items.setObjectName("Items")
        self.Table.addTab(self.Items, "")
        self.Nicknames = QtWidgets.QWidget()
        self.Nicknames.setObjectName("Nicknames")
        self.Table.addTab(self.Nicknames, "")
        self.Weakness = QtWidgets.QWidget()
        self.Weakness.setObjectName("Weakness")
        self.Table.addTab(self.Weakness, "")
        self.Cracker = QtWidgets.QWidget()
        self.Cracker.setObjectName("Cracker")
        self.Table.addTab(self.Cracker, "")
        self.Defender = QtWidgets.QWidget()
        self.Defender.setObjectName("Defender")
        self.Table.addTab(self.Defender, "")
        self.Leader = QtWidgets.QWidget()
        self.Leader.setObjectName("Leader")
        self.Table.addTab(self.Leader, "")
        self.Musician = QtWidgets.QWidget()
        self.Musician.setObjectName("Musician")
        self.Table.addTab(self.Musician, "")
        self.Hunter = QtWidgets.QWidget()
        self.Hunter.setObjectName("Hunter")
        self.Table.addTab(self.Hunter, "")
        self.Pathfinder = QtWidgets.QWidget()
        self.Pathfinder.setObjectName("Pathfinder")
        self.Table.addTab(self.Pathfinder, "")
        self.Discard = QtWidgets.QWidget()
        self.Discard.setObjectName("Discard")
        self.Table.addTab(self.Discard, "")
        self.gridLayout.addWidget(self.Table, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        LOTR.setCentralWidget(self.centralwidget)

        self.retranslateUi(LOTR)
        self.Table.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LOTR)
        self.select_hero_click()
        self.disarmament_click()
        self.disarmor_click()
        self.disitem_click()
        self.determination_click()
        self.secrecy_click()
        self.courage_click()
        self.skill_deck_click()
        self.shuffle_card_btn_click()
        self.discarding_btn_click()
        self.drop_click()



        x = 0
        y = 0
        for i, v in enumerate(main.Weapon):
            exec(f'''self.weapon{i} = QtWidgets.QPushButton(self.Weapon)''')
            exec(f'''self.weapon{i}.setEnabled(True)''')
            exec(f'''self.weapon{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.weapon{i}.setText("")''')
            exec(f'''icon_weapon{i} = QtGui.QIcon()''')
            exec(f'''icon_weapon{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.weapon{i}.setIcon(icon_weapon{i})''')
            exec(f'''self.weapon{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.weapon{i}.setObjectName(f"weapon{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250
            exec(f'''self.weapon{i}_click()''')

        x = 0
        y = 0
        for i, v in enumerate(main.Armor):
            exec(f'''self.armor{i} = QtWidgets.QPushButton(self.Armor)''')
            exec(f'''self.armor{i}.setEnabled(True)''')
            exec(f'''self.armor{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.armor{i}.setText("")''')
            exec(f'''icon_armor{i} = QtGui.QIcon()''')
            exec(f'''icon_armor{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.armor{i}.setIcon(icon_armor{i})''')
            exec(f'''self.armor{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.armor{i}.setObjectName(f"armor{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250
            exec(f'''self.armor{i}_click()''')

        x = 0
        y = 0
        for i, v in enumerate(main.Items):
            exec(f'''self.item{i} = QtWidgets.QPushButton(self.Items)''')
            exec(f'''self.item{i}.setEnabled(True)''')
            exec(f'''self.item{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.item{i}.setText("")''')
            exec(f'''icon_item{i} = QtGui.QIcon()''')
            exec(f'''icon_item{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.item{i}.setIcon(icon_item{i})''')
            exec(f'''self.item{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.item{i}.setObjectName(f"item{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250
            exec(f'''self.item{i}_click()''')

        x = 0
        y = 0
        for i, v in enumerate(main.Nicknames):
            exec(f'''self.nickname{i} = QtWidgets.QPushButton(self.Nicknames)''')
            exec(f'''self.nickname{i}.setEnabled(True)''')
            exec(f'''self.nickname{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.nickname{i}.setText("")''')
            exec(f'''icon_nickname{i} = QtGui.QIcon()''')
            exec(f'''icon_nickname{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.nickname{i}.setIcon(icon_nickname{i})''')
            exec(f'''self.nickname{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.nickname{i}.setCheckable(True)''')
            exec(f'''self.nickname{i}.setObjectName(f"nickname{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250
            exec(f'''self.nickname{i}_click()''')

        x = 0
        y = 0
        for i, v in enumerate(main.Weakness):
            exec(f'''self.weaknes{i} = QtWidgets.QPushButton(self.Weakness)''')
            exec(f'''self.weaknes{i}.setEnabled(True)''')
            exec(f'''self.weaknes{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.weaknes{i}.setText("")''')
            exec(f'''icon_weaknes{i} = QtGui.QIcon()''')
            exec(f'''icon_weaknes{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.weaknes{i}.setIcon(icon_weaknes{i})''')
            exec(f'''self.weaknes{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.weaknes{i}.setCheckable(True)''')
            exec(f'''self.weaknes{i}.setObjectName(f"weaknes{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250
            exec(f'''self.weaknes{i}_click()''')

        x = 0
        y = 0
        for i, v in enumerate(main.Cracker_plus):
            exec(f'''self.cracker{i} = QtWidgets.QPushButton(self.Cracker)''')
            exec(f'''self.cracker{i}.setEnabled(True)''')
            exec(f'''self.cracker{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.cracker{i}.setText("")''')
            exec(f'''icon_cracker{i} = QtGui.QIcon()''')
            exec(f'''icon_cracker{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.cracker{i}.setIcon(icon_cracker{i})''')
            exec(f'''self.cracker{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.cracker{i}.setCheckable(True)''')
            exec(f'''self.cracker{i}.setObjectName(f"cracker{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250
            exec(f'''self.cracker{i}_click()''')

        x = 0
        y = 0
        for i, v in enumerate(main.Defender_plus):
            exec(f'''self.defender{i} = QtWidgets.QPushButton(self.Defender)''')
            exec(f'''self.defender{i}.setEnabled(True)''')
            exec(f'''self.defender{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.defender{i}.setText("")''')
            exec(f'''icon_defender{i} = QtGui.QIcon()''')
            exec(f'''icon_defender{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.defender{i}.setIcon(icon_defender{i})''')
            exec(f'''self.defender{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.defender{i}.setCheckable(True)''')
            exec(f'''self.defender{i}.setObjectName(f"defender{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250
            exec(f'''self.defender{i}_click()''')

        x = 0
        y = 0
        for i, v in enumerate(main.Leader_plus):
            exec(f'''self.leader{i} = QtWidgets.QPushButton(self.Leader)''')
            exec(f'''self.leader{i}.setEnabled(True)''')
            exec(f'''self.leader{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.leader{i}.setText("")''')
            exec(f'''icon_leader{i} = QtGui.QIcon()''')
            exec(f'''icon_leader{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.leader{i}.setIcon(icon_leader{i})''')
            exec(f'''self.leader{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.leader{i}.setCheckable(True)''')
            exec(f'''self.leader{i}.setObjectName(f"leader{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250
            exec(f'''self.leader{i}_click()''')

        x = 0
        y = 0
        for i, v in enumerate(main.Musician_plus):
            exec(f'''self.musician{i} = QtWidgets.QPushButton(self.Musician)''')
            exec(f'''self.musician{i}.setEnabled(True)''')
            exec(f'''self.musician{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.musician{i}.setText("")''')
            exec(f'''icon_musician{i} = QtGui.QIcon()''')
            exec(f'''icon_musician{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.musician{i}.setIcon(icon_musician{i})''')
            exec(f'''self.musician{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.musician{i}.setCheckable(True)''')
            exec(f'''self.musician{i}.setObjectName(f"musician{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250
            exec(f'''self.musician{i}_click()''')

        x = 0
        y = 0
        for i, v in enumerate(main.Hunter_plus):
            exec(f'''self.hunter{i} = QtWidgets.QPushButton(self.Hunter)''')
            exec(f'''self.hunter{i}.setEnabled(True)''')
            exec(f'''self.hunter{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.hunter{i}.setText("")''')
            exec(f'''icon_hunter{i} = QtGui.QIcon()''')
            exec(f'''icon_hunter{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.hunter{i}.setIcon(icon_hunter{i})''')
            exec(f'''self.hunter{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.hunter{i}.setCheckable(True)''')
            exec(f'''self.hunter{i}.setObjectName(f"hunter{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250
            exec(f'''self.hunter{i}_click()''')

        x = 0
        y = 0
        for i, v in enumerate(main.Pathfinder_plus):
            exec(f'''self.pathfinder{i} = QtWidgets.QPushButton(self.Pathfinder)''')
            exec(f'''self.pathfinder{i}.setEnabled(True)''')
            exec(f'''self.pathfinder{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.pathfinder{i}.setText("")''')
            exec(f'''icon_pathfinder{i} = QtGui.QIcon()''')
            exec(f'''icon_pathfinder{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.pathfinder{i}.setIcon(icon_pathfinder{i})''')
            exec(f'''self.pathfinder{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.pathfinder{i}.setCheckable(True)''')
            exec(f'''self.pathfinder{i}.setObjectName(f"pathfinder{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250
            exec(f'''self.pathfinder{i}_click()''')

        for fear_num in range(1, 8):
            exec(f'''self.fear_click{fear_num}()''')

        for damage_num in range(1, 7):
            exec(f'''self.damage_click{damage_num}()''')

        for i in range(1, 5):
            exec(f'''self.card_up{i}_click()''')

        for i in range(1, 5):
            exec(f'''self.card_down{i}_click()''')

        for i in range(1, 5):
            exec(f'''self.preparing{i}_click()''')

        for i in range(1, 5):
            exec(f'''self.use_skill{i}_click()''')




#==============================================================================






    def retranslateUi(self, LOTR):
        _translate = QtCore.QCoreApplication.translate
        LOTR.setWindowTitle(_translate("LOTR", "LOTR"))
        self.card_down_btn_3.setText(_translate("LOTR", "Вниз"))
        self.card_up_btn_3.setText(_translate("LOTR", "Вверх"))
        self.card_up_btn_4.setText(_translate("LOTR", "Вверх"))
        self.card_down_btn_4.setText(_translate("LOTR", "Вниз"))
        self.card_up_btn_2.setText(_translate("LOTR", "Вверх"))
        self.card_down_btn_2.setText(_translate("LOTR", "Вниз"))
        self.card_up_btn_1.setText(_translate("LOTR", "Вверх"))
        self.card_down_btn_1.setText(_translate("LOTR", "Вниз"))
        self.Select_hero_btn.setText(_translate("LOTR", "Подтвердить выбор"))
        self.shuffle_card_btn.setText(_translate("LOTR", "Перемешать колоду"))
        self.discarding_btn.setText(_translate("LOTR", "В сброс"))
        self.Select_hero.setItemText(0, _translate("LOTR", "Гимли"))
        self.Select_hero.setItemText(1, _translate("LOTR", "Леголас"))
        self.Select_hero.setItemText(2, _translate("LOTR", "Елена"))
        self.Select_hero.setItemText(3, _translate("LOTR", "Беравор"))
        self.Select_hero.setItemText(4, _translate("LOTR", "Арагорн"))
        self.Select_hero.setItemText(5, _translate("LOTR", "Бильбо"))
        self.Table.setTabText(self.Table.indexOf(self.Main_table), _translate("LOTR", "Main"))
        self.Table.setTabText(self.Table.indexOf(self.Weapon), _translate("LOTR", "Оружие"))
        self.Table.setTabText(self.Table.indexOf(self.Armor), _translate("LOTR", "Броня"))
        self.Table.setTabText(self.Table.indexOf(self.Items), _translate("LOTR", "Вещи"))
        self.Table.setTabText(self.Table.indexOf(self.Nicknames), _translate("LOTR", "Прозвища"))
        self.Table.setTabText(self.Table.indexOf(self.Weakness), _translate("LOTR", "Слабость"))
        self.Table.setTabText(self.Table.indexOf(self.Cracker), _translate("LOTR", "Взломщик"))
        self.Table.setTabText(self.Table.indexOf(self.Defender), _translate("LOTR", "Защитник"))
        self.Table.setTabText(self.Table.indexOf(self.Leader), _translate("LOTR", "Лидер"))
        self.Table.setTabText(self.Table.indexOf(self.Musician), _translate("LOTR", "Музыкант"))
        self.Table.setTabText(self.Table.indexOf(self.Hunter), _translate("LOTR", "Охотник"))
        self.Table.setTabText(self.Table.indexOf(self.Pathfinder), _translate("LOTR", "Следопыт"))
        self.Table.setTabText(self.Table.indexOf(self.Discard), _translate("LOTR", "Сброс"))

    for i, v in enumerate(main.Weapon):
        exec(f'''def weapon{i}_click(self):
            self.weapon{i}.clicked.connect(lambda: self.select_weapon('{v}'))''')

    def select_weapon(self, path):
        active_weapon_icon = QtGui.QIcon()
        active_weapon_icon.addPixmap(QtGui.QPixmap(f"{path}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if Ui_LOTR.active_weapon == 0:
            Ui_LOTR.active_weapon += 1
            self.weapon_1.setIcon(active_weapon_icon)
            self.weapon_1.setGeometry(QtCore.QRect(1027, 500, 155, 241))
        else:
            self.weapon_2.setIcon(active_weapon_icon)
            self.weapon_2.setGeometry(QtCore.QRect(1204, 500, 155, 241))

    def disarmament_click(self):
        self.weapon_1.clicked.connect(self.disarmament_1)
        self.weapon_2.clicked.connect(self.disarmament_2)

    def disarmament_1(self):
        if Ui_LOTR.active_weapon != 0:
            Ui_LOTR.active_weapon -= 1
        deactive_weapon_icon = QtGui.QIcon()
        deactive_weapon_icon.addPixmap(QtGui.QPixmap("Cards\Оружие.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weapon_1.setIcon(deactive_weapon_icon)
        self.weapon_1.setGeometry(QtCore.QRect(1022, 510, 161, 228))

    def disarmament_2(self):
        deactive_weapon_icon = QtGui.QIcon()
        deactive_weapon_icon.addPixmap(QtGui.QPixmap("Cards\Оружие.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weapon_2.setIcon(deactive_weapon_icon)
        self.weapon_2.setGeometry(QtCore.QRect(1202, 510, 161, 228))

    for i, v in enumerate(main.Armor):
        exec(f'''def armor{i}_click(self):
            self.armor{i}.clicked.connect(lambda: self.select_armor('{v}'))''')

    def select_armor(self, path):
        active_armor_icon = QtGui.QIcon()
        active_armor_icon.addPixmap(QtGui.QPixmap(f"{path}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.armor.setIcon(active_armor_icon)
        self.armor.setGeometry(QtCore.QRect(1141, 742, 155, 241))

    def disarmor_click(self):
        self.armor.clicked.connect(self.disarmor)

    def disarmor(self):
        deactive_armor_icon = QtGui.QIcon()
        deactive_armor_icon.addPixmap(QtGui.QPixmap("Cards\Броня.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.armor.setIcon(deactive_armor_icon)
        self.armor.setGeometry(QtCore.QRect(1140, 750, 161, 228))

    for i, v in enumerate(main.Items):
        exec(f'''def item{i}_click(self):
            self.item{i}.clicked.connect(lambda: self.select_item('{v}'))''')

    def select_item(self, path):
        active_item_icon = QtGui.QIcon()
        active_item_icon.addPixmap(QtGui.QPixmap(f"{path}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if Ui_LOTR.active_item == 0:
            Ui_LOTR.active_item += 1
            self.item_1.setIcon(active_item_icon)
            self.item_1.setGeometry(QtCore.QRect(1318, 742, 155, 241))
        else:
            self.item_2.setIcon(active_item_icon)
            self.item_2.setGeometry(QtCore.QRect(1497, 742, 155, 241))

    def disitem_click(self):
        self.item_1.clicked.connect(self.disitem_1)
        self.item_2.clicked.connect(self.disitem_2)

    def disitem_1(self):
        if Ui_LOTR.active_item != 0:
            Ui_LOTR.active_item -= 1
        deactive_item_icon = QtGui.QIcon()
        deactive_item_icon.addPixmap(QtGui.QPixmap("Cards\Предмет.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.item_1.setIcon(deactive_item_icon)
        self.item_1.setGeometry(QtCore.QRect(1314, 750, 161, 228))

    def disitem_2(self):
        deactive_item_icon = QtGui.QIcon()
        deactive_item_icon.addPixmap(QtGui.QPixmap("Cards\Предмет.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.item_2.setIcon(deactive_item_icon)
        self.item_2.setGeometry(QtCore.QRect(1496, 750, 161, 228))

    for i, v in enumerate(main.Nicknames):
        exec(f'''def nickname{i}_click(self):
            self.nickname{i}.clicked.connect(lambda: self.select_nickname('{v}', '{i}'))''')

    def select_nickname(self, path, num):
        exec(f'''if self.nickname{num}.isChecked():
            Ui_LOTR.deck.append('{path}')
            self.nickname{num}.setIconSize(QtCore.QSize(100, 200))
else:
    self.nickname{num}.setIconSize(QtCore.QSize(160, 240))
    Ui_LOTR.deck.remove('{path}')''')


    for i, v in enumerate(main.Weakness):
        exec(f'''def weaknes{i}_click(self):
            self.weaknes{i}.clicked.connect(lambda: self.select_weaknes('{v}', '{i}'))''')

    def select_weaknes(self, path, num):
        exec(f'''if self.weaknes{num}.isChecked():
            Ui_LOTR.deck.append('{path}')
            self.weaknes{num}.setIconSize(QtCore.QSize(100, 200))
else:
    self.weaknes{num}.setIconSize(QtCore.QSize(160, 240))
    Ui_LOTR.deck.remove('{path}')''')


    for i, v in enumerate(main.Cracker_plus):
        exec(f'''def cracker{i}_click(self):
            self.cracker{i}.clicked.connect(lambda: self.select_cracker('{v}', '{i}'))''')

    def select_cracker(self, path, num):
        exec(f'''if self.cracker{num}.isChecked():
            Ui_LOTR.deck.append('{path}')
            self.cracker{num}.setIconSize(QtCore.QSize(100, 200))
else:
    self.cracker{num}.setIconSize(QtCore.QSize(160, 240))
    Ui_LOTR.deck.remove('{path}')''')

    for i, v in enumerate(main.Defender_plus):
        exec(f'''def defender{i}_click(self):
            self.defender{i}.clicked.connect(lambda: self.select_defender('{v}', '{i}'))''')

    def select_defender(self, path, num):
        exec(f'''if self.defender{num}.isChecked():
            Ui_LOTR.deck.append('{path}')
            self.defender{num}.setIconSize(QtCore.QSize(100, 200))
else:
    self.defender{num}.setIconSize(QtCore.QSize(160, 240))
    Ui_LOTR.deck.remove('{path}')''')

    for i, v in enumerate(main.Leader_plus):
        exec(f'''def leader{i}_click(self):
            self.leader{i}.clicked.connect(lambda: self.select_leader('{v}', '{i}'))''')

    def select_leader(self, path, num):
        exec(f'''if self.leader{num}.isChecked():
            Ui_LOTR.deck.append('{path}')
            self.leader{num}.setIconSize(QtCore.QSize(100, 200))
else:
    self.leader{num}.setIconSize(QtCore.QSize(160, 240))
    Ui_LOTR.deck.remove('{path}')''')

    for i, v in enumerate(main.Musician_plus):
        exec(f'''def musician{i}_click(self):
            self.musician{i}.clicked.connect(lambda: self.select_musician('{v}', '{i}'))''')

    def select_musician(self, path, num):
        exec(f'''if self.musician{num}.isChecked():
            Ui_LOTR.deck.append('{path}')
            self.musician{num}.setIconSize(QtCore.QSize(100, 200))
else:
    self.musician{num}.setIconSize(QtCore.QSize(160, 240))
    Ui_LOTR.deck.remove('{path}')''')

    for i, v in enumerate(main.Hunter_plus):
        exec(f'''def hunter{i}_click(self):
            self.hunter{i}.clicked.connect(lambda: self.select_hunter('{v}', '{i}'))''')

    def select_hunter(self, path, num):
        exec(f'''if self.hunter{num}.isChecked():
            Ui_LOTR.deck.append('{path}')
            self.hunter{num}.setIconSize(QtCore.QSize(100, 200))
else:
    self.hunter{num}.setIconSize(QtCore.QSize(160, 240))
    Ui_LOTR.deck.remove('{path}')''')

    for i, v in enumerate(main.Pathfinder_plus):
        exec(f'''def pathfinder{i}_click(self):
            self.pathfinder{i}.clicked.connect(lambda: self.select_pathfinder('{v}', '{i}'))''')

    def select_pathfinder(self, path, num):
        exec(f'''if self.pathfinder{num}.isChecked():
            Ui_LOTR.deck.append('{path}')
            self.pathfinder{num}.setIconSize(QtCore.QSize(100, 200))
else:
    self.pathfinder{num}.setIconSize(QtCore.QSize(160, 240))
    Ui_LOTR.deck.remove('{path}')''')

    def courage_click(self):
        self.courage.clicked.connect(self.courage_)

    def courage_(self):
        if self.courage.isChecked():
            icon_courage = QtGui.QIcon()
            icon_courage.addPixmap(QtGui.QPixmap("Cards/Смелость/Смелость.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.courage.setIcon(icon_courage)
            self.courage.setGeometry(QtCore.QRect(32, 500, 155, 241))
        else:
            icon_courage = QtGui.QIcon()
            icon_courage.addPixmap(QtGui.QPixmap("Cards/Смелость/Смелость_рубашка.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.courage.setIcon(icon_courage)
            self.courage.setGeometry(QtCore.QRect(30, 510, 161, 228))

    def determination_click(self):
        self.determination.clicked.connect(self.determination_)

    def determination_(self):
        if self.determination.isChecked():
            icon_determination = QtGui.QIcon()
            icon_determination.addPixmap(QtGui.QPixmap("Cards/Решительность/Решительность.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.determination.setIcon(icon_determination)
            self.determination.setGeometry(QtCore.QRect(31, 741, 155, 241))
        else:
            icon_determination = QtGui.QIcon()
            icon_determination.addPixmap(QtGui.QPixmap("Cards/Решительность/Решительность_рубашка.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.determination.setIcon(icon_determination)
            self.determination.setGeometry(QtCore.QRect(28, 746, 161, 228))

    def secrecy_click(self):
        self.secrecy.clicked.connect(self.secrecy_)

    def secrecy_(self):
        if self.secrecy.isChecked():
            icon_secrecy = QtGui.QIcon()
            icon_secrecy.addPixmap(QtGui.QPixmap("Cards/Скрытность/Скрытность.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.secrecy.setIcon(icon_secrecy)
            self.secrecy.setGeometry(QtCore.QRect(233, 745, 155, 241))
        else:
            icon_secrecy = QtGui.QIcon()
            icon_secrecy.addPixmap(QtGui.QPixmap("Cards/Скрытность/Скрытность_рубашка.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.secrecy.setIcon(icon_secrecy)
            self.secrecy.setGeometry(QtCore.QRect(231, 750, 161, 228))

    for fear_num in range(1, 8):
        exec(f'''def fear_click{fear_num}(self):
            self.Fear_botton_{fear_num}.clicked.connect(lambda: self.fear_up({fear_num}))''')

    def fear_up(self, fear_num):
        exec(f'''if self.Fear_botton_{fear_num}.isChecked():
            icon_fear_path{fear_num} = Ui_LOTR.fear_deck.pop()
            icon_fear{fear_num} = QtGui.QIcon()
            icon_fear{fear_num}.addPixmap(QtGui.QPixmap(icon_fear_path{fear_num}), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Fear_botton_{fear_num}.setIcon(icon_fear{fear_num})
            self.Fear_botton_{fear_num}.setGeometry(QtCore.QRect(self.Fear_botton_{fear_num}.geometry().getRect()[0] + 3, self.Fear_botton_{fear_num}.geometry().getRect()[1], 155, 241))
            Ui_LOTR.fear_deck[:0] = [icon_fear_path{fear_num}]
else:
    icon_fear = QtGui.QIcon()
    icon_fear.addPixmap(QtGui.QPixmap("Cards/Обратная_сторона_страха"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.Fear_botton_{fear_num}.setGeometry(QtCore.QRect(self.Fear_botton_{fear_num}.geometry().getRect()[0] - 3, self.Fear_botton_{fear_num}.geometry().getRect()[1], 160, 228))
    self.Fear_botton_{fear_num}.setIcon(icon_fear)''')

    for damage_num in range(1, 7):
        exec(f'''def damage_click{damage_num}(self):
            self.Damage_botton_{damage_num}.clicked.connect(lambda: self.damage_up({damage_num}))''')

    def damage_up(self, damage_num):
        exec(f'''if self.Damage_botton_{damage_num}.isChecked():
            icon_damage_path{damage_num} = Ui_LOTR.damage_deck.pop()
            icon_damage{damage_num} = QtGui.QIcon()
            icon_damage{damage_num}.addPixmap(QtGui.QPixmap(icon_damage_path{damage_num}), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Damage_botton_{damage_num}.setIcon(icon_damage{damage_num})
            self.Damage_botton_{damage_num}.setGeometry(QtCore.QRect(self.Damage_botton_{damage_num}.geometry().getRect()[0] + 1, self.Damage_botton_{damage_num}.geometry().getRect()[1], 155, 241))
            Ui_LOTR.damage_deck[:0] = [icon_damage_path{damage_num}]
else:
    icon_damage = QtGui.QIcon()
    icon_damage.addPixmap(QtGui.QPixmap("Cards/Обратная_сторона_урона"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.Damage_botton_{damage_num}.setGeometry(QtCore.QRect(self.Damage_botton_{damage_num}.geometry().getRect()[0] - 1, self.Damage_botton_{damage_num}.geometry().getRect()[1], 160, 228))
    self.Damage_botton_{damage_num}.setIcon(icon_damage)''')

    for i in range(1, 5):
        exec(f'''def card_up{i}_click(self):
            self.card_up_btn_{i}.clicked.connect(lambda: self.card_up({i}))''')

    def card_up(self, ind):
        card = Ui_LOTR.choice_skill_check_deck[ind-1]
        if card:
            Ui_LOTR.deck.append(card)
            Ui_LOTR.choice_skill_check_deck[ind - 1] = 0
            icon_up = QtGui.QIcon()
            icon_up.addPixmap(QtGui.QPixmap('Cards/Обратная_сторона_навыка.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            exec(f'self.choice_skill_{ind}.setIcon(icon_up)')


    for i in range(1, 5):
        exec(f'''def card_down{i}_click(self):
            self.card_down_btn_{i}.clicked.connect(lambda: self.card_down({i}))''')

    def card_down(self, ind):
        card = Ui_LOTR.choice_skill_check_deck[ind-1]
        if card:
            Ui_LOTR.deck[:0] = [card]
            Ui_LOTR.choice_skill_check_deck[ind - 1] = 0
            icon_up = QtGui.QIcon()
            icon_up.addPixmap(QtGui.QPixmap('Cards/Обратная_сторона_навыка.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            exec(f'self.choice_skill_{ind}.setIcon(icon_up)')

    for i in range(1, 5):
        exec(f'''def preparing{i}_click(self):
            self.choice_skill_{i}.clicked.connect(lambda: self.preparing({i}))''')

    def preparing(self, ind):
        card = Ui_LOTR.choice_skill_check_deck[ind-1]
        if card:

            for index, occupied in enumerate(Ui_LOTR.active_skill_deck):
                if not occupied:
                    Ui_LOTR.active_skill_deck[index] = card
                    icon_active = QtGui.QIcon()
                    icon_active.addPixmap(QtGui.QPixmap(f'{card}'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    exec(f'self.skill_{index+1}_activate.setIcon(icon_active)')
                    exec(f'self.skill_{index+1}_activate.setGeometry(QtCore.QRect(self.skill_{index+1}_activate.geometry().getRect()[0]+4, self.skill_{index+1}_activate.geometry().getRect()[1], 155, 241))')
                    Ui_LOTR.choice_skill_check_deck[ind - 1] = 0
                    icon_deactive = QtGui.QIcon()
                    icon_deactive.addPixmap(QtGui.QPixmap('Cards/Обратная_сторона_навыка.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    exec(f'self.choice_skill_{ind}.setIcon(icon_deactive)')
                    break

    for i in range(1, 5):
        exec(f'''def use_skill{i}_click(self):
            self.skill_{i}_activate.clicked.connect(lambda: self.use_skill({i}))''')

    def use_skill(self, ind):
        card = Ui_LOTR.active_skill_deck[ind-1]
        if card:
            Ui_LOTR.active_skill_deck[ind - 1] = 0
            Ui_LOTR.discarding_deck.append(card)

            icon_use = QtGui.QIcon()
            icon_use.addPixmap(QtGui.QPixmap('Cards/Подготовленный навык.JPG'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            exec(f'self.skill_{ind}_activate.setIcon(icon_use)')
            exec(f'self.skill_{ind}_activate.setGeometry(QtCore.QRect(self.skill_{ind}_activate.geometry().getRect()[0]-4, self.skill_{ind}_activate.geometry().getRect()[1], 161, 228))')



    def skill_deck_click(self):
        self.skill_deck.clicked.connect(self.skill_select)

    def skill_select(self):
        for i, ready_skill in enumerate(Ui_LOTR.choice_skill_check_deck):
            if not ready_skill:
                Ui_LOTR.choice_skill_check_deck[i] = Ui_LOTR.deck.pop()
                exec(f'''icon_choice_skill{i+1} = QtGui.QIcon()
icon_choice_skill{i+1}.addPixmap(QtGui.QPixmap(Ui_LOTR.choice_skill_check_deck[{i}]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
self.choice_skill_{i+1}.setIcon(icon_choice_skill{i+1})''')
                break


    def select_hero_click(self):
        self.Select_hero_btn.clicked.connect(self.select_hero)

    def select_hero(self):
        global hero_name

        hero_name_ru = self.Select_hero.currentText()
        hero_name = translit(f'{hero_name_ru}', language_code='ru', reversed=True)
        Ui_LOTR.deck = main.start_deck(hero_name)

        self.weapon_2.setEnabled(True)
        self.item_1.setEnabled(True)
        self.skill_2_activate.setEnabled(True)
        self.drop_btn.setEnabled(True)
        self.armor.setEnabled(True)
        self.skill_deck.setEnabled(True)
        self.weapon_1.setEnabled(True)
        self.skill_3_activate.setEnabled(True)
        self.choice_skill_1.setEnabled(True)
        self.card_down_btn_1.setEnabled(True)
        self.choice_skill_4.setEnabled(True)
        self.choice_skill_3.setEnabled(True)
        self.choice_skill_2.setEnabled(True)
        self.skill_4_activate.setEnabled(True)
        self.skill_1_activate.setEnabled(True)
        self.Fear_botton_7.setEnabled(True)
        self.Damage_botton_2.setEnabled(True)
        self.Damage_botton_6.setEnabled(True)
        self.Damage_botton_5.setEnabled(True)
        self.Fear_botton_3.setEnabled(True)
        self.Fear_botton_2.setEnabled(True)
        self.Damage_counter.setEnabled(True)
        self.Fear_botton_4.setEnabled(True)
        self.Fear_botton_1.setEnabled(True)
        self.Damage_botton_3.setEnabled(True)
        self.Fear_counter.setEnabled(True)
        self.Fear_botton_6.setEnabled(True)
        self.Damage_botton_1.setEnabled(True)
        self.Fear_botton_5.setEnabled(True)
        self.Damage_botton_4.setEnabled(True)
        self.item_2.setEnabled(True)
        self.card_down_btn_2.setEnabled(True)
        self.card_down_btn_3.setEnabled(True)
        self.card_down_btn_4.setEnabled(True)
        self.card_up_btn_1.setEnabled(True)
        self.card_up_btn_2.setEnabled(True)
        self.card_up_btn_3.setEnabled(True)
        self.card_up_btn_4.setEnabled(True)
        self.secrecy.setEnabled(True)
        self.determination.setEnabled(True)
        self.courage.setEnabled(True)
        self.shuffle_card_btn.setEnabled(True)
        self.discarding_btn.setEnabled(True)
        self.Select_hero.close()
        self.Select_hero_btn.close()
        self.Hero_card.setPixmap(QtGui.QPixmap(f"Cards/Карты персонажей/{hero_name_ru}.JPG"))

    def shuffle_card_btn_click(self):
        self.shuffle_card_btn.clicked.connect(self.shuffle_card)

    def shuffle_card(self):
        Ui_LOTR.deck.extend(Ui_LOTR.discarding_deck)
        for card in Ui_LOTR.choice_skill_check_deck:
            if card:
                Ui_LOTR.deck.append(card)
        shuffle(Ui_LOTR.deck)
        Ui_LOTR.discarding_deck = []
        Ui_LOTR.choice_skill_check_deck = [0, 0, 0, 0]
        icon_discard = QtGui.QIcon()
        icon_discard.addPixmap(QtGui.QPixmap('Cards/Обратная_сторона_навыка.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        for i in range(1, 5):
            exec(f'self.choice_skill_{i}.setIcon(icon_discard)')


    def discarding_btn_click(self):
        self.discarding_btn.clicked.connect(self.discarding)

    def discarding(self):
        for card in Ui_LOTR.choice_skill_check_deck:
            if card:
                Ui_LOTR.discarding_deck.append(card)
        Ui_LOTR.choice_skill_check_deck = [0, 0, 0, 0]
        icon_discard = QtGui.QIcon()
        icon_discard.addPixmap(QtGui.QPixmap('Cards/Обратная_сторона_навыка.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        for i in range(1, 5):
            exec(f'self.choice_skill_{i}.setIcon(icon_discard)')

    def drop_click(self):
        self.drop_btn.clicked.connect(self.drop)


    def drop(self):
        self.Table.removeTab(12)
        self.Discard = QtWidgets.QWidget()
        self.Discard.setObjectName("Discard")
        self.Table.addTab(self.Discard, "Сброс")
        x = 0
        y = 0
        for i, v in enumerate(Ui_LOTR.discarding_deck):
            exec(f'''self.discarding{i} = QtWidgets.QPushButton(self.Discard)''')
            exec(f'''self.discarding{i}.setEnabled(True)''')
            exec(f'''self.discarding{i}.setGeometry(QtCore.QRect(x, y, 155, 241))''')
            exec(f'''self.discarding{i}.setText("")''')
            exec(f'''icon_discarding{i} = QtGui.QIcon()''')
            exec(f'''icon_discarding{i}.addPixmap(QtGui.QPixmap(f"{v}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)''')
            exec(f'''self.discarding{i}.setIcon(icon_discarding{i})''')
            exec(f'''self.discarding{i}.setIconSize(QtCore.QSize(160, 240))''')
            exec(f'''self.discarding{i}.setCheckable(True)''')
            exec(f'''self.discarding{i}.setObjectName(f"discarding{i}")''')
            x += 155
            if x > 1550:
                x = 0
                y += 250

            # exec(f'''self.discarding{i}_click()''')
#Может быть передавать Ui_LOTR.discarding_deck



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LOTR()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())