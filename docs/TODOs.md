[//]: # (TODO work on those TODOs)

# TODOs

* App related
    * May dockerize this app, see exmaple https://github.com/tiangolo/full-stack-fastapi-postgresql
    * Use Keycloak (https://www.keycloak.org/) running in a Docker for IAM (Identity and Authorization Management): Enables users
    * [CONCEPT BRANCH] Enable storing heros per users in a database (PostgreSQL in a Docker)
    * Use Nimoy (https://github.com/browncoat-ninjas/nimoy), a test framework inspired by Spock for
      Java (https://spockframework.org/)
      , or pytest plugin spock (https://github.com/zen-xu/spock)


* Rulebook related
    * Add rule that rulebooks can declare incompatibility to others
    * Add handling of optional rules
    * [CONCEPT BRANCH] Make 'any_of' usable as replacement of an actual value (string) in formal rule definition
    * DisAdvantages should/must refer concrete features not simple strings, so we can do further checks on having them


* API related
    * Add an import and export endpoint, may use a format already supported by other tools
    * Add hero endpoint that gives possible values for a requested feature of an uncompleted hero
        * Decide how to handle non-filled hero features (like supporting pre-checks, were only a species and culture has been
          selected)
    * Give hints which hero feature values are usable considering given hero and rulebooks, instead of simple feedback of unusable
      feature value due to 'higher' (in sense of more general) hero feature. Including for warnings, like atypical (hint which
      would
      be typical)


* Hero related
    * Add spells to hero features
    * Add liturgies to hero features
    * Add special talents to hero features
    * Give hero an 'sex' attribute, since it could be used as a requirement (see https://ulisses-regelwiki.de/pro_mawdli.html
      and https://ulisses-regelwiki.de/ZB_Derwisch.html)