# Interact with the official API of League of Legends

* Get information of your or any summoner account.
* Look info of previously matches or a current game.
* Look all champions mastery.
* View details about leagues.
* View the current rotation champions.
* Get details about the current status of the servers.

### How to use

In order to communicate with the API of League of Legends, you must generate a valid API key in [the official site for developers of Riot](https://developer.riotgames.com/).

When you have your own API key, in the file `main.py`, search the variable `apiKey` and put them into the quotation marks.

Search the variable `reg` and put the desired region into the quotation marks. You can consult all the existent regions [here](https://developer.riotgames.com/regional-endpoints.html).

<img src="https://res.cloudinary.com/dzrar46ht/image/upload/v1559864389/Git/apiReg_qltgzp.png" />

Keep in mind that all queries must to have the region and the API key, if one of them are wrong you will get an error.

### Example of use

<img src="https://res.cloudinary.com/dzrar46ht/image/upload/v1559864530/Git/exampleApiLol_q93gzc.png" />

The above code gets the information account of the user `example` and saves them into a [dictionary](https://www.w3schools.com/python/python_dictionaries.asp) called `account`.  After that, it request all matches of the user `example` using the previously retrieved data.

### Return values

All functions are documented to know what they do, but not the returned values, if you have any doubt with the returned values you can consult the API methods in the [Riot Developer Portal](https://developer.riotgames.com/api-methods/) and obtain information of all the return values.
