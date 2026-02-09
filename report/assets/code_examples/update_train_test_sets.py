def update_train_test_sets(id_num, batch_size=64):
    """Updates the training and testing sets, and returns the name of the
    dataset.

    :param id_num: The ID number of the dataset
    :param batch_size: The batch size
    """
    batch_size = batch_size
    selected_dataset = selected_dataset_list[id_num]
    SEQ_PATH =  Path.home() / ".genomic_benchmarks" / selected_dataset

    classes = [
        x.stem for x
        in (SEQ_PATH/"train").iterdir()
        if x.is_dir()
    ]
    num_classes = len(classes)

    train_set = tf.keras.preprocessing.text_dataset_from_directory(
        SEQ_PATH / "train",
        batch_size=batch_size,
        class_names=classes,
        shuffle=True,
        seed=SEED,
    )

    test_set = tf.keras.preprocessing.text_dataset_from_directory(
        SEQ_PATH / "test",
        batch_size=batch_size,
        class_names=classes,
    )

    if num_classes > 2:
        train_set = train_set.map(
            lambda x, y: (x, tf.one_hot(y, depth=num_classes)))

    if num_classes > 2:
        test_set = test_set.map(
            lambda x, y: (x, tf.one_hot(y, depth=num_classes)))

    vectorize_layer.adapt(train_set.map(lambda x, y: x))
    vocab_size = len(vectorize_layer.get_vocabulary())
    vectorize_layer.get_vocabulary()

    train_ds = train_set.map(vectorize_text)
    test_ds = test_set.map(vectorize_text)

    return selected_dataset
