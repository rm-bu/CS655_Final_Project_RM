import socket
import re
from md5_solver import * 
from md5_solver_query_receiver import receive_query

receive_query("10.10.4.2", 9004, "10.10.4.1", 9005)
