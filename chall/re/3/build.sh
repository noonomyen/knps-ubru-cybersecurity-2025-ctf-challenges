#!/bin/bash

set -e

javac Hidden.java
jar cf Hidden.jar Hidden.class
mv Hidden.jar re-3.jar

zip re-3.zip re-3.jar
