import copy


def replace_TU(data_wrapper):
    print("replace T with U")
    data_wrapper2 = copy.deepcopy(data_wrapper)
    data_wrapper2.data_df['seq'] = data_wrapper2.data_df['seq'].apply(lambda seq: seq.replace('T', 'U'))

    return data_wrapper2