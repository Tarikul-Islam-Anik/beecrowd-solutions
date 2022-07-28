a = IO.gets("") |> String.trim |> String.to_float
b = IO.gets("") |> String.trim |> String.to_float
m = (a * 3.5 + b * 7.5) / 11 |> :erlang.float_to_binary([decimals: 5])
IO.puts "MEDIA = #{m}"
