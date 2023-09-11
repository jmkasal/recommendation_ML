import csv

def make_tuple(vals):
    #clean_data = tuple()
    vals = "".join(vals)
    clean_data = tuple(vals.strip(';()').split(','))
    return clean_data

def sql_to_csv(file_name):
    with open(file_name, 'r', encoding='UTF-8') as in_file:
        for line in in_file:
            vals = line.split()
            if 'VALUES' in vals:
                with open('../data.csv', 'a', encoding='UTF-8') as out_file:
                    writer = csv.writer(out_file)
                    data = make_tuple(vals[vals.index('VALUES') + 1:])
                    writer.writerow(data)
    return 'Success'

#def fast_to_sql(file_name):

def main():
    print(sql_to_csv(r"/SQL_files/tag_user.sql"))


if __name__ == '__main__':
    main()