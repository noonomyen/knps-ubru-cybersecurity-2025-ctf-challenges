#!/bin/bash

set -e

javac Hidden.java
jar --create --main-class=Hidden --file Hidden.jar Hidden.class
mv Hidden.jar re-3.jar

zip re-3.zip re-3.jar
