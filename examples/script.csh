#!NuSMV -source
read_model -i examples/sample_fsa.smv
go
check_ltlspec -P "safety" -o NuSMV/temp/result1.txt 
check_ltlspec -P "liveness" -o NuSMV/temp/result2.txt 
quit
