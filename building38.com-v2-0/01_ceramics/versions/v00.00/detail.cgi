#!/usr/bin/perl

BEGIN
{
	unshift (@INC,"/home/building38/libperl");
}

use CGI;
use CGI::Carp qw/fatalsToBrowser/;
use DBI;
use HTML::Template;

$cgi = new CGI();
$dbh = DBI->connect("DBI:mysql:risd38:localhost","building38","123457z");
$t = new HTML::Template(filename => "detail.tmpl");

$nId = $cgi->param("glaze");

$info = getInfo($nId);
$t->param($info);
$prop = getPropertiesFlat($nId);
$t->param($prop);
$ingr = getIngredients($nId);
$t->param({recipe=>$ingr});

print $cgi->header();
print $t->output();

sub getInfo
{
	my($nId,$sth,$res) = @_;
	
	$sth = $dbh->prepare("select glaze_name, description, comment from glaze where id = ?");
	$sth->execute($nId);
	$res = $sth->fetchrow_hashref();
	return $res;
}

sub getIngredients
{
	my($nId,$sth,$res) = @_;
	
	$sth = $dbh->prepare("select ingr_name, ingr_val from glaze_recipe where glaze_id = ?");
	$sth->execute($nId);
	$res = $sth->fetchall_arrayref({});
	return $res;
}

sub getPropertiesFlat
{
	my($nId,$sth,$row,$res) = @_;
	
	$sth = $dbh->prepare("select prop_name, prop_val from glaze_properties where glaze_id = ?");
	$sth->execute($nId);
	while ($row = $sth->fetchrow_hashref())
	{
		if ($res->{$row->{prop_name}})
		{
			$res->{$row->{prop_name}} = $res->{$row->{prop_name}} . ", " . $row->{prop_val};
		}
		else
		{
			$res->{$row->{prop_name}} = $row->{prop_val};
		}
	}
	return $res;
}

