==================================================================
=     			Prerequisite		                 =
==================================================================

- Python 3 needs to be installed in your system
- Your may install IDE like PyCharm/Jupiter for working with python
- All the contained files need to be in the same package of project in order to execute proprely



==================================================================
=     	         Steps for Execution(Editor used PyCharm)	 =
==================================================================

- Open PyCharm
- Create a new project
- Create a new package inside your project
- Copy the provided files inside the newly created package
- Open quiz_execution.py
- Click Run>Run...>quiz_execution

The program will be executed.

==================================================================
=     	         Steps for Execution(Using Command Prompt)	 =
==================================================================

- Open Command Prompt
- Change the directory to the directory where files are present
- run your code by typing file_name.py (Example quiz_execution.py)

Your program will be executed

===================================================================
=     	         Steps to execute Docker File	                  =
===================================================================

Prerequisite : docker is installed
Copy py script,.jsonfile,dockerfile in folder say "C:\assignment"
cd to above dir

Execute following command
docker build -t <image_name> .
docker run -it <image_name>

OR Alterternatively

User can use the image uploaded "https://hub.docker.com/repository/docker/shushantghosh857/assignment"
image name - py_quiz_assignment
