import random
import time
import sys
from urllib.error import HTTPError
import requests
from PyQt5.QtWidgets import (QVBoxLayout, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QCheckBox, QHBoxLayout)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtTest import QTest
from PyQt5.QtGui import QIcon, QPixmap

class Cardastrophy(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("cardastrophylogo.png"))
        self.kingcount = 2
        self.planetcount = 2
        self.jestercount = 2
        self.robotcount = 2
        self.dragoncount = 2
        self.chimeracount = 2
        self.ghostbutlercount = 1
        self.hourglasscount = 2
        self.dicecount = 2
        self.rand = 1
        self.kazanma = 0
        self.kaybetme = 0
        self.token = 0
        self.chosencards = 0
        self.bsignal = 0
        self.hgsignal = 0
        self.chimerasignal = 0
        self.dicesignal = 0
        self.coinlabel = QLabel(f"Card-Token🎴: {self.token}")
        self.coinlabel.setObjectName("coinlabel")
        self.titlelabel = QLabel("CARDASTROPHY", self)
        self.titlelabel.setObjectName("titlelabel")
        self.playbutton = QPushButton("Play Against AI🧠")
        self.playbutton.setObjectName("playbutton")
        self.deck = QPushButton("Your Deck📜")
        self.deck.setObjectName("deck")
        self.backtomenu = QPushButton("◀️Back to Menu")
        self.backtomenu.setObjectName("backtomenu")
        self.tur = QLabel(f"ROUND {self.rand}")
        self.tur.setObjectName("tur")
        self.player = QLabel("❓")
        self.player.setObjectName("player")
        self.vs = QLabel("vs")
        self.vs.setObjectName("vs")
        self.ai = QLabel("❓")
        self.ai.setObjectName("ai")
        self.gameover = QLabel("")
        self.gameover.setObjectName("gameover")
        self.rw = QLabel("")
        self.rw.setObjectName("rw")
        self.desc = QLabel("")
        self.desc.setObjectName("desc")
        self.again = QPushButton("Play Again🔁")
        self.again.setObjectName("again")
        self.victory = QLabel(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
        self.victory.setObjectName("victory")
        self.dragon = QPushButton(f"🐉({self.dragoncount})",self)
        self.king = QPushButton(f"🫅({self.kingcount})",self)
        self.robot = QPushButton(f"🤖({self.robotcount})",self)
        self.jester = QPushButton(f"🃏({self.jestercount})",self)
        self.planet = QPushButton(f"🪐({self.planetcount})",self)
        self.shop = QPushButton("Shop💎")
        self.dragondeck = QCheckBox("🐉")
        self.dragondeck.setObjectName("dragondeck")
        self.kingdeck = QCheckBox("🫅")
        self.kingdeck.setObjectName("kingdeck")
        self.robotdeck = QCheckBox("🤖")
        self.robotdeck.setObjectName("robotdeck")
        self.planetdeck = QCheckBox("🪐")
        self.planetdeck.setObjectName("planetdeck")
        self.jesterdeck = QCheckBox("🃏")
        self.jesterdeck.setObjectName("jesterdeck")
        self.butlerdeck = QCheckBox("🤵‍♂️👻")
        self.butlerdeck.setObjectName("butlerdeck")
        self.hourglassdeck = QCheckBox("⌛")
        self.hourglassdeck.setObjectName("hourglassdeck")
        self.chimeradeck = QCheckBox("👹🦁🐍")
        self.chimeradeck.setObjectName("chimeradeck")
        self.dragonvalue = 1
        self.kingvalue = 1
        self.jestervalue = 1
        self.robotvalue = 1
        self.planetvalue = 1
        self.butlervalue = 0
        self.hourglassvalue = 0
        self.chimeravalue = 0
        self.dicevalue = 0
        self.butler = QPushButton("🤵‍/👻 Butler(🎴2500)")
        self.butler.setObjectName("butler")
        self.boughtbutler = 0
        self.boughthourglass = 0
        self.boughtchimera = 0
        self.boughtdice = 0
        self.butlercharacter = QPushButton("🤵‍♂️")
        self.butlercharacter.setObjectName("butlercharacter")
        self.chimera = QPushButton(f"👹🦁🐍({self.chimeracount})")
        self.chimera.setObjectName("chimera")
        self.ghostbutler = QPushButton(f"👻({self.ghostbutlercount})")
        self.ghostbutler.setObjectName("ghostbutler")
        self.hourglass = QPushButton("⌛Hourglass(🎴1500)")
        self.hourglass.setObjectName("hourglass")
        self.hourglassbutton = QPushButton(f"⌛({self.hourglasscount})")
        self.chimerabuy = QPushButton("👹🦁🐍Chimera(🎴2500)")
        self.chimerabuy.setObjectName("chimerabuy")
        self.clionatk = QPushButton("🦁")
        self.cgoatatk = QPushButton("👹")
        self.csnakeatk = QPushButton("🐍")
        self.clionatk.setObjectName("clionatk")
        self.cgoatatk.setObjectName("cgoatatk")
        self.csnakeatk.setObjectName("csnakeatk")
        self.lioncount = 1
        self.goatcount = 1
        self.snakecount = 1
        self.diceshop = QPushButton("🎲 Life Dice(🎴1500)")
        self.diceshop.setObjectName("diceshop")
        self.deckdice = QCheckBox("🎲")
        self.deckdice.setObjectName("deckdice")
        self.dice = QPushButton(f"🎲({self.dicecount})")
        self.dice.setObjectName("dice")
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cardastrophy")

        self.coinlabel.setAlignment(Qt.AlignLeft)
        self.titlelabel.setAlignment(Qt.AlignCenter)
        self.player.setAlignment(Qt.AlignCenter)
        self.ai.setAlignment(Qt.AlignCenter)
        self.vs.setAlignment(Qt.AlignCenter)
        self.gameover.setAlignment(Qt.AlignCenter)
        self.victory.setAlignment(Qt.AlignCenter)
        self.desc.setAlignment(Qt.AlignCenter)
        self.tur.setAlignment(Qt.AlignCenter)
        self.rw.setAlignment(Qt.AlignCenter)

        attacklayout = QHBoxLayout()
        attacklayout.addWidget(self.clionatk)
        attacklayout.addWidget(self.cgoatatk)
        attacklayout.addWidget(self.csnakeatk)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.playbutton)
        button_layout.addWidget(self.deck)
        button_layout.addWidget(self.butler)
        button_layout.addWidget(self.hourglass)
        button_layout.addWidget(self.chimerabuy)
        button_layout.addWidget(self.diceshop)
        button_layout.addWidget(self.backtomenu)
        button_layout.addWidget(self.shop)
        button_layout.addWidget(self.again)
        button_layout.addWidget(self.dragon)
        button_layout.addWidget(self.king)
        button_layout.addWidget(self.robot)
        button_layout.addWidget(self.jester)
        button_layout.addWidget(self.planet)
        button_layout.addWidget(self.butlercharacter)
        button_layout.addWidget(self.ghostbutler)
        button_layout.addWidget(self.hourglassbutton)
        button_layout.addWidget(self.chimera)
        button_layout.addWidget(self.dice)

        layout = QVBoxLayout()
        layout.addWidget(self.coinlabel)
        layout.addWidget(self.titlelabel)
        layout.addWidget(self.tur)
        layout.addWidget(self.player)
        layout.addWidget(self.vs)
        layout.addWidget(self.ai)
        layout.addWidget(self.gameover)
        layout.addWidget(self.rw)
        layout.addWidget(self.desc)
        layout.addWidget(self.victory)
        layout.addLayout(attacklayout)
        layout.addLayout(button_layout)

        checkboxlayout = QHBoxLayout()
        checkboxlayout.addWidget(self.dragondeck)
        checkboxlayout.addWidget(self.kingdeck)
        checkboxlayout.addWidget(self.robotdeck)
        checkboxlayout.addWidget(self.jesterdeck)
        checkboxlayout.addWidget(self.planetdeck)
        checkboxlayout.addWidget(self.butlerdeck)
        checkboxlayout.addWidget(self.hourglassdeck)
        checkboxlayout.addWidget(self.chimeradeck)
        checkboxlayout.addWidget(self.deckdice)
        layout.addLayout(checkboxlayout)

        self.player.hide()
        self.ai.hide()
        self.vs.hide()
        self.gameover.hide()
        self.victory.hide()
        self.desc.hide()
        self.tur.hide()
        self.rw.hide()
        self.dragon.hide()
        self.jester.hide()
        self.robot.hide()
        self.king.hide()
        self.planet.hide()
        self.again.hide()
        self.backtomenu.hide()
        self.dragondeck.hide()
        self.jesterdeck.hide()
        self.kingdeck.hide()
        self.robotdeck.hide()
        self.planetdeck.hide()
        self.butler.hide()
        self.butlerdeck.hide()
        self.butlercharacter.hide()
        self.ghostbutler.hide()
        self.hourglass.hide()
        self.hourglassdeck.hide()
        self.hourglassbutton.hide()
        self.chimerabuy.hide()
        self.chimeradeck.hide()
        self.chimera.hide()
        self.clionatk.hide()
        self.cgoatatk.hide()
        self.csnakeatk.hide()
        self.diceshop.hide()
        self.deckdice.hide()
        self.dice.hide()

        self.setLayout(layout)

        self.setStyleSheet("""
        QLabel#player {
            font-size: 55px;
            font-family: 'Segoe UI Emoji';
        }
        QLabel#ai {
            font-size: 55px;
            font-family: 'Segoe UI Emoji';
        }
        QLabel#titlelabel {
            font-size: 55px;
            font-family: Arial;
            font-weight: Bold;
        }
        QLabel#coinlabel {font-size: 20px; font-family: 'Segoe UI Emoji'}
        QPushButton {
            font-size: 30px;
            font-family: Calibri;
            }
            
        QLabel#vs {
            font-size: 20px;
            font-family: Arial;
            }
        QLabel#desc {
            font-size: 30px;
            font-family: Arial;
            }
        QLabel#victory {
            font-size: 30px;
            font-family: 'Segoe UI Emoji';
            }
        QLabel#tur {
            font-size: 30px;
            font-family: Arial;
            font-weight: bold;
            }
        QPushButton:hover {
            background-color: #d4d4d4;
            }
        QLabel#gameover {
            font-size: 30px;
            font-family: 'Segoe UI Emoji';
            }
        QLabel#rw {
            font-size: 30px;
            font-family: 'Segoe UI Emoji';
            }
        QCheckBox {
            font-size: 50px;
            font-family: 'Segoe UI Emoji';
            }
        QPushButton#butler {
            background-color: purple;
            }
        QPushButton#chimerabuy {
            background-color: purple;
            }
        QPushButton#hourglass {
            background-color: yellow;
            }
        QPushButton#diceshop {
            background-color: yellow;
            }
        """)

        self.aianswer()

        self.dragon.clicked.connect(self.choosedragon)
        self.dice.clicked.connect(self.choosedice)
        self.butlercharacter.clicked.connect(self.choosebutler)
        self.hourglassbutton.clicked.connect(self.choosehg)
        self.chimera.clicked.connect(self.choosechimera)
        self.king.clicked.connect(self.chooseking)
        self.robot.clicked.connect(self.chooserobot)
        self.planet.clicked.connect(self.chooseplanet)
        self.jester.clicked.connect(self.choosejester)
        self.shop.clicked.connect(self.openshop)
        self.playbutton.clicked.connect(self.startgame)
        self.again.clicked.connect(self.playagain)
        self.backtomenu.clicked.connect(self.menuback)
        self.deck.clicked.connect(self.modifydeck)
        self.dragondeck.stateChanged.connect(self.enabledragon)
        self.kingdeck.stateChanged.connect(self.enableking)
        self.planetdeck.stateChanged.connect(self.enableplanet)
        self.jesterdeck.stateChanged.connect(self.enablejester)
        self.robotdeck.stateChanged.connect(self.enablerobot)
        self.butler.clicked.connect(self.buyalfred)
        self.butlerdeck.stateChanged.connect(self.enablebutler)
        self.chimeradeck.stateChanged.connect(self.enablechimera)
        self.deckdice.stateChanged.connect(self.enabledice)
        self.ghostbutler.clicked.connect(self.ghostbutlerchoose)
        self.hourglass.clicked.connect(self.buyhglass)
        self.chimerabuy.clicked.connect(self.buychimeracard)
        self.hourglassdeck.stateChanged.connect(self.enablehourglass)
        self.clionatk.clicked.connect(self.winloselion)
        self.cgoatatk.clicked.connect(self.winlosegoat)
        self.csnakeatk.clicked.connect(self.winlosesnake)
        self.diceshop.clicked.connect(self.buydice)

    def choosedragon(self):
        self.player.setText("🐉")
        self.dragoncount -= 1
        self.dragon.setText(f"🐉({self.dragoncount})")
        self.winlosedragon()
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        if self.dragoncount == 0:
            self.dragon.hide()
            self.desc.setText("You have ran out of dragons.")
            QTimer.singleShot(1000, lambda: self.desc.clear())

    def chooseking(self):
        self.player.setText("🫅")
        self.kingcount -= 1
        self.king.setText(f"🫅({self.kingcount})")
        self.winloseking()
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        if self.kingcount == 0:
            self.king.hide()
            self.desc.setText("You have ran out of kings.")
            QTimer.singleShot(1000, lambda: self.desc.clear())

    def chooserobot(self):
        self.player.setText("🤖")
        self.robotcount -= 1
        self.robot.setText(f"🤖({self.robotcount})")
        self.winloserobot()
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        if self.robotcount == 0:
            self.robot.hide()
            self.desc.setText("You have ran out of robots.")
            QTimer.singleShot(1000, lambda: self.desc.clear())

    def chooseplanet(self):
        self.player.setText("🪐")
        self.planetcount -= 1
        self.planet.setText(f"🪐({self.planetcount})")
        self.winloseplanet()
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        if self.planetcount == 0:
            self.planet.hide()
            self.desc.setText("You have ran out of planets.")
            QTimer.singleShot(1000, lambda: self.desc.clear())

    def choosejester(self):
        self.player.setText("🃏")
        self.jestercount -= 1
        self.jester.setText(f"🃏({self.jestercount})")
        self.winlosejester()
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        if self.jestercount == 0:
            self.jester.hide()
            self.desc.setText("You have ran out of jesters.")
            QTimer.singleShot(1000, lambda: self.desc.clear())
    def choosebutler(self):
        self.player.setText("🤵")
        self.butlercount -= 1
        self.butlercharacter.setText(f"🤵({self.butlercount})")
        self.winlosebutler()
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        if self.butlercount == 0:
            self.butlercharacter.hide()
            self.ghostbutler.show()
            self.desc.setText("The Ghost Butler is now lurking around.")
            QTimer.singleShot(1000, lambda: self.desc.clear())
    def choosehg(self):
        self.player.setText("⌛")
        self.hourglasscount -= 1
        self.hourglassbutton.setText(f"⌛({self.hourglasscount})")
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        if self.hourglasscount == 0:
            self.hourglassbutton.hide()
            self.desc.setText("You cannot skip any more rounds.")
            QTimer.singleShot(1000, lambda: self.desc.clear())
    def choosedice(self):
        self.player.setText("🎲")
        self.dicecount -= 1
        self.dice.setText(f"🎲({self.dicecount})")
        revivecard = [1, 2, 3, 4, 5]
        newcard = random.choice(revivecard)
        if newcard == 1:
            self.kingcount += 1
            self.king.show()
            self.king.setText(f"🫅({self.kingcount})")
        elif newcard == 2:
            self.dragoncount += 1
            self.dragon.show()
            self.dragon.setText(f"🐉({self.dragoncount})")
        elif newcard == 3:
            self.jestercount += 1
            self.jester.show()
            self.jester.setText(f"🃏({self.jestercount})")
        elif newcard == 4:
            self.robotcount += 1
            self.robot.show()
            self.robot.setText(f"🤖({self.robotcount})")
        elif newcard == 5:
            self.planetcount += 1
            self.planet.show()
            self.planet.setText(f"🪐({self.planetcount})")
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        if self.dicecount == 0:
            self.dice.hide()
            self.desc.setText("The life dice has faded away.")
            QTimer.singleShot(1000, lambda: self.desc.clear())
    def choosechimera(self):
        self.player.setText("👹🦁🐍")
        self.chimeracount -= 1
        self.chimera.setText(f"👹🦁🐍({self.chimeracount})")
        self.choosechead()
        if self.chimeracount == 0:
            self.chimera.hide()
            QTimer.singleShot(1000, lambda: self.desc.clear())
    def ghostbutlerchoose(self):
        self.player.setText("👻")
        self.ghostbutlercount -= 1
        self.ghostbutler.setText(f"👻({self.ghostbutlercount})")
        self.winlosegb()
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        if self.ghostbutlercount == 0:
            self.ghostbutler.hide()
            self.desc.setText("The Ghost has faded away.")
            QTimer.singleShot(1000, lambda: self.desc.clear())

    def aianswer(self):
        QTest.qWait(1000)
        opsiyons = ["🫅", "🤖", "🐉", "🃏", "🪐"]
        aimove = random.choice(opsiyons)
        self.ai.setText(aimove)

    def winlosedragon(self):
        aitext = self.ai.text()
        if "🫅" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The king has tamed the dragon.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        if "🤵" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The butler has haunted the dragon.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🐉" in aitext:
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("It's a tie.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        else:
            self.kazanma += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText(f"You have won round {self.rand}")
            self.token += 50
            self.coinlabel.setText(f"Card-Token🎴: {self.token}")
            QTimer.singleShot(500, lambda: self.desc.clear())

    def winloseplanet(self):
        aitext = self.ai.text()
        if "🤖" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The planet was taken over by robots.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🃏" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The planet was beaten by the jester.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🐉" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The planet destroyed by the dragon.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🪐" in aitext:
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("It's a tie.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        else:
            self.kazanma += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText(f"You have won round {self.rand}")
            self.token += 50
            self.coinlabel.setText(f"Card-Token🎴: {self.token}")
            QTimer.singleShot(500, lambda: self.desc.clear())
    def winlosejester(self):
        aitext = self.ai.text()
        if "🫅" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The king executed the jester.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🐉" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The dragon burned the jester.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🃏" in aitext:
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("It's a tie.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🤵" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The butler has purified the jester.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        else:
            self.kazanma += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText(f"You have won round {self.rand}")
            self.token += 50
            self.coinlabel.setText(f"Card-Token🎴: {self.token}")
            QTimer.singleShot(500, lambda: self.desc.clear())
    def winloseking(self):
        aitext = self.ai.text()
        if "🪐" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The planet has overthrown the king.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🫅" in aitext:
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("It's a tie.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        else:
            self.kazanma += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText(f"You have won round {self.rand}")
            self.token += 50
            self.coinlabel.setText(f"Card-Token🎴: {self.token}")
            QTimer.singleShot(500, lambda: self.desc.clear())
    def winloserobot(self):
        aitext = self.ai.text()
        if "🐉" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The dragon has burned the robot.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🃏" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The robot was tampered by the jester")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🫅" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The robot was executed by the king.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🤖" in aitext:
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("It's a tie.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        else:
            self.kazanma += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText(f"You have won round {self.rand}")
            self.token += 50
            self.coinlabel.setText(f"Card-Token🎴: {self.token}")
            QTimer.singleShot(500, lambda: self.desc.clear())
    def winlosebutler(self):
        aitext = self.ai.text()
        if "🤖" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The robot has killed the butler.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🫅" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The butler was executed by the king.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🪐" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The butler couldn't handle the planet.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🤵" in aitext:
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("It's a tie.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        else:
            self.kazanma += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText(f"You have won round {self.rand}")
            self.token += 50
            self.coinlabel.setText(f"Card-Token🎴: {self.token}")
            QTimer.singleShot(500, lambda: self.desc.clear())

    def winlosegb(self):
        self.kazanma += 1
        self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
        self.desc.setText(f"You have won round {self.rand}")
        self.token += 50
        self.coinlabel.setText(f"Card-Token🎴: {self.token}")
        QTimer.singleShot(500, lambda: self.desc.clear())

    def winloselion(self):
        self.kazanma += 1
        self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
        self.desc.setText(f"You have won round {self.rand}")
        self.token += 50
        self.coinlabel.setText(f"Card-Token🎴: {self.token}")
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        QTimer.singleShot(500, lambda: self.desc.clear())
        self.lioncount -= 1
        self.clionatk.hide()
        self.cgoatatk.hide()
        self.csnakeatk.hide()

    def winlosegoat(self):
        aitext = self.ai.text()
        if "🫅" in aitext:
            self.kazanma += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The Chimera has eaten the king.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🐉" in aitext:
            self.kazanma += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The dragon was torn to shreds.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        elif "🤵" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The butler was torn to shreds.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        else:
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The chimera has protected itself.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        self.clionatk.hide()
        self.cgoatatk.hide()
        self.csnakeatk.hide()
        self.goatcount -= 1
        QTimer.singleShot(500, lambda: self.desc.clear())

    def winlosesnake(self):
        aitext = self.ai.text()
        if "🫅" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The king has tamed the chimera.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        if "🤵" in aitext:
            self.kaybetme += 1
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText("The butler has haunted the chimera.")
            QTimer.singleShot(500, lambda: self.desc.clear())
        else:
            self.kazanma += 2
            self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
            self.desc.setText(f"You have won round {self.rand}")
            self.token += 50
            self.coinlabel.setText(f"Card-Token🎴: {self.token}")
            QTimer.singleShot(500, lambda: self.desc.clear())
        self.aianswer()
        self.player.setText("❓")
        self.rounds()
        self.tur.setText(f"ROUND {self.rand}")
        self.clionatk.hide()
        self.cgoatatk.hide()
        self.csnakeatk.hide()
        self.snakecount -= 1
        QTimer.singleShot(500, lambda: self.desc.clear())

    def openshop(self):
        self.jester.hide()
        self.robot.hide()
        self.king.hide()
        self.planet.hide()
        self.dragon.hide()
        self.titlelabel.hide()
        self.vs.hide()
        self.player.hide()
        self.ai.hide()
        self.tur.hide()
        self.victory.hide()
        self.desc.hide()
        self.playbutton.hide()
        self.backtomenu.show()
        self.deck.hide()
        self.kingdeck.hide()
        self.robotdeck.hide()
        self.jesterdeck.hide()
        self.planetdeck.hide()
        self.dragondeck.hide()
        self.shop.hide()
        self.hourglass.show()
        self.butler.show()
        self.chimerabuy.show()
        self.diceshop.show()

    def rounds(self):
        self.rand += 1
        if self.rand > 10:
            self.endgame()

    def endgame(self):
        print("=== Endgame Debug Start ===")
        print("self.tur:", self.tur)
        print("self.desc:", self.desc)

        self.gameover.setText("🎮Game Over🎮")
        if self.kazanma > self.kaybetme:
            self.rw.setText("Congratulations, you have won🎉")
        elif self.kazanma < self.kaybetme:
            self.rw.setText("You have unfortunately lost😢")
        else:
            self.rw.setText("It's a tie🤝")
        self.dragon.hide()
        self.king.hide()
        self.robot.hide()
        self.jester.hide()
        self.planet.hide()
        self.vs.hide()
        self.player.hide()
        self.ai.hide()
        self.tur.hide()
        self.again.show()
        self.backtomenu.show()
        self.butler.hide()
        self.ghostbutler.hide()
        QTimer.singleShot(1000, lambda: None)
        self.ghostbutler.hide()
        self.chimera.hide()
        self.clionatk.hide()
        self.cgoatatk.hide()
        self.csnakeatk.hide()
        self.hourglassbutton.hide()
        self.dice.hide()

    def startgame(self):
        self.playbutton.hide()
        self.deck.hide()
        self.shop.hide()
        self.player.show()
        self.ai.show()
        self.vs.show()
        self.gameover.show()
        self.victory.show()
        self.desc.show()
        self.tur.show()
        self.rw.show()
        if self.dragonvalue == 1:
            self.dragon.show()
        else:
            self.dragon.hide()
        if self.jestervalue == 1:
            self.jester.show()
        else:
            self.jester.hide()
        if self.robotvalue == 1:
            self.robot.show()
        else:
            self.robot.hide()
        if self.kingvalue == 1:
            self.king.show()
        else:
            self.king.hide()
        if self.planetvalue == 1:
            self.planet.show()
        else:
            self.planet.hide()
        if self.butlervalue == 1:
            self.butlercharacter.show()
        else:
            self.butlercharacter.hide()
        if self.hourglassvalue == 1:
            self.hourglassbutton.show()
        else:
            self.hourglassbutton.hide()
        if self.chimeravalue == 1:
            self.chimera.show()
        else:
            self.chimera.hide()
        if self.dicevalue == 1:
            self.dice.show()
        else:
            self.dice.hide()

        self.rand = 1
        self.tur.setText(f"ROUND {self.rand}")
        self.dragoncount = 2
        self.dragon.setText(f"🐉({self.dragoncount})")
        self.robotcount = 2
        self.robot.setText(f"🤖({self.robotcount})")
        self.kingcount = 2
        self.king.setText(f"🫅({self.kingcount})")
        self.jestercount = 2
        self.jester.setText(f"🃏({self.jestercount})")
        self.planetcount = 2
        self.planet.setText(f"🪐({self.planetcount})")
        self.butlercount = 2
        self.butlercharacter.setText(f"🤵({self.butlercount})")
        self.player.setText("❓")
        self.rw.clear()
        self.gameover.clear()
        self.again.hide()
        self.kazanma = 0
        self.kaybetme = 0
        self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")
        self.kingdeck.hide()
        self.robotdeck.hide()
        self.jesterdeck.hide()
        self.planetdeck.hide()
        self.dragondeck.hide()

    def playagain(self):
        self.playbutton.hide()
        self.shop.hide()
        self.player.show()
        self.ai.show()
        self.vs.show()
        self.gameover.show()
        self.victory.show()
        self.desc.show()
        self.tur.show()
        self.rw.show()
        self.backtomenu.hide()
        self.rand = 1
        self.tur.setText(f"ROUND {self.rand}")
        if self.dragonvalue == 1:
            self.dragon.show()
            self.dragoncount = 2
            self.dragon.setText(f"🐉({self.dragoncount})")
        else:
            self.dragon.hide()

        if self.robotvalue == 1:
            self.robot.show()
            self.robotcount = 2
            self.robot.setText(f"🤖({self.robotcount})")
        else:
            self.robot.hide()

        if self.kingvalue == 1:
            self.kingcount = 2
            self.king.show()
            self.king.setText(f"🫅({self.kingcount})")
        else:
            self.king.hide()

        if self.jestervalue == 1:
            self.jester.show()
            self.jestercount = 2
            self.jester.setText(f"🃏({self.jestercount})")
        else:
            self.jester.hide()

        if self.planetvalue == 1:
            self.planet.show()
            self.planetcount = 2
            self.planet.setText(f"🪐({self.planetcount})")
        else:
            self.planet.hide()
        if self.butlervalue == 1:
            self.butlercharacter.show()
            self.butlercount = 2
            self.butlercharacter.setText(f"🤵({self.butlercount})")
        else:
            self.butlercharacter.hide()
        if self.hourglassvalue == 1:
            self.hourglassbutton.show()
            self.hourglasscount = 2
            self.hourglassbutton.setText(f"⌛({self.hourglasscount})")
        else:
            self.hourglassbutton.hide()
        if self.chimeravalue == 1:
            self.chimera.show()
            self.chimeracount = 2
            self.lioncount = 1
            self.goatcount = 1
            self.snakecount = 1
            self.chimera.setText(f"👹🦁🐍({self.chimeracount})")
        else:
            self.chimera.hide()
        if self.dicevalue == 1:
            self.dice.show()
            self.dicecount = 2
            self.dice.setText(f"🎲({self.dicecount})")
        else:
            self.dice.hide()
        self.player.setText("❓")
        self.rw.clear()
        self.gameover.clear()
        self.again.hide()
        self.kazanma = 0
        self.kaybetme = 0
        self.victory.setText(f"✅: {self.kazanma} | ❌: {self.kaybetme} ")

    def menuback(self):
        self.victory.hide()
        self.backtomenu.hide()
        self.titlelabel.show()
        self.titlelabel.setText("CARDASTROPHY")
        self.playbutton.show()
        self.again.hide()
        self.shop.show()
        self.gameover.hide()
        self.rw.hide()
        self.deck.show()
        self.kingdeck.hide()
        self.robotdeck.hide()
        self.jesterdeck.hide()
        self.planetdeck.hide()
        self.dragondeck.hide()
        self.butler.hide()
        self.butlerdeck.hide()
        self.butlercharacter.hide()
        self.ghostbutler.hide()
        self.hourglass.hide()
        self.hourglassdeck.hide()
        self.hourglassbutton.hide()
        self.chimerabuy.hide()
        self.chimeradeck.hide()
        self.chimera.hide()
        self.clionatk.hide()
        self.cgoatatk.hide()
        self.csnakeatk.hide()
        self.diceshop.hide()
        self.deckdice.hide()

    def modifydeck(self):
        self.titlelabel.setText("Your Deck")
        self.playbutton.hide()
        self.shop.hide()
        self.dragondeck.show()
        self.kingdeck.show()
        self.robotdeck.show()
        self.jesterdeck.show()
        self.planetdeck.show()
        if self.boughtbutler == 2:
            self.butlerdeck.show()
        if self.boughtchimera == 2:
            self.chimeradeck.show()
        if self.boughthourglass == 2:
            self.hourglassdeck.show()
        if self.boughtdice == 2:
            self.deckdice.show()
        if self.dragonvalue == 1:
            self.dragondeck.setChecked(True)
        if self.kingvalue == 1:
            self.kingdeck.setChecked(True)
        if self.robotvalue == 1:
            self.robotdeck.setChecked(True)
        if self.jestervalue == 1:
            self.jesterdeck.setChecked(True)
        if self.planetvalue == 1:
            self.planetdeck.setChecked(True)
        self.deck.hide()

    def enabledragon(self, state):
        if state == Qt.Unchecked:
            self.dragonvalue = 2
            self.chosencards -= 1
        elif state == Qt.Checked:
            self.dragonvalue = 1
            self.chosencards += 1
            print(self.chosencards)
        self.backtomenu.setVisible(self.chosencards == 5)
    def enableking(self, state):
        if state == Qt.Unchecked:
            self.kingvalue = 2
            self.chosencards -= 1
        elif state == Qt.Checked:
            self.kingvalue = 1
            self.chosencards += 1
            print(self.chosencards)
        self.backtomenu.setVisible(self.chosencards == 5)
    def enableplanet(self, state):
        if state == Qt.Unchecked:
            self.planetvalue = 2
            self.chosencards -= 1
            print(self.chosencards)
        elif state == Qt.Checked:
            self.planetvalue = 1
            self.chosencards += 1
            print(self.chosencards)
        self.backtomenu.setVisible(self.chosencards == 5)
    def enablerobot(self, state):
        if state == Qt.Unchecked:
            self.robotvalue = 2
            self.chosencards -= 1
            print(self.chosencards)
        elif state == Qt.Checked:
            self.robotvalue = 1
            self.chosencards += 1
            print(self.chosencards)
        self.backtomenu.setVisible(self.chosencards == 5)
    def enablejester(self, state):
        if state == Qt.Unchecked:
            self.jestervalue = 2
            self.chosencards -= 1
            print(self.jestervalue)
        elif state == Qt.Checked:
            self.jestervalue = 1
            self.chosencards += 1
            print(self.jestervalue)
        self.backtomenu.setVisible(self.chosencards == 5)

    def enablebutler(self, state):
        if state == Qt.Unchecked:
            self.butlervalue = 2
            self.chosencards -= 1
            print(self.butlervalue)
        elif state == Qt.Checked:
            self.butlervalue = 1
            self.chosencards += 1
            print(self.butlervalue)
        self.backtomenu.setVisible(self.chosencards == 5)

    def enablehourglass(self, state):
        if state == Qt.Unchecked:
            self.hourglassvalue = 2
            self.chosencards -= 1
            print(self.hourglassvalue)
        elif state == Qt.Checked:
            self.hourglassvalue = 1
            self.chosencards += 1
            print(self.hourglassvalue)
        self.backtomenu.setVisible(self.chosencards == 5)

    def enablechimera(self, state):
        if state == Qt.Unchecked:
            self.chimeravalue = 2
            self.chosencards -= 1
            print(self.chimeravalue)
        elif state == Qt.Checked:
            self.chimeravalue = 1
            self.chosencards += 1
            print(self.chimeravalue)
        self.backtomenu.setVisible(self.chosencards == 5)

    def enabledice(self, state):
        if state == Qt.Unchecked:
            self.dicevalue = 2
            self.chosencards -= 1
            print(self.dicevalue)
        elif state == Qt.Checked:
            self.dicevalue = 1
            self.chosencards += 1
            print(self.dicevalue)
        self.backtomenu.setVisible(self.chosencards == 5)

    def buyalfred(self):
        if self.token == 2500 or self.token > 2500:
            self.boughtbutler = 2
            self.bsignal = 2
            self.butler.hide()
            self.token -= 2500
            self.coinlabel.setText(f"Card-Token🎴: {self.token}")
        else:
            pass
    def buyhglass(self):
        if self.token == 1500 or self.token > 1500:
            self.boughthourglass = 2
            self.hgsignal = 2
            self.hourglass.hide()
            self.token -= 1500
            self.coinlabel.setText(f"Card-Token🎴: {self.token}")
        else:
            pass
    def buychimeracard(self):
        if self.token == 2500 or self.token > 2500:
            self.boughtchimera = 2
            self.chimerasignal = 2
            self.chimerabuy.hide()
            self.token -= 2500
            self.coinlabel.setText(f"Card-Token🎴: {self.token}")
        else:
            pass
    def buydice(self):
        if self.token == 1500 or self.token > 1500:
            self.boughtdice = 2
            self.dicesignal = 2
            self.diceshop.hide()
            self.token -= 1500
            self.coinlabel.setText(f"Card-Token🎴: {self.token}")
        else:
            pass
    def choosechead(self):
        if self.lioncount == 1:
            self.clionatk.show()
        else:
            self.clionatk.hide()
        if self.goatcount == 1:
            self.cgoatatk.show()
        else:
            self.cgoatatk.hide()
        if self.snakecount == 1:
            self.csnakeatk.show()
        else:
            self.csnakeatk.hide()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    cardastrophy = Cardastrophy()
    cardastrophy.show()
    sys.exit(app.exec_())

