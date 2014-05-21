SimpleRegister
==============
A simple [Trac](http://trac.edgewall.org/) plugin that creates Register link containing an email to the administrator. This is an alternative to [AccountManagerPlugin](http://trac-hacks.org/wiki/AccountManagerPlugin) that allows to manually validate the registration and avoid SPAM. I am aware that the latest version of above plugin includes account validation feature, but it is still not stable enough for production use.

Build
=====
To build the plugin run
	
	./setup.py bdist_egg

It should generate an egg file in dist/ directory which needs to be copied to Trac plugins/ directory.

Configure
=========
Add a new section in your conf/trac.ini specifying an email of a person responsible for account registration:

	[simpleregister]
	email = admin@yourdomain.com

To control the order in which the links appear, you can use metanav setting in trac section as follows:

	[trac]
	...
	metanav = login, logout, register, prefs, help, about

