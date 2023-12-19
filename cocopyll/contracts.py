from datetime import date
from enum import Enum

from .observables import BoolObservable, FloatObservable

class Contract:
    pass

class Zero(Contract):
    pass

class One(Contract):
    currency: Enum

class Give(Contract):
    contract: Contract

class And(Contract):
    contract1: Contract
    contract2: Contract

class Or(Contract):
    contract1: Contract
    contract2: Contract

class Cond(Contract):
    obs: BoolObservable
    contract1: Contract
    contract2: Contract

class Scale(Contract):
    obs: FloatObservable
    contract: Contract

class When(Contract):
    obs: BoolObservable
    contract: Contract

class Anytime(Contract):
    obs: BoolObservable
    contract: Contract

class Until(Contract):
    obs: BoolObservable
    contract: Contract
