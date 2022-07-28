a = IO.gets("") |> String.trim |> String.to_float
b = IO.gets("") |> String.trim |> String.to_float
c = IO.gets("") |> String.trim |> String.to_float
m = (a * 2 + b * 3 + c * 5) / 10 |> :erlang.float_to_binary([decimals: 1])
IO.puts "MEDIA = #{m}"
