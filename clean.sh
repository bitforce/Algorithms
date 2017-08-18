if test "find . -name '.ropeproject'"; then
    find . -name '.ropeproject' -type d -exec echo "removing '{}'" \;
    rm -rf `find . -type d -name '.ropeproject'`
fi
if test "find . -name '__pycache__'"; then
    find . -name '__pycache__' -type d -exec echo "removing '{}'" \;
    rm -rf `find . -type d -name '__pycache__'`
fi
if test "find . -name '.cache'"; then
    find . -name '.cache' -type d -exec echo "removing '{}'" \;
    rm -rf `find . -type d -name '.cache'`
fi
