(defn parse-int [s]
   (Integer. (re-find  #"\d+" s )))

(def a (read-string (read-line)))
(def b (read-string (read-line)))
(println "X =" (+ a b))
