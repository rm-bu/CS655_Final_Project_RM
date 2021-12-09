import socket
import re
from md5_solver import * 
from md5_solver_query_receiver import receive_query

receive_query("10.10.5.2", 9006, "10.10.5.1", 9007)
