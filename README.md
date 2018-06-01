# selenium-grid-docker-compose-sample
you can use selenium grid with docker-compose

## How to use

Download and open selenium-grid-sample.

```
git clone https://github.com/sleepless-se/selenium-grid-sample.git
```

or

download as zip and open the folder

Start docker compose(Python SeleniumGrid Chorme)

```
cd selenium-grid-sample
docker-compose up -d
```

Login python container

```
docker exec -it python /bin/bash
```

Run sample program.

```
python tests/sample.py
```

##How to check the selenium browser.

###Connect server for Mac

`Finder - Go - Connect server`

Enter this address.

`vnc://localhost:5900` then connect.

Password is `secret`.

Now you can see the selenium!!

##How to update sample program.

Go to your local tests folder in selenium-grid-sample.

You can see `screenshots.png`. It took when you run sample.py

The file comes from Python container.

So you can edit sample.py then run the file from Python container.

```
python tests/sample.py
```

Enjoy selenium grid!