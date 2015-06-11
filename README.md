# peeringdb-py

A [PeeringDB](https://beta.peeringdb.com/docs/) 2.0 API client Python library. Making use of the new [REST API](https://beta.peeringdb.com/docs/api_specs/).

## Installation

To install peeringdb-py, simply:

```
$ sudo pip install peeringdb
```

## Getting started

```python
>>> import peeringdb
>>> pdb = peeringdb.PeeringDB()
>>> print pdb.asn(2906)
```

Find common IX locations:

```python
>>> import peeringdb
>>> pdb = peeringdb.PeeringDB()
>>> print pdb.matching_ixlan([2906, 5089])
```

## Caching

This library can optionally use Redis to improve the performance of your application, responses from the PeeringDB API by default are cached for 15 minutes.

By default the library will use the Redis running on localhost:6379, this can be easily disabled:

```python
>>> import peeringdb
>>> pdb = peeringdb.PeeringDB(cache=False)
```

Or a different host and port specificed:

```python
>>> import peeringdb
>>> pdb = peeringdb.PeeringDB(cache_host=mycache.bigisp.org, cache_port=6800)
```

## Contributing

 1. Fork the repo on GitHub
 2. Commit changes to a branch in your fork
 3. Pull request "upstream" with your changes
 4. Merge changes in to "upstream" repo

## License

Copyright 2015 Netflix, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
