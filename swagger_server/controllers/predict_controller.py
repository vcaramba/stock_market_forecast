import connexion
import six


from swagger_server.models.data_to_predict import DataToPredict  # noqa: E501
from swagger_server.models.predict_response import PredictResponse  # noqa: E501

def predict(data_to_predict):  # noqa: E501
    """Predict value

     # noqa: E501

    :param data_to_predict: List of texts to perform prediction on
    :type data_to_predict: dict | bytes

    :rtype: List[PredictResponse]
    """
    if connexion.request.is_json:
        data_to_predict = DataToPredict.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
