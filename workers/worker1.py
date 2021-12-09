import socket
import re
from md5_solver import * 
from md5_solver_query_receiver import receive_query

receive_query("10.10.2.2", 9000, "10.10.2.1", 9001)
