requirements:
1. glob
2. os
3. time
4. google
5. google-cloud
6. google-cloud-translate

```
pip install -r requirements.txt
```
How to use:
1. Select file path using FILEPATH variable.(the file must be line seperated text file)
2. Select source and target language code.(check main.py)
3. Run the code (main.py)

Result:
1. Result file will be created at same directory of the
2. Name convention - <original_filename>_<source_language_code>-<target_language_code>.txt

Warning:
1. I STRONGLY RECOMMENT NOT USING THIS CODE IF YOU HAVE TO CONSIDER THE COST. (*BECAUSE THE CREDENTIAL IS NOT FREE!!)
2. The code requires json file named 'service_credentials.json' for which is authentcation. (You need your own credential)
3. You need to fill PROJECT_ID and LOCATION value in google_translate.py

Errors & Solutions:
1. too many words: reduce UNIT variable
2. too many requests: increase DELAY variable
3. request number exceeeded: wait for 1-2 hours and retry it.

Tips:
1. The FILEPATH variable can be both absolute/relative path.
2. If you have any other quetions, please contact me.
