import System.IO


numPad = ["123",
          "456",
          "789"]

weirdPad = ["  1  ",
            " 234 ",
            "56789",
            " ABC ",
            "  D  "]

getNextButton :: [String] -> (Int, Int) -> Char -> (Int, Int)
getNextButton pad (x,y) instr
    | instr == 'L' = validateCoords pad (x, y) (max 0 (x-1), y)
    | instr == 'R' = validateCoords pad (x, y) (min limit (x+1), y)
    | instr == 'U' = validateCoords pad (x, y) (x, max 0 (y-1))
    | instr == 'D' = validateCoords pad (x, y) (x, min limit (y+1))
    where limit = (length pad) - 1

validateCoords :: [String] -> (Int, Int) -> (Int, Int) -> (Int, Int)
validateCoords pad oldc newc = if getCharAt pad newc == ' '
                               then oldc
                               else newc

getFinalKey :: [String] -> (Int, Int) -> String -> Char
getFinalKey pad start instrs = getCharAt pad $ foldl (\acc x -> getNextButton pad acc x) start instrs

getCharAt :: [String] -> (Int, Int) -> Char
getCharAt pad (x,y) = (pad !! y) !! x

main = do
    handle <- openFile "in02.txt" ReadMode
    contents <- hGetContents handle
    let allLines = lines contents
    putStrLn "The answer to part 1 is:"
    print $ map (getFinalKey numPad (1, 1)) allLines
    putStrLn "The answer to part 2 is:"
    print $ map (getFinalKey weirdPad (0, 2)) allLines
