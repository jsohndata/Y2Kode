#!/usr/bin/perl

use CGI;
use CGI::Carp qw/fatalsToBrowser/;
use HTML::Template;
use Data::Dumper;

require "glaze.pl";

$cgi = new CGI();
$t = new HTML::Template(filename => "detail.tmpl",die_on_bad_params=>0);
$nId = $cgi->param("glaze");
$t->param(getInfo($nId));
$t->param(getMolecular($nId));
$t->param(getPropertiesFlat($nId));
$t->param({"recipe"=>getList($nId,"base")});
$t->param({"analysis"=>getList($nId,"analysis")});
$t->param({"colorant"=>getList($nId,"colorant")});

print $cgi->header();
print $t->output();

