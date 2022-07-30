#!/usr/bin/osascript

use framework "CoreBrightness"
on run argv
	set client to current application's CBBlueLightClient's new
	client's setEnabled:true
	set strength to 25 as number
	client's setStrength:(strength / 100.0) commit:true
end run
