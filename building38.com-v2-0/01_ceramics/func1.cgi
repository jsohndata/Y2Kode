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
	$sG .= " and glaze_name like '%$glaze_name%'";
}

# Cone
$cone = $cgi->param("cone");
if ($cone)
{
	$sP .= " and prop_name = 'cone' and prop_val  = '$cone'";
}

# Surface
@surface = $cgi->param("surface");
if (@surface)
{
	$sP .= " and prop_name = 'surface' and prop_val  in ['".join(@surface,"','")."']";
}

# Color
@color = $cgi->param("color");
if (@color)
{
	$sP .= " and prop_name = 'color' and prop_val  in ['".join(@color,"','")."']";
}

# Value
@value = $cgi->param("value");
if (@value)
{
	$sP .= " and prop_name = 'value' and prop_val  in ['".join(@value,"','")."']";
}

# Firing
$firing = $cgi->param("firing");
if ($firing)
{
	$sP .= " and prop_name = 'firing' and prop_val = '$firing'";
}

# Oxide
@oxide = $cgi->param("oxide");
if (@oxide)
{
	$sP .= " and prop_name = 'oxide' and prop_val  in ['".join(@oxide,"','")."']";
}

# Hazard
$hazard = $cgi->param("hazard");
if ($hazard)
{
	$sP .= " and prop_name = 'hazard' and prop_val like '%$hazard%'";
}

# Description
$description = $cgi->param("description");
if ($description)
{
	$sG .= " and prop_name = 'hazard' and prop_val like '%$description%'";
}

$sth1 = $dbh->prepare("select glaze_id from glaze_properties where 1=1 $sP");
$sth1->execute();
while (($id) = $sth1->fetchrow_array())
{
	$ids{$id} += 1
}

$sth1 = $dbh->prepare("select id from glaze where 1=1 $sG");
$sth1->execute();
while (($id) = $sth1->fetchrow_array())
{
	$ids{$id} += 1
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

