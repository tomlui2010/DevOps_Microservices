import json
import wikipediaapi

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
    
    
    

    wiki_object = wikipediaapi.Wikipedia('SampleProject (test@udacity.com)', 'en')
    scraped_page = wiki_object.page(entity)
    if scraped_page.exists():
        res= scraped_page.summary[0:100]
        statusCode = ALL_GOOD_STATUS
    else:
        res= "\nWiki page for this word does not exist!\n"  
        statusCode = BAD_REQUEST_STATUS
    
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
