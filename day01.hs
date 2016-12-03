import System.IO
import Data.Char
import Data.List
import qualified Data.Set as Set

-- Direction is encoded as an integer, 0 being up, 1 being right, etc.
data Block = Block {x :: Int, y :: Int, direction :: Int} deriving (Ord, Show)
instance Eq Block where
    a == b = ((x a) == (x b)) && ((y a) == (y b))

splitIntoInstrs :: String -> [String]
splitIntoInstrs inp = groupBy (\x y -> (isDigit x) && (isDigit y)) inp

removeUnnecessary :: [String] -> [String]
removeUnnecessary inp = [item | item <- inp, item /= ",", item /= " "]


groupPairs :: [String] -> [[String]]
groupPairs [] = []
groupPairs xs = (take 2 xs) : (groupPairs (drop 2 xs))

getTuple :: [String] -> (String, Int)
getTuple (instr:distance:_) = (instr, read distance :: Int)

getDirection :: Int -> String -> Int
getDirection current turn
    | current == 3 && turn == "R" = 0
    | current == 0 && turn == "L" = 3
    | turn == "R" = current + 1
    | turn == "L" = current - 1


getNewBlock :: Block -> (String, Int) -> Block
getNewBlock b (turn,distance)
    | newdir == 0 = Block (x b) ((y b) + distance) newdir
    | newdir == 1 = Block ((x b) + distance) (y b) newdir
    | newdir == 2 = Block (x b) ((y b) - distance) newdir
    | newdir == 3 = Block ((x b) - distance) (y b) newdir
    where newdir = getDirection (direction b) turn

getInBetween :: Block -> Block -> [Block]
-- b is the block we're moving to, a is the one we start at
getInBetween a b
    | a == b = []
    | (x a) > (x b) = b : (getInBetween a (Block ((x b) + 1) (y a) 0))
    | (x a) < (x b) = b : (getInBetween a (Block ((x b) - 1) (y a) 0))
    | (y a) > (y b) = b : (getInBetween a (Block (x a) ((y b) + 1) 0))
    | (y a) < (y b) = b : (getInBetween a (Block (x a) ((y b) - 1) 0))

findFirstRepeat :: [Block] -> [Block] -> Block
findFirstRepeat seen (x:y:rem) = if not $ null inter then (inter !! 0) else (findFirstRepeat (seen ++ between) (y : rem))
    where between = getInBetween x y
          inter = intersect between seen

main = do
    handle <- openFile "in01.txt" ReadMode
    contents <- hGetContents handle
    let cleanedInput = groupPairs $ removeUnnecessary $ splitIntoInstrs contents
        instrTuples = map getTuple cleanedInput
        allStops = scanl getNewBlock (Block 0 0 0) instrTuples
        finalBlock = last allStops
        firstRepeat = findFirstRepeat [] allStops
    putStrLn "The part 1 answer is:"
    print (x finalBlock + y finalBlock)
    putStrLn "The part 2 answer is:"
    print (x firstRepeat + y firstRepeat)
