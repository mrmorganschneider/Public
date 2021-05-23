#!/user/bin/perl
use File::Copy;

##############################################################################
#Perl script to edit the default ebcdic header with line specific information#
#Created by Morgan Schneider - Polarcus Nadia Nov 5, 2012                    #
##############################################################################

#Check to ensure correct number of command line arguments were passed

$num_args = $#ARGV + 1;
if ($num_args != 5) {
	
	print "\nUsage: ebcdic.pl Linename FGSP LGSP Date Reel\n";
	exit;
}

#Set current date
my ($day, $month, $year)=(localtime)[3,4,5];

if ($day =~ /^\d{1}$/){ #check if day is only 1 digit long
	$day =~ s/$day/0$day/;
}
$month += 1;

if ($month =~ /^\d{1}$/){ #check if day is only 1 digit long
	$month =~ s/$month/0$month/;
}

$year += 1900;

#input data editing

if ($ARGV[1] =~ /^\d{3}$/){ #check if FGFFID is only 3 digits long
	$ARGV[1] =~ s/$ARGV[1]/0$ARGV[1]/;
}

if ($ARGV[2] =~ /^\d{3}$/){ #check if LGFFID is only 3 digits long
	$ARGV[2] =~ s/$ARGV[2]/0$ARGV[2]/;
}

#adjust reel number to the correct value based on the number of files in the .ebcdic_headers directory
#my $dirEbcdic = '/home/gxt/morgan/randd/perl/.ebcdic_headers';
#my @headers = <$dirEbcdic/*>;
#my $intCount = @headers;

#$intReelnum = $intCount + 1160;

#Change this section according to your job parameters

$strOriginalfile = "UPDATED_Total_3D_ebcdic.txt";
$strNFHheaderfile = "NFH_EBCDIC.txt";
$strDefaultlinename = "3DM6NNNNXYZZZ"; #default line name in the ebcdic header
$strDefaultreelnum = "RRRR"; #default reel number in ebcdic
$strDefaultdate = "DD-MMM-YYYY"; #default date format in ebcdic
$strDefaultFGFFID = "FFFF"; #default first good ffid in ebcdic
$strDefaultLGFFID = "LLLL"; #default last good ffid in ebcdic

#Copy original ebcdic to new file using line name
#copy($strOriginalfile, $ARGV[0]) or die "ERROR: File copy was unsucessful.";

#Read default lines from ebcdic txt file
open(FILE, "<", $strOriginalfile) or die "ERROR: Original file not found.";
my @oldlines = <FILE>;
close(FILE);

#search the input lines one by one for the default pattern in ebcdic and replace as necessary
my @newlines;
foreach(@oldlines) {

	$_ =~ s/$strDefaultlinename/$ARGV[0]/;
	$_ =~ s/$strDefaultreelnum/$ARGV[4]/;
	$_ =~ s/$strDefaultdate/$ARGV[3]/;
	$_ =~ s/$strDefaultFGFFID/$ARGV[1]/;
	$_ =~ s/$strDefaultLGFFID/$ARGV[2]/;
	
	push(@newlines, $_);
}

#create new file and populate it with the edited ebcdic data
open(FILE, "+>", "HEADERS/$ARGV[0]") or die $!;
print FILE @newlines;
close(FILE);

print "EBCDIC copy and editing completed successfully\n";

#Read default NFH ebcdic file 
open(FILE, "<", $strNFHheaderfile) or die "ERROR: Original file not found.";
my @NFHoldlines = <FILE>;
close(FILE);

#search the input lines one by one for the default pattern in ebcdic and replace as necessary
my @NFHnewlines;
foreach(@NFHoldlines) {

	$_ =~ s/$strDefaultlinename/$ARGV[0]/;
	$_ =~ s/$strDefaultdate/$ARGV[3]/;
	$_ =~ s/ZZ-ZZ-ZZZZ/$day-$month-$year/;
	
	push(@NFHnewlines, $_);
}

#create new file and populate it with the edited ebcdic data
open(FILE, "+>", "NFH/HEADERS/$ARGV[0]") or die $!;
print FILE @NFHnewlines;
close(FILE);

print "NFH copy and editing completed successfully\n";
