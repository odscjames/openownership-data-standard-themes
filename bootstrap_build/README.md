# Bootstrap Build

You'll need

  *  npm
  *  sass 3.5+

In this directory run

    git clone https://github.com/twbs/bootstrap.git  bootstrap
    cd bootstrap && git checkout v4.0.0 && cd ..
    
Gulp-cli should be installed globally

    sudo npm install -g grunt-cli

Then install needed packages

    npm install

To build run

    cp src/_variables.scss  bootstrap/scss/_variables.scss 
    grunt sass


## Credits

With heavy help from https://github.com/pberrecloth/ods_standards_lab
