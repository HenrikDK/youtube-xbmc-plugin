# Add the following two lines(with version numbers) to a file called 'release', and run.
#BETAVERSION=
#RELEASEVERSION=

URL=http://hg.tobiasussing.dk/hgweb.cgi/youtubexbmc/
DIRNAME=plugin.video.youtube
RELEASEPATH=/usr/local/www/data/hg/nightly-repo/
TMPDIR="/tmp/release-tmp-$$"

# Check if trigger is set
if [ -f release ]; then
    echo "Found release";
    BETAVERSION=`cat release | grep "BETA" | sed -e 's/BETAVERSION=//'`
    RELEASEVERSION=`cat release | grep "RELEASE" | sed -e 's/RELEASEVERSION=//'`
    #rm release;
else
    echo "Not set to release";
    exit;
fi

mkdir $TMPDIR
cd $TMPDIR

mkdir trunk
hg clone $URL trunk/$DIRNAME
hg clone $URL $DIRNAME -b release

echo "WORKING DIR $TMPDIR DOING $DIRNAME"
cd $TMPDIR/$DIRNAME;
hg update release;
cp -R $TMPDIR/trunk/$DIRNAME/plugin/* $TMPDIR/$DIRNAME/;
rm -fv *pyc */*pyc */*/*pyc  *~ */*~ */*/*~

# THIS NEEDS ATTENTION!!!
#hg add * */* */*/*;
#hg add *
for j in `ls $TMPDIR/$DIRNAME/ | egrep "addon.xml"`; do
   echo "Cleaning addon.xml $j";
   cat $TMPDIR/trunk/$DIRNAME/plugin/$j | sed -e 's/.beta//' | sed -e 's/ Beta//' | sed -e 's/.999/.0/'> $TMPDIR/$DIRNAME/$j;
done;
VERSION=`cat $TMPDIR/$DIRNAME/addon.xml |grep "addon id" |awk -F\'  ' { print $4 } '`;
CVERSION=`cat $TMPDIR/$DIRNAME/default.py $TMPDIR/$DIRNAME/lib/*.py |grep "version =" |awk -F\"  ' { print $2 } '`;
if [ "$VERSION" != "$CVERSION" ]; then
  echo "ERROR version mismatch on $DIRNAME";
  echo "$DIRNAME version $VERSION - $CVERSION";
  exit
fi;
if [ "$VERSION" = "$CVERSION" ]; then
   echo "Removing beta tags";
   for j in `ls $TMPDIR/$DIRNAME/ | egrep ".py"`; do
          echo "Cleaning .py $j";
             cat $TMPDIR/trunk/$DIRNAME/plugin/$j | sed -e 's/.beta//' | sed -e 's/ Beta//' > $TMPDIR/$DIRNAME/$j;
   done;
   for j in `ls $TMPDIR/$DIRNAME/lib/ | grep ".py"`; do
          echo "Cleaning lib .py $j";
             cat $TMPDIR/trunk/$DIRNAME/plugin/lib/$j | sed -e 's/.beta//' | sed -e 's/ Beta//' > $TMPDIR/$DIRNAME/lib/$j;
   done;
fi;

echo "Push updates to relese branch"
cd $TMPDIR/$DIRNAME/
hg add && hg commit -m "Release script commit" && hg push || echo "Nothing to commit"

if [ -d $RELEASEPATH ]; then
    # Make zip file
    cd $TMPDIR;
    zip -r $DIRNAME-$VERSION.zip $DIRNAME/ -x *.pyc */*.hg/*
    mv $DIRNAME-$VERSION.zip $RELEASEPATH/$DIRNAME/
    cp $DIRNAME/changelog.txt $RELEASEPATH/$DIRNAME/changelog-$VERSION.txt
    if [ -f $DIRNAME/icon.png ]; then
        cp $DIRNAME/icon.png $RELEASEPATH/$DIRNAME/;
    fi
fi

rm -fr $TMPDIR

######
if [ -d $RELEASEPATH ]; then
    pwd
    cd $RELEASEPATH 
    pwd
    cp $DIRNAME/addon.xml addons/$DIRNAME-release.xml

    echo "<?xml version='1.0' encoding='UTF-8'?><addons>" > addons-temp.xml
    cat addons/* >> addons-temp.xml
    echo "</addons>" >> addons-temp.xml
    sed -e "s/<?xml version='1.0' encoding='UTF-8' standalone='yes'?>//g" addons-temp.xml | sed -e 's/<?xml version="1.0" encoding="UTF-8" standalone="yes"?>//g' > addons.xml
    rm addons-temp.xml
    md5 -r addons.xml > addons.xml.md5
fi
