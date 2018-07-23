## Docker - beyond the basics

Exercises for the advanced Docker training by [Otomato](http://otomato.link)

  If using Strigo - please do the following to set up the environment:
  
  ```
  sudo usermod -G docker $USER
  sudo su - $USER
  git clone https://github.com/otomato-gh/docker-training
  cd docker-training/mynetbox
  docker build . -t mynetbox
