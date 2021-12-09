import socket
import re
from md5_solver import * 
from md5_solver_query_receiver import receive_query

receive_query("10.10.8.2", 9012, "10.10.8.1", 9013)
