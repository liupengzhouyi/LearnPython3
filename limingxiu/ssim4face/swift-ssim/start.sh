rm -f ./result_txt/*

for file in ./script/*
do
    {   
        python3 $file
    }&
done