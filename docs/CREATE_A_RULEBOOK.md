# How to create a rulebook

## minimal setup

### add minimal required file structure

1) Create a folder under `<root>/resources/rulebook/` with the name/identifier of the rulebook
2) Within that create all required files:
  * `_entrypoint.lp` : is the only file which gets loaded directly by the engine
  * `meta.lp` : shall include information about the rulebook like its usability and known feature (values)
  * `rules.lp` : shall contain the actual rules

### fulfill minimum logic program requirements

* `meta.lp`
  * add `#program rulebook_usable.`
    * having the fact `rulebook("<name>").` where `<name>` is the same as the rulebook folder name
* `_entrypoint.lp`
  * add `#include "<file>".` for `meta.lp` and `rules.lp`

### general requirements

* each pre-defined `#program` (`rulebook_usable`,`meta`,`world_facts`,`hero_facts`) that is used must define itself as a
  fact `program("<name>").` for rulebook validation

## general explanations and recommendations

See `CHEATSHEET.lp` for a quick introduction and overview into clingo language of logic programs.

Most functions (like 'requires') have two parameters (X,Y) and can be read as "X requires Y", so that the function name is
inbetween. An e.g. can be `requires(culture("Auelfen"),species("Elfen")).` which means that "culture of 'Auelfen' requires species
to be 'Elfen'".
It is recommended to follow the approach of having the 'causing' feature which defines the rule to be the first parameter. It
allows better backtracking of the rule to the actual rule within the actual published rulebook.

Following programs are known/designed/pre-defined by the engine:

* `#program rulebook_usable.` :
  * can declare a dependency on another rulebook with `rulebook_depends("<this>", "<other>").`
* `#program meta.` :
  * can declare an extra hero validation step which gets executed at correct position by number
    with `extra_hero_validation_step(<number>).`. Having such ofcourse requires the actual `#program validate_hero_step_<number>.`
* `#program world_facts.` :
  * shall contain ALL facts AND rules of the rulebook.
  * It is recommended to have this program in `meta.lp` for the `known_<feature>(<values>).` facts and in `rules.lp` for the
    rules, like `requires(<X>,<Y>).`
* `#program hero_facts.` :
  * here are facts of an actual hero (context) generated
  * whenever a rulebook adds a new hero feature also programmatic changes at the hero model and schema must be done. These must be
    optionally then.

## pre-defined common...

...hero validation steps (actually programs):

* `validate_hero_step_50`: general pre-check: e.g. checks that experience level is known
* `validate_hero_step_100`: check species usable
* `validate_hero_step_150`: check species requirements
* `validate_hero_step_200`: check culture usable
* `validate_hero_step_250`: check culture requirements
* `validate_hero_step_300`: check profession usable
* `validate_hero_step_350`: check profession requirements
* `validate_hero_step_400`: check (dis)advantages usable
* `validate_hero_step_450`: check (dis)advantages requirements
* `validate_hero_step_500`: check skills (talents, combat techniques) usable
* `validate_hero_step_550`: check skills (talents, combat techniques) requirements

...world known feature facts:

* `known_experience_level("<name>",<CC>,<S>,<CT>,<CCP>,<SL>,<FS>).` : with CC := max characteristic lvl, S := max skill lvl, CT :=
  max combat technique lvl, CCP := max characteristic points, SL := max spells and liturgies, FS := max foreign spell
  for 'Inexperienced', 'Average', 'Experienced', 'Competent', 'Masterful', 'Brilliant', 'Legendary'

...hero feature facts:

* `experience_level("<name>").`
* `species("<name>").`
* `culture("<name>").`
* `profession("<name>").`
* `talent("<name>",<level>).`
* `combat_technique("<name>",<level>).`
* `advantage("<name>","<refers>",<level>).`
* `disadvantage("<name>","<refers>",<level>).`

...functions that produces an error if exists:

* `rulebook_missing("<causingRulebook>","<missingRulebook>").` : whenever a used rulebooks missing a rulebook it depends on
* `unknown(<feature>(<parameters>)).` : whenever a common hero feature with given parameters is not defined
  as `known_<feature>(<parameters>)`
* `unusable_by(<causingFeature>("<name>"),<referredFeature>("<name>")).` : whenever a common hero feature does not allow another
  feature (which has no level) to be present (whitelist)
* `missing_level(<causingFeature>("<name>"),<referredFeature>("<name>",<minLevel>)).` : whenever a common hero feature requires
  another feature on a minimum level
  * whenever a selection of referred feature values must have a minimum level the corresponding `"<name>"` is replaced
    with `any_of(<choices>,<selectionTupleOfNames>)`.
* `max_lvl_exceeded(<referredFeature>("<name>",<level>),<maxLevel>).` : whenever a feature exceeds the maximum level caused by
  heros experience level

...functions that produces a warning if exists:

* `missing_usual(<causingFeature>("<name>"),<referredFeature>("<name>")).` : whenever a feature is missing another feature that
  shall be usually present
* `missing_typical(<causingFeature>("<name>"),<referredFeature>("<name>","<refers>",<level>)).` : whenever a feature is missing
  another typical feature on a minimum level
* `atypical(<causingFeature>("<name>"),<referredFeature>("<name>","<refers>")).` : whenever a feature found another atypical
  feature (of any level)

## common functions to use in custom rulebooks (besides above)

World known features:

* `known_species("<name>").`
* `known_culture("<name>").`
* `known_profession("<name>").`
* `known_advantage("<name>","<refers>",<level>).` : with <refers> being optionally (can be empty)
* `known_disadvantage("<name>","<refers>",<level>).` : with <refers> being optionally (can be empty)
* `known_talent("<name>").`
* `known_combat_technique("<name>").`

Formal rules (functions) that triggers pre-defined rules producing above pre-defined...

* ...errors:
  * `unusable_by` if `requires(<causingFeature>("<name>"),<referredFeature>("<name>")).`
  * `missing_level` if `requires(<causingFeature>("<name>"),<referredFeature>("<name>",<minLevel>)).`
  * `missing_level` with `any_of`
    if `requires(<causingFeature>("<name>"),any_of(<choices>,<referredFeature>,<selectionTupleOfNames>,<minLevel>)).`
  * `missing_level` if `requires(<causingFeature>("<name>"),<referredFeature>("<name>","<refers>",<minLevel>)).`
* ...warnings:
  * `missing_usual` if `has_usual(<causingFeature>("<name>"),<referredFeature>("<name>")).`
  * `missing_typical` if `has_typical(<causingFeature>("<name>"),<referredFeature>("<name>","<refers>",<minLevel>)).`
  * `atypical` if `has_atypical(<causingFeature>("<name>"),<referredFeature>("<name>","<refers>",<minLevel>)).`

## examples how to add a new profession using a new talent

This rulebook (expansion) depends on the base rulebook 'dsa5' to work.

1) make profession 'Fischer' and talent 'Angelwissen' known:
  * in `meta.lp` at program `world_facts` add
    * `known_profession("Fischer").`
    * `known_talent("Angelwissen").`
2) define the rules (validation errors) for this profession, using the new talent:
  * in `rules.lp` at program `world_facts` add
    * Only allow specific species for this profession: `requires(profession("Fischer"),culture("Elfen";"Halbelfen";"Mensch")).`
    * Require a talents on a minimum level: `requires(profession("Fischer"),talent("Körperbeherrschung",4;"Angelwissen",6)).`
    * Require two talents out of three on a minimum level of
      four: `requires(profession("Fischer"),any_of(2,talent,("Wildnisleben","Selbstbeherrschung","Schwimmen"),4)).`
3) define soft-rules (validation warnings) for this profession
  * Usually used with specific cultures: `has_usual(profession("Fischer"),culture("Auelfen";"Waldelfen";"Aranier";"Novadis")).`
  * Typically, has an advantage: `has_typical(profession("Fischer"),advantage("Richtungssinn","",2)).`
  * Some disadvantages are
    atypical: `has_atypical(profession("Fischer"),disadvantage("Krankheitsanfällig","",1;"Kälteempfindlich","",1)).`
