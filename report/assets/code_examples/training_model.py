def train_and_evaluate_models(set_name, epochs):
    """Returns the training and evaluation the metrics for the models.

    :param set_name: Name of dataset
    :param epochs: Number of epochs to train
    :return: Dictionary of model information
    """
    model_info =  {
        "basic_name": None,
        "basic_history": None,
        "basic_evaluation": None,
        "final_name": None,
        "final_history": None,
        "final_evaluation": None,
    }

    print(f"Training Models for: {set_name}")
    basic_name, basic_model = create_basic_cnn_model(num_classes, vocab_size)
    model_info["basic_name"] = basic_name
    basic_history = basic_model.fit(
        train_ds,
        epochs=epochs,
        verbose=0,
    )
    model_info["basic_history"] = basic_history
    model_info["basic_evaluation"] = basic_model.evaluate(
        test_ds, verbose=0, return_dict=True)

    final_name, final_model = create_final_cnn_model(num_classes, vocab_size)
    model_info["final_name"] = final_name
    final_history = final_model.fit(
        train_ds,
        epochs=epochs,
        verbose=0,
    )
    model_info["final_history"] = final_history
    model_info["final_evaluation"] = final_model.evaluate(
        test_ds, verbose=0, return_dict=True)

    return model_info
