import arxiv
import pandas as pd


big_slow_client = arxiv.Client(
  page_size = 1000,
  delay_seconds = 10.0,
  num_retries = 5
)

search_ASD = arxiv.Search(
  query = "ASD",
  max_results = 3000000,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

results_ASD = list(big_slow_client.results(search_ASD))

search_autism = arxiv.Search(
  query = "autism",
  max_results = 3000000,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

result_autism = list(big_slow_client.results(search_autism))

# Combine results without duplicates based on both title and entry_id
combined_results = {}

for r in results_ASD:
  combined_results[(r.title, r.entry_id)] = r

for r in result_autism:
  combined_results[(r.title, r.entry_id)] = r

# Extract titles and entry_ids from the combined results
target_titles = []
target_entry_ids = []

for key, value in combined_results.items():
  target_titles.append(key[0])
  target_entry_ids.append(key[1])

# Export to CSV
df = pd.DataFrame({
  'Title': target_titles,
  'Entry_ID': target_entry_ids
})
df.to_csv('target_titles.csv', index=False)
