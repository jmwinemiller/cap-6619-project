selected_dataset_list = [
    "dummy_mouse_enhancers_ensembl",
    "drosophila_enhancers_stark",
    "human_enhancers_cohn",
    "human_nontata_promoters",
]

for dataset in selected_dataset_list:
    if not is_downloaded(dataset):
        download_dataset(dataset)
    print(info(dataset, description=True))
    print("\n")
