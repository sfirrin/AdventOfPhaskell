import System.IO
import Text.Regex.Posix
import Data.List
import Data.Char

pattern = "([a-z-]+)([0-9]+)\\[([a-z]+)\\]"

fourthTup :: (String, String, String, [String]) -> [String]
fourthTup (_,_,_,xs) = xs

splitData :: String -> [String]
splitData dat = fourthTup matches
    where matches = dat =~ pattern :: (String,String,String,[String])

getCorrect :: String -> String
getCorrect inp = take 5 (map snd (concat sortedTups))
    where sortedTups = map sort $ groupBy (\x y -> (fst x) == (fst y)) freqCharTups
          freqCharTups = reverse . sort $ map (\x -> (length x, head x)) grouped
          grouped = group $ sort noDashes
          noDashes = [i | i <- inp, i /= '-']

translateChar :: Int -> Char -> Char
translateChar _ '-' = ' '
translateChar change c = chr newValue
    where origValue = (ord c) - 97
          newValue = ((origValue + change) `mod` 26) + 97

translate :: [String] -> (String, Int)
translate (str:change:_) = (map (translateChar changeVal) str, changeVal)
    where changeVal = read change :: Int


main = do
    handle <- openFile "in04.txt" ReadMode
    rawInput <- hGetContents handle
    let splitRooms = map splitData $ lines rawInput
        validRooms = [room | room <- splitRooms, getCorrect (room !! 0) == room !! 2]
        translatedRooms = map translate validRooms
    putStrLn "The part 1 answer is:"
    print $ foldl (\acc room -> acc + (read (room !! 1) :: Int)) 0 validRooms
    putStrLn "Part 2:"
    print $ [room | room <- translatedRooms, "northpole" `isInfixOf` (fst room)]
