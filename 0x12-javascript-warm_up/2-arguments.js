!#/usr/bin/node
const { argv } = require('node:process');

if(argv[2] !== NULL)
{
  console.log('No argument');
}
else
{
  console.log('Argument found');
}
