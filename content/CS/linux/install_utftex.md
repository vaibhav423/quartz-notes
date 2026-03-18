Steps:

    First clone the repo

git clone https://github.com/bartp5/libtexprintf
cd libtexprintf

    Generate the configure file

./autogen.sh

    Generate the Makefile

./configure --prefix=/path/to/install
./configure --prefix=/data/data/com.termux/files/usr

    Make and install

make
make install
