[//]: # (TODO work on those TODOs)

# TODOs

* Use Nimoy (https://github.com/browncoat-ninjas/nimoy), a test framework inspired by Spock for Java (https://spockframework.org/)
  , or pytest plugin spock (https://github.com/zen-xu/spock)
* Give hints which hero feature values are usable considering given hero and rulebooks, instead of simple feedback of unusable
  feature value due to 'higher' (in sense of more general) hero feature. Including for warnings, like atypical (hint which would
  be typical)
* Give hero an 'sex' attribute, since it could be used as a requirement (see https://ulisses-regelwiki.de/pro_mawdli.html
  and https://ulisses-regelwiki.de/ZB_Derwisch.html)
* Add user management, supporting web sessions and storing heros in a database
* Add an import and export endpoint, may use a format already supported by other tools
* Add species 'Halbelfen' from dsa5 base rulebook.
* Add handling of optional rules
* Decide how to handle non-filled hero features (like supporting pre-checks, were only a species and culture has been selected)
* May dockerize this app, see exmaple https://github.com/tiangolo/full-stack-fastapi-postgresql
