(defn parse-float [s]
   (Float. (re-find  #"\d+" s )))

(def r (read-string (read-line)))

(println (format "A=%.4f" (* 3.14159 (* r r))))