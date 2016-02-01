## Easy Git pushing from shell
* This uses the aliases I have already created with Git
* So to add, commit and push with a given message, just do `gg.sh message`
* Add to your bashrc or create a symlink to use it from wherever :D

* Currently working on a auto-push hook :)
* The auto-pusher is called AutoPusher.py, and can be run as ./AutoPusher (with appropriate make file)
* It contains an auto-msg for readme updates, lets see if it works.
* Looks like it works, so everything, up to 2 directories deep, will be pushed automatically, 
if it is either a README change (with auto message) or if it has been committed but not pushed.