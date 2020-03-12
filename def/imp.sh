# /bin/sh
oper=OP_WtsnAdmin
~/apex/apex.sh Import APPLICATION -df APPLICATION.def -oi $oper -ignorewarning -upsert
~/apex/apex.sh Import FLOW -df FLOW.def -oi $oper -ignorewarning -upsert


