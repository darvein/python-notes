class AnonymouseSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, response):
        self.responses.append(response)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
