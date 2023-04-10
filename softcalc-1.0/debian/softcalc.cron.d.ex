#
# Regular cron jobs for the softcalc package
#
0 4	* * *	root	[ -x /usr/bin/softcalc_maintenance ] && /usr/bin/softcalc_maintenance
