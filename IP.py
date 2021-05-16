from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import pandas as pd
import matplotlib.pyplot as plt
import requests
import bs4
import numpy as np
import re as res


def f1():
	addst.deiconify()
	root.withdraw()
	addst_entrno.delete(0, END)
	addst_entname.delete(0, END)
	addst_entmarks.delete(0, 100)
	addst_entrno.focus()


def f2():
	root.deiconify()
	addst.withdraw()

def f3():
	con = None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = "insert into student values('%d', '%s', '%d')"
		rno = int(addst_entrno.get())
		name = addst_entname.get()
		marks = int(addst_entmarks.get())
		
		
		if (rno == 0):
			showerror( "Failure", 'Roll should start from 1')
		elif rno < 0:
			showerror( "Failure", 'Roll no should contain positive integers only')
		elif len(name) == 0:
			showerror( "Failure", 'Name should not be blank') 
		elif not name.isalpha():
			showerror( "Failure", 'Name should contain Alphabets only')
		elif len(name) <= 2:
			showerror( "Failure", 'Name should contain more than two letters ')
		elif marks < 0 or marks > 100:
			showerror( "Failure", 'Marks should not be less than 0 and not greater than 100 ')
		else:
			cursor.execute(sql % (rno, name, marks))
			con.commit()
			showinfo("Success", 'record inserted')
	except Exception as e:
		
		showerror("Failure", 'Roll no and Marks should not be empty and should contain integers only')
		con.rollback()
	
	finally:
		if con is not None:
			con.close()
			

		addst_entrno.delete(0, END)
		addst_entname.delete(0, END)
		addst_entmarks.delete(0, 100)
		addst_entrno.focus()

def f4():
	root.deiconify()
	viewst.withdraw()

def f5():
	viewst.deiconify()
	root.withdraw()
	viewst_data.delete(1.0,END)
	con = None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		info = ""
		data = cursor.fetchall()
		for d in data:
			info = info + " rno = " + str(d[0]) + " name = " + str(d[1]) +  " marks = " + str(d[2]) + "\n"
		viewst_data.insert(INSERT,info)
	except exception as e:
		showerror('failure', e)
	finally:
		if con is not None:
			con.close()


def f6():
	updatest.deiconify()
	root.withdraw()
	updatest_entrno.delete(0, END)
	updatest_entname.delete(0, END)
	updatest_entmarks.delete(0, 100)
	updatest_entrno.focus()


def f7():
	root.deiconify()
	updatest.withdraw()


def f8():
	con = None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = " update student set name = '%s', marks = '%d' where rno = '%d' "
		name = updatest_entname.get()
		marks = int(updatest_entmarks.get())
		rno = int(updatest_entrno.get())

		if (rno == 0):
			showerror( "Failure", 'Roll should start from 1')
		elif rno < 0:
			showerror( "Failure", 'Roll no should contain positive integers only')
		elif len(name) == 0:
			showerror( "Failure", 'Name should not be blank')
		elif not name.isalpha():
			showerror( "Failure", 'Name should contain Alphabets only')
		elif len(name) <= 2:
			showerror( "Failure", 'Name should contain more than two letters ')
		elif marks < 0 or marks > 100:
			showerror( "Failure", 'Marks should not be less than 0 and not greater than 100 ')
		else:
			cursor.execute(sql % (name, marks, rno))
			if cursor.rowcount>0:
				con.commit()
				showinfo("Success", 'record updated')
			else:
				showerror('Failure', 'Record does not exists')
				
	except Exception as e:
		showerror('failure', 'Roll no and Marks should not be blank and contain integers only')
		con.rollback()
	finally:
		if con is not None:
			con.close()
		updatest_entrno.delete(0, END)
		updatest_entname.delete(0, END)
		updatest_entmarks.delete(0, 100)
		updatest_entrno.focus()

def f9():
	con = None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = "delete from student where rno is ('%d')"
		rno = int(deletest_entrno.get())
		cursor.execute(sql % (rno))
		
		if cursor.rowcount>0:
			con.commit()
			showinfo('Success', 'Record deleted')
		else:
			showerror('Failure', 'Record does not exists')
			
	except Exception as e:
		showerror('failure', 'Roll no should contain integers only')
		con.rollback()
	finally:
		if con is not None:
			con.close()
		deletest_entrno.delete(0, END)
		deletest_entrno.focus()

def f10():
	deletest.deiconify()
	root.withdraw()
	deletest_entrno.delete(0, END)

def f11():
	root.deiconify()
	deletest.withdraw()

def f12():
	
	con = None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		df = pd.DataFrame([[xy for xy in x] for x in data])
		x=df[1]
		y=df[2]
		my_colors = ['red', 'green', 'blue'] 
		
		plt.xlabel("Students")
		plt.ylabel("Marks")
		plt.title("Student's Performance")
		plt.bar(x,y ,color=my_colors)
		plt.show()
		
	except Exception as e:
		print(e)
		showerror('failure', e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f13():
	try:
		wa = "https://ipinfo.io/"
		res = requests.get(wa)
		print(res)

		data = res.json()
		print(data)

		city_name = data['city']
		print("city_name = ", city_name)

		a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2 = "&q=" + city_name
		a3 = "&appid=" + "c6e315d09197cec231495138183954bd"

		wa = a1 + a2 + a3
		res = requests.get(wa)
		print(res)
		
		data = res.json()
		print(data)
				
		
		temp = data['main']['temp']
		print(temp)
		return "Location : " + city_name + "               Temperature : " + str(temp)

	except Exception as e:
		showerror('failure', e)
	

def f14():
	try:

		wa = "https://www.brainyquote.com/quote_of_the_day"
		res = requests.get(wa)
		print(res)

		data = bs4.BeautifulSoup(res.text, "html.parser")
		#print(data)

		info = data.find('img', {'class':'p-qotd'})
		print(info)

		print(" Text part ", info ['alt'])
		info = info['alt']

		return "QOTD : " + info
		f.close()
		
	except Exception as e:
		showerror('failure', e)







	


	

root = Tk()
root.title("S. M. S.")
root.geometry("620x600+400+50")



root_btnadd = Button(root, text="Add", font=('Arial', 20, 'bold'), width = 5, relief="solid", command=f1)
root_btnview = Button(root, text="View", font=('Arial', 20, 'bold'), width = 5, relief="solid", command=f5)
root_btnupdate = Button(root, text="Update", font=('Arial', 20, 'bold'), width = 6, relief="solid", command=f6)
root_btndelete = Button(root, text="Delete", font=('Arial', 20, 'bold'), width = 5, relief="solid", command=f10)
root_btncharts = Button(root, text="Charts", font=('Arial', 20, 'bold'), width = 5, relief="solid", command=f12)

root.configure(background = 'sky blue')

root_lbllocation = Label(root, text="Location: ", borderwidth=2, bg='gray95', anchor='w',width=37, relief="solid", font=('Arial', 20))
#root_lbltemp = Label(root, text="Temp:", bg='#90ee90', font=('Arial', 20))
root_lblqotd = Label(root, text="QOTD:", borderwidth=2, bg='gray95', anchor='w', relief="solid", font=('Arial', 12,), width=65)




													
root_btnadd.pack(pady=10)
root_btnview.pack(pady=10)
root_btnupdate.pack(pady=10)
root_btndelete.pack(pady=10)
root_btncharts.pack(pady=10)

root_lblqotd.config(text=f14())
root_lbllocation.config(text=f13())

root_lbllocation.place(height=50, x=10, y=400)
#root_lbltemp.place(height=40, x=280, y=380)
root_lblqotd.place(height=50, x=10, y=470)



##********************************************************* Add *************************************************************************
addst = Toplevel(root)
addst.title("Add student")
addst.geometry("620x620+400+50")

addst_lblrno = Label(addst, text="enter rno", font=('Arial', 20, 'bold')) 
addst_entrno = Entry(addst, bd=5, font=('Arial', 20, 'bold')) 

addst_lblname = Label(addst, text="enter name", font=('Arial', 20, 'bold'))
addst_entname = Entry(addst, bd=5, font=('Arial', 20, 'bold'))
addst_lblmarks = Label(addst, text="enter marks", font=('Arial', 20, 'bold'))
addst_entmarks = Entry(addst, bd=5, font=('Arial', 20, 'bold'))

addst_btnsave = Button(addst, text="Save", relief="solid",font=('Arial', 20, 'bold'), command=f3)
addst_btnback = Button(addst, text="Back", relief="solid",font=('Arial', 20, 'bold'), command=f2)

addst_lblrno.pack(pady=10)
addst_entrno.pack(pady=10)
addst_lblname.pack(pady=10)
addst_entname.pack(pady=10)
addst_lblmarks.pack(pady=10)
addst_entmarks.pack(pady=10)

addst_btnsave.pack(pady=10)
addst_btnback.pack(pady=10)

addst.configure(background = 'firebrick4')

addst.withdraw()

##**************************************************View**************************************************************************

viewst = Toplevel(root)
viewst.title("View Student")
viewst.geometry("620x620+400+50")
viewst_data = ScrolledText(viewst, width=33, height=13, font=('Arial', 14, 'bold'))
viewst_btnback = Button(viewst, text="Back", relief="solid", font=('Arial', 20, 'bold'), command=f4)

viewst_data.pack(pady=10)
viewst_btnback.pack(pady=10)

viewst.configure(background = 'gray26')
viewst.withdraw()


##*******************************************************Update*******************************************************************

updatest = Toplevel(root)
updatest.title("Update student")
updatest.geometry("620x620+400+50")

updatest_lblrno = Label(updatest, text="enter rno", font=('Arial', 20, 'bold'))
updatest_entrno = Entry(updatest, bd=5, font=('Arial', 20, 'bold'))
updatest_lblname = Label(updatest, text="enter name", font=('Arial', 20, 'bold'))
updatest_entname = Entry(updatest, bd=5, font=('Arial', 20, 'bold'))
updatest_lblmarks = Label(updatest, text="enter marks", font=('Arial', 20, 'bold'))
updatest_entmarks = Entry(updatest, bd=5, font=('Arial', 20, 'bold'))

updatest_btnsave = Button(updatest, text="Save", relief="solid", font=('Arial', 20, 'bold'), command=f8)
updatest_btnback = Button(updatest, text="Back", relief="solid", font=('Arial', 20, 'bold'), command=f7)

updatest_lblrno.pack(pady=10)
updatest_entrno.pack(pady=10)
updatest_lblname.pack(pady=10)
updatest_entname.pack(pady=10)
updatest_lblmarks.pack(pady=10)
updatest_entmarks.pack(pady=10)

updatest_btnsave.pack(pady=10)
updatest_btnback.pack(pady=10)

updatest.configure(background = 'bisque4')

updatest.withdraw()

##**********************************************Delete********************************************************

deletest = Toplevel(root)
deletest.title("Delete student")
deletest.geometry("620x620+400+50")

deletest_lblrno = Label(deletest, text="enter rno", font=('Arial', 20, 'bold'))
deletest_entrno = Entry(deletest, bd=5, font=('Arial', 20, 'bold'))

deletest_btndelete = Button(deletest, text="Delete", relief="solid", font=('Arial', 20, 'bold'), command=f9)
deletest_btnback = Button(deletest, text="Back", relief="solid", font=('Arial', 20, 'bold'), command=f11)

deletest_lblrno.pack(pady=10)
deletest_entrno.pack(pady=10)

deletest_btndelete.pack(pady=10)
deletest_btnback.pack(pady=10)

deletest.configure(background = 'dark slate gray')

deletest.withdraw()



root.mainloop()
