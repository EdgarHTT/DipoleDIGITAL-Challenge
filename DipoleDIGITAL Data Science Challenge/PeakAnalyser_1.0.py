import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def analyserFunc(file_root="Sample Data/dipoleDIGITAL_SampleData_3.txt", prominence1=5, prominence2=5):
    """
    Analyzes the txt file for peak values in voltage and depth.

    Parameters:
    file_root (str): The path to the data file.
    prominence1 (float): The prominence for detecting depth peaks.
    prominence2 (float): The prominence for detecting voltage peaks.

    Returns:
    tuple: A tuple containing the DataFrame and the indices of voltage peaks.
    """
    try:
        # Read the sample data into a DataFrame
        df = pd.read_csv(file_root)  # Assuming the file is CSV formatted

        # Data frame preparation
        df['Time'] = pd.to_datetime(df['Time'])  # Convert 'Time' column to datetime
        df.columns = ['Time', 'ShootingVoltage', 'Depth', 'ShootingVoltage2']  # Rename columns for clarity
        df = df.drop(columns=["ShootingVoltage2"])  # Drop duplicated column
        df.set_index('Time', inplace=True)  # Set time as index

        # Finding Peaks: From a 1D array it finds the local maxima by simple comparison
        depthPeaks, _ = find_peaks(df['Depth'], prominence=prominence1)
        VoltagePeaks, _ = find_peaks(-1 * df['ShootingVoltage'], prominence=prominence2)

        # Plot size
        plt.figure(figsize=(16, 10))

        # Plotting Time vs ShootingVoltage
        plt.subplot(2, 1, 1)
        plt.plot(df.index, df['ShootingVoltage'], label='ShootingVoltage', color='b')
        plt.plot(df.index[VoltagePeaks], df['ShootingVoltage'][VoltagePeaks], 'rx',
                 label=f"Peak Voltage: {df.index[VoltagePeaks][0]} {df['ShootingVoltage'][VoltagePeaks][0]}")
        for nPeak in range(len(VoltagePeaks)):
            plt.text(df.index[VoltagePeaks][nPeak], df['ShootingVoltage'][VoltagePeaks][nPeak],
                     str(df['ShootingVoltage'][VoltagePeaks][nPeak]))
        plt.xlabel('Time')
        plt.ylabel('ShootingVoltage')
        plt.title('ShootingVoltage over Time')
        plt.legend()

        # Plotting Time vs Depth
        plt.subplot(2, 1, 2)
        plt.plot(df.index, df['Depth'], label='Depth', color='g')
        plt.plot(df.index[depthPeaks], df['Depth'][depthPeaks], 'rx',
                 label=f"Peak depth: {df.index[depthPeaks][0]} {df['Depth'][depthPeaks][0]}")
        for nPeak in range(len(depthPeaks)):
            plt.text(df.index[depthPeaks][nPeak], df['Depth'][depthPeaks][nPeak],
                     str(df['Depth'][depthPeaks][nPeak]))
        plt.xlabel('Time')
        plt.ylabel('Depth')
        plt.title('Depth over Time')
        plt.legend()

        # Adjusting the layout and displaying the plot
        plt.tight_layout()
        plt.show()

        return df, VoltagePeaks

    except Exception as e:
        print(f"An error occurred: {e}")

def depthToPeak(df, VoltagePeaks):
    """
    Prints the depths corresponding to the voltage peaks.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    VoltagePeaks (list): The indices of the voltage peaks.
    """
    print("Voltage peak:\t corresponds to depth:")
    for nPeak in VoltagePeaks:
        print(f"{df['ShootingVoltage'][nPeak]} \t{df['Depth'][nPeak]}")

# Execute the analysis function and retrieve the data and peaks
df, VoltagePeaks = analyserFunc()

# Print the depth to voltage peak correspondences
if df is not None and VoltagePeaks is not None:
    depthToPeak(df, VoltagePeaks)