# Copyright 2015 Netflix. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from distutils.core import setup
setup(
  name = 'peeringdb',
  packages = ['peeringdb'], # this must be the same as the name above
  version = '0.3',
  description = 'PeeringDB API Python library',
  author = 'Nat Morris',
  author_email = 'nat@netflix.com',
  url = 'https://github.com/netflix/peeringdb-py',
  download_url = 'https://github.com/netflix/peeringdb-py/tarball/master',
  keywords = ['peering', 'peeringdb', 'bgp'],
  license = 'Apache 2.0',
  classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Telecommunications Industry',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 2.7',
    'Topic :: Database :: Front-Ends',
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: System :: Networking'
  ],
)
