from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk

class App(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.create_widgets()

	def create_widgets(self):
		self.fram_pesq_tag = ctk.CTkFrame(self)
		self.fram_buttons = ctk.CTkFrame(self)
		self.frame_analise = ctk.CTkFrame(self)

		self.fram_pesq_tag.pack(side=TOP,fill=X,padx=5,pady=(0,10))
		self.frame_analise.pack(side=LEFT,fill=X,expand=1,padx=5,pady=(0,10))
		self.fram_buttons.pack(side=RIGHT,fill=Y,padx=5,pady=(0,10))

		#VAR PY
		self.option_menu_options = ["CLASS_NAME","XPATH","ID","NAME","CSS","CLASS_NAMES"]
		Var_bool = BooleanVar()

		#VAR TKINTER

		self.Tag1 = StringVar()
		self.Name_tag = StringVar()
		self.Atribute_pgr = StringVar()
		self.Console = StringVar()
		self.Key_to_send = StringVar()
		self.Pesq_adentro = BooleanVar()


		self.Button_clicar = ctk.CTkButton(self.fram_buttons,text="Clicar",command=self.Clicar)
		self.Button_Send_key = ctk.CTkButton(self.fram_buttons,text="Send key",command=self.Send_key)
		self.Button_Pegar_at = ctk.CTkButton(self.fram_buttons,text='Pegar_Atributo',command=self.Pegar_Atributo)
		self.Entry_Pegar_at = ctk.CTkEntry(self.fram_buttons,textvariable=self.Atribute_pgr)
		self.Button_iframe = ctk.CTkButton(self.fram_buttons,command=self.Mdr_Frame,text='Mudar Pro Frame')
		self.Button_Var = ctk.CTkButton(self.fram_buttons,command=self.Criar_Var,text='Criar Variable')


		self.Name_Psq = ctk.CTkEntry(self.fram_pesq_tag,textvariable=self.Name_tag,width=400)
		self.option_menu = ctk.CTkOptionMenu(self.fram_pesq_tag, variable=self.Tag1, values=self.option_menu_options,width=40)
		self.Button_Pesq_tag = ctk.CTkButton(self.fram_pesq_tag,command=self.Pesq_XPATH,text="Pesquisar TAG")
		self.Butoon_Pesq_adentr = ctk.CTkCheckBox(self.fram_pesq_tag, text="Pesquisar Dentro", variable=self.Pesq_adentro, onvalue=True, offvalue=False)

		self.Console_entry_Label = ctk.CTkLabel(self.frame_analise,text='Console',anchor='w')
		self.Console_entry = ctk.CTkEntry(self.frame_analise,state=DISABLED,textvariable=self.Console)
		self.Console_txt_label = ctk.CTkLabel(self.frame_analise,text='Texto',anchor='w')
		self.Console_txt = ctk.CTkTextbox(self.frame_analise)
		self.send_key = ctk.CTkEntry(self.frame_analise,textvariable=self.Key_to_send)

		# SINALIZANDO A OPÇÃO DEFAULT DO OPTIONMENU
		self.option_menu.set("CSS")




		#frame2
		self.option_menu.pack(side=LEFT)
		self.Name_Psq.pack(side=LEFT,fill=X,expand=True)
		self.Button_Pesq_tag.pack(side=LEFT,padx=5)
		self.Butoon_Pesq_adentr.pack(side=LEFT,)

		#rest
		self.Button_clicar.pack(fill='x',pady=5,padx=5,)
		self.Button_Send_key.pack(fill='x',pady=5,padx=5)
		self.Entry_Pegar_at.pack(fill='x',pady=2,padx=5)
		self.Button_Pegar_at.pack(fill='x',pady=2,padx=5)
		self.Button_iframe.pack(fill='x',pady=2,padx=5)
		self.Button_Var.pack(fill='x',pady=2,padx=5)

		self.Console_entry_Label.pack(fill='x')
		self.Console_entry.pack(fill='x')
		self.Console_txt_label.pack(fill='x')
		self.Console_txt.pack(fill='x',expand=1)


		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get('https://www.google.com/')


		self.mainloop()

		self.driver.quit()


	##vai no cmd como adm e escreve" pip install selenium" ai e so executar o progama ctrl + b
	def Mdr_Frame(self):
		self.driver.switch_to.frame(self.element)
		self.Button_iframe_sair = Button(self.fram_buttons,command=self.Sair_frame,text='Sair do Frame')
		self.Button_iframe_sair.pack()

	def Sair_frame(self):
		if self.Button_iframe_sair:
			self.driver.switch_to.default_content()
			self.Button_iframe_sair.destroy()

	def Clicar(self):
		self.element.click()

	def Send_key(self):
		self.element.send_keys(Keys.PAGE_DOWN)

	def Pegar_Atributo(self):
		self.Console_txt.insert(END,self.element.get_attribute(self.Atribute_pgr.get()))
		if self.Console.get() == '':
			self.Console.set("Tente Novamente")

	def Pesq_Url(self):
		self.driver.get(self.Url.get())	

	def Pesq_XPATH(self):
		#TODO PESQUISAR DENTRO 

		match self.Tag1.get():
			case 'CLASS_NAMES':
				try:
					self.element = self.driver.find_elements(By.CLASS_NAME, self.Name_tag.get())
					self.Console.set(self.element)
					try:
						for i in self.element:
							self.Console_txt.insert(END, i.text)
					except:
						pass
				except:
					self.Console.set("Não encontrou")
					
			case 'CLASS_NAME':
				try:
					self.element = self.driver.find_element(By.CLASS_NAME, self.Name_tag.get())
					self.Console.set(self.element)
					try:
						self.Console_txt.insert(END, self.element.text)
					except:
						pass
				except:
					self.Console.set("Não encontrou")
					
			case 'XPATH':
				try:
					self.element = self.driver.find_element(By.XPATH, self.Name_tag.get())
					self.Console.set(self.element)
					try:
						self.Console_txt.insert(END, self.element.text)
					except:
						pass
				except:
					self.Console.set("Não encontrou")
					
			case 'ID':
				try:
					self.element = self.driver.find_element(By.ID, self.Name_tag.get())
					self.Console.set(self.element)
					try:
						self.Console_txt.insert(END, self.element.text)
					except:
						pass
				except:
					self.Console.set("Não encontrou")
					
			case 'NAME':
				try:
					self.element = self.driver.find_element(By.NAME, self.Name_tag.get())
					self.Console.set(self.element)
					try:
						self.Console_txt.insert(END, self.element.text)
					except:
						pass
				except:
					self.Console.set("Não encontrou")
					
			case 'CSS':
				try:
					self.element = self.driver.find_element(By.CSS_SELECTOR, self.Name_tag.get())
					self.Console.set(self.element)
					try:
						self.Console_txt.insert(END, self.element.text)
					except:
						pass
				except:
					self.Console.set("Não encontrou")
					
			case _:
				messagebox.showwarning('Alerta', 'Selecione Tag')

	def Var_dinamica(self):
		self.Dado_var

		while self.Var_bool.get() == True:
			self.update()
			self.Dado_var.set(self.driver.find_element(By.CLASS_NAME,self.Name_tag.get()).text)

	def Criar_Var(self):
		self.Dado_var
		self.Dado_Entry

		if self.Var_bool.get() == False:

			Dado_var = StringVar()
			Dado_var.set(self.element.text)

			Dado_Entry = Entry(self.fram_buttons,textvariable=Dado_var,state=DISABLED)
			Dado_Entry.pack(fill=X)
			self.Var_bool.set(True)
			self.Var_dinamica()
		else:
			Dado_Entry.destroy()
			self.Var_bool.set(False)

if __name__ == "__main__":
	App()
	App.janela.mainloop()