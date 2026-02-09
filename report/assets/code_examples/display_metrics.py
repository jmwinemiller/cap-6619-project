def plot_metrics(model_info_dict, set_name, horizontal=False):
    """Shows the plots for the training accuracy, f1 score, and loss.
    Then shows the scores for the model.

    :param model_info_dict: Dictionary of model information
    :param set_name: Name of dataset
    :param horizontal: Whether to show the plots horizontally
    """
    b_hist = model_info_dict["basic_history"]
    acc_1 = np.array(b_hist.history["binary_accuracy"])
    f1_1 = np.array(b_hist.history["f1_score"])
    loss_1 = np.array(b_hist.history["loss"])

    f_hist = model_info_dict["final_history"]
    acc_2 = np.array(f_hist.history["binary_accuracy"])
    f1_2 = np.array(f_hist.history["f1_score"])
    loss_2 = np.array(f_hist.history["loss"])

    # Shifted the starting index to start at 1 instead of 0
    epochs = np.arange(loss_1.shape[0]) + 1

    fig_size = (15, 5) if horizontal else (5, 15)
    plt.figure(figsize=fig_size)
    models = [model_info_dict["basic_name"], model_info_dict["final_name"]]

    rows = 1 if horizontal else 3
    cols = 3 if horizontal else 1

    plt.subplot(rows, cols, 1)
    plt.plot(epochs, acc_1, epochs, acc_2)
    plt.title("Training Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.legend(models, loc="lower right")

    plt.subplot(rows, cols, 2)
    plt.plot(epochs, f1_1, epochs, f1_2, linestyle="--")
    plt.title("Training F1 Score")
    plt.xlabel("Epochs")
    plt.ylabel
    plt.legend(models, loc="lower right")

    plt.subplot(rows, cols, 3)
    plt.plot(epochs, loss_1, epochs, loss_2)
    plt.title("Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Crossentropy Loss")
    plt.legend(models, loc="upper right")

    plt.show()

    for m in models:
        eval = model_info_dict[f"{m}_evaluation"]
        print(f"{m.title()} Model for Set: {set_name}:")
        print(f"Total Loss: {round(eval['loss'], 6)}")
        print(f"Accuracy: {round(eval['binary_accuracy'] * 100, 2)}%")
        print(f"F1 Score: {round(eval['f1_score'], 2)}")
        print()
