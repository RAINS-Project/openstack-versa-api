#!/usr/bin/env python
#----------------------------------------------------------------------
# This is a WSGI server file writen by Zan Wang from MAX instructed by Dr. Xi Yang
# Version 1.0 Date 02/19/2015 Just the framework of the WSGI server add handler
# Function in later
#----------------------------------------------------------------------

from flask import Flask, request, Response
import httplib

import sys

class LocalServer:
    def __init__(self,methods):


        self.app = Flask(__name__)

        @self.app.route('/info/aggregate/<path:url>', methods=['POST'])
        def info_aggregate_args(url,delta):
            pass

        @self.app.route('/info/externalcheck/<path:extck_id>', methods=['PUT'])
        def info_externalcheck_args(extck_id):
            pass

        @self.app.route('/info/experiment/<path:exp_id>', methods=['GET'])
        def info_experiment_args(exp_id):
            pass

        @self.app.route('/info/node/<path:node_id>', methods=['GET'])
        def info_node_args(node_id):
            pass

        @self.app.route('/info/interface/<path:iface_id>', methods=['GET'])
        def info_interface_args(iface_id):
            pass



if __name__ == '__main__':
    # We only come here when running directly under Flask, i.e.,
    # when run as "python ./web_server.py"
    Server=LocalServer('..')
    Server.app.run(debug=True, host="0.0.0.0", port=4334)
~                                                          
