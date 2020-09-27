#
# extract data from a CHANEL ATM result
# [20200831] (air@cmu.edu) Created
#

import sys,os, argparse
import xmltodict, csv
import pickle as pkl
from pprint import pprint
import re

#  declarations
VERBOSE = False
EXTRACTS = 5  # number of tasks in each hit

def make_time(dtime) :
    return dtime.strftime('%Y-%m-%d %H:%M:%S')  # usecs not useful in this domain
#

def burst_ident(ident) :
    '''get the elm index; dangerous: assumes input format is correct '''
    rslt = re.match(r'(NUMBER|ANSWER)_(\d*)',ident)
    return (rslt[0],rslt[1],rslt[2])
#

def fetch_data(xmlstring) : 
    ''' extract slot-value pairs , place in a dic'''
    doc = xmltodict.parse(xmlstring)
    answers = doc['QuestionFormAnswers']['Answer']
    datums = {}
    
    # pull together (seq#: ExtractID, Score) with seq# as a dic key
    for elm in answers :
        # pull out non-ratings content
        if elm["QuestionIdentifier"] == 'comment' :
            if elm['FreeText'] != 'None?' : datums['comment'] = elm['FreeText']
            continue
        # sort out the extracts and their ratings
        rslt = burst_ident(elm["QuestionIdentifier"])
        if not rslt[2] in datums : datums[rslt[2]] = { 'ExtractID' : None, 'Rating' : None }
        if rslt[1] == 'NUMBER' : datums[rslt[2]]['ExtractID'] = elm['FreeText']
        if rslt[1] == 'ANSWER' : datums[rslt[2]]['Rating'] = elm["FreeText"]

    return (datums)
#

def process(pklfile) :
    ''' digest the input file into db table equivalent row sets '''

    pickl=  pkl.load(open(pklfile,"rb"))
    if VERBOSE : print('found',len(pickl),'sets')

    # data layouts
    AssigmtColumns = ['HITId','WorkerId','AssignID','AcceptTime','SubmitTime','CHECK','Comment']
    ExcerptColumns = ['HITId','WorkerId','ExtractID','Rating']

    # queue up product for tables; first row is labels (as for .csv files)
    assignment_record    = [AssigmtColumns]  # a HIT session
    excerpt_record       = [ExcerptColumns]  # individual Extract info
    attn_check_record    = [ExcerptColumns]  # individual Extract catch trial
    raw_record  = []  # all the rows, no headers (ie, just the unpickled data)

    # process list of AMT output chunks, each with its list of 'Assignments'
    i =1
    for assignment_set in pickl :

        # Assignments contain multiple HITs,
        # in a list, HITs can be from different workers;
        # a HIT contains an 'Answer' plus meta-info
        for assign in assignment_set['Assignments'] :
            
            Accept_dt = make_time(assign['AcceptTime'])  # | first one is session timestamp
            Submit_dt = make_time(assign['SubmitTime'])  # | difference is time spent on HIT
            Answer = fetch_data(assign['Answer'])  # parse the xml into a dic

            # assemble

            # assemble Excerpts records  -> actual results, by excerpt
            for item in map(str,range(1,EXTRACTS)) :

                raw_record.append( [ Answer[item]['ExtractID'], 
                                     assign['WorkerId'],
                                     Answer[item]['Rating'] ] )
                
                if re.match(r'ATTENTION-CHECK',Answer[str(item)]['ExtractID']) :
                    attn_check_record.append( [ assign['HITId'],
                                                assign['WorkerId'],
                                                Answer[item]['ExtractID'], 
                                                Answer[item]['Rating'] ] )
                    catch = Answer[item]['Rating']
                else:
                    excerpt_record.append( [ assign['HITId'],
                                             assign['WorkerId'],
                                             Answer[item]['ExtractID'], 
                                             Answer[item]['Rating'] ] )

            # assemble Assignment record  --> meta information, by HIT
            assignment_record.append( [ assign['HITId'],
                                        assign['WorkerId'],
                                        assign['AssignmentId'],
                                        Accept_dt, Submit_dt,
                                        catch,
                                        Answer['comment'] if 'comment' in Answer else None ] )
                

    return (assignment_record, excerpt_record, attn_check_record, raw_record)  #, attn_check_record)



if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('pkl', type=str, help='Path to .pkl retrieved from hits')
    parser.add_argument('dest', type=str, help='Path to file for results')
    arg = parser.parse_args()

    # sort out the data
    (assignment_record, excerpt_record, attn_check_record, raw_record) = process(arg.pkl)

    # write csv file for each target table
    base = os.path.splitext(os.path.split(arg.pkl)[1])[0]  # use the pkl basename (why not?)
    with open( os.path.join(arg.dest,base+'-assigmt'+'.csv'), "w") as fd :
        writer= csv.writer(fd, delimiter='\t')
        writer.writerows(assignment_record)
    with open(os.path.join(arg.dest,base+'-excerpt'+'.csv'), "w") as fd :
        writer= csv.writer(fd, delimiter='\t')
        writer.writerows(excerpt_record)
    with open(os.path.join(arg.dest,base+'-attnchk'+'.csv'), "w") as fd :
        writer= csv.writer(fd, delimiter='\t')
        writer.writerows(attn_check_record)
    with open(os.path.join(arg.dest,base+'-raw'+'.csv'), "w") as fd :
        writer= csv.writer(fd, delimiter='\t')
        writer.writerows(raw_record)

# <main> done
    
#

