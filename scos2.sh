BASEDIR=$(dirname "$0")
echo "$BASEDIR"
gnome-terminal -- python3 "$BASEDIR"/main.py
