if (!dir.exists("../data/processed")) {
  dir.create("../data/processed",recursive = TRUE)
}

st |> write.csv("../data/processed/st.csv")
write.csv(st, paste0("../data/processed", "/st.csv"))

write.csv(st, "a.csv")