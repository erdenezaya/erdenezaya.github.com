How to install Python & Django on Windows
#########################################

:Date: 2011-09-06 17:30:00
:Tags: python, Django
:Category: Python

Аль дээр энэ бичлэгийг оруулах санаатай байсан чинь өөр зүйлд сатаараад мартаж орхиж. Нэг хүнд миний заавар хэрэг болж надад санууллаа хэхэ. Ингээд өөрийнхөө суулгасан аргачлалаа та бүхэнтэй хуваалцахаар боллоо.

Эхний алхам:

Та дараах сайтаас python installer татаж авах хэрэгтэй.

 http:// Python.org/downloads/python2.7.1 exe

Дараа нь мөн адил Django framework татна.

http:// Djangoproject.com/downloads
 үүнийг татаж аваад Python суусан газартаа хуулаад задална.

Дараагийн алхам:

cmd –ийг дуудаж ажиллуулан Django.zip файлаа задалсан зам руу орно. Дараах командыг бичээрэй. Энэ бол Django суулгах команд юм.

python setup.py install
 
Игээд  django суулаа. Зөв суусан эсэхийг  дараах командаар шалгана. Ямар нэгэн алдаа өгөхгүй бол суусан болно
 
 python
      >> import django
               

Төсөл хөгжүүлэх Editor сонгоно. Editor –ээ python & django project хөгжүүлэхэд бэлтгэнэ. Дараах сайтаас eclipse editor –ийг татаж авах боломжтой.

http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-SDK-3.6.1-win32.zip

Хэрэв Eclipse editor –ийг сонгосон бол дараах нэмэлтүүдийг суулгана.

http://pydev.org/updates
http://download.aptana.org/tools/studio/plugin/update/studio/

Дараах команд нь төсөл болон application үүсгэнэ. 

Төсөл үүсгэх команд:

python django-admin.py startproject  project_name  
Application үүсгэх команд:

Python django-admin.py startapp app_name
