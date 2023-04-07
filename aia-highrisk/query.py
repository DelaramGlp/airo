'''
Created on 7 Apr 2023

@author: delaramglp
'''
import rdflib

def getLocal(uri):
    pos = -1
    pos = uri.rfind('#')
    if pos < 0 :
        pos = uri.rfind('/')
    #if pos < 0 :
     #   pos =  uri.rindex(':')
    return uri[pos+1:]



g = rdflib.Graph()
g.parse("https://raw.githubusercontent.com/DelaramGlp/airo/main/example.ttl" , format="turtle")

highrisk_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX airo:<https://w3id.org/airo#>
SELECT  ?system ?domain ?purpose ?user ?subject
    WHERE { ?system a airo:AISystem;
                    airo:isAppliedWithinDomain ?domain;
                    airo:hasPurpose ?purpose;
                    airo:isUsedBy ?user ;
                    airo:hasAISubject ?subject .}
"""

for row in g.query(highrisk_query):
     print("System: "+getLocal(str(row.system )))
     print("Domain: "+ getLocal(str(row.domain)))
     print("Purpose: "+getLocal(str(row.purpose)))
     print("User: "+getLocal(str(row.user)))
     print("AI Subject: "+getLocal(str(row.subject)))
     