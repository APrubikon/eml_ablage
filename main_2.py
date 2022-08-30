import os
import glob
import email
from email import policy

indir = '/Volumes/TeamDrive/Nasrallah (0144)/Aufträge/22-005 Diverse Inkassoangelegenheiten'
outdir = os.path.join(indir, 'output')

os.makedirs(outdir, exist_ok=True)
files = glob.glob(os.path.join(indir, '*.eml'))

for eml_file in files:
    # This will not work in Python 2
    msg = email.message_from_file(open(eml_file), policy=policy.default)
    for att in msg.iter_attachments():
        # Tabs may be added for indentation and not stripped automatically
        filename = att.get_filename().replace('\t', '')
        # Here we suppose for simplicity sake that each attachment has a valid unique filename,
        # which, generally speaking, is not true.
        print(msg.get_param())
       #with open(os.path.join(outdir, filename), 'wb') as f:
       #    f.write(att.get_content())