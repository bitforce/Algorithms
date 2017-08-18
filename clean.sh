if test "find . -name '.ropeproject'"; then
    find . -name '.ropeproject' -type d -exec echo "removing '{}'" \;
    rm -rf `find . -type d -name '.ropeproject'`
fi
