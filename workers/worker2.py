import socket
import re
from md5_solver import * 
from md5_solver_query_receiver import receive_query

receive_query("10.10.3.2", 9002, "10.10.3.1", 9003)
