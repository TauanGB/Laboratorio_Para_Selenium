from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import json
import time
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
import os

class App(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.create_widgets()

		#

	def create_widgets(self):
		self.fram_pesq_tag = ctk.CTkFrame(self)
		self.fram_buttons = ctk.CTkFrame(self)
		self.frame_analise = ctk.CTkFrame(self)
		self.fram_sends = ctk.CTkFrame(self.fram_buttons)

		self.fram_pesq_tag.pack(side=TOP,fill=X,padx=5,ipadx=5,ipady=5,pady=(5,10))
		self.frame_analise.pack(side=LEFT,fill=BOTH,expand=1,padx=5,pady=(0,10))
		self.fram_buttons.pack(side=RIGHT,fill=Y,padx=5,pady=(0,10))

		#VAR PY
		self.option_menu_Bts = ['ENTER','PG DOWN','LIMPAR',"TAB"]
		self.option_menu_options = ["CLASS_NAME","XPATH","ID","NAME","CSS_SELECTOR","CLASS_NAMES"]
		Var_bool = BooleanVar()

		#VAR TKINTER

		self.element = ''
		self.Tag1 = StringVar()
		self.Bt1 = StringVar()

		self.label_Send_bt = ctk.CTkLabel(self.fram_buttons,text='INTERAÇÕES',anchor='w')
		self.Button_Send_bt = ctk.CTkButton(self.fram_sends,text=" Clicar ",command=self.Send_Key)
		self.option_bts = ctk.CTkOptionMenu(self.fram_sends, variable=self.Bt1, values=self.option_menu_Bts,width=40)
		self.label_Send_texto = ctk.CTkLabel(self.fram_sends,text='Enviar Texto',anchor='w')
		self.Entry_Send_texto = ctk.CTkEntry(self.fram_sends,placeholder_text='Texto para enviar',)
		self.Button_Send_texto = ctk.CTkButton(self.fram_sends,text=" > ",command=self.Send_Text)

		self.Button_clicar = ctk.CTkButton(self.fram_buttons,text="Clicar em Elemento",command=self.Clicar)
		self.Button_Pegar_at = ctk.CTkButton(self.fram_buttons,text='Pegar Atributo',command=self.Pegar_Atributo)
		self.Entry_Pegar_at = ctk.CTkEntry(self.fram_buttons,placeholder_text='Value para puxar',)


		self.Name_Psq = ctk.CTkEntry(self.fram_pesq_tag,placeholder_text="Metodo de pesquisa",width=400)
		self.option_menu = ctk.CTkOptionMenu(self.fram_pesq_tag, variable=self.Tag1, values=self.option_menu_options,width=40)
		self.Button_Pesq_tag = ctk.CTkButton(self.fram_pesq_tag,command=self.Pesq_XPATH,text="Pesquisar TAG")
		self.Button_iframe = ctk.CTkButton(self.fram_pesq_tag,command=self.Mdr_Frame,text='Acessar o Frame')
		self.Butoon_Pesq_adentr = ctk.CTkCheckBox(self.fram_pesq_tag, text="Pesquisar Apartir do atual elemento",  onvalue=True, offvalue=False)


		self.Console_entry_Label = ctk.CTkLabel(self.frame_analise,text='Console',anchor='w')
		self.Console_entry = ctk.CTkEntry(self.frame_analise, state=DISABLED)
		self.Console_txt_label = ctk.CTkLabel(self.frame_analise,text='Texto',anchor='w')
		self.Console_txt = ctk.CTkTextbox(self.frame_analise)
		self.Historico_txt_label = ctk.CTkLabel(self.frame_analise,text='Historico',anchor='w')
		self.Historico_txt = ctk.CTkTextbox(self.frame_analise)
		self.send_key = ctk.CTkEntry(self.frame_analise)

		# SINALIZANDO A OPÇÃO DEFAULT DO OPTIONMENU
		self.option_menu.set("CSS_SELECTOR")
		self.option_bts.set("ENTER")

		#TODO BOTÃO CRIANDO ANTERIROMENTE 
		'''self.Button_Var = ctk.CTkButton(self.fram_buttons,command=self.Criar_Var,text='Criar Variable')
		self.Button_Var.pack(fill='x',pady=2,padx=5)'''



		#frame2
		self.option_menu.pack(side=LEFT)
		self.Name_Psq.pack(side=LEFT,fill=X,expand=True)
		self.Button_Pesq_tag.pack(side=LEFT,padx=5)
		self.Button_iframe.pack(side=LEFT,padx=5)
		self.Butoon_Pesq_adentr.pack(side=LEFT)

		self.label_Send_bt.pack(side=TOP,fill=X,padx=5,pady=(5,0))

		self.option_bts.grid(column=0,row=0,padx=5,pady=5)
		self.Button_Send_bt.grid(column=1,row=0,pady=5,padx=5)
		self.label_Send_texto.grid(column=0,columnspan=2,sticky="nesw",row=1,pady=5,padx=5)
		self.Entry_Send_texto.grid(column=0,columnspan=2,sticky="nesw",row=2,pady=5,padx=5)
		self.Button_Send_texto.grid(column=0,columnspan=2,sticky="nesw",row=3,pady=5,padx=5)
		self.fram_sends.pack(side=TOP,fill=Y,padx=5,pady=(0,10))
		

		#rest
		self.Button_clicar.pack(fill='x',pady=15,padx=5,)
		self.Button_Pegar_at.pack(fill='x',pady=2,padx=5)
		self.Entry_Pegar_at.pack(fill='x',pady=2,padx=5)

		self.Console_entry_Label.pack(fill='x')
		self.Console_entry.pack(fill='x')
		self.Console_txt_label.pack(fill='x')
		self.Console_txt.pack(fill=BOTH,expand=1)
		self.Historico_txt_label.pack(fill='x')
		self.Historico_txt.pack(fill=BOTH,expand=1)


		self.driver = webdriver.Chrome()
		self.driver.maximize_window()

		self.carregar_dados()

		self.mainloop()

		self.Salvar_dados()
		
		self.driver.quit()


	def Salvar_dados(self):
		with open("Banco.json", 'w') as arquivo:
			DadosTmp = {"Site":self.driver.current_url}
			json.dump(DadosTmp, arquivo, indent=4)

	def carregar_dados(self):
		if not os.path.exists("Banco.json"):
			dados_iniciais = {"Site": "https://www.google.com/"} 
			self.driver.get("https://www.google.com/")
			with open("Banco.json", 'w') as arquivo: 
				json.dump(dados_iniciais, arquivo, indent=4) 
		else:
			with open("Banco.json", 'r') as arquivo:
				DadosTmp = json.load(arquivo)
				self.driver.get(DadosTmp["Site"])

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
		self.Historico_txt.insert(END,f"self.driver.find_element(By.{self.Tag1.get()},{self.Name_Psq.get()}).click()\n")

	def Send_Text(self):
		self.element.send_keys(self.Entry_Send_texto.get())
		self.Historico_txt.insert(END,f"self.driver.find_element(By.{self.Tag1.get()},{self.Name_Psq.get()}).send_keys('{self.Entry_Send_texto.get()}')\n")
		
		pass

	def Send_Key(self):
		match self.label_Send_bt:
			case "ENTER" :
				self.element.send_keys(Keys.ENTER)

			case "PG DOWN" :
				self.element.send_keys(Keys.PAGE_DOWN)

			case "LIMPAR" :
				self.element.send_keys(Keys.BACK_SPACE)

			case "TAB" :
				self.element.send_keys(Keys.TAB)

	def Pegar_Atributo(self):
		if self.Entry_Pegar_at.get() != '':
			self.Console_txt.insert(END,self.element.get_attribute(self.Entry_Pegar_at.get()))

	def Pesq_Url(self):
		self.driver.get(self.Url.get())

	def Pesq_XPATH(self):
		#TODO PESQUISAR DENTRO
		self.Console_entry.configure(state='normal')
		self.Console_txt.delete(0.0,END)
		self.Console_entry.delete(0,END)

		match self.Tag1.get():
			case 'CLASS_NAMES':
				try:
					self.element = self.driver.find_elements(By.CLASS_NAME, self.Name_Psq.get())
					self.Console_entry.insert(END,self.element)
					try:
						for i in self.element:
							self.Console_txt.insert(END, i.text)
					except:
						pass
				except:
					self.Console_entry.insert(END,"Não encontrou")
					
			case 'CLASS_NAME':
				try:
					self.element = self.driver.find_element(By.CLASS_NAME, self.Name_Psq.get())
					self.Console_entry.insert(END,self.element)
					try:
						self.Console_txt.insert(END, self.element.text)
					except:
						pass
				except:
					self.Console_entry.insert(END,"Não encontrou")
					
			case 'XPATH':
				try:
					self.element = self.driver.find_element(By.XPATH, self.Name_Psq.get())
					self.Console_entry.insert(END,self.element)
					try:
						self.Console_txt.insert(END, self.element.text)
					except:
						pass
				except:
					self.Console_entry.insert(END,"Não encontrou")
					
			case 'ID':
				try:
					self.element = self.driver.find_element(By.ID, self.Name_Psq.get())
					self.Console_entry.insert(END,self.element)
					try:
						self.Console_txt.insert(END, self.element.text)
					except:
						pass
				except:
					self.Console_entry.insert(END,"Não encontrou")
					
			case 'NAME':
				try:
					self.element = self.driver.find_element(By.NAME, self.Name_Psq.get())
					self.Console_entry.insert(END,self.element)
					try:
						self.Console_txt.insert(END, self.element.text)
					except:
						pass
				except:
					self.Console_entry.insert(END,"Não encontrou")
					
			case 'CSS_SELECTOR':
				try:
					self.element = self.driver.find_element(By.CSS_SELECTOR, self.Name_Psq.get())
					self.Console_entry.insert(END,self.element)
					try:
						self.Console_txt.insert(END, self.element.text)
					except:
						pass
				except:
					self.Console_entry.insert(END,"Não encontrou")
					
			case _:
				messagebox.showwarning('Alerta', 'Selecione Tag')
		
		self.Console_entry.configure(state='disabled')


if __name__ == "__main__":
	App()
	App.janela.mainloop()