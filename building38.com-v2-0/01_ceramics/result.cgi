#!/usr/bin/perl

use CGI;
use CGI::Carp qw/fatalsToBrowser/;
use HTML::Template;
use Data::Dumper;

require "glaze.pl";

$cgi = new CGI();
$t = new HTML::Template(filename => "result.tmpl",die_on_bad_params=>0);

$sG = "";
$sP = "";

# Glaze Name
$glaze_name = $cgi->param("glaze_name");
if ($glaze_name)
{
	$sth1 = $dbh->prepare("select id from glaze where glaze_name like '%$glaze_name%'");
	$sth1->execute();
	while (($id) = $sth1->fetchrow_array())
	{
		$ids{$id} += 1
	}
}

# Cone
$cone = $cgi->param("cone");
if ($cone)
{
	$sth1 = $dbh->prepare("select glaze_id from glaze_properties where prop_name = 'cone' and prop_val  = '$cone'");
	$sth1->execute();
	while (($id) = $sth1->fetchrow_array())
	{
		$ids{$id} += 1
	}
}

# Surface
@surface = $cgi->param("surface");
if (@surface)
{
	$sth1 = $dbh->prepare("select glaze_id from glaze_properties where prop_name = 'surface' and prop_val  in ('".join("','",@surface)."')");
	$sth1->execute();
	while (($id) = $sth1->fetchrow_array())
	{
		$ids{$id} += 1
	}
}

# Color
@color = $cgi->param("color");
if (@color)
{
	$sth1 = $dbh->prepare("select glaze_id from glaze_properties where prop_name = 'color' and prop_val  in ('".join("','",@color)."')");
	$sth1->execute();
	while (($id) = $sth1->fetchrow_array())
	{
		$ids{$id} += 1
	}
}

# Value
@value = $cgi->param("value");
if (@value)
{
	$sth1 = $dbh->prepare("select glaze_id from glaze_properties where prop_name = 'value' and prop_val  in ('".join("','",@value)."')");
	$sth1->execute();
	while (($id) = $sth1->fetchrow_array())
	{
		$ids{$id} += 1
	}
}

# Firing
$firing = $cgi->param("firing");
if ($firing)
{
	$sth1 = $dbh->prepare("select glaze_id from glaze_properties where prop_name = 'firing' and prop_val = '$firing'");
	$sth1->execute();
	while (($id) = $sth1->fetchrow_array())
	{
		$ids{$id} += 1
	}
}

# Oxide
@oxide = $cgi->param("oxide");
if (@oxide)
{
	$sth1 = $dbh->prepare("select glaze_id from glaze_properties where prop_name = 'oxide' and prop_val  in ('".join("','",@oxide)."')");
	$sth1->execute();
	while (($id) = $sth1->fetchrow_array())
	{
		$ids{$id} += 1
	}
}

# Hazard
$hazard = $cgi->param("hazard");
if ($hazard)
{
	$sth1 = $dbh->prepare("select glaze_id from glaze_properties where prop_name = 'hazard' and prop_val like '%$hazard%'");
	$sth1->execute();
	while (($id) = $sth1->fetchrow_array())
	{
		$ids{$id} += 1
	}
}

# Description
$description = $cgi->param("description");
if ($description)
{
	$sth1 = $dbh->prepare("select id from glaze where description like '%$description%'");
	$sth1->execute();
	while (($id) = $sth1->fetchrow_array())
	{
		$ids{$id} += 1
	}
}

$sth1 = $dbh->prepare("select id from glaze");
$sth1->execute();
while (($id) = $sth1->fetchrow_array())
{
	$ids{$id} += 1
}

@idSort = sort { $ids{$b} <=> $ids{$a} } (keys %ids);

$rRes = [];
for $nGlazeId (@idSort)
{
	$tData = {};
	
	$nId = $nGlazeId;
	$tData->{id} = $nId;
	
	$rData = getInfo($nId);
	$tData->{glaze_name} = $rData->{glaze_name};
	
	$rData = getPropertiesFlat($nId);
	$tData->{cone} = $rData->{cone};
	$tData->{surface} = $rData->{surface};
	$tData->{value} = $rData->{value};
	$tData->{color} = $rData->{color};
	$tData->{hazard} = $rData->{hazard};
	
	$tData->{recipe} = getList($nId,"base");
	$tData->{recipe_total} = getTotal($tData->{recipe});
	push(@$rRes,$tData);
}
$t->param({"result"=>$rRes});

$glaze_name = $cgi->param("glaze_name");
$cone = $cgi->param("cone");
@surface = $cgi->param("surface");
@color = $cgi->param("color");
@value = $cgi->param("value");
$firing = $cgi->param("firing");
@oxide = $cgi->param("oxide");
$hazard = $cgi->param("hazard");
$description = $cgi->param("description");

print $cgi->header();
print $t->output();

