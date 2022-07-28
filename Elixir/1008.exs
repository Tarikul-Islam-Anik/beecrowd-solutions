num = IO.gets("") |> String.trim() |> String.to_integer()
hours = IO.gets("") |> String.trim() |> String.to_integer()
percent = IO.gets("") |> String.trim() |> String.to_float()

IO.puts("NUMBER = #{num}")
IO.puts("SALARY = U$ #{(hours * percent) |> :erlang.float_to_binary(decimals: 2)}")
