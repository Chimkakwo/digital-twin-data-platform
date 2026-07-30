from pathlib import Path

import pandas as pd

COLUMN_NAMES = [
    "Time",
    "P1",
    "P2",
    "P3",
    "P4",
    "MainFlow",
    "Flowrate",
    "P5",
    "rpm",
    "DPV1",
    "DPV2",
    "DPV3",
    "DPV4",
    "DPV5",
    "Comment",
]

HEADER_ROWS = 24
ATMOSPHERIC_PRESSURE_BAR = 1.013


def read_lvm_file(file_path: str | Path) -> pd.DataFrame:
    """Read and clean one LabVIEW measurement file."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    dataframe = pd.read_table(
        file_path,
        sep="\t",
        skiprows=HEADER_ROWS,
        names=COLUMN_NAMES,
    )

    dataframe = dataframe.drop(
        columns=["Comment", "MainFlow"],
        errors="ignore",
    )

    dataframe = dataframe.apply(pd.to_numeric, errors="coerce")

    dataframe[["P3", "P4", "P5"]] = (
        dataframe[["P3", "P4", "P5"]] + ATMOSPHERIC_PRESSURE_BAR
    )

    dataframe["Pressure"] = dataframe["P3"] - dataframe["P2"]

    return dataframe


def read_condition_folder(folder_path: str | Path) -> pd.DataFrame:
    """Read and merge all LabVIEW files in one condition folder."""

    folder_path = Path(folder_path)

    if not folder_path.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    if not folder_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder_path}")

    lvm_files = sorted(folder_path.glob("*.lvm"))

    if not lvm_files:
        raise ValueError(f"No .lvm files found in: {folder_path}")

    dataframes = []

    for run_number, file_path in enumerate(lvm_files, start=1):
        dataframe = read_lvm_file(file_path)

        dataframe["run_number"] = run_number
        dataframe["source_file"] = file_path.name

        dataframes.append(dataframe)

    merged_dataframe = pd.concat(
        dataframes,
        ignore_index=True,
    )

    return merged_dataframe


def build_dataset(raw_data_path: str | Path) -> dict[str, pd.DataFrame]:
    """Read all operating-condition folders and return one DataFrame per condition."""

    raw_data_path = Path(raw_data_path)

    if not raw_data_path.exists():
        raise FileNotFoundError(f"Folder not found: {raw_data_path}")

    datasets = {}

    for folder in sorted(raw_data_path.iterdir()):
        if not folder.is_dir():
            continue

        print(f"Processing {folder.name}...")

        dataframe = read_condition_folder(folder)

        dataframe["condition"] = folder.name

        datasets[folder.name] = dataframe

    return datasets


if __name__ == "__main__":
    raw_data_folder = Path("data/raw")

    datasets = build_dataset(raw_data_folder)

    print("\nDataset Summary")
    print("-" * 40)

    for name, dataframe in datasets.items():
        print(f"{name:<22} {dataframe.shape}")
