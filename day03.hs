import System.IO
import Data.List

groupNumbers :: String -> [String]
groupNumbers = groupBy (\x y -> (x /= ' ') && (y /= ' '))

removeSpaces :: [String] -> [String]
removeSpaces inp = [item | item <- inp, item /= " "]

intList :: [String] -> [Int]
intList xs = [read x :: Int | x <- xs]

cleanInput :: [String] -> [[Int]]
cleanInput = map (intList . removeSpaces . groupNumbers)

triples :: [[Int]] -> [[[Int]]]
triples [] = []
triples xs = take 3 xs : (triples $ drop 3 xs)

getFromTrip :: Int -> [[Int]] -> [Int]
getFromTrip i (a:b:c:_) = [a !! i, b !! i, c !! i]

reorganizeTrip :: [[Int]] -> [[Int]]
reorganizeTrip trip = [getFromTrip i trip | i <- [0..2]]

getNumberValid :: [[Int]] -> Int
getNumberValid allDims = length [dims | dims <- allDims, (sum $ init dims) > last dims]

main = do
    handle <- openFile "in03.txt" ReadMode
    contents <- hGetContents handle
    let cleanedInput = cleanInput $ lines contents
        sortedInput = map sort cleanedInput
        trips = triples cleanedInput
        -- vertical = foldl (\acc x -> acc ++ (reorganizeTrip x)) trips
        vertical = map sort $ concat $ map reorganizeTrip trips
    putStrLn "The answer to part 1 is:"
    -- print $ length [dims | dims <- sortedInput, (sum $ init dims) > last dims]
    print $ getNumberValid sortedInput
    putStrLn "Part 2 is:"
    print $ getNumberValid vertical
    hClose handle
