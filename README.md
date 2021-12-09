# CS655_Final_Project_RM
Final Project for CS655

This project requires that each of the nodes contain a particular set of files. The topology of the GENI resources can be found in the rspec file.

The Web Interface node must contain cgi_server.py, and a folder cgi-bin containing interface.py.

The Manager node must contain md5_solver.py and manager.py.

Each worker node must contain md5_solver.py, md5_solver_query_receiver.py, and the corresponding worker file (i.e., Worker 1 has worker1.py, Worker 2 has worker2.py, etc.)

To run the program, manager.py (in the Manager node) and worker1.py, worker2.py, worker3.py, and worker4.py (in the Worker nodes) must all be run. Then, cgi_server can be run from the Web Interface node. This allows the cgi interface for cgi-bin/interface.py to accessed, which contains the form for the user's query. After entering the query, the Manager will distribute the task among the workers, and when all the workers have finished, the interface will be updated with the answer.

A demo mp4 file has been uploaded. (It pauses in middle while the workers are running to avoid taking up too much time.)
