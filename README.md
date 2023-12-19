# cocopyll #

`cocopyll` è un ironico tentativo di implementazione in Python di un Domain Specific Language (DSL) applicato ai contratti finanziari, ispirato da *Composing contracts: an adventure in financial engineering*, un paper di Simon Peyton Jones (SPJ), Jean-Marc Eber e Julian Seward, presentato all'International Conference of Functional Programming (ICFP) nel settembre 2000.

Il modello di SPJ *et al.* era basato sulla programmazione funzionale e il primo tentativo di implementazione è stato effettuato in Haskell da Anton van Staten ([qui](https://web.archive.org/web/20130814194431/http://contracts.scheming.org) la pagina originale e [qui](https://github.com/cmahon/composing-contracts) una ricostruzione del codice); successivamente, il modello è stato utilizzato nell'ambito della progettazione e della valutazione di [*smart contracts*](https://it.wikipedia.org/wiki/Smart_contract).

Su Github si trovano numerosi tentativi di implementazione del modello, per lo più scritti in linguaggi di programmazione funzionale, tra i più interessanti si possono citare:
* https://github.com/falconair/ComposingContracts, scritto in Scala, è descritto nella sua implementazione in un [post](http://falconair.github.io/2015/01/30/composingcontracts.html) sul blog dell'autore;
* https://github.com/cmahon/composing-contracts, il citato codice di van Staten ricostruito;
* https://github.com/luphord/monte-carlo-contracts, un'implementazione in Python, limitata alla simulazione Monte Carlo per la valutazione dei contratti;
* https://github.com/trvrmcs/composing_contracts, un'altra implementazione in Python, con concetti di programmazione funzionale;
* https://github.com/JuliaActuary/FinanceModels.jl, una libreria in Julia che sembra largamente ispirata ai concetti di SPJ;

e altri.

