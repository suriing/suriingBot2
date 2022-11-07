import random
from PIL import Image
import numpy as np

class ladder():
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pass

    def run(self, Peoples=8, HLadders=16):
        self.outText = ""
        x_set = range(HLadders-1)
        y_set = range(Peoples-1)

        self.map = [[0]*Peoples for y_set in range(0, HLadders)]    # 지도
        self.route = [[0]*Peoples for y_set in range(0, HLadders)]  # 이동경로
        start = []
        self.route_dict = {}
        # 맵을 표시할 배열을 초기화한다
        i = 0

        # 경로 생성
        while (i < len(x_set)):
            x = random.choice(x_set)
            y = random.choice(y_set)
            x_tmp = x+1
            y_tmp = y+1
            if (self.map[x][y] == 0 and self.map[x][y+1] == 0):
                self.map[x][y] = self.map[x][y+1] = 1
                start.append([x, y])
                i = i + 1
        # 도착지를 렌덤으로 생성함
        target = random.randint(0, Peoples-1)
        self.prize = target

        # 콘솔에서 확인하기 위한 정보(outText) 생성
        self.outText += "당첨(Prize) : " + str(self.prize) + "\n"
        AZ2 = iter(self.ALPHABET)
        peopleDescText = next(AZ2)
        for i in range(0, Peoples-1):
            peopleDescText += "  "
            peopleDescText += next(AZ2)
        self.outText += peopleDescText + "\n"

        # 누가 당첨인지 확인하는 알고리즘
        index = len(x_set)-1
        self.route[index+1][target] = 1   # 이동경로 마지막줄
        self.route_dict[index+1] = target   # 이동경로 마지막줄
        while (index >= 0):
            if (self.map[index][target] == 0):
                self.route[index][target] = 1   # 이동경로 수직이동
                self.route_dict[index] = target
                index = index - 1
            elif (self.map[index][target] == 1):
                if ([index, target] in start):
                    self.route[index][target] = 1   #
                    self.route_dict[index] = [target+1, target] # 이동경로 왼쪽이동
                    target = target + 1
                    self.route[index][target] = 1   #
                    index = index - 1
                else:
                    self.route_dict[index] = [target-1, target] # 이동경로 오른쪽이동
                    self.route[index][target] = 1   #
                    target = target - 1
                    self.route[index][target] = 1   #
                    index = index - 1
            result = target
        for i in range(HLadders):
            hmap = str(self.map[i])
            hmap = hmap.replace("0", "|")
            hmap = hmap.replace("1", "-")
            hmap = hmap.replace("[", "")
            hmap = hmap.replace("]", "")
            hmap = hmap.replace(",", " ")
            # print(hmap)
            self.outText += hmap + "\n"

        self.winner = self.ALPHABET[result]
        NUM1 = iter(range(26))
        resultText = str(next(NUM1))
        for i in range(0, Peoples-1):
            curNUM1 = next(NUM1)
            if curNUM1 > 9:
                resultText += " "
            else:
                resultText += "  "
            resultText += str(curNUM1)
        self.outText += resultText + "\n"
        self.outText += "당첨자(Winner) : " + self.winner + "\n"


    def draw(self, max_width=1600, max_height=3200, BG_COLOR=(255, 255, 255), DEFAULT_COLOR=(0, 0, 0), PICKED_COLOR=(255, 0, 0)):
        # np array to image
        pxBG = Image.new('RGB', (1, 1), BG_COLOR)
        pxDE = Image.new('RGB', (1, 1), DEFAULT_COLOR)
        pxPI = Image.new('RGB', (1, 1), PICKED_COLOR)
        # pixel data
        px_____ = np.column_stack(
            (pxBG, pxBG, pxBG, pxBG, pxBG))  # □□□□□
        px__0__ = np.column_stack(
            (pxBG, pxBG, pxDE, pxBG, pxBG))  # □□■□□
        px000__ = np.column_stack(
            (pxDE, pxDE, pxDE, pxBG, pxBG))  # ■■■□□
        px__000 = np.column_stack(
            (pxBG, pxBG, pxDE, pxDE, pxDE))  # □□■■■
        px_000_ = np.column_stack(
            (pxBG, pxDE, pxDE, pxDE, pxBG))  # □■■■□
        px_0_0_ = np.column_stack(
            (pxBG, pxDE, pxBG, pxDE, pxBG))  # □■□■□
        px_00__ = np.column_stack(
            (pxBG, pxDE, pxDE, pxBG, pxBG))  # □■■□□
        px_0___ = np.column_stack(
            (pxBG, pxDE, pxBG, pxBG, pxBG))  # □■□□□
        px___0_ = np.column_stack(
            (pxBG, pxBG, pxBG, pxDE, pxBG))  # □□□■□
        px__00_ = np.column_stack(
            (pxBG, pxBG, pxDE, pxDE, pxBG))  # □□■■□
        px0___0 = np.column_stack(
            (pxDE, pxBG, pxBG, pxBG, pxDE))  # ■□□□■
        px00_00 = np.column_stack(
            (pxDE, pxDE, pxBG, pxDE, pxDE))  # ■■□■■
        px0_0_0 = np.column_stack(
            (pxDE, pxBG, pxDE, pxBG, pxDE))  # ■□■□■
        px_00_0 = np.column_stack(
            (pxBG, pxDE, pxDE, pxBG, pxDE))  # □■■□■
        px__P__ = np.column_stack(
            (pxBG, pxBG, pxPI, pxBG, pxBG))  # □□P□□
        pxPPP__ = np.column_stack(
            (pxPI, pxPI, pxPI, pxBG, pxBG))  # PPP□□
        px__PPP = np.column_stack(
            (pxBG, pxBG, pxPI, pxPI, pxPI))  # □□PPP
        pxㅣ = np.vstack((
            px__0__,
            px__0__,
            px__0__,
            px__0__,
            px__0__
        ))  # |
        pxㅣ_r = np.vstack((
            px__P__,
            px__P__,
            px__P__,
            px__P__,
            px__P__
        ))  # | for route
        pxㅓ = np.vstack((
            px__0__,
            px__0__,
            px000__,
            px__0__,
            px__0__
        ))  # ┤
        pxㅓ_ru = np.vstack((
            px__P__,
            px__P__,
            pxPPP__,
            px__0__,
            px__0__
        ))  # ┤ for route from up
        pxㅓ_rd = np.vstack((
            px__0__,
            px__0__,
            pxPPP__,
            px__P__,
            px__P__
        ))  # ┤ for route from side
        pxㅏ = np.vstack((
            px__0__,
            px__0__,
            px__000,
            px__0__,
            px__0__
        ))  # ├
        pxㅏ_ru = np.vstack((
            px__P__,
            px__P__,
            px__PPP,
            px__0__,
            px__0__
        ))  # ├ for route from up
        pxㅏ_rd = np.vstack((
            px__0__,
            px__0__,
            px__PPP,
            px__P__,
            px__P__
        ))  # ├ for route from side
        pxㅣs = np.vstack((
            px_____,
            px__0__,
            px__0__,
            px__0__,
            px__0__
        ))  # | for start
        pxㅣsr = np.vstack((
            px_____,
            px__P__,
            px__P__,
            px__P__,
            px__P__
        ))  # | for start route
        pxㅣe = np.vstack((
            px__0__,
            px__0__,
            px__0__,
            px__0__,
            px_____
        ))  # | for end
        pxㅣer = np.vstack((
            px__P__,
            px__P__,
            px__P__,
            px__P__,
            px_____
        ))  # | for end route
        blackDot = np.vstack((
            px_____,
            px_____,
            px__0__,
            px_____,
            px_____
        ))
        redDot = np.vstack((
            px_____,
            px_____,
            px__P__,
            px_____,
            px_____
        ))
        pxA = np.vstack((
            px_000_,
            px_0_0_,
            px_000_,
            px_0_0_,
            px_0_0_
        ))  # A
        pxB = np.vstack((
            px_00__,
            px_0_0_,
            px_000_,
            px_0_0_,
            px_00__
        ))  # B
        pxC = np.vstack((
            px_000_,
            px_0___,
            px_0___,
            px_0___,
            px_000_
        ))  # C
        pxD = np.vstack((
            px_00__,
            px_0_0_,
            px_0_0_,
            px_0_0_,
            px_00__
        ))  # D
        pxE = np.vstack((
            px_000_,
            px_0___,
            px_00__,
            px_0___,
            px_000_
        ))  # E
        pxF = np.vstack((
            px_000_,
            px_0___,
            px_00__,
            px_0___,
            px_0___
        ))  # F
        pxG = np.vstack((
            px_000_,
            px_0___,
            px_0_0_,
            px_0_0_,
            px_000_
        ))  # G
        pxH = np.vstack((
            px_0_0_,
            px_0_0_,
            px_000_,
            px_0_0_,
            px_0_0_
        ))  # H
        pxI = np.vstack((
            px__0__,
            px_____,
            px__0__,
            px__0__,
            px__0__
        ))  # I
        pxJ = np.vstack((
            px___0_,
            px___0_,
            px___0_,
            px_0_0_,
            px_000_
        ))  # J
        pxK = np.vstack((
            px_0_0_,
            px_0_0_,
            px_00__,
            px_0_0_,
            px_0_0_
        ))  # K
        pxL = np.vstack((
            px_0___,
            px_0___,
            px_0___,
            px_0___,
            px_000_
        ))  # L
        pxM = np.vstack((
            px0___0,
            px00_00,
            px0_0_0,
            px0___0,
            px0___0
        ))  # M
        pxN = np.vstack((
            px_00__,
            px_0_0_,
            px_0_0_,
            px_0_0_,
            px_0_0_
        ))  # N
        pxO = np.vstack((
            px_000_,
            px_0_0_,
            px_0_0_,
            px_0_0_,
            px_000_
        ))  # O
        pxP = np.vstack((
            px_000_,
            px_0_0_,
            px_000_,
            px_0___,
            px_0___
        ))  # P
        pxQ = np.vstack((
            px_000_,
            px_0_0_,
            px_0_0_,
            px_0_0_,
            px_00_0
        ))  # Q
        pxR = np.vstack((
            px_000_,
            px_0_0_,
            px_00__,
            px_0_0_,
            px_0_0_
        ))  # R
        pxS = np.vstack((
            px__00_,
            px_0___,
            px_000_,
            px___0_,
            px_00__
        ))  # S
        pxT = np.vstack((
            px_000_,
            px__0__,
            px__0__,
            px__0__,
            px__0__
        ))  # T
        pxU = np.vstack((
            px_0_0_,
            px_0_0_,
            px_0_0_,
            px_0_0_,
            px_00__
        ))  # U
        pxV = np.vstack((
            px_0_0_,
            px_0_0_,
            px_0_0_,
            px_0_0_,
            px__0__
        ))  # V
        pxW = np.vstack((
            px0___0,
            px0___0,
            px0_0_0,
            px00_00,
            px0___0
        ))  # W
        pxX = np.vstack((
            px_0_0_,
            px_0_0_,
            px__0__,
            px_0_0_,
            px_0_0_
        ))  # X
        pxY = np.vstack((
            px_0_0_,
            px_0_0_,
            px_000_,
            px__0__,
            px__0__
        ))  # Y
        pxZ = np.vstack((
            px_000_,
            px___0_,
            px__0__,
            px_0___,
            px_000_
        ))  # Z
        pxALPHABET = [pxA, pxB, pxC, pxD, pxE, pxF, pxG, pxH, pxI, pxJ, pxK, pxL,
                    pxM, pxN, pxO, pxP, pxQ, pxR, pxS, pxT, pxU, pxV, pxW, pxX, pxY, pxZ]
        px0 = pxO  # 0
        px1 = np.vstack((
            px__00_,
            px___0_,
            px___0_,
            px___0_,
            px___0_
        ))  # 1
        px2 = np.vstack((
            px_000_,
            px___0_,
            px_000_,
            px_0___,
            px_000_
        ))  # 2
        px3 = np.vstack((
            px_000_,
            px___0_,
            px__00_,
            px___0_,
            px_000_
        ))  # 3
        px4 = np.vstack((
            px_0_0_,
            px_0_0_,
            px_000_,
            px___0_,
            px___0_
        ))  # 4
        px5 = np.vstack((
            px_000_,
            px_0___,
            px_000_,
            px___0_,
            px_000_
        ))  # 5
        px6 = np.vstack((
            px_000_,
            px_0___,
            px_000_,
            px_0_0_,
            px_000_
        ))  # 6
        px7 = np.vstack((
            px_000_,
            px___0_,
            px__0__,
            px__0__,
            px__0__
        ))  # 7
        px8 = np.vstack((
            px_000_,
            px_0_0_,
            px_000_,
            px_0_0_,
            px_000_
        ))  # 8
        px9 = np.vstack((
            px_000_,
            px_0_0_,
            px_000_,
            px___0_,
            px_000_
        ))  # 9
        pxDIGIT = {0: px0, 1: px1, 2: px2, 3: px3, 4: px4, 5: px5, 6: px6, 7: px7, 8: px8, 9: px9, 10: px0, 11: px1, 12: px2,
                13: px3, 14: px4, 15: px5, 16: px6, 17: px7, 18: px8, 19: px9, 20: px0, 21: px1, 22: px2, 23: px3, 24: px4, 25: px5}
        # change winner color & prize color
        wImg = Image.fromarray(pxALPHABET[self.ALPHABET.index(self.winner)])
        pImg = Image.fromarray(pxDIGIT[self.prize])
        for i in range(5):
            for j in range(5):
                wdata = wImg.getpixel((i, j))
                pdata = pImg.getpixel((i, j))
                if wdata == DEFAULT_COLOR:
                    wImg.putpixel((i, j), PICKED_COLOR)
                if pdata == DEFAULT_COLOR:
                    pImg.putpixel((i, j), PICKED_COLOR)
        wImgAry = np.array(wImg)
        pImgAry = np.array(pImg)


        # draw peoples row & startrow & digit_row & targets row & end_row
        for i in range(len(self.map[1])):
            if i == 0:
                if i == self.ALPHABET.index(self.winner):
                    peoples = wImgAry
                    start_row = pxㅣsr
                else:
                    peoples = pxA
                    start_row = pxㅣs
                if self.prize == 0:
                    targets = redDot
                    end_row = pxㅣer
                    digit_row = pImgAry
                else:
                    targets = blackDot
                    end_row = pxㅣe
                    digit_row = px0
                pading_row = px_____
            else:
                if i == self.ALPHABET.index(self.winner):
                    peoples = np.column_stack((peoples, wImgAry))
                    start_row = np.column_stack((start_row, pxㅣsr))
                else:
                    peoples = np.column_stack((peoples, pxALPHABET[i]))
                    start_row = np.column_stack((start_row, pxㅣs))
                if i == self.prize:
                    targets = np.column_stack((targets, redDot))
                    end_row = np.column_stack((end_row, pxㅣer))
                    digit_row = np.column_stack((digit_row, pImgAry))
                else:
                    targets = np.column_stack((targets, blackDot))
                    end_row = np.column_stack((end_row, pxㅣe))
                    digit_row = np.column_stack((digit_row, pxDIGIT[i]))
                pading_row = np.column_stack((pading_row, px_____))

        pixmap = np.vstack((pading_row, peoples, start_row))

        # draw map
        expxㅏ = False
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if j == 0: # first of row
                    if self.map[i][j] == 0: # ㅣ
                        if self.route[i][j] == 1:
                            curRow = pxㅣ_r
                        else:
                            curRow = pxㅣ
                        expxㅏ = False
                    else: # not ㅣ
                        if self.route[i][j] == 1:
                            if self.route_dict[i][0] == j:
                                curRow = pxㅏ_ru
                            else:
                                curRow = pxㅏ_rd
                        else:
                            curRow = pxㅏ
                        expxㅏ = True
                else: # rest of row
                    if self.map[i][j] == 0: # ㅣ
                        if self.route[i][j] == 1:
                            curRow = np.column_stack((curRow, pxㅣ_r))
                        else:
                            curRow = np.column_stack((curRow, pxㅣ))
                        expxㅏ = False
                    else: # not ㅣ
                        if expxㅏ: # ㅓ
                            if self.route[i][j] == 1: # route
                                if self.route_dict[i][0] == j:
                                    curRow = np.column_stack((curRow, pxㅓ_ru))
                                else:
                                    curRow = np.column_stack((curRow, pxㅓ_rd))
                            else: # not route
                                curRow = np.column_stack((curRow, pxㅓ))
                            expxㅏ = False
                        else: # ㅏ
                            if self.route[i][j] == 1: # route
                                if self.route_dict[i][0] == j:
                                    curRow = np.column_stack((curRow, pxㅏ_ru))
                                else:
                                    curRow = np.column_stack((curRow, pxㅏ_rd))
                            else: # not route
                                curRow = np.column_stack((curRow, pxㅏ))
                            expxㅏ = True
            expxㅏ = False
            pixmap = np.vstack((pixmap, curRow))

        pixmap = np.vstack((pixmap, end_row, digit_row, targets))

        original_img = Image.fromarray(pixmap)
        # resize to approx. max_width or max_height
        resize_ratio = min(int(max_width / original_img.width),
                           int(max_height / original_img.height))
        resize_img = original_img.resize((int(original_img.width * resize_ratio), int(
            original_img.height * resize_ratio)), Image.Resampling.BOX)
        return resize_img