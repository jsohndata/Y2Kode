#!/usr/bin/perl

use CGI;
use CGI::Carp qw/fatalsToBrowser/;
use HTML::Template;
use Data::Dumper;
require "../glaze.pl";


$cgi = new CGI();
$t = new HTML::Template(filename => "admindet.tmpl",die_on_bad_params=>0);

# Get the glaze id
$glazeId = $cgi->param("glaze");
unless ($glazeId)
{

	$sth = $dbh->prepare("select id from glaze order by id desc");
	$sth->execute();
	($maxId) = $sth->fetchrow_array();
	$glazeId = $maxId+1;
	$dbh->do("insert into glaze (id) values ('$glazeId')");	
}

# save any new glaze info sent
@params = ("glaze_name","description","comment");
foreach $var (@params)
{
	$val = $cgi->param($var);
	if ($val ne "")
	{
		$val = $dbh->quote($val);
		$dbh->do("update glaze set $var=$val where id='$glazeId'");
	}
}

# save any new property
if ($cgi->param("prop_name") ne "")
{
	$sth = $dbh->prepare("insert into glaze_properties (glaze_id,prop_name,prop_val) values (?,?,?)");
	$sth->execute($glazeId,$cgi->param("prop_name"),$cgi->param("prop_val"));
}

# save any new ingredient
if ($cgi->param("ingr_type") ne "")
{
	$sth = $dbh->prepare("insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (?,?,?,?)");
	$sth->execute($glazeId,$cgi->param("ingr_type"),$cgi->param("ingr_name"),$cgi->param("ingr_val"));
}

# See if anything was to be deleted
if ($cgi->param("action") eq "delete")
{
	$dbh->do("delete from ".$cgi->param("table")." where ".(($cgi->param("table")eq"glaze_properties")?"prop":"ingr")."_name = ".$dbh->quote($cgi->param("name"))." and glaze_id='$glazeId'");
}

$sth = $dbh->prepare("select id,glaze_name,description,comment from glaze where id=$glazeId");
$sth->execute();
$rRes = $sth->fetchrow_hashref();
$t->param($rRes);
$sth->finish;

$sth = $dbh->prepare("select P.glaze_id,G.glaze_name,P.prop_name,P.prop_val from glaze_properties P left join glaze G on P.glaze_id = G.id where P.glaze_id = $glazeId order by P.prop_name");
$sth->execute();
$rRes = $sth->fetchall_arrayref({});
{
	$t->param("table_properties"=>$rRes);
}
$sth->finish;

$sth = $dbh->prepare("select P.glaze_id,G.glaze_name,P.ingr_type,P.ingr_name,P.ingr_val from glaze_recipe P left join glaze G on P.glaze_id = G.id where P.glaze_id = $glazeId order by P.ingr_type, P.ingr_name");
$sth->execute();
$rRes = $sth->fetchall_arrayref({});
{
	$t->param("table_recipe"=>$rRes);
}
$sth->finish;

print $cgi->header();
print $t->output();

