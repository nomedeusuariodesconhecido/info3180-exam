University of the West Indies
Faculty of Science & Technology
Department of Computing
INFO3180 - Dynamic Web Development II
-----------------------------------------
TITLE: e-mailSeach App
AUTHOR: 620064203
DATE: August 27, 2015
-----------------------------------------

*DESCRIPTION*

This Python Flask WebApp is a simple e-mail address search engine. It accepts the name of an individual as the query criterion at the search bar and returns the corresponding e-mail address as it is stored in the "Contacts" postgresql 
database. The results are displayed on the same webpage below the search bar.

*STRUCTURE OF APP*

	VIEWS:
		- home(): 
		  displays the root page of the app by rendering the 'ContactsForm.html' template which deplays the search bar. 
		
		-displayEmails():
		 queries the "Emails" object of the "Contacts" database and returns the e-mail address which is passed to the 'ContactsForm.html' template. Renders the 'ContactsForm.html' template with updated HTML showing the e-mail address and individual's name below the search bar.
		 
-----------------------------------------

*HOW TO USE*

For simplicity, the app interacts with a postgresql database that is pre-populated with the following data.
		 
id  |       name      	 |           email            
----+--------------------+----------------------------
 23 | Allan Angus     	 | allan.angus@flask.com
 24 | Barbara Baggins 	 | barbara.baggins@flask.com
 25 | Daniel Dunn     	 | daniel.dunn@flask.com
 26 | Carl Cuff      	   | carl.cuff@flask.com
 27 | Justine Jetta   	 | justine.jetta@flask.com
 28 | Elian Elton      	 | elian.elton@flask.com
 29 | Francine Ffrench 	 | francine.ffrench@flask.com
 30 | Georgette Glaxon 	 | georgette.glaxon@flask.com
 31 | Harry Houdini   	 | harry.houdini@flask.com
 32 | Ilias Ingram    	 | ilias.ingram@flask.com

The search bar accepts any of the 10 names under the name column (full name, case sensitive) and returns the e-mail associated with it.

E.g.

Type: "Justine Jetta" (without quotes) into the search bar and the application will return >>

justine.jetta@flask.com
	        Justine Jetta
