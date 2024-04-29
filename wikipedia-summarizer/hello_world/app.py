import json
import wikipedia

# prints when function loads
print('Loading function')


def lambda_handler(event, context):
    ''' Wikipedia page summarizer.
        :param event: a request with a wikipedia "entity" that has page information
        :return: a response that contains the first sentence of a wikipedia page,
            the response is JSON formatted.'''
    
    ## Check that the request has some input body and save it
    if 'body' in event:
        body = json.loads(event["body"])
    
    ## Get the wikipedia "entity" from the body of the request
    entity = body["entity"]
    
    ## Define the status
    BAD_REQUEST_STATUS = 400
    ALL_GOOD_STATUS = 200 
    
    # Exception handling
    try:
        res = wikipedia.summary(entity, sentences=1) # first sentence, result
        statusCode = ALL_GOOD_STATUS
    except wikipedia.exceptions.PageError:
        res= "\nThis word does not exist!\n"
        statusCode = BAD_REQUEST_STATUS
    except wikipedia.exceptions.DisambiguationError: 
        statusCode = BAD_REQUEST_STATUS
        res = "\nThere are multiple references to this word!\n"
    except:
        statusCode = BAD_REQUEST_STATUS
        res = "\nSorry, Cannot Handle this request!\n"

    # print statements
    print(f"context: {context}, event: {event}")
    print(f"Response from wikipedia API: {res}")
    
    ## Format the response as JSON and return the result
    response = {
        "statusCode": statusCode,
        "headers": { "Content-type": "application/json" },
        "body": json.dumps(
            {
                "summary": res
            }
        )
    }
    
    return response
