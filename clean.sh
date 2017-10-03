remove() {
    if test "find . -name $1"; then
        find . -name $1 -type $2 -exec echo removing {} \;
        rm -rf `find . -type $2 -name $1`
    fi
}
remove .ropeproject d
remove __pycache__ d
remove .cache d
remove .DS_Store f
remove *.class f
remove *.pyc f
