import socket
import re
from md5_solver import * 
from md5_solver_query_receiver import receive_query

receive_query("10.10.7.2", 9010, "10.10.7.1", 9011)
