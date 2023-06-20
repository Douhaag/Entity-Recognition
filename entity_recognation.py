import spacy
from tkinter import *

fenetre= Tk()
fenetre.geometry('400x400')
fenetre.title('Entity Recognition')
fenetre['bg']='green'
fenetre.resizable(height=False,width=False)
Label1=Label(fenetre, text="Entity Recognition",font=("verdana",18,"italic bold"),fg="white",bg="green")
Label1.place(x='90',y='20')
nlp = spacy.load("en_core_web_sm")





def gettexte():
     doc = nlp(ma_variable.get())
    
def reponse():
    doc = nlp(ma_variable.get())
    for ent in doc.ents:
         Label3['text']=("reponse is:")
         Label2['text']=(ent.text, ent.label_)
   
ma_variable=StringVar()  
   
entree=Entry(fenetre,textvariable=ma_variable,width=100,)
entree.place(y='180')
Bouton=Button(fenetre,text="valider",bg='white',fg='black',command=reponse,width=30)
Bouton.place(x='110',y='230')
Label3=Label(fenetre, text="",font=("verdana",10,"italic bold"),fg="white",bg="green")
Label3.place(y='270')
Label2=Label(fenetre, text="",font=("verdana",10,"italic bold"),fg="black",bg="yellow")
Label2.place(x='20',y='290')




fenetre.mainloop()

