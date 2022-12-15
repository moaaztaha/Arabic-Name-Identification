import matplotlib.pyplot as plt

def plot_loss(history: dict, plot:bool = True):
    """
    Plot validation and training losses across epochs.
    """
    loss = history['loss']
    val_loss = history['val_loss']
    epochs = range(1, len(loss) + 1)
    
    # "bo" is for "blue dot"
    plt.plot(epochs, loss, 'bo', label='Training loss')
    # r is for "solid red line"
    plt.plot(epochs, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    if plot:
        plt.show()

def plot_accuracy(history: dict, plot: bool = True):
    """
    Plot training and validation accuracies across epochs.
    """
    acc = history['binary_accuracy']
    val_acc = history['val_binary_accuracy']
    epochs = range(1, len(acc) + 1)

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'r', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend(loc='lower right')

    if plot:
        plt.show()

def plot_history(history:dict):
    """
    Plot training and validation losses and accuracies across epochs.
    """
    fig = plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)
    plot_loss(history, plot=False)
    plt.subplot(1, 2, 2)
    plot_accuracy(history, plot=False)