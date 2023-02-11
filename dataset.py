import csv


class Dataset:
    def __init__(self, file_location) -> None:
        self.file_location = file_location
        self.questionnaires = self.__parseCsv()

    def __parseCsv(self):
        parsedData = {}
        with open(self.file_location, "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row in reader:
                if not row[0] in parsedData:
                    parsedData[row[0].lower().strip()] = [row[1].lower().strip()]
                else:
                    parsedData[row[0].lower().strip()].append(row[1].lower().strip())

        return parsedData

    def getUniqueTags(self) -> list[str]:
        return list(self.questionnaires.keys())

    def generateQuestionaire(self, tag: str) -> list[str]:
        return self.questionnaires[tag]


if __name__ == "__main__":
    dataset = Dataset("data/behavior-based-questions.csv")
    print(dataset.getUniqueTags())
    print(dataset.generateQuestionaire("flexibility"))
