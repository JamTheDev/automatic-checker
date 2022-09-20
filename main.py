import os
import shutil

OUTPUT_DIR = "./output/"


def main():
    answersDir = input("Enter path to the answer sheet: ")
    questionnaresDir = input("Enter path to questionnares: ")

    rename_files(questionnaresDir)
    perform_check(answersDir)


def rename_files(dirOfFiles: str):
    outputDirs = os.listdir(OUTPUT_DIR)
    outputDirLen = len(outputDirs)

    print("Found " + str(len(outputDirs)) +
          " existing files in the output directory. Deleting...")
    for dir in outputDirs:
        os.remove(os.path.join(OUTPUT_DIR, dir))

    print("Removed all existing files.")

    dirs = os.listdir(dirOfFiles)
    print("Renaming files...")
    print("Found " + str(len(dirs)) + " file(s).")

    if outputDirLen != len(dirs):
        print("There were " + str((outputDirLen - len(dirs))) + " changes in files.")

    for dir in dirs:
        # rename file
        os.rename(os.path.join(dirOfFiles, dir), os.path.join(
            dirOfFiles, dir.replace(" ", "_")))
        # copy to OUTPIR_DIR
        shutil.copy(os.path.join(dirOfFiles, dir), OUTPUT_DIR)

    print("Successfully moved and renamed files!")


def write_to_file(content):
    with open("./results.txt", "w") as d:
        d.write(content)
        d.close()


def perform_check(answers_file: str):
    with open(answers_file) as _data:
        to_write = ""
        questionnare_directory = os.listdir(OUTPUT_DIR)
        answers_data = _data.read().lower().split("\n")
        for dir in questionnare_directory:
            with open(os.path.join(OUTPUT_DIR, dir)) as data:
                data_converted = data.read().split("\n")
                student_name = data_converted[0]
                student_section = data_converted[1]

                data_converted.pop(0)
                data_converted.pop(1)

                answers = ""
                score = 0

                for i in range(len(data_converted)):
                    if answers_data[i-1] == data_converted[i-1].replace(" ", "").lower():
                        score += 1

                to_write += str.format("-------\n{student_name}\n{student_section}\nScore: {score}\n--------",
                                       student_name=student_name, student_section=student_section, score=score)

            to_write += "-------"
            write_to_file(to_write)
        print("Finished writing file.")


if __name__ == "__main__":
    main()
