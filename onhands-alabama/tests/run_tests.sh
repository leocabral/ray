docker rm -f "onhands-alabama"
cp -r ../onhands-core tests/
cp -r onhandsalabama/ tests/
docker run -i -t -v "$(pwd):/home/onhands-test/"  --name "onhands-alabama" "onhands-alabama" sh -c "cd tests; ./test.sh"
rm -rf tests/onhands-core
