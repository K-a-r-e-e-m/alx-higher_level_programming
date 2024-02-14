#!/usr/bin/node

/* fs --> File System module */
const fileSys = require('fs');

// Read a file and run it ./fileA ./fileB ./Filec
const fileA = fileSys.readFileSync('./' + process.argv[2]);
const fileB = fileSys.readFileSync('./' + process.argv[3]);
fileSys.writeFileSync('./' + process.argv[4], fileA + fileB, 'utf-8');
//      writeFileSync(^^^^^^^^^^File^^^^^^^^, ^^^^Data^^^^^,  option);
