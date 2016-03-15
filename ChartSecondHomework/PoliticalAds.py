# coding: utf-8
import agate
tester = agate.TypeTester(limit=100)
commercials = agate.Table.from_csv('commercials.csv', column_types = tester)
print(commercials)
def split_subjects(row):
    subjectList = row['subject'].split(',')
    subjectNumber = len(subjectList)
    return subjectList, subjectNumber
# def 
commercials_with_subjects = commercials.where(lambda row: row['subject'] != None)
commercials_by_subject = commercials_with_subjects.pivot('subject')
#commercials_subject_splits = commercials_with_subjects.compute([ ('subjects', agate.Formula(agate.Text(), split_subjects)) ])
commercials_by_subject.print_table()
#commercials_subject_splits_column = commericals_subject_splits.compute
#market_month_totals = by_market_by_month.aggregate([ ('count', agate.Length()) ])
#market_month_totals = market_month_totals.order_by(lambda row: (row['market'], row['month'])) market_month_totals.print_table()
