import os
import pandas as pd

def process_folder(folder_path, output_filename):
    """
    Processes all .dat files in a given folder.
    Each .dat file represents one depth at that x-location.
    Extracts instantaneous u,v,w from columns 3,4,5 (0-indexed: 2,3,4),
    computes u', v', w',
    and saves each depth in its own sheet inside one Excel file.
    """

    writer = pd.ExcelWriter(output_filename, engine="xlsxwriter")

    for file in os.listdir(folder_path):
        if file.lower().endswith(".dat"):
            file_path = os.path.join(folder_path, file)
            print(f"Processing {file_path} ...")

            # Read with flexible whitespace handling
            try:
                df = pd.read_csv(file_path, delim_whitespace=True, header=None)
            except:
                df = pd.read_csv(file_path, sep=r"\s+", header=None)

            # Extract instantaneous velocities (3rd, 4th, 5th columns)
            u = df.iloc[:, 2]
            v = df.iloc[:, 3]
            w = df.iloc[:, 4]

            # Compute mean velocities
            u_mean, v_mean, w_mean = u.mean(), v.mean(), w.mean()

            # Compute fluctuations
            df_out = pd.DataFrame({
                "u_instant": u,
                "v_instant": v,
                "w_instant": w,
                "u_prime": u - u_mean,
                "v_prime": v - v_mean,
                "w_prime": w - w_mean
            })

            # Prepare a safe sheet name (max 31 chars)
            sheet_name = os.path.splitext(file)[0][:31]
            df_out.to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save() # type: ignore
    print(f"\nSaved results to {output_filename}\n")


# -------------------------------
# MAIN EXECUTION
# -------------------------------
if __name__ == "__main__":

    # Hard-coded folder paths for each x-location
    folder_x215 = "D:\\Confidential\\u'v'w'\\x = 2.15"
    folder_x365 = "D:\\Confidential\\u'v'w'\\x = 3.65"
    folder_x515 = "D:\\Confidential\\u'v'w'\\x = 5.15"

    process_folder(folder_x215, "fluctuations_x215.xlsx")
    process_folder(folder_x365, "fluctuations_x365.xlsx")
    process_folder(folder_x515, "fluctuations_x515.xlsx")

    print("ALL LOCATIONS PROCESSED SUCCESSFULLY!")
