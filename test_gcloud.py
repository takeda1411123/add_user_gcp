import subprocess
args = 'gcloud projects add-iam-policy-binding all-project-264506 --member user:akira7275129@gmail.com --role roles/viewer'
try:
    res = subprocess.check_call(args.split(" "))
except:
    print("Error.")
