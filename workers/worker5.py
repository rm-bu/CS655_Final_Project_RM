import socket
import re
from md5_solver import * 
from md5_solver_query_receiver import receive_query

receive_query("10.10.6.2", 9008, "10.10.6.1", 9009)
