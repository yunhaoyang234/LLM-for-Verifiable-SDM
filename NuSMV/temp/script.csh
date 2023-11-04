read_model -i NuSMV/temp/verif.smv 
go
check_ltlspec -P "spec1" -o NuSMV/temp/result1.txt 
check_ltlspec -P "spec2" -o NuSMV/temp/result2.txt 
check_ltlspec -P "spec3" -o NuSMV/temp/result3.txt 
quit