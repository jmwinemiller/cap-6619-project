def create_final_cnn_model(num_classes, vocab_size):
    """Returns a CNN model and model name.

    :param num_classes: The number of classes to classify
    :param vocab_size: The size of the vocabulary
    :return: Model name and CNN model
    """
    name = "final"

    if num_classes == 2:
        last_layer = Dense(1, activation="sigmoid")
        loss = BinaryCrossentropy(from_logits=True)
        acc = BinaryAccuracy(threshold=0.5)
    else:
        last_layer = Dense(num_classes, activation="softmax")
        loss = "categorical_crossentropy"
        acc = CategoricalAccuracy()

    onehot_layer = Lambda(
        lambda x: tf.one_hot(tf.cast(x, "int64"), depth=vocab_size))

    model = Sequential(
        [
            onehot_layer,

            Conv1D(
                filters=16,
                kernel_size=8,
                data_format="channels_last",
            ),
            BatchNormalization(),
            Activation("relu"),
            MaxPooling1D(),

            Conv1D(
                filters=8,
                kernel_size=8,
                data_format="channels_last",
                activation="relu",
            ),
            BatchNormalization(),
            MaxPooling1D(),

            Conv1D(
                filters=4,
                kernel_size=8,
                data_format="channels_last",
                activation="relu",
            ),
            BatchNormalization(),
            MaxPooling1D(),

            GlobalAveragePooling1D(),
            Flatten(),
            Dense(units=512, activation="relu"),
            last_layer,
        ]
    )

    model.compile(
        optimizer="adam",
        loss=loss,
        metrics=[acc, f1_score],
    )

    return name, model
