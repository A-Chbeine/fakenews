from elasticsearch import Elasticsearch

es = Elasticsearch(host="http://localhost", port=9200, http_auth=('elastic', 'changeme'))


def read_and_transform(txt_file):
    d = dict()
    data = list()
    with open(txt_file, 'r', encoding='UTF8') as f:
        tmp = f.readlines()
        f.close()
    for x in tmp:
        d['text'] = x.split(';')[0]
        d['label'] = ((x.split(';')[1]).replace('\n', '')).upper()
        dictionary_copy = d.copy()
        data.append(dictionary_copy)
    return data


def create_index(ind):
    es.indices.create(index=ind, ignore=400, settings={'method': 'POST'})


def insert_one_data(_index, text):
    res = es.index(index=_index, doc_type='authors', document=text)
    print(f'res = {res}')


if __name__ == '__main__':
    index = "fake_news"
    data = read_and_transform('../scrapping/FakeNews.txt')
    print(data)
    create_index(index)
    for num, d in enumerate(data):
        insert_one_data(index, d)
