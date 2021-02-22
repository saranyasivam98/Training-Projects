from segregate_csv_files.check_csv import *
main()
args = arg_parse()
setup_logging()
dir_path = Path.cwd() / args.d
if dir_path.is_dir():
    os.chdir(dir_path)
    csv_files, csv_files_str = get_csv_files(Path.cwd())
    file_names = get_file_names(csv_files)

    cr_dates = clear_repetition(file_names)
    final_dates = check_proper_dates(cr_dates)
    file_dates = is_date(final_dates, FMTS)
    unique_dates = unique(file_dates)
    create_directory(unique_dates)
    copy_files(csv_files_str, FMTS, unique_dates)
    ambiguity(unique_dates)
else:
    LOGGER.error("The directory doesnt exist")
