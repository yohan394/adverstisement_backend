# refactoring Dockerfile  + undockerize Database + Integration with Previous apps(Rtc/Chat)

> WHAT's NEXT NEXT NEXT2: 

 

## MAIN CHANGES
```markdown
1. edit Dockerfile to make rebuild process faster. (eliminate unproductive or unnecessary lines)
2. Use local database instead of dockerized database to simulate production environment.
3. Integrate Chat and Rtc in the current app.

X. APPENDIX

    @ MYSQL MONITORING TOOL
```
---
### 1. edit Dockerfile to make rebuild process faster. (eliminate unproductive or unnecessary lines)
 - ATTEMPTS :
 
 > SUCCESS
 ```markdown
    - Get rid of "pip install ~ " command in Dockerfile.
```
> SUCCESS
```markdown
    - Combine "RUN sudo apt get ~" into single command with corresponding comments.
```
> SUCCESS
```markdown
    - State version number for 2 packages: 'mysqlclient', 'Pillow'.
```
> FAIL
```markdown
    - Eliminate usage of both 'build_deps','tmp' folders.(goal: use just one directory)
    - REASON FOR FAILURE : some packages are looking for certain directories by default.
```

> FAIL
```markdown   
    - Add --no-cache argument to all 'apt add update~ ' command.
      - REASON FOR FAILURE : installation failure when --no-cache argument is appended.
```

 - BEFORE AND AFTER :
> BEFORE:
```markdown
FROM python:3.8-alpine

# [SET-PATH]
ENV PATH="/scripts:${PATH}"

# [REQUIREMENTS-COPY]
COPY ./requirements.txt /requirements.txt

# [APP_DIRECTORY-COPY]
RUN mkdir /app
COPY ./app /app
WORKDIR /app

# [ADD-STATIC-VOLUMES]
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# [USER-ADDITION] : add user & give ownership to static directories.
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

# [USER-SETTING] : user could be chosen as <non-root>. But if so, manage.py migrate could have ownership problems.
USER root

# [MY-SQL-RELATED] : musl-dev gcc omited because already apk added in the above commands.
RUN apk add --update mysql-client
RUN apk update \
    && apk add --virtual build_deps python3-dev gcc musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip install mysqlclient

# [REQUIREMENTS-DEPENDENCIES-PRECOMPILE]
RUN apk add --update --no-cache --virtual .tmp libc-dev linux-headers libressl-dev libffi-dev libffi

# [REQUIREMENTS] : EXCEPTION = mysqlclient
RUN pip install -r /requirements.txt


# TO USE DJANGO MODEL.IMAGEFIELD INSTALL PILLOW WITH OS-DEPENDENCY
RUN apk add --update --no-cache jpeg-dev zlib-dev
RUN apk add --update --no-cache --virtual .build-deps build-base linux-headers
RUN pip install Pillow

# [SCRIPT-DIRECTORY-COPY]
COPY ./scripts /scripts

# [BASH-SCRIPTS] :
#   1. collectstatic + uwsgi initialize
RUN chmod +x /scripts/*

# [TMP-DIRECTORIES-DELETE]
RUN apk del .tmp
RUN apk del build_deps

CMD ["entrypoint.sh"]
```
> AFTER:
```markdown
FROM python:3.8-alpine

# [SET-PATH]
ENV PATH="/scripts:${PATH}"

# [REQUIREMENTS-COPY]
COPY ./requirements.txt /requirements.txt

# [APP_DIRECTORY-COPY]
RUN mkdir /app
COPY ./app /app
WORKDIR /app

# [ADD-STATIC-VOLUMES]
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# [USER-ADDITION] : add user & give ownership to static directories.
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

# [USER-SETTING] : user could be chosen as <non-root>. But if so, manage.py migrate could have ownership problems.
USER root

# [MY-SQL-RELATED] :
RUN apk add --update mysql-client
RUN apk update \
    # MARIADB
    && apk add --virtual build_deps python3-dev gcc musl-dev \
    && apk add --no-cache mariadb-dev \
     # ETC [=channels/Django/uWSGI/gunicorn/cryptography/channels_redis] :
    && apk add --virtual .tmp libc-dev linux-headers libressl-dev libffi-dev libffi \
    # PILLOW :
    && apk add --virtual --no-cache .tmp jpeg-dev zlib-dev build-base \
    && pip install -r /requirements.txt

# [SCRIPT-DIRECTORY-COPY]
COPY ./scripts /scripts

# [BASH-SCRIPTS] :
#   1. collectstatic + uwsgi initialize
RUN chmod +x /scripts/*

# [TMP-DIRECTORIES-DELETE]
RUN apk del .tmp
RUN apk del build_deps

CMD ["entrypoint.sh"]
```
     
---

### 2. Use local database instead of dockerized database to simulate production environment.
#### 2-1. OBJECTIVE
 - ##### Links that helped achive this goal:
   - multiple instance
     - https://dev.mysql.com/doc/refman/8.0/en/multiple-windows-command-line-servers.html 
   - mariadb replication
     - https://gunnm.tistory.com/146
 - ##### master-slave replication with respect to : 
    - single machine
    - windows operating system
#### 2-2. PREREQUISITE
 - ##### Run Multiple mariadb instance.
 - ##### Set up slave and master information.
 - ##### Test that the setup works.

#### 2-3. REMINDER
 - ##### slave version should be greater or equal to the master version of mariadb.
 - ##### unique server-id parameter value must be set. 

#### 2-4. STEPS TAKEN
 > A. COPY MARIADB PROGRAM DIRECTORY TO USE AS SLAVE.
```markdown
> MASTER_DIR = ORIGINAL DIRECTORY [=C:\Program Files\MariaDB 10.3\]
> SLAVE_DIR = COPIED DIRECTORY [=C:\Program Files\MariaDB 10.3_slave\]
```

 > B. CHANGE INI FILES IN BOTH DIRECTORY

 - ADDED to MASTER_DIR/my.ini:
```markdown
server-id = 1
sync_binlog=1
log-bin=mysql-bin
innodb_flush_log_at_trx_commit = 1
```
 
 - CHANGES in SLAVE_DIR/my.ini:
   - name of the instance : [mysqld] -> [myqld_slave]
   - port number : 3306 -> 3307
```markdown
[mysqld_slave1]
port=3307
```
 - ADDED to SLAVE_DIR/my.ini:
```markdown
server-id=2
relay-log-index=slave-relay-bin.index
relay-log=slave-relay-bin
replicate-do-db='app_grouptango'
```
 - DELETED from SLAVE_DIR/my.ini:
```markdown
[client]
port=3306
plugin-dir=C:/Program Files/MariaDB 10.3/lib/plugin
```

 > B. Run both mariadb instances + set replication relationship.
 - Key Points : 
   - B-1. Restart/start mysql services for master and slave.
   - B-2. Go to the MASTER_DIR bin directory in login to mysql.
```markdown
> cd path/to/MASTER_DIR/bin
> mysql -u USER_ID -pPASSWORD 
```
   - B-3. Create user that could access from Master to Slave.
   - B-4. Check that user is created.
   - "SHOW MASTER STATUS;" mysql-command should NOT return an empty set.
   - If you set the log-bin argument in the MASTER_DIR/my.ini file, it would return a record with File and Position column.
```markdown
# grant replication slave on *.* to 'repl_user'@'%' identified by 'password';
# select user,host from mysql.users;
# show master status;
```
   - B-5. Access slave mysql database that was assigned a different port value.
```markdown
> cd path/to/SLAVE_DIR/bin
> mysql -u SLAVE_USER_ID -pPASSWORD --port=SLAVE_PORT
```
   - B-6. Run "CHANGE MASTER TO" command in SLAVE-DATABASE.
```markdown
CHANGE MASTER TO MASTER_HOST='your_master_host',MASTER_USER='repl_user',MASTER_PASSWORD='password', MASTER_PORT='master_port', MASTER_CONNECT_RETRY=30;
```
   - B-7. Check slave status.
```markdown
# show slave status;
```
    

---

### 3. Integrate Chat and Rtc in the current app.
 - #### Combined rtc app with chat -> renamed app as chat.
 - #### Removed class 'viewed' from chat/models.py which was used to keep track of unread chat messages.
 - #### Added screen share feature using rtcmulticonnection api.
 - #### **(note)##
   - when running the application using manage.py chatsocket does not work. (keep note of this)
   - when running from docker-compose, make sure to set the settings.APPLICATION_STAGE to settings.STAGE_OF_PRODUCTION.
   - when running from manage.py, make sure to set the settings.APPLICATION_STAGE to settings.STAGE_OF_DEVELOPING.   
---

## X. APPENDIX
 Useful links that helped achive the results :
   - multiple instance
     - https://dev.mysql.com/doc/refman/8.0/en/multiple-windows-command-line-servers.html 
   - mariadb replication
     - https://gunnm.tistory.com/146
 
> ##### @ MYSQL MONITORING TOOL