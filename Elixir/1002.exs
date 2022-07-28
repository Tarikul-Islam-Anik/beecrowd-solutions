r = IO.gets("") |> String.trim() |> String.to_float()
area = (3.14159 * r * r) |> :erlang.float_to_binary([decimals: 4])
IO.puts("A=#{area}")
