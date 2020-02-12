import connexion
import six


from swagger_server.models.train_data import TrainData  # noqa: E501
from swagger_server.models.train_started_success import TrainStartedSuccess  # noqa: E501



def train_post(trainData):  # noqa: E501
    """Trains a new model

     # noqa: E501

    :param trainData: Neural network training parameters and training data description
    :type trainData: dict | bytes

    :rtype: TrainStartedSuccess
    """
    if connexion.request.is_json:
        trainData = TrainData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
