def cerify_http_code(response_data, expected_data):

    assert response_data.status_code == int(expected_data),  "Expeced HTTP Status : " + expected_data
def verify_key(response_data, key):
    assert len(response_data[key])!=0, "key is not Empty : " +key
    assert response_data[key]  > 0, "key should be greater then zero:" + key

