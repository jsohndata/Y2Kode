#!/usr/bin/perl

use CGI;
use CGI::Carp qw/fatalsToBrowser/;
use HTML::Template;
use Data::Dumper;
require "../glaze.pl";


$cgi = new CGI();
$action = $cgi->param("action");
if ($action eq "delete")
{
	$glazeId = $cgi->param("glaze");
	$dbh->do("delete from glaze_recipe where glaze_id = $glazeId");
	$dbh->do("delete from glaze_properties where glaze_id = $glazeId");
	$dbh->do("delete from glaze where id = $glazeId");
}

$t = new HTML::Template(filename => "admin.tmpl",die_on_bad_params=>0);

$sth = $dbh->prepare("select id,glaze_name,description,comment from glaze");
$sth->execute();
$rRes = $sth->fetchall_arrayref({});
{
	$t->param("table_glaze"=>$rRes);
}
$sth->finish;

print $cgi->header();
print $t->output();

