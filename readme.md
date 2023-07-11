# 開發一組具備OLED單色螢幕及按鈕的復古遊戲機
課程出發點為教導學生簡易 IO ，利用按鈕輸入以及螢幕控制，搭配點陣圖以試算表讀取座標繪圖運用。利用 OLED 點亮後，不進行刷新。記錄軌跡後存成 list 格式，碰觸到自己軌跡則遊戲結束，類似貪食蛇遊戲規則，並計算軌跡點之數量，學習檔案存取。迷宮繪製，將迷宮併入軌跡，以條件式判斷點是否位於 list 中。課程可為專題製作，改為兩個玩家同時進行，各自操控所屬進行對戰。為符合7~9年級學習內容，本課程不涉及物件導向。

## 硬體組裝
1. 材料
	+ raspberry pico 
	+ OLED 0.96":I2C( GND - VCC - SCL - SDA)
	+ 按鈕 * 7
	+ 有源蜂鳴器
	+ M2 , M3 螺絲 = 8 , 4
1. 配置
	1. 解銲OLED、根據接線圖銲接 OLED 與 pico
		+ 接線圖 ![pin](/media/01_oled.png)
	1. 放按鈕、蜂鳴器於上層壓克力板、銲接配線、貼膠帶
		+ 接線圖 ![pin](/media/02_button.png)
	1. 放 Reset 按鈕於下層、穿過壓克力與 pico 銲接、鎖 M2 螺絲 4 個
	1. 鎖 OLED 與上層壓克力的 M2 螺絲 4 個
	1. 鎖上下層壓克力間 M3 螺絲 4 個
		+ 實際圖 ![pin](/media/03_arr.jpeg)
		+ 實際圖 ![pin](/media/03_arrBack.jpeg)
		+ 實際圖 ![pin](/media/04_oledOnBoard.jpeg)
		+ 實際圖 ![pin](/media/05_finish.jpeg)

## 流程
0. pinTest 硬體測試
	+ OLED 管理套件 - 安裝 ssd1306(micropython-ssd1306)
	+ 按鈕
	+ 蜂鳴器
1. button_thread，雙執行緒：按鈕只兩個，利用一個 thread 讀取方向、主程式顯示方向
	1. 利用按鈕決定方向
		+ 先設定方向 = 0 (0,1,2,3 = 右,下,左,上)
		+ 如果按鈕 == 0 , 則 方向值加減 1
			+ 右按鈕 ,  方向 + 1
			+ 左按鈕 ,  方向 - 1
	2. 主程式
		+ 根據 %4 的結果判斷方向，如果餘數 == 0 ,1 , 2 , 3 ，則 螢幕呈現各方向
		+ 加上一個兩個按鈕同時按就停止的條件式
1. 改成會跑的點
	+ 方向 0 , x + 1
	+ 方向 1 , y + 1
	+ 另外兩個怎麼設計呢？
1. 保留軌跡
	+ OLED 不刷新，螢幕點不消失
	+ 跑到邊緣後要能跳到螢幕另一側
		+ x > 127 , x = 0
		+ x < 0 , x = 127
		+ y 要怎麼改呢？
	+ 把軌跡存成 list
1. 如果在軌跡內，則....
1. 讀取檔案
1. 失敗了。就爆炸吧
	+ 定義函式
	+ 繪圖
		+ [圖檔範例](http://gg.gg/picocamp)		
		+ 讀取檔案
		+ 把每一個座標抓出後繪點陣圖
	+ break
1. 單一迷宮檔案製作
1. 迷宮跑者
	1. google 試算表繪圖、複製座標資料
	2. 第一列資料包括預設方向、起始點座標、終點座標（好幾個）....
	3. 用 readlines 讀取剩餘資料，str 轉為 int , 存為 list 為 path 軌跡資料，用以產生碰撞時、跟自己的軌跡合併 
1. 計算分數
	1. 當座標所在 in path:
		1. 蜂鳴器叫
		3. 遊戲結束
	2. 當抵達終點：
		1. 好棒棒
1. 不只一個迷宮時，使用 for 迴圈直接按順序下去
	1. 設定迷宮初始檔名值
	2. 沒抵達終點時，使用 contiune，進行下一次迭代繼續重複
	3. (若抵達才開始進行)，這裡不縮行，進行蜂鳴、算分數、跑過關動畫、進入下一關 maze
