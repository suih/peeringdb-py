# peeringdb-py

A [PeeringDB](https://beta.peeringdb.com/docs/) 2.0 API client Python library. Making use of the new [REST API](https://beta.peeringdb.com/docs/api_specs/).

## Caching

This library can optionally use Redis to improve the performance of your application, responses from the PeeringDB API by default are cached for 15 minutes.

## Installation

To install peeringdb-py, simply:

```
$ sudo pip install peeringdb
```

## Getting started

```
import peeringdb
pdb = peeringdb.PeeringDB()
print pdb.asn(2906)
```

Find common IX locations:

```
import peeringdb
pdb = peeringdb.PeeringDB()
print pdb.matching_ixlan([2906, 5089])
```

## Contributing

 1. Fork the repo on GitHub
 2. Commit changes to a branch in your fork
 3. Pull request "upstream" with your changes
 4. Merge changes in to "upstream" repo

## License

Apache 2.0

## Author

nat@netflix.com