#! /bin/sh
oper=OP_GCPAdmin
rm -f *.def
~/apex/apex.sh Export APPLICATION -outf APPLICATION.def -oi $oper
~/apex/apex.sh Export FLOW -outf FLOW.def -oi $oper


