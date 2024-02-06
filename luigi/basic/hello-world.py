import luigi


class HelloLuigi(luigi.Task):

    def output(self):
        return luigi.LocalTarget('hello-luigi.txt')

    def run(self):
        with self.output().open("w") as outfile:
            outfile.write("Hello Luigi!")


if __name__ == "__main__":
    luigi.build([HelloLuigi()], workers=1, local_scheduler=True)