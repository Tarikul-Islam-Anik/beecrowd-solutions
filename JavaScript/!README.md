## How to read sample input in Javascript? 

You probably have noticed that Beecrowd has these two lines of boilerplate code in the beginning of each problem:

```javascript
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
```

Actually, they're using file reading technicque to read the input. Here they are reading the sample input from the `stdin` file from `/dev` folder. stdin is a special file that is used to read the input from the standard input.

To achive this, first create a folder called `dev` in your project folder. 

![Create_dev_folder](https://i.ibb.co/M11TCR8/1.png)

Then create a file called `stdin` in the `dev` folder. 

![Create_sdin_file](https://i.ibb.co/mDbgRdM/2.png)

Then open the `stdin` file in your text editor and write the sample input. In the JavaScript file, you can use the `fs` module to read the input from the `stdin` file.

```javascript
var input = require('fs').readFileSync('dev/stdin', 'utf8');
var lines = input.split('\n');
```
> Notice that I've wrote `dev/stdin` to access the file. You've to add a slash(/) before the file name when you're going to submit the answer.

![Enter_input_values](https://i.ibb.co/2qvpRHN/3.png)

Run the code and see the output.
        
    SOMA = 40

When you ready to submit your solution, don't forget to change the file path from `dev/stdin` to `/dev/stdin` in the code. Otherwise you'll get an error.

![added_a_slash](https://i.ibb.co/xDcLyCt/4.png)


Now you can successfully work on your code locally and submit it without any trouble. 

**Happy Coding!**