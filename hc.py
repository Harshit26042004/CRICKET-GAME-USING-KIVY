import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
import random
import math

tot=0
innings=1
tot1=0
x=0
u_ball=0
c_ball=0
u_overs=0
c_overs=0
u_rr=0
c_rr=0
u_sr=0
c_sr=0
y=0

def play():
	class mygrid(GridLayout):
		def __init__(self,**kwargs):
			super(mygrid,self).__init__(**kwargs)
			
			self.cols=1
			self.tossgrid=GridLayout()
			self.tossgrid.cols=1
			self.toss=Button(text="Toss")
			self.tossgrid.add_widget(self.toss)
			self.toss.bind(on_press=self.toss_control)
			self.input=Button(background_color=[101,67,33,0.5])
			self.tossgrid.add_widget(self.input)
			self.add_widget(self.tossgrid)
			self.topgrid=GridLayout()
			self.topgrid.cols=3
			self.grid=GridLayout()
			self.grid.cols=3
			self.grid.add_widget(Label(text="Your total score:"))
			self.grid.add_widget(Label(text="Target:"))
			self.grid.add_widget(Label(text="Opponent total score:"))
			self.input1=TextInput()
			self.grid.add_widget(self.input1)
			self.input2=TextInput()
			self.grid.add_widget(self.input2)
			self.input3=TextInput()
			self.grid.add_widget(self.input3)
			self.grid.add_widget(Label(text="Your current run:"))
			self.grid.add_widget(Label(text=""))
			self.grid.add_widget(Label(text="Opponent current run:"))
			self.input4=TextInput()
			self.grid.add_widget(self.input4)
			self.input5=TextInput()
			self.grid.add_widget(self.input5)
			self.input6=TextInput()
			self.grid.add_widget(self.input6)
			self.add_widget(self.grid)

	
			self.button1=Button(text='1')
			self.topgrid.add_widget(self.button1)
			self.button1.bind(on_press=self.number1)
			self.button2=Button(text='2')
			self.topgrid.add_widget(self.button2)
			self.button2.bind(on_press=self.number2)
			self.button3=Button(text='3')
			self.topgrid.add_widget(self.button3)
			self.button3.bind(on_press=self.number3)
			self.button4=Button(text='4')
			self.topgrid.add_widget(self.button4)
			self.button4.bind(on_press=self.number4)
			self.button5=Button(text='5',)
			self.topgrid.add_widget(self.button5)
			self.button5.bind(on_press=self.number5)
			self.button6=Button(text='6')
			self.topgrid.add_widget(self.button6)
			self.button6.bind(on_press=self.number6)
			self.add_widget(self.topgrid)
			self.bottomgrid=GridLayout()
			self.bottomgrid.cols=1
			self.bottomgrid2=GridLayout(cols=2)
			self.add_widget(self.bottomgrid)
			self.resultlab=Button(background_color=[101,67,33,0.5])
			self.bottomgrid.add_widget(self.resultlab)
			self.statsbut=Button(text='View Statistics')
			self.bottomgrid.add_widget(self.statsbut)
			self.statsbut.bind(on_press=self.statis)
			self.exitbut=Button(text='Exit')
			self.bottomgrid2.add_widget(self.exitbut)
			self.exitbut.bind(on_press=myapp.close_application)
			self.playbut=Button(text='Play again')
			self.bottomgrid2.add_widget(self.playbut)
			self.box=1
			self.playbut.bind(on_press=self.play_again)
			self.bottomgrid.add_widget(self.bottomgrid2)
		    
		def onButtonPress(self,button):
			self.layout = GridLayout(cols = 1, padding = 10)
			self.popup = Popup(title ='Toss',content = self.layout)
			self.popup.open()
			heads= Button(text = "Heads")
			tails = Button(text = "Tails") 
			self.layout.add_widget(heads) 
			self.layout.add_widget(tails)  

			heads.bind(on_press=self.heads)
			tails.bind(on_press=self.tails)
	
		def heads(self,instance):
			global x
			global innings
			global tot
			global tot1
			tot=0
			tot1=0
			innings=1
			a=1
			if a == random.randint(0,1):
				layout=GridLayout(cols=1,padding=10)
				self.tosswon=Popup(title='You won the toss',content=layout)
				batting=Button(text='Batting')
				bowling=Button(text='Bowling')
				layout.add_widget(batting)
				self.tosswon.open()
				layout.add_widget(bowling)
				batting.bind(on_press=self.batfirst)
				bowling.bind(on_press=self.bowlfirst)
			else:
				c_toss=random.randint(0,1)
				if c_toss==1:
					x=2
					self.input.text='Computer won the toss and decided to bat first'
				if c_toss==0:
					x=1
					self.input.text='Computer won the toss and decided to bowl first'
				self.popup.dismiss()
			
		def tails(self,instance):
			global x
			global innings
			global tot
			global tot1
			tot=0
			tot1=0
			innings=1
			a=0
			if a == random.randint(0,1):
				layout=GridLayout(cols=1,padding=10)
				self.tosswon=Popup(title='You won the toss',content=layout)
				batting=Button(text='Batting')
				bowling=Button(text='Bowling')
				layout.add_widget(batting)
				self.tosswon.open()
				layout.add_widget(bowling)
				batting.bind(on_press=self.batfirst)
				bowling.bind(on_press=self.bowlfirst)
			else:
				c_toss=random.randint(0,1)
				if c_toss==1:
					x=2
					self.input.text='Computer won the toss and decided to bat first'
				if c_toss==0:
					x=1
					self.input.text='Computer won the toss and decided to bowl first'
				self.popup.dismiss()
				
		def batfirst(self,instance):
			global x
			global innings
			global tot
			global tot1
			tot=0
			tot1=0
			self.input.text='You won the toss and decided to bat first'
			x=1
			innings=1
			self.tosswon.dismiss()
			self.popup.dismiss()
			
		def bowlfirst(self,instance):
			global x
			global innings
			global tot
			global tot1
			tot=0
			tot1=0
			self.input.text='You won the toss and decided to bowl first'
			x=2
			innings=1
			self.tosswon.dismiss()
			self.popup.dismiss()
			
			
		def batting(self,runs):
			global tot
			global innings
			global u_ball
			u_ball+=1
			while True:
				c_run=random.randint(1,6)
				self.input6.text=str(c_run)
				self.input4.text=str(runs)
				if c_run==runs:
					self.input1.text=str(tot)
					self.input2.text=str(tot+1)
					self.input5.text='OUT!'
					innings=2
					return
				else:
					tot+=runs
					self.input1.text=str(tot)
					return
			
		def bowling(self,runs):
			global tot1
			global innings
			global c_ball
			c_ball+=1
			while True:
				c_run=random.randint(1,6)
				self.input4.text=str(runs)
				self.input6.text=str(c_run)
				if c_run==runs:
					self.input5.text='OUT!'
					innings=3
					if tot1==tot:
						self.resultlab.text='Game Tied'
						self.resultbox(0)
						self.stat(1)
						return
					if tot1<tot:
						self.resultlab.text='You won the game'
						self.resultbox(1)
						self.stat(1)
						return
				else:
					tot1+=c_run
					self.input3.text=str(tot1)
					if tot1>tot:
						self.resultlab.text='Computer won the game'
						innings=3
						self.resultbox(2)
						self.stat(1)
					return
						
		def batting1(self,runs):
			global tot1
			global innings
			global c_ball
			c_ball+=1
			while True:
				c_run=random.randint(1,6)
				self.input4.text=str(runs)
				self.input6.text=str(c_run)
				if c_run==runs:
					self.input3.text=str(tot1)
					self.input2.text=str(tot1+1)
					innings=2
					self.input5.text='OUT!'
					return
				else:
					tot1+=c_run
					self.input3.text=str(tot1)
					return
					
		def bowling1(self,runs):
			global tot
			global innings
			global u_ball
			u_ball+=1
			while True:
				c_run=random.randint(1,6)
				self.input4.text=str(runs)
				self.input6.text=str(c_run)
				if c_run==runs:
					self.input1.text=str(tot)
					self.input5.text='OUT!'
					innings=3
					if tot1==tot:
						self.resultlab.text='Game Tied'
						self.resultbox(0)
						self.stat(1)
						return
					if tot1>tot:
						self.resultlab.text='Computer won the game'
						self.resultbox(2)
						self.stat(1)
						return
				else:
					tot+=runs
					self.input1.text=str(tot)
					if tot1<tot:
						innings=3
						self.resultlab.text='You won the game'
						self.resultbox(1)
						self.stat(1)
					return
	
		def statis(self,instance):
			self.stat(2)
			
			
		def stat(self,z):
			global tot
			global tot1
			global u_ball
			global c_ball
			global u_overs
			global c_overs
			global u_rr
			global u_sr
			global c_rr
			global c_sr
			
			for i in range(0,1):
				if u_ball==0 or c_ball==0:
					if u_ball==0 and c_ball!=0:
						u_overs=0
						u_rr=' - '
						u_sr=' - '
						c_overs=math.floor(c_ball/6)+((c_ball%6)/10)
						c_rr=round((tot1/c_ball)*6,2)
						c_sr=round((tot1/c_ball)*100,2)
					if c_ball==0 and u_ball!=0:
						c_overs=0
						c_rr=' - '
						c_sr=' - '
						u_overs=math.floor(u_ball/6)+((u_ball%6)/10)
						u_rr=round((tot/u_ball)*6,2)
						u_sr=round((tot/u_ball)*100,2)	
					if u_ball==0 and c_ball==0:
						u_overs=0
						u_rr=' - '
						u_sr=' - '
						c_overs=0
						c_rr=' - '
						c_sr=' - '		
				else:
					u_overs=math.floor(u_ball/6)+((u_ball%6)/10)
					u_rr=round((tot/u_ball)*6,2)
					u_sr=round((tot/u_ball)*100,2)
					c_overs=math.floor(c_ball/6)+((c_ball%6)/10)
					c_rr=round((tot1/c_ball)*6,2)
					c_sr=round((tot1/c_ball)*100,2)
					
					
			for i in range(0,1):
				if z==1:
					self.u_stats=Label(text='Your total score: {}\nBalls faced by you: {}\nOvers faced by you: {}\nYour run rate: {}\nYour strike rate: {}'.format(tot,u_ball,u_overs,u_rr,u_sr))
					self.stats.add_widget(self.u_stats)
					self.c_stats=Label(text='Opponent total score: {}\nBalls faced by opponent: {}\nOvers faced by opponent: {}\nOpponent run rate: {}\nOpponent strike rate: {}'.format(tot1,c_ball,c_overs,c_rr,c_sr))
					self.stats.add_widget(self.c_stats)
				elif z==2:
					self.statistic=GridLayout(cols=1,padding=0)
					self.grid2=GridLayout(cols=2)
					self.statistic.add_widget(self.grid2)
					self.statistics=Popup(title='Game statistics',content=self.statistic)
					self.statistics.open()
					self.u_stats=Label(text='Your total score: {}\nBalls faced by you: {}\nOvers faced by you: {}\nYour run rate: {}\nYour strike rate: {}'.format(tot,u_ball,u_overs,u_rr,u_sr))
					self.grid2.add_widget(self.u_stats)
					self.c_stats=Label(text='Opponent total score: {}\nBalls faced by opponent: {}\nOvers faced by opponent: {}\nOpponent run rate: {}\nOpponent strike rate: {}'.format(tot1,c_ball,c_overs,c_rr,c_sr))
					self.grid2.add_widget(self.c_stats)
					self.grid3=GridLayout(cols=1)
					self.statistic.add_widget(self.grid3)
					self.resultstat=Label(text=self.resultlab.text,font_size=72)
					self.grid3.add_widget(self.resultstat)
					self.exitstat=Button(text='Return')
					self.grid3.add_widget(self.exitstat)
					self.exitstat.bind(on_press=self.statistics.dismiss)
					self.exitgame=Button(text='Exit Game')
					self.grid3.add_widget(self.exitgame)
					self.exitgame.bind(on_press=myapp.close_application)
			return
			
			
		def resultbox(self,res):
			self.layout=GridLayout(cols=1,padding=0)
			self.result1=Popup(title='Result',content=self.layout)
			self.layout2=GridLayout(cols=2,padding=0)
			if res==0:
				text1=Label(text='Game tied',font_size=72)
			elif res==1:
				text1=Label(text='You won the game',font_size=72)
			elif res==2:
				text1=Label(text='Computer won the game',font_size=72)
			self.layout.add_widget(text1)
			self.stats=GridLayout(cols=2)
			self.layout.add_widget(self.stats)
			self.viewscore=Button(text='View Final Score')
			self.layout.add_widget(self.viewscore)
			self.viewscore.bind(on_press=self.result1.dismiss)
			exit=Button(text='Exit')
			playagain=Button(text='Play again')
			self.layout2.add_widget(exit)
			self.layout2.add_widget(playagain)
			self.result1.open()
			self.layout.add_widget(self.layout2)
			exit.bind(on_press=myapp.close_application)
			self.box=0
			playagain.bind(on_press=self.play_again)
			
		def control(self,run):
			if innings==1 and x==1:
				self.batting(run)		
			elif innings==2 and x==1:
				self.input5.text=''
				self.bowling(run)
			elif innings==1 and x==2:
				self.input5.text=''
				self.batting1(run)
			elif innings==2 and x==2:
				self.input5.text=''
				self.bowling1(run)
				
		def toss_control(self,instance):
			global y
			if y==0:
				self.onButtonPress(instance)
				y+=1
			else:
				return
			

		def play_again(self,instance):
			global tot
			global innings
			global tot1
			global x
			global u_ball
			global c_ball
			global y
			
			tot=0
			innings=1
			tot1=0
			x=0
			u_ball=0
			c_ball=0
			y=0
			self.input.text=''
			self.resultlab.text=''
			
			if self.box==0:
				self.result1.dismiss()
			App.get_running_app().stop()
			play()
			
		def number1(self,instance):
			self.control(1)
			
		def number2(self,instance):
			self.control(2)
			
		def number3(self,instance):
			self.control(3)
			
		def number4(self,instance):
			self.control(4)
			
		def number5(self,instance):
			self.control(5)
			
		def number6(self,instance):
			self.control(6)

			
	class myapp(App):
		def close_application(self):
			App.get_running_app().stop()
			Window.close()
			
		def build(self):
			return mygrid()
	
	if __name__=='__main__':
		myapp().run()
		

play()

