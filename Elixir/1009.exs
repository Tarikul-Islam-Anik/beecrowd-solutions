person_name = IO.gets("")
salary = IO.gets("") |> String.trim() |> String.to_float()
sales = IO.gets("") |> String.trim() |> String.to_float()

if sales > 0.0 do
  IO.puts("TOTAL = R$ #{(salary + (sales * 0.15)) |> :erlang.float_to_binary(decimals: 2)}")
else
  IO.puts("TOTAL = R$ #{salary |> :erlang.float_to_binary(decimals: 2)}")
end
