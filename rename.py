import os

dir = 'C:\\Users\\walte\\Desktop\\smartNamer\\pdfs_test'

def numbering(pdfs_dir):
    # Directory containing the PDFs
    pdfs_dir = pdfs_dir
    origin_files = os.listdir(pdfs_dir)

    i=0
    for file in origin_files:
        old_file_path = os.path.join(pdfs_dir, file)
        new_file_path = os.path.join(pdfs_dir, f"{str(i)}.pdf")
        print(new_file_path)
        os.rename(old_file_path, new_file_path)
        i+=1
    files = os.listdir(pdfs_dir)

    return files


def rename(pdfs_dir, names):
    origin_files = os.listdir(pdfs_dir)
    names = names
    print(names)
    for old_name,new_name in zip(origin_files, names):
        old_file_path = os.path.join(pdfs_dir, old_name)
        new_file_path = os.path.join(pdfs_dir, new_name)
        os.rename(old_file_path,new_file_path)