# Basic data types #
data Currency = USD | GBP | EUR | ZAR | KYD | CHF deriving (Eq, Show)
type Date = (CalendarType, TimeStep)
type TimeStep = int
type CalendarType = ()
mkDate :: TimeStep -> Date  mkDate s = ((), s)
time0 :: Date   time0 = mkDate 0

# Contract implementation #
data Contract = 
    Zero |
    One Currency |
    Give Contract |
    And Contract Contract |
    Or Contract Contract |
    Cond Obs(Bool) Contract Contract |
    Scale Obs(Double) Contract |
    When Obs(Bool) Contract |
    Anytime Obs(Bool) Contract |
    Until Obs(Bool) Contract
deriving Show

# Observable data type #
newtype Obs a = Obs(Date -> PR a)
instance Show a => Show(Obs a) where
    show(Obs o) = let (PR (rv:_ )) = o time0 in "(Obs " ++ show rv ++ ")"

# Primitives for deriving contracts #




