#khai báo các module cần thiết 
from PIL import Image, ImageTk #hàm phụ trợ cho giao diện lồng ảnh trong giao diện
from tkinter import Tk, BOTH, Canvas, NW, Frame, Label 
from tkinter import messagebox as mbox 
from tkinter.ttk import Frame, Button, Style #hàm phụ trợ thiết kế giao diện
import cv2 
import numpy as np 

#khai báo các biến toàn cục
img = cv2.imread('twice.jpg')
rows, cols, ch = img.shape

class BTL(Frame):
	def __init__(self, parent): #hàm khởi tạo tkinter
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()

	def initUI(self): #hàm thiết lập UI
		self.parent.title('Bài Tập Lớn') #tạo tiêu đề cho khung Tkinter
		self.pack(fill = BOTH, expand = 1)

		Style().configure("TFrame", background="#333")

		bard = Image.open("logo.png")
		bardejov = ImageTk.PhotoImage(bard)
		label1 = Label(self, image = bardejov)
		label1.image = bardejov
		label1.place(x = 0, y = 0)

		introd = Button(self, text = "General Introduction", command = self.onIntro)
		introd.grid(padx = 10, pady = 20)
		introd.place(x = 150, y = 10)
		resize = Button(self, text = "Scaling", command = self.onResize)
		resize.grid(row = 1, column = 0)
		resize.place(x = 170, y = 50)
		transl = Button(self, text = "Translation", command = self.onTranslation)
		transl.grid(row = 2, column = 0)
		transl.place(x = 170, y = 80)
		rotate = Button(self, text = "Rotate", command = self.onRotate)
		rotate.grid(row = 3, column = 0)
		rotate.place(x = 170, y = 110)
		affine = Button(self, text = "Affine Transform", command = self.onAffine)
		affine.grid(row = 4, column = 0)
		affine.place(x = 157, y = 140)
		perspt = Button(self, text = "Perspective Transform", command = self.onPerspect)
		perspt.grid(row = 5, column = 0)
		perspt.place(x = 142, y = 170)
		applic = Button(self, text = "Application", command = self.onApply)
		applic.grid(row = 5, column = 0)
		applic.place(x = 170, y = 200)
		exit11 = Button(self, text = "Exit", command = self.onQuit)
		exit11.grid(row = 6, column = 0)
		exit11.place(x = 170, y = 270)

	def onQuit (self): #hàm thoát/ dừng chương trình
		self.quit()

	def onIntro (self): #hàm giới thiệu chung chung =)) mặc dù hong biết cần hong nữa
		mbox.showinfo("Hello everyone!!!", "Đây là bài tập lớn của nhóm mình")

	def nothing (x, event = None): #hàm đúng theo tên là nothing =)) 
		pass

	def onResize (self): #hàm Scaling trong tài liệu
		im = img

		cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)
		cv2.namedWindow('Resize', cv2.WINDOW_AUTOSIZE)

		cv2.createTrackbar('x', 'Resize', 10, 20, self.nothing)	
		cv2.createTrackbar('y', 'Resize', 10, 20, self.nothing)
		cv2.createTrackbar('Larange', 'Resize', 0, 2, self.nothing)
		cv2.createTrackbar('mode', 'Resize', 0, 1, self.nothing) #với 0 là chưa chạy, 1 là phóng to, 2 là thu nhỏ

		while(1):
			cv2.imshow("Image", im)

			k = cv2.waitKey(1) & 0xFF
			if k == 27: 
				break

			Ox = cv2.getTrackbarPos ('x', 'Resize')
			Oy = cv2.getTrackbarPos ('y', 'Resize')
			b = cv2.getTrackbarPos ('Larange', 'Resize')
			if b == 0:
				b = cv2.INTER_AREA
			if b == 1:
				b = cv2.INTER_CUBIC
			if b == 2:
				b = cv2.INTER_LINEAR

			M1 = cv2.getTrackbarPos ('mode', 'Resize')

			Ox = Ox/10
			Oy = Oy/10

			if Ox == 0: 
				Ox = 1/10

			if Oy == 0:
				Oy = 1/10

			if M1 == 0:
				self.nothing
			if M1 == 1:
				im = cv2.resize(img, None, fx = Ox, fy = Oy, interpolation = b)
		cv2.destroyAllWindows()

	def onTranslation (self): #hàm translation
		im = img

		cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
		cv2.namedWindow('Translation', cv2.WINDOW_AUTOSIZE)

		cv2.createTrackbar('Zn', 'Translation', 10, 20, self.nothing)
		cv2.createTrackbar('Oz1', 'Translation', 20, 40, self.nothing)
		cv2.createTrackbar('Oy', 'Translation', cols, cols*2, self.nothing)#Chỉnh thông số theo số pixel ảnh
		cv2.createTrackbar('Oz2', 'Translation', 20, 40, self.nothing)
		cv2.createTrackbar('Zd', 'Translation', 10, 20, self.nothing)
		cv2.createTrackbar('Ox', 'Translation', rows, rows*2, self.nothing)#Chỉnh thông số theo số pixel ảnh
		
		cv2.createTrackbar('switch', 'Translation', 0, 1, self.nothing)

		while(1):
			cv2.imshow("Image", im)

			k = cv2.waitKey(1) & 0xFF
			if k == 27: 
				break

			a1 = cv2.getTrackbarPos ('Zn', 'Translation')
			b1 = cv2.getTrackbarPos ('Oz1', 'Translation')
			y = cv2.getTrackbarPos ('Oy', 'Translation')
			b2 = cv2.getTrackbarPos ('Oz2', 'Translation')
			a2 = cv2.getTrackbarPos ('Zd', 'Translation')
			x = cv2.getTrackbarPos ('Ox', 'Translation')

			s = cv2.getTrackbarPos ('switch','Translation')

			#hệ số zoom (ngang, dọc)
			a1 = a1/10
			if a1 == 0:	a1 = 1/10
			a2 = a2/10
			if a2 == 0:	a2 = 1/10

			#hệ số trục Oz Có thể chỉnh thêm nếu muốn
			b1 = (b1-20)/10 
			b2 = (b2-20)/10

			#hệ số trục tọa độ
			y = y - cols
			x = x - rows

			M = np.float32([[a1, b1, y], [b2, a2, x]])
			if s == 0:
				self.nothing

			if s == 1:
				im = cv2.warpAffine (img, M, (cols, rows))
		cv2.destroyAllWindows()

	def onRotate (self): #hàm Rotate
		im = img

		cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
		cv2.namedWindow('Rotate', cv2.WINDOW_AUTOSIZE)

		cv2.createTrackbar('alpha', 'Rotate', 360, 720, self.nothing)
		cv2.createTrackbar('Width', 'Rotate', int(cols/2), cols, self.nothing)
		cv2.createTrackbar('Height', 'Rotate', int(rows/2), rows, self.nothing)
		cv2.createTrackbar('Zoom', 'Rotate', 10, 20, self.nothing)
		cv2.createTrackbar('switch', 'Rotate', 0, 1, self.nothing)

		while(1):
			cv2.imshow("Image", im)

			k = cv2.waitKey(1) & 0xFF
			if k == 27: 
				break

			a = cv2.getTrackbarPos ('alpha', 'Rotate')
			b = cv2.getTrackbarPos ('Zoom', 'Rotate')
			c = cv2.getTrackbarPos ('width', 'Rotate')
			d = cv2.getTrackbarPos ('height', 'Rotate')
			s = cv2.getTrackbarPos ('switch','Rotate')

			a = a - 360
			b = b / 10
			if b == 0:
				b = 1/10

			M1 = cv2.getRotationMatrix2D ((c, d), a, b)# hệ số cuối là hệ số zoom

			if s == 0:
				self.nothing

			if s == 1:
				im = cv2.warpAffine (img, M1, (cols, rows))
		cv2.destroyAllWindows()

	def onAffine (self): #hàm Afine
		im = img

		cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
		cv2.namedWindow('Affine', cv2.WINDOW_NORMAL)

		#theo lý thuyết thì đây là 3 điểm đầu vào
		cv2.createTrackbar('a1', 'Affine', 50, rows, self.nothing)
		cv2.createTrackbar('a2', 'Affine', 50, cols, self.nothing)
		cv2.createTrackbar('b1', 'Affine', 200, rows, self.nothing) 
		cv2.createTrackbar('b2', 'Affine', 50, cols, self.nothing)
		cv2.createTrackbar('c1', 'Affine', 50, rows, self.nothing)
		cv2.createTrackbar('c2', 'Affine', 200, cols, self.nothing)

		#3 điểm đầu ra #lưu ý mốt đổi rows vs cows lại với nhau
		cv2.createTrackbar('d1', 'Affine', rows, 2*rows, self.nothing)
		cv2.createTrackbar('d2', 'Affine', cols, 2*cols, self.nothing)
		cv2.createTrackbar('e1', 'Affine', rows, 2*rows, self.nothing)
		cv2.createTrackbar('e2', 'Affine', cols, 2*cols, self.nothing)
		cv2.createTrackbar('f1', 'Affine', rows, 2*rows, self.nothing)
		cv2.createTrackbar('f2', 'Affine', cols, 2*cols, self.nothing)

		switch = "0: OFF" + "\n1:Affine"
		cv2.createTrackbar(switch, 'Affine', 0, 1, self.nothing)

		while(1):
			cv2.imshow("Image", im)

			k = cv2.waitKey(1) & 0xFF
			if k == 27: 
					break

			a1 = cv2.getTrackbarPos ('a1', 'Affine')
			a2 = cv2.getTrackbarPos ('a2', 'Affine')
			b1 = cv2.getTrackbarPos ('b1', 'Affine')
			b2 = cv2.getTrackbarPos ('b1', 'Affine')
			c1 = cv2.getTrackbarPos ('c1', 'Affine')
			c2 = cv2.getTrackbarPos ('c2', 'Affine')

			d1 = cv2.getTrackbarPos ('d1', 'Affine')
			d1 = d1 - rows
			d2 = cv2.getTrackbarPos ('d2', 'Affine')
			d2 = d2 - cols
			e1 = cv2.getTrackbarPos ('e1', 'Affine')
			e1 = e1 - rows
			e2 = cv2.getTrackbarPos ('e2', 'Affine')
			e2 = e2 - cols
			f1 = cv2.getTrackbarPos ('f1', 'Affine')
			f1 = f1 - rows
			f2 = cv2.getTrackbarPos ('f2', 'Affine')
			f2 = f2 - cols

			s = cv2.getTrackbarPos (switch, 'Affine')

			#số liệu cho Affine
			pts1 = np.float32([[a1, a2], [b1, b2], [c1, c2]])
			pts2 = np.float32([[d1, d2], [e1, e2], [f1, f2]])
			M = cv2.getAffineTransform (pts1, pts2)

			if s == 0:
				self.nothing
			if s == 1:
				im = cv2.warpAffine (img, M, (rows, cols))

		cv2.destroyAllWindows()

	def onPerspect (self):
		im = img

		cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
		cv2.namedWindow('Perspect', cv2.WINDOW_NORMAL)

		cv2.createTrackbar('a1', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('a2', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('b1', 'Perspect', 0, 255, self.nothing) 
		cv2.createTrackbar('b2', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('c1', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('c2', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('d1', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('d2', 'Perspect', 0, 255, self.nothing)

		cv2.createTrackbar('e1', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('e2', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('f1', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('f2', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('g1', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('g2', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('h1', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('h2', 'Perspect', 0, 255, self.nothing)

		cv2.createTrackbar('row', 'Perspect', 0, 255, self.nothing)
		cv2.createTrackbar('col', 'Perspect', 0, 255, self.nothing) 

		switch = "0: OFF" + "\n1: Perspective"
		cv2.createTrackbar(switch, 'Perspect', 0, 1, self.nothing)

		while(1):
			cv2.imshow("Image", im)

			k = cv2.waitKey(1) & 0xFF
			if k == 27: 
					break

			a1 = cv2.getTrackbarPos ('a1', 'Perspect')
			a2 = cv2.getTrackbarPos ('a2', 'Perspect')
			b1 = cv2.getTrackbarPos ('b1', 'Perspect')
			b2 = cv2.getTrackbarPos ('b1', 'Perspect')
			c1 = cv2.getTrackbarPos ('c1', 'Perspect')
			c2 = cv2.getTrackbarPos ('c2', 'Perspect')
			d1 = cv2.getTrackbarPos ('d1', 'Perspect')
			d2 = cv2.getTrackbarPos ('d2', 'Perspect')

			e1 = cv2.getTrackbarPos ('e1', 'Perspect')
			e2 = cv2.getTrackbarPos ('e2', 'Perspect')
			f1 = cv2.getTrackbarPos ('f1', 'Perspect')
			f2 = cv2.getTrackbarPos ('f2', 'Perspect')
			g1 = cv2.getTrackbarPos ('g1', 'Perspect')
			g2 = cv2.getTrackbarPos ('g2', 'Perspect')
			h1 = cv2.getTrackbarPos ('h1', 'Perspect')
			h2 = cv2.getTrackbarPos ('h2', 'Perspect')

			i1 = cv2.getTrackbarPos ('row', 'Perspect')
			i2 = cv2.getTrackbarPos ('col', 'Perspect')

			s = cv2.getTrackbarPos (switch, 'Perspect')

			#số liệu cho Perspective
			pts3 = np.float32([[a1, a2], [b1, b2], [c1, c2], [d1, d2]])
			pts4 = np.float32([[e1, e2], [f1, f2], [g1, g2], [h1, h2]])
			M = cv2.getPerspectiveTransform (pts3, pts4)

			if s == 0:
				self.nothing
			if s == 1:
				im = cv2.warpPerspective (img, M, (i1, i2))

		cv2.destroyAllWindows()

	def onApply (self):
		cv2.namedWindow('Real', cv2.WINDOW_NORMAL)
		cv2.namedWindow('Face', cv2.WINDOW_NORMAL)

		face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		faces = face_cascade.detectMultiScale(img, scaleFactor = 1.337, minNeighbors = 6, minSize = (30, 30))
		number = len(faces)

		im = np.zeros((300, 300, 3), np.uint8)

		cv2.createTrackbar('Faces', 'Face', 0, number - 1, self.nothing) 
		cv2.createTrackbar('Switch', 'Face', 0, 1, self.nothing) 

		while(1):

			i = cv2.getTrackbarPos ('Faces', 'Face')
			s = cv2.getTrackbarPos ('Switch', 'Face')

			if s == 0:
				self.nothing
			if s == 1:
				x, y, w, h = faces[i] 

				pts3 = np.float32([[x, y], [x + w, y], [x, y + h], [x + w, y + h]])
				pts4 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
				M = cv2.getPerspectiveTransform (pts3, pts4)

				im = cv2.warpPerspective (img, M, (w, h))
			
			cv2.imshow("Face", im)
			cv2.imshow('Real', img)


			k = cv2.waitKey(1) & 0xFF
			if k == 27: 
				break
			
		cv2.destroyAllWindows()

root = Tk()
root.geometry("400x408+750+100")
# root.configure(background = 'blue') #chỉnh sửa màu nền
app = BTL(root)
root.mainloop()