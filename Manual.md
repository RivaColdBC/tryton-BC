# Estricto manual de como se realiza el montaje del Tryton BC
## general:

```console
python -m venv venv
call .\.venv\Scripts\activate.bat
source venv/bin/activate

python .hooks/link_modules
**cmd con administrador**

pip install -e trytond -e tryton -e proteus
pip install -r requirements.txt -r requirements-dev.txt
```

## sao:

```console
npm i --legacy-peer-deps
npm i -g grunt-cli

### for dev
grunt dev 
### for production
grunt default
use just grunt
```

## trytond:
Into trytond folder:
```console
pip install .
python bin/trytond-admin -c trytond.conf -d tryton -p
python bin/trytond-admin -c trytond.conf -d tryton --all
python bin/trytond -c trytond.conf
```

## gunicorn and server
Into trytond folder:
```
gunicorn --workers=5 --worker-class=gevent -b 0.0.0.0:8000 -c gunicorn.config.py trytond.application:app
into service: /etc/systemd/system/trytond.service
sudo systemctl daemon-reload
sudo systemctl start trytond
sudo systemctl stop trytond
sudo systemctl status trytond
sudo systemctl restart trytond
```

### delete module:
- account_statement_coda
- authentication_saml
- marketing_campaign


## module change
- delete .\sao\node_modules\po2json\package.json -> main:""
- change moment.js updaterlocale

# Fichero modificado
```
requirements.txt
requirements-dev.txt
trytond/trytond.conf
sao/custom.css
sao/custom.js
```

## tryton client:

```
Run mysys64
For the developing use python bin/tryton
For the build use make-win32-installler.sh and will get tryton.exe at the same folder
```
