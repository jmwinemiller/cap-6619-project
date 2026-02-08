def f1_score(y_true, y_pred):
    """Returns the F1 score.

    :param y_true: The true labels
    :param y_pred: The predicted labels
    :return: The F1 score
    """
    def precision(y_true, y_pred):
        """Returns the precision.

        :param y_true: The true labels
        :param y_pred: The predicted labels
        :return: The precision
        """
        true_positives = ops.sum(
            ops.round(ops.clip(tf.cast(y_true, tf.float32) * y_pred, 0, 1)))
        predicted_positives = ops.sum(ops.round(ops.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision

    def recall(y_true, y_pred):
        """Returns the recall.

        :param y_true: The true labels
        :param y_pred: The predicted labels
        :return: The recall
        """
        true_positives = ops.sum(
            ops.round(ops.clip(tf.cast(y_true, tf.float32) * y_pred, 0, 1)))
        possible_positives = tf.cast(
            ops.sum(ops.round(ops.clip(y_true, 0, 1))), tf.float32)
        recall = (
            tf.cast(true_positives, tf.float32)
            / (possible_positives + K.epsilon())
        )
        return recall

    precision = precision(y_true, y_pred)
    recall = recall(y_true, y_pred)
    return 2 * ((precision * recall) / (precision + recall + K.epsilon()))
