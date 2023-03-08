#!/usr/bin/perl


use DBI;
$dbh = DBI->connect("DBI:mysql:risd38:localhost","building38","123457z");

sub getInfo
{
	my($nId,$sth,$res) = @_;
	
	$sth = $dbh->prepare("select glaze_name, description, comment from glaze where id = ?");
	$sth->execute($nId);
	$res = $sth->fetchrow_hashref();
	return $res;
}

sub getList
{
	my($nId,$sType,$sth,$res) = @_;
	
	$sth = $dbh->prepare("select ingr_name, ingr_val from glaze_recipe where glaze_id = ? and ingr_type = ?");
	$sth->execute($nId,$sType);
	$res = $sth->fetchall_arrayref({});
	return $res;
}

sub getTotal
{
	my($res,$rRow,$nTotal) = @_;
	
	$nTotal=0;
	foreach $rRow (@$res)
	{
		$nTotal += $rRow->{ingr_val};
	}
	return $nTotal;
}



sub getMolecular
{
	my($nId,$list,$ingr,$res) = @_;
	
	$list = &getList($nId,"molecular");
	foreach $ingr (@$list)
	{
		$res->{$ingr->{ingr_name}} = $ingr->{ingr_val};
	}
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

return 1;