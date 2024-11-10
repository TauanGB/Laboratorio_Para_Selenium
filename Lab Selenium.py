from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from tkinter import messagebox
from tkinter import *

##vai no cmd como adm e escreve" pip install selenium" ai e so executar o progama ctrl + b
def Mdr_Frame():
	global Button_iframe_sair
	global element
	driver.switch_to.frame(element)
	Button_iframe_sair = Button(fram_buttons,command=Sair_frame,text='Sair do Frame')
	Button_iframe_sair.pack()

def Sair_frame():
	global Button_iframe_sair
	driver.switch_to.default_content()
	Button_iframe_sair.destroy()

def Clicar():
	global element
	element.click()

def Send_key():
	global element
	element.send_keys(Keys.PAGE_DOWN)

def Pegar_Atributo():
	global element
	Console_txt.insert(END,element.get_attribute(Atribute_pgr.get()))
	if Console.get() == '':
		Console.set("Tente Novamente")

def Pesq_Url():
	driver.get(Url.get())
	

def Pesq_XPATH():
	global element
	if Pesq_adentro.get() == True:
		if Tag1.get() == 'CLASS_NAMES' :
			try:
				element = element.find_elements(By.CLASS_NAME, Name_tag.get())
				Console.set(element)
				try:
					Console_txt.insert(END,element.text)
				except :
					pass
			except:
				Console.set("Não encontrou")

		if Tag1.get() == 'CLASS_NAME' :
			try:
				element = element.find_element(By.CLASS_NAME, Name_tag.get())
				Console.set(element)
				try:
					Console_txt.insert(END,element.text)
				except :
					pass
			except:
				Console.set("Não encontrou")

		elif Tag1.get() == 'XPATH':
			try:
				element = element.find_element(By.XPATH, Name_tag.get())
				Console.set(element)
				try:
					Console_txt.insert(END,element.text)
				except :
					pass
			except:
				Console.set("Não encontrou")
		
		elif Tag1.get() == 'ID':
			try:
				element = element.find_element(By.ID, Name_tag.get())
				Console.set(element)
				try:
					Console_txt.insert(END,element.text)
				except :
					pass
			except:
				Console.set("Não encontrou")
		
		elif Tag1.get() == 'NAME':
			try:
				element = element.find_element(By.NAME, Name_tag.get())
				Console.set(element)
				try:
					Console_txt.insert(END,element.text)
				except :
					pass
			except:
				Console.set("Não encontrou")

		elif Tag1.get() == 'CSS':
			try:
				element = driver.find_element(By.CSS_SELECTOR, Name_tag.get())
				Console.set(element)
				try:
					Console_txt.insert(END,element.text)
				except :
					pass
			except:
				Console.set("Não encontrou")

		else:
			messagebox.showwarning('Alerta','Selecione Tag')
	else:
		if Tag1.get() == 'CLASS_NAMES' :
			try:
				element = driver.find_elements(By.CLASS_NAME, Name_tag.get())
				Console.set(element)
				try:
					for i in element:
						Console_txt.insert(END,i.text)
				except :
					pass
			except:
				Console.set("Não encontrou")

		elif Tag1.get() == 'CLASS_NAME' :
			try:
				element = driver.find_element(By.CLASS_NAME, Name_tag.get())
				Console.set(element)
				try:
					Console_txt.insert(END,element.text)
				except :
					pass
			except:
				Console.set("Não encontrou")

		elif Tag1.get() == 'XPATH':
			try:
				element = driver.find_element(By.XPATH, Name_tag.get())
				Console.set(element)
				try:
					Console_txt.insert(END,element.text)
				except :
					pass
			except:
				Console.set("Não encontrou")
		
		elif Tag1.get() == 'ID':
			try:
				element = driver.find_element(By.ID, Name_tag.get())
				Console.set(element)
				try:
					Console_txt.insert(END,element.text)
				except :
					pass
			except:
				element = Console.set("Não encontrou")
		
		elif Tag1.get() == 'NAME':
			try:
				element = driver.find_element(By.NAME, Name_tag.get())
				Console.set(element)
				try:
					Console_txt.insert(END,element.text)
				except :
					pass
			except:
				element = Console.set("Não encontrou")

		elif Tag1.get() == 'CSS':
			try:
				element = driver.find_element(By.CSS_SELECTOR, Name_tag.get())
				Console.set(element)
				try:
					Console_txt.insert(END,element.text)
				except :
					pass
			except:
				element = Console.set("Não encontrou")
		else:
			messagebox.showwarning('Alerta','Selecione Tag')

def Var_dinamica():
	global element
	global Dado_var

	while Var_bool.get() == True:
		Janela.update()
		Dado_var.set(driver.find_element(By.CLASS_NAME,Name_tag.get()).text)

def Criar_Var():
	global element
	global Dado_var
	global Dado_Entry

	if Var_bool.get() == False:

		Dado_var = StringVar()
		Dado_var.set(element.text)

		Dado_Entry = Entry(fram_buttons,textvariable=Dado_var,state=DISABLED)
		Dado_Entry.pack(fill=X)
		Var_bool.set(True)
		Var_dinamica()
	else:
		Dado_Entry.destroy()
		Var_bool.set(False)


Janela = Tk()
Janela.config(bg='black')
fram_pesq_tag = Frame(Janela,bg='black')
fram_buttons = Frame(Janela,bg='black')
Frame_analise = Frame(Janela,bg='black')

fram_pesq_tag.pack(side=TOP,fill=X,padx=5,pady=(0,10))
Frame_analise.pack(side=LEFT,padx=5,pady=(0,10))
fram_buttons.pack(side=RIGHT,fill=Y,padx=5,pady=(0,10))

#VAR PY
option_menu = ["CLASS_NAME","XPATH","ID","NAME","CSS","CLASS_NAMES"]
Var_bool = BooleanVar()

#VAR TKINTER

Tag1 = StringVar()
Name_tag = StringVar()
Atribute_pgr = StringVar()
Console = StringVar()
Key_to_send = StringVar()
Pesq_adentro = BooleanVar()

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/')

Button_clicar = Button(fram_buttons,text="Clicar",command=Clicar,width=15,bg='#2D2D2D',fg='white',bd=2)
Button_Send_key = Button(fram_buttons,text="Send key",command=Send_key,width=15,bg='#2D2D2D',fg='white',bd=2)
Button_Pegar_at = Button(fram_buttons,text='Pegar_Atributo',command=Pegar_Atributo,width=15,bg='#2D2D2D',fg='white',bd=2)
Entry_Pegar_at = Entry(fram_buttons,width=15,textvariable=Atribute_pgr,bg='#2D2D2D',fg='white',bd=2)
Button_iframe = Button(fram_buttons,command=Mdr_Frame,text='Mudar Pro Frame',bg='#2D2D2D',fg='white',bd=2,width=15)
Button_Var = Button(fram_buttons,command=Criar_Var,text='Criar Variable',bg='#2D2D2D',fg='white',bd=2,width=15)


Name_Psq = Entry(fram_pesq_tag,textvariable= Name_tag)
option_menu = OptionMenu(fram_pesq_tag,Tag1,*option_menu)
Button_Pesq_tag = Button(fram_pesq_tag,command=Pesq_XPATH,text="Pesquisar TAG",bg='#2D2D2D',fg='white',bd=2)
Butoon_Pesq_adentr = Checkbutton(fram_pesq_tag, text = "Pesquisar Dentro",variable = Pesq_adentro,onvalue = True, offvalue = False,bg='black',fg='white',bd=2,selectcolor='gray')

Console_entry_Label = Label(Frame_analise,text='Console',bg='black',fg='white')
Console_entry = Entry(Frame_analise,width=45,state=DISABLED,textvariable= Console)
Console_txt_label = Label(Frame_analise,text='Texto',bg='black',fg='white')
Console_txt = Text(Frame_analise,width=40,height=10)
send_key = Entry(Frame_analise,width=45,textvariable=Key_to_send)




#frame2
option_menu.pack(side=LEFT)
Name_Psq.pack(side=LEFT,fill=X,expand=True)
Button_Pesq_tag.pack(side=LEFT,padx=5)
Butoon_Pesq_adentr.pack(side=LEFT)

#rest
Button_clicar.pack(pady=10)
Button_Send_key.pack(pady=10)
Entry_Pegar_at.pack()
Button_Pegar_at.pack(pady=(0,10))
Button_iframe.pack()
Button_Var.pack()

Console_entry_Label.pack(anchor=W)
Console_entry.pack(anchor=W)
Console_txt_label.pack(anchor=W)
Console_txt.pack(anchor=W)



mainloop()

driver.quit()