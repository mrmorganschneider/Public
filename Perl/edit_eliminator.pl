#!/usr/bin/perl
#use File::Copy;

#### EDIT ELIMINATOR PERL SCRIPT ####
# Designed to reduce the number of  #
# traces from 3600 to 2400 for the  #
# Total 3D Burma survey requirements#
# Created by Morgan Schneider       #
#####################################


#open edits file
open(FILE, "<", $ARGV[0]) or die "ERROR: Original $ARGV[0] file not found.";
my $strOLDedits = <FILE>;
close(FILE);

#Begin edits processing

#Shot edits

#$strOLDedits =~ s/\:1-3600\//\:1-2400\//g;

#cable 1
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:(2[4-9][0-9]|3[0-5][0-9]|360)\///g;
$strOLDedits =~ s/\d{1,4}\:(2[4-9][0-9]|3[0-5][0-9]|360)\///g;
$strOLDedits =~ s/\:240\-\d{3}/\:240/g;
$strOLDedits =~ s/\:(2[4-9][0-9]|3[0-5][0-9]|360)\-/\:240\-/g;
$strOLDedits =~ s/\-(2[4-9][0-9]|3[0-5][0-9]|360)\//\-240\//g;
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:240\-240\///g;
$strOLDedits =~ s/\d{1,4}\:240\-240\///g;

#cable 2
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:(6[0-9][0-9]|7[0-1][0-9]|720)\///g;
$strOLDedits =~ s/\d{1,4}\:(6[0-9][0-9]|7[0-1][0-9]|720)\///g;
$strOLDedits =~ s/\:600\-\d{3}/\:600/g;
$strOLDedits =~ s/\:(6[0-9][0-9]|7[0-1][0-9]|720)\-/\:600\-/g;
$strOLDedits =~ s/\-(6[0-9][0-9]|7[0-1][0-9]|720)\//\-600\//g;
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:600\-600\///g;
$strOLDedits =~ s/\d{1,4}\:600\-600\///g;

#cable 3
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:(9[6-9][0-9]|10[0-7][0-9]|1080)\///g;
$strOLDedits =~ s/\d{1,4}\:(9[6-9][0-9]|10[0-7][0-9]|1080)\///g;
$strOLDedits =~ s/\:960\-\d{3,4}/\:960/g;
$strOLDedits =~ s/\:(9[6-9][0-9]|10[0-7][0-9]|1080)\-/\:960\-/g;
$strOLDedits =~ s/\-(9[6-9][0-9]|10[0-7][0-9]|1080)\//\-960\//g;
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:960\-960\///g;
$strOLDedits =~ s/\d{1,4}\:960\-960\///g;

#cable 4
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:(13[2-9][0-9]|14[0-3][0-9]|1440)\///g;
$strOLDedits =~ s/\d{1,4}\:(13[2-9][0-9]|14[0-3][0-9]|1440)\///g;
$strOLDedits =~ s/\:1320\-\d{4}/\:1320/g;
$strOLDedits =~ s/\:(13[2-9][0-9]|14[0-3][0-9]|1440)\-/\:1320\-/g;
$strOLDedits =~ s/\-(13[2-9][0-9]|14[0-3][0-9]|1440)\//\-1320\//g;
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:1320\-1320\///g;
$strOLDedits =~ s/\d{1,4}\:1320\-1320\///g;

#cable 5
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:(16[8-9][0-9]|17[0-9][0-9]|1800)\///g;
$strOLDedits =~ s/\d{1,4}\:(16[8-9][0-9]|17[0-9][0-9]|1800)\///g;
$strOLDedits =~ s/\:1680\-\d{4}/\:1680/g;
$strOLDedits =~ s/\:(16[8-9][0-9]|17[0-9][0-9]|1800)\-/\:1680\-/g;
$strOLDedits =~ s/\-(16[8-9][0-9]|17[0-9][0-9]|1800)\//\-1680\//g;
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:1680\-1680\///g;
$strOLDedits =~ s/\d{1,4}\:1680\-1680\///g;

#cable 6
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:(20[4-9][0-9]|21[0-5][0-9]|2160)\///g;
$strOLDedits =~ s/\d{1,4}\:(20[4-9][0-9]|21[0-5][0-9]|2160)\///g;
$strOLDedits =~ s/\:2040\-\d{4}/\:2040/g;
$strOLDedits =~ s/\:(20[4-9][0-9]|21[0-5][0-9]|2160)\-/\:2040\-/g;
$strOLDedits =~ s/\-(20[4-9][0-9]|21[0-5][0-9]|2160)\//\-2040\//g;
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:2040\-2040\///g;
$strOLDedits =~ s/\d{1,4}\:2040\-2040\///g;

#cable 7
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:(24[0-9][0-9]|25[0-1][0-9]|2520)\///g;
$strOLDedits =~ s/\d{1,4}\:(24[0-9][0-9]|25[0-1][0-9]|2520)\///g;
$strOLDedits =~ s/\:2400\-\d{4}/\:2400/g;
$strOLDedits =~ s/\:(24[0-9][0-9]|25[0-1][0-9]|2520)\-/\:2400\-/g;
$strOLDedits =~ s/\-(24[0-9][0-9]|25[0-1][0-9]|2520)\//\-2400\//g;
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:2400\-2400\///g;
$strOLDedits =~ s/\d{1,4}\:2400\-2400\///g;

#cable 8
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:(27[6-9][0-9]|28[0-7][0-9]|2880)\///g;
$strOLDedits =~ s/\d{1,4}\:(27[6-9][0-9]|28[0-7][0-9]|2880)\///g;
$strOLDedits =~ s/\:2760\-\d{4}/\:2760/g;
$strOLDedits =~ s/\:(27[6-9][0-9]|28[0-7][0-9]|2880)\-/\:2760\-/g;
$strOLDedits =~ s/\-(27[6-9][0-9]|28[0-7][0-9]|2880)\//\-2760\//g;
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:2760\-2760\///g;
$strOLDedits =~ s/\d{1,4}\:2760\-2760\///g;

#cable 9
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:(31[2-9][0-9]|32[0-3][0-9]|3240)\///g;
$strOLDedits =~ s/\d{1,4}\:(31[2-9][0-9]|32[0-3][0-9]|3240)\///g;
$strOLDedits =~ s/\:3120\-\d{4}/\:3120/g;
$strOLDedits =~ s/\:(31[2-9][0-9]|32[0-3][0-9]|3240)\-/\:3120\-/g;
$strOLDedits =~ s/\-(31[2-9][0-9]|32[0-3][0-9]|3240)\//\-3120\//g;
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:3120\-3120\///g;
$strOLDedits =~ s/\d{1,4}\:3120\-3120\///g;

#cable 10
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:(34[8-9][0-9]|35[0-9][0-9]|3600)\///g;
$strOLDedits =~ s/\d{1,4}\:(34[8-9][0-9]|35[0-9][0-9]|3600)\///g;
$strOLDedits =~ s/\:3480\-\d{4}/\:3480/g;
$strOLDedits =~ s/\:(34[8-9][0-9]|35[0-9][0-9]|3600)\-/\:3480\-/g;
$strOLDedits =~ s/\-(34[8-9][0-9]|35[0-9][0-9]|3600)\//\-3480\//g;
$strOLDedits =~ s/\d{1,4}\-\d{1,4}\:3480\-3480\///g;
$strOLDedits =~ s/\d{1,4}\:3480\-3480\///g;

#create output file
open(FILE,"+>", "FT/$ARGV[0]") or die $!;
print FILE $strOLDedits;
close(FILE);

print "Edits eliminated with extreme prejudice\n";
