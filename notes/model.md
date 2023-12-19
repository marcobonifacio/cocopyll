# Model #

## Contracts ##
* **zero**: no rights, no obligations, infinite horizon
* **one**: immediately pays the holder one unit of currency k, infinite horizon
* **give**: swaps rights and obligations of a contract
* **and**: acquires both contracts, expires when both expire
* **or**: acquires either one of the contracts, not both, expires when both expire
* **cond**: acquires the first contract if an observable is true at acquisition date or the second if the observable is false
* **scale**: acquires a contract with rights and obligations multiplied by value of an observable
* **when**: acquires an obligation to acquire a contract as soon as an observable becomes true
* **anytime**: acquires an opportunity to acquire a contract at any time an observable is true
* **until**: acquires an obligation to drop a contract as soon as an observable becomes true

## Observables ##
* **konst**: observable with the same value anytime
* **lift**: observable resulting from application of function f to an observable
* **lift2**: observable resulting from application of function f to a pair of observables
* **date**: observable returning a date