pizzadjango
===========

Projeto de uma app sendo criada ao vivo

pizzadjango - appfog
====================

$ af push pizza --url pizza.rs.af.cm
Would you like to deploy from the current directory? [Yn]: y
Detected a Standalone Application, is this correct? [Yn]: n
1: Rails
2: Spring
3: Grails
4: Lift
5: JavaWeb
6: Standalone
7: Sinatra
8: Node
9: PHP
10: Erlang/OTP Rebar
11: WSGI
12: Django
13: Rack
14: Play
Select Application Type: 12
Selected Python Django Application
1: AWS US East - Virginia
2: AWS EU West - Ireland
3: AWS Asia SE - Singapore
4: Rackspace AZ 1 - Dallas
5: HP AZ 2 - Las Vegas
Select Infrastructure: 4
Application Deployed URL [pizza.rs.af.cm]:
Memory reservation (128M, 256M, 512M, 1G, 2G) [128M]:
How many instances? [1]:
Create services to bind to 'pizza'? [yN]: y
1: mongodb
2: mysql
3: postgresql
4: rabbitmq
5: redis
What kind of service?: 2
Specify the name of the service [mysql-de451]: pizzabd
Create another? [yN]: n
Would you like to save this configuration? [yN]: n
Creating Application: OK
Creating Service [pizzabd]: OK
Binding Service [pizzabd]: OK
Uploading Application:
  	Checking for available resources: OK
  	Processing resources: OK
  	Packing application: OK
  	Uploading (6K): OK
Push Status: OK
Staging Application 'pizza': OK
Starting Application 'pizza': OK
