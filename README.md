# log_report

# Requirements:
    * Python 3.6
    * Virtualenv
    * Pip
    * MongoDB 3.4 

### Tip how to configure workspace:
[Python workspace](https://medium.com/@henriquebastos/the-definitive-guide-to-setup-my-python-workspace-628d68552e14)

# Setup Project:

### Configuring requiriments:

```
$ make setup
```

### Env vars:

* Set `DATABASE_URL` in a `.env` file There is a exemple in `.env-example`

### Exporting Logs:
```
$ make export_log
```

### Getting Summary:
```
$ make summary
```


### Getting Ranking on web page:
```
$ make run
```

### Running Tests:
```
$ make test
```

