import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#======================================================================================================================================
#======================================================================================================================================
# DATA FILEPATHS AND DIRECTORIES
#======================================================================================================================================
#======================================================================================================================================
DATA_DIR = 'infile'
RESULTS_DIR = 'outfile/results'
PLOTS_DIR = 'outfile/plots'

top_scint_14hr_fp = f'{DATA_DIR}/SDleft_AxLab_M_024_roomtemp.txt' # @param {type:"string"}
mid_scint_14hr_fp = f'{DATA_DIR}/SDmiddle_AxLab_M_024_roomtemp.txt' # @param {type:"string"}
bot_scint_14hr_fp = f'{DATA_DIR}/SDright_AxLab_M_024_roomtemp.txt' # @param {type:"string"}

top_scint_flight_fp = f'{DATA_DIR}/left_AxLab_M_038_flight.txt' # @param {type:"string"}
mid_scint_flight_fp = f'{DATA_DIR}/middle_AxLab_M_037 copy_flight.txt' # @param {type:"string"}
bot_scint_flight_fp = f'{DATA_DIR}/right_AxLab_M_038 copy_flight.txt' # @param {type:"string"}

top_scint_flight_seg3_fp = f'{DATA_DIR}/left_AxLab_M_038_flight_seg3.txt' # @param {type:"string"}
mid_scint_flight_seg3_fp = f'{DATA_DIR}/middle_AxLab_M_037 copy_flight_seg3.txt' # @param {type:"string"}
bot_scint_flight_seg3_fp = f'{DATA_DIR}/right_AxLab_M_038 copy_flight_seg3.txt' # @param {type:"string"}

top_scint_feb1_fp = f'{DATA_DIR}/AxLab_M_020_top.txt' # @param {type:"string"}
mid_scint_feb1_fp = f'{DATA_DIR}/AxLab_M_020_mid.txt' # @param {type:"string"}


#======================================================================================================================================
#======================================================================================================================================
# DATAFRAME COLUMN STRUCTURES
#======================================================================================================================================
#======================================================================================================================================
_cols1 = ['Event','Time[s]','Coincident[bool]','ADC[0-4095]', 'top','Deadtime[s]','Temp[C]','Pressure[Pa]']
_cols2 = ['Event','Time[s]','Coincident[bool]','ADC[0-4095]', 'mid','Deadtime[s]','Temp[C]','Pressure[Pa]']
_cols3 = ['Event','Time[s]','Coincident[bool]','ADC[0-4095]', 'bot','Deadtime[s]','Temp[C]','Pressure[Pa]']

df_cols = ['Top', 'Mid', 'Bot', 'Mean', 'STD', 'Top-Bot', 'Top-Mid', 'Mid-Bot', 'Total', 'Min-Max']
df_cols2 = ['Top', 'Mid', 'Mean', 'STD', 'Total', 'Min-Max']


#======================================================================================================================================
#======================================================================================================================================
# EXTRACTING FLIGHT DATA mV VALUES
#======================================================================================================================================
#======================================================================================================================================
top_14hr = pd.read_csv(top_scint_14hr_fp, sep='\t', comment='#', header=None, skiprows=3, names=_cols1, engine='python')['top'][0:138709]
mid_14hr = pd.read_csv(mid_scint_14hr_fp, sep='\t', comment='#', header=None, skiprows=3, names=_cols2, engine='python')['mid'][0:138709]
bot_14hr = pd.read_csv(bot_scint_14hr_fp, sep='\t', comment='#', header=None, skiprows=3, names=_cols3, engine='python')['bot'][0:138709]

top_flight = pd.read_csv(top_scint_flight_fp, sep='\t', comment='#', header=None, skiprows=3, names=_cols1, engine='python')['top'][0:147765]
mid_flight = pd.read_csv(mid_scint_flight_fp, sep='\t', comment='#', header=None, skiprows=3, names=_cols2, engine='python')['mid'][0:147765]
bot_flight = pd.read_csv(bot_scint_flight_fp, sep='\t', comment='#', header=None, skiprows=3, names=_cols3, engine='python')['bot'][0:147765]

top_flight_seg3 = pd.read_csv(top_scint_flight_seg3_fp, sep='\t', comment='#', header=None, skiprows=3, names=_cols1, engine='python')['top'][0:68647]
mid_flight_seg3 = pd.read_csv(mid_scint_flight_seg3_fp, sep='\t', comment='#', header=None, skiprows=3, names=_cols2, engine='python')['mid'][0:68647]
bot_flight_seg3 = pd.read_csv(bot_scint_flight_seg3_fp, sep='\t', comment='#', header=None, skiprows=3, names=_cols3, engine='python')['bot'][0:68647]

top_feb1 = pd.read_csv(top_scint_feb1_fp, sep='\t', comment='#', header=None, skiprows=3, names=_cols1, engine='python')['top'][0:701459]
mid_feb1 = pd.read_csv(mid_scint_feb1_fp, sep='\t', comment='#', header=None, skiprows=3, names=_cols2, engine='python')['mid'][0:701459]


#======================================================================================================================================
#======================================================================================================================================
# COMBINING DATA INTO ONE DATAFRAME
#======================================================================================================================================
#======================================================================================================================================
combined_14hr = pd.concat([top_14hr, mid_14hr, bot_14hr], axis=1)

combined_flight = pd.concat([top_flight, mid_flight, bot_flight], axis=1)

combined_flight_seg3 = pd.concat([top_flight_seg3, mid_flight_seg3, bot_flight_seg3], axis=1)

combined_feb1 = pd.concat([top_feb1, mid_feb1], axis=1)


#======================================================================================================================================
#======================================================================================================================================
# TOP - MID; TOP - BOT; MID - BOT DATAFRAME EXTRAPOLATION
#======================================================================================================================================
#======================================================================================================================================
top_mid_14hr = top_14hr - mid_14hr
top_bot_14hr = top_14hr - bot_14hr
mid_bot_14hr = mid_14hr - bot_14hr

top_mid_flight = top_flight - mid_flight
top_bot_flight = top_flight - bot_flight
mid_bot_flight = mid_flight - bot_flight

top_mid_flight_seg3 = top_flight_seg3 - mid_flight_seg3
top_bot_flight_seg3 = top_flight_seg3 - bot_flight_seg3
mid_bot_flight_seg3 = mid_flight_seg3 - bot_flight_seg3


#======================================================================================================================================
#======================================================================================================================================
# TOTAL AND MAX - MIN EXTRAPOLATION
#======================================================================================================================================
#======================================================================================================================================
total_14hr = top_14hr + mid_14hr + bot_14hr
min_max_14hr = (combined_14hr.max(axis=1) - combined_14hr.min(axis=1))/(top_14hr + mid_14hr + bot_14hr)

total_flight = top_flight + mid_flight + bot_flight
min_max_flight = (combined_flight.max(axis=1) - combined_flight.min(axis=1))/(top_flight + mid_flight + bot_flight)

total_flight_seg3 = top_flight_seg3 + mid_flight_seg3 + bot_flight_seg3
min_max_flight_seg3 = (combined_flight_seg3.max(axis=1) - combined_flight_seg3.min(axis=1))/(top_flight_seg3 + mid_flight_seg3 + bot_flight_seg3)

total_feb1 = top_feb1 + mid_feb1
min_max_feb1 = (combined_feb1.max(axis=1) - combined_feb1.min(axis=1))/(top_feb1 + mid_feb1)


#======================================================================================================================================
#======================================================================================================================================
# MEAN AND STANDARD DEVIATION EXTRAPOLATION; STD IS SAMPLE NOT POPULATION
#======================================================================================================================================
#======================================================================================================================================
mean_14hr = pd.DataFrame({
    "mean": combined_14hr.mean(axis=1),
})
std_14hr = pd.DataFrame({
    "std": combined_14hr.std(axis=1),
})

mean_flight = pd.DataFrame({
    "mean": combined_flight.mean(axis=1),
})
std_flight = pd.DataFrame({
    "std": combined_flight.std(axis=1),
})

mean_flight_seg3 = pd.DataFrame({
    "mean": combined_flight_seg3.mean(axis=1),
})
std_flight_seg3 = pd.DataFrame({
    "std": combined_flight_seg3.std(axis=1),
})

mean_feb1 = pd.DataFrame({
    "mean": combined_feb1.mean(axis=1),
})
std_feb1 = pd.DataFrame({
    "std": combined_feb1.std(axis=1),
})


#======================================================================================================================================
#======================================================================================================================================
# CONCATENATING ALL DATA INTO ONE DATA FRAME
#======================================================================================================================================
#======================================================================================================================================
df_14hr = pd.concat([top_14hr, mid_14hr, bot_14hr, mean_14hr, std_14hr, top_bot_14hr, top_mid_14hr, mid_bot_14hr, total_14hr, min_max_14hr], names=df_cols, axis=1)

df_flight = pd.concat([top_flight, mid_flight, bot_flight, mean_flight, std_flight, top_bot_flight, top_mid_flight, mid_bot_flight, total_flight, min_max_flight], names=df_cols, axis=1)

df_flight_seg3 = pd.concat([top_flight_seg3, mid_flight_seg3, bot_flight_seg3, mean_flight_seg3, std_flight_seg3, top_bot_flight_seg3, top_mid_flight_seg3, mid_bot_flight_seg3, total_flight_seg3, min_max_flight_seg3], names=df_cols, axis=1)

df_feb1 = pd.concat([top_feb1, mid_feb1, mean_feb1, std_feb1, total_feb1, min_max_feb1], names=df_cols2, axis=1)


#======================================================================================================================================
#======================================================================================================================================
# CUTTING ANOMALOUS DATA
#======================================================================================================================================
#======================================================================================================================================
df_14hr_cut = df_14hr[df_14hr["std"].gt((-0.5) * df_14hr["mean"] + 190) & 
        df_14hr["std"].lt((-0.5) * df_14hr["mean"] + 230) & 
        df_14hr["mean"].between(100, 200) & 
        df_14hr["top"].lt(290) & 
        df_14hr["mid"].lt(290) & 
        df_14hr["bot"].lt(290)].reset_index(drop=True)

df_flight_cut = df_flight[df_flight["std"].gt((-0.5) * df_flight["mean"] + 190) & 
        df_flight["std"].lt((-0.5) * df_flight["mean"] + 230) & 
        df_flight["mean"].between(100, 200) & 
        df_flight["top"].lt(290) & 
        df_flight["mid"].lt(290) & 
        df_flight["bot"].lt(290)].reset_index(drop=True)

df_flight_seg3_cut = df_flight_seg3[df_flight_seg3["std"].gt((-0.5) * df_flight_seg3["mean"] + 190) & 
        df_flight_seg3["std"].lt((-0.5) * df_flight_seg3["mean"] + 230) & 
        df_flight_seg3["mean"].between(100, 200) & 
        df_flight_seg3["top"].lt(290) & 
        df_flight_seg3["mid"].lt(290) & 
        df_flight_seg3["bot"].lt(290)].reset_index(drop=True)

df_feb1_cut = df_feb1[df_feb1["std"].gt((-0.5) * df_feb1["mean"] + 190) & 
        df_feb1["std"].lt((-0.5) * df_feb1["mean"] + 230) & 
        df_feb1["mean"].between(100, 200) & 
        df_feb1["top"].lt(290) & 
        df_feb1["mid"].lt(290)].reset_index(drop=True)


#======================================================================================================================================
#======================================================================================================================================
# TOP - MID vs BOT PLOTS
#======================================================================================================================================
#======================================================================================================================================
topmidbot_14hr_fig = plt.figure(figsize=(8, 6))

topmidbot_14hr= plt.hist2d(
    df_14hr["bot"],
    df_14hr[1],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top-Mid (mV)")
plt.title("Top-Mid vs Bot 14 Hour Ground Test Event Heatmap - All Events")

plt.colorbar(topmidbot_14hr[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmidbot_14hr.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topmidbot_flight_fig = plt.figure(figsize=(8, 6))

topmidbot_flight= plt.hist2d(
    df_flight["bot"],
    df_flight[1],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top-Mid (mV)")
plt.title("Top-Mid vs Bot Full Flight Event Heatmap - All Events")

plt.colorbar(topmidbot_flight[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmidbot_flight.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topmidbot_flight_seg3_fig = plt.figure(figsize=(8, 6))

topmidbot_flight_seg3= plt.hist2d(
    df_flight_seg3["bot"],
    df_flight_seg3[1],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top-Mid (mV)")
plt.title("Top-Mid vs Bot High Altitude Flight Event Heatmap - All Events")

plt.colorbar(topmidbot_flight_seg3[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmidbot_flight_seg3.png")
plt.close()

#======================================================================================================================================
# CUTS
#======================================================================================================================================
topmidbot_14hr_fig_cut = plt.figure(figsize=(8, 6))

topmidbot_14hr_cut = plt.hist2d(
    df_14hr_cut["bot"],
    df_14hr_cut[1],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top-Mid (mV)")
plt.title("Top-Mid vs Bot 14 Hour Ground Test Event Heatmap - Anomalous Events")

plt.colorbar(topmidbot_14hr_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmidbot_14hr_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topmidbot_flight_cut_fig = plt.figure(figsize=(8, 6))

topmidbot_flight_cut = plt.hist2d(
    df_flight_cut["bot"],
    df_flight_cut[1],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top-Mid (mV)")
plt.title("Top-Mid vs Bot Full Flight Event Heatmap - Anomalous Events")

plt.colorbar(topmidbot_flight_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmidbot_flight_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topmidbot_flight_seg3_cut_fig = plt.figure(figsize=(8, 6))

topmidbot_flight_seg3_cut = plt.hist2d(
    df_flight_seg3_cut["bot"],
    df_flight_seg3_cut[1],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top-Mid (mV)")
plt.title("Top-Mid vs Bot High Altitude Flight Event Heatmap - Anomalous Events")

plt.colorbar(topmidbot_flight_seg3_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmidbot_flight_seg3_cut.png")
plt.close()


#======================================================================================================================================
#======================================================================================================================================
# MID - BOT vs TOP PLOTS
#======================================================================================================================================
#======================================================================================================================================
midbottop_14hr_fig = plt.figure(figsize=(8, 6))

midbottop_14hr = plt.hist2d(
    df_14hr["top"],
    df_14hr[2],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top (mV)")
plt.ylabel("Mid-Bot (mV)")
plt.title("Mid-Bot vs Top 14 Hour Ground Test Event Heatmap - All Events")

plt.colorbar(midbottop_14hr[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbottop_14hr.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
midbottop_flight_fig = plt.figure(figsize=(8, 6))

midbottop_flight = plt.hist2d(
    df_flight["top"],
    df_flight[2],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top (mV)")
plt.ylabel("Mid-Bot (mV)")
plt.title("Mid-Bot vs Top Full Flight Event Heatmap - All Events")

plt.colorbar(midbottop_flight[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbottop_flight.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
midbottop_flight_seg3_fig = plt.figure(figsize=(8, 6))

midbottop_flight_seg3 = plt.hist2d(
    df_flight_seg3["top"],
    df_flight_seg3[2],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top (mV)")
plt.ylabel("Mid-Bot (mV)")
plt.title("Mid-Bot vs Top High Altitude Flight Event Heatmap - All Events")

plt.colorbar(midbottop_flight_seg3[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbottop_flight_seg3.png")
plt.close()

#======================================================================================================================================
# CUTS
#======================================================================================================================================
midbottop_14hr_cut_fig = plt.figure(figsize=(8, 6))

midbottop_14hr_cut = plt.hist2d(
    df_14hr_cut["top"],
    df_14hr_cut[2],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top (mV)")
plt.ylabel("Mid-Bot (mV)")
plt.title("Mid-Bot vs Top 14 Hour Ground Test Event Heatmap - Anomalmous Events")

plt.colorbar(midbottop_14hr_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbottop_14hr_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
midbottop_flight_cut_fig = plt.figure(figsize=(8, 6))

midbottop_flight_cut = plt.hist2d(
    df_flight_cut["top"],
    df_flight_cut[2],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top (mV)")
plt.ylabel("Mid-Bot (mV)")
plt.title("Mid-Bot vs Top Full Flight Event Heatmap - Anomalous Events")

plt.colorbar(midbottop_flight_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbottop_flight_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
midbottop_flight_seg3_cut_fig = plt.figure(figsize=(8, 6))

midbottop_flight_seg3_cut = plt.hist2d(
    df_flight_seg3_cut["top"],
    df_flight_seg3_cut[2],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top (mV)")
plt.ylabel("Mid-Bot (mV)")
plt.title("Mid-Bot vs Top High Altitude Flight Event Heatmap - Anomalous Events")

plt.colorbar(midbottop_flight_seg3_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbottop_flight_seg3_cut.png")
plt.close()


#======================================================================================================================================
#======================================================================================================================================
# TOP - BOT vs MID PLOTS
#======================================================================================================================================
#======================================================================================================================================
topbotmid_14hr_fig = plt.figure(figsize=(8, 6))

topbotmid_14hr = plt.hist2d(
    df_14hr["mid"],
    df_14hr[0],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top-Bot (mV)")
plt.title("Top-Bot vs Mid 14 Hour Ground Test Event Heatmap - All Events")

plt.colorbar(topbotmid_14hr[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbotmid_14hr_fig.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topbotmid_flight_fig = plt.figure(figsize=(8, 6))

topbotmid_flight = plt.hist2d(
    df_flight["mid"],
    df_flight[0],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top-Bot (mV)")
plt.title("Top-Bot vs Mid Full Flight Event Heatmap - All Events")

plt.colorbar(topbotmid_flight[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbotmid_flight.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topbotmid_flight_seg3_fig = plt.figure(figsize=(8, 6))

topbotmid_flight_seg3 = plt.hist2d(
    df_flight_seg3["mid"],
    df_flight_seg3[0],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top-Bot (mV)")
plt.title("Top-Bot vs Mid High Altitude Flight Event Heatmap - All Events")

plt.colorbar(topbotmid_flight_seg3[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbotmid_flight_seg3.png")
plt.close()

#======================================================================================================================================
# CUTS
#======================================================================================================================================
topbotmid_14hr_cut_fig = plt.figure(figsize=(8, 6))

topbotmid_14hr_cut = plt.hist2d(
    df_14hr_cut["mid"],
    df_14hr_cut[0],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top-Bot (mV)")
plt.title("Top-Bot vs Mid 14 Hour Ground Test Event Heatmap - Anomalmous Events")

plt.colorbar(topbotmid_14hr_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbotmid_14hr_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topbotmid_flight_cut_fig = plt.figure(figsize=(8, 6))

topbotmid_flight_cut = plt.hist2d(
    df_flight_cut["mid"],
    df_flight_cut[0],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top-Bot (mV)")
plt.title("Top-Bot vs Mid Full Flight Event Heatmap - Anomalous Events")

plt.colorbar(topbotmid_flight_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbotmid_flight_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topbotmid_flight_seg3_cut_fig = plt.figure(figsize=(8, 6))

topbotmid_flight_seg3_cut = plt.hist2d(
    df_flight_seg3_cut["mid"],
    df_flight_seg3_cut[0],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top-Bot (mV)")
plt.title("Top-Bot vs Mid High Altitude Flight Event Heatmap - Anomalous Events")

plt.colorbar(topbotmid_flight_seg3_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbotmid_flight_seg3_cut.png")
plt.close()


#======================================================================================================================================
#======================================================================================================================================
# TOP vs MID PLOTS
#======================================================================================================================================
#======================================================================================================================================
topmid_14hr_fig = plt.figure(figsize=(8, 6))

topmid_14hr = plt.hist2d(
    df_14hr["mid"],
    df_14hr["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Mid 14 Hour Ground Test Event Heatmap - All Events")

plt.colorbar(topmid_14hr[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmid_14hr.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topmid_flight_fig = plt.figure(figsize=(8, 6))

topmid_flight = plt.hist2d(
    df_flight["mid"],
    df_flight["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Mid Full Flight Event Heatmap - All Events")

plt.colorbar(topmid_flight[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmid_flight.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topmid_flight_seg3_fig = plt.figure(figsize=(8, 6))

topmid_flight_seg3 = plt.hist2d(
    df_flight_seg3["mid"],
    df_flight_seg3["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Mid High Altitude Flight Event Heatmap - All Events")

plt.colorbar(topmid_flight_seg3[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmid_flight_seg3.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topmid_feb1_fig = plt.figure(figsize=(8, 6))

topmid_feb1 = plt.hist2d(
    df_feb1["mid"],
    df_feb1["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Mid February 1st Event Heatmap - All Events")

plt.colorbar(topmid_feb1[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmid_feb1.png")
plt.close()

#======================================================================================================================================
# CUTS
#======================================================================================================================================
topmid_14hr_cut_fig = plt.figure(figsize=(8, 6))

topmid_14hr_cut = plt.hist2d(
    df_14hr_cut["mid"],
    df_14hr_cut["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Mid 14 Hour Ground Test Event Heatmap - Anomalous Events")

plt.colorbar(topmid_14hr_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmid_14hr_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topmid_flight_cut_fig = plt.figure(figsize=(8, 6))

topmid_flight_cut = plt.hist2d(
    df_flight_cut["mid"],
    df_flight_cut["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Mid Full Flight Event Heatmap - Anomalous Events")

plt.colorbar(topmid_flight_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmid_flight_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topmid_flight_seg3_cut_fig = plt.figure(figsize=(8, 6))

topmid_flight_seg3_cut = plt.hist2d(
    df_flight_seg3_cut["mid"],
    df_flight_seg3_cut["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Mid High Altitude Flight Event Heatmap - Anomalous Events")

plt.colorbar(topmid_flight_seg3_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmid_flight_seg3_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topmid_feb1_cut_fig = plt.figure(figsize=(8, 6))

topmid_feb1_cut = plt.hist2d(
    df_feb1_cut["mid"],
    df_feb1_cut["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mid (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Mid February 1st Event Heatmap - Anomalous Events")

plt.colorbar(topmid_feb1_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topmid_feb1_cut.png")
plt.close()


#======================================================================================================================================
#======================================================================================================================================
# MID vs BOT PLOTS
#======================================================================================================================================
#======================================================================================================================================
midbot_14hr_fig = plt.figure(figsize=(8, 6))

midbot_14hr = plt.hist2d(
    df_14hr["bot"],
    df_14hr["mid"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Mid (mV)")
plt.title("Mid vs Bot 14 Hour Ground Test Event Heatmap - All Events")

plt.colorbar(midbot_14hr[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbot_14hr.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
midbot_flight_fig = plt.figure(figsize=(8, 6))

midbot_flight = plt.hist2d(
    df_flight["bot"],
    df_flight["mid"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Mid (mV)")
plt.title("Mid vs Bot Full Flight Event Heatmap - All Events")

plt.colorbar(midbot_flight[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbot_flight.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
midbot_flight_seg3_fig = plt.figure(figsize=(8, 6))

midbot_flight_seg3 = plt.hist2d(
    df_flight_seg3["bot"],
    df_flight_seg3["mid"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Mid (mV)")
plt.title("Mid vs Bot High Altitude Flight Event Heatmap - All Events")

plt.colorbar(midbot_flight_seg3[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbot_flight_seg3.png")
plt.close()

#======================================================================================================================================
# CUTS
#======================================================================================================================================
midbot_14hr_cut_fig = plt.figure(figsize=(8, 6))

midbot_14hr_cut = plt.hist2d(
    df_14hr_cut["bot"],
    df_14hr_cut["mid"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Mid (mV)")
plt.title("Mid vs Bot 14 Hour Ground Test Event Heatmap - Anomalous Events")

plt.colorbar(midbot_14hr_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbot_14hr_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
midbot_flight_cut_fig = plt.figure(figsize=(8, 6))

midbot_flight_cut = plt.hist2d(
    df_flight_cut["bot"],
    df_flight_cut["mid"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Mid (mV)")
plt.title("Mid vs Bot Full Flight Event Heatmap - Anomalous Events")

plt.colorbar(midbot_flight_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbot_flight_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
midbot_flight_seg3_cut_fig = plt.figure(figsize=(8, 6))

midbot_flight_seg3_cut = plt.hist2d(
    df_flight_seg3_cut["bot"],
    df_flight_seg3_cut["mid"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Mid (mV)")
plt.title("Mid vs Bot High Altitude Flight Event Heatmap - Anomalous Events")

plt.colorbar(midbot_flight_seg3_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/midbot_flight_seg3_cut.png")
plt.close()


#======================================================================================================================================
#======================================================================================================================================
# TOP vs BOT PLOTS
#======================================================================================================================================
#======================================================================================================================================
topbot_14hr_fig = plt.figure(figsize=(8, 6))

topbot_14hr = plt.hist2d(
    df_14hr["bot"],
    df_14hr["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Bot 14 Hour Ground Test Event Heatmap - All Events")

plt.colorbar(topbot_14hr[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbot_14hr.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topbot_flight_fig = plt.figure(figsize=(8, 6))

topbot_flight = plt.hist2d(
    df_flight["bot"],
    df_flight["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Bot Full Flight Event Heatmap - All Events")

plt.colorbar(topbot_flight[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbot_flight.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topbot_flight_seg3_fig = plt.figure(figsize=(8, 6))

topbot_flight_seg3 = plt.hist2d(
    df_flight_seg3["bot"],
    df_flight_seg3["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Bot High Altitude Flight Event Heatmap - All Events")

plt.colorbar(topbot_flight_seg3[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbot_flight_seg3.png")
plt.close()

#======================================================================================================================================
# CUTS
#======================================================================================================================================
topbot_14hr_cut_fig = plt.figure(figsize=(8, 6))

topbot_14hr_cut = plt.hist2d(
    df_14hr_cut["bot"],
    df_14hr_cut["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Bot 14 Hour Ground Test Event Heatmap - Anomalous Events")

plt.colorbar(topbot_14hr_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbot_14hr_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topbot_flight_cut_fig = plt.figure(figsize=(8, 6))

topbot_flight_cut = plt.hist2d(
    df_flight_cut["bot"],
    df_flight_cut["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Bot Full Flight Event Heatmap - Anomalous Events")

plt.colorbar(topbot_flight_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbot_flight_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
topbot_flight_seg3_cut_fig = plt.figure(figsize=(8, 6))

topbot_flight_seg3_cut = plt.hist2d(
    df_flight_seg3_cut["bot"],
    df_flight_seg3_cut["top"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Bot (mV)")
plt.ylabel("Top (mV)")
plt.title("Top vs Bot High Altitude Flight Event Heatmap - Anomalous Events")

plt.colorbar(topbot_flight_seg3_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/topbot_flight_seg3_cut.png")
plt.close()


#======================================================================================================================================
#======================================================================================================================================
# RANGE / TOTAL vs TOTAL PLOTS; RANGE / TOTAL GIVES THE RATIO BETWEEN SPREAD AND PEAKS
#======================================================================================================================================
#======================================================================================================================================
ratio_14hr_fig = plt.figure(figsize=(8, 6))

ratio_14hr = plt.hist2d(
    df_14hr[3],
    df_14hr[4],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top + Mid + Bot (mV)")
plt.ylabel("(Max-Min)/(Top + Mid + Bot)")
plt.title("Range/(total mV) vs total mV 14 Hour Ground Test Event Heatmap - All Events")

plt.colorbar(ratio_14hr[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/ratio_14hr.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
ratio_flight_fig = plt.figure(figsize=(8, 6))

ratio_flight = plt.hist2d(
    df_flight[3],
    df_flight[4],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top + Mid + Bot (mV)")
plt.ylabel("(Max-Min)/(Top + Mid + Bot)")
plt.title("Range/(total mV) vs total mV Full Flight Event Heatmap - All Events")

plt.colorbar(ratio_flight[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/ratio_flight.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
ratio_flight_seg3_fig = plt.figure(figsize=(8, 6))

ratio_flight_seg3 = plt.hist2d(
    df_flight_seg3[3],
    df_flight_seg3[4],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top + Mid + Bot (mV)")
plt.ylabel("(Max-Min)/(Top + Mid + Bot)")
plt.title("Range/(total mV) vs total mV High Altitude Flight Event Heatmap - All Events")

plt.colorbar(ratio_flight_seg3[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/ratio_flight_seg3.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
ratio_feb1_fig = plt.figure(figsize=(8, 6))

ratio_feb1 = plt.hist2d(
    df_feb1[0],
    df_feb1[1],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top + Mid (mV)")
plt.ylabel("(Max-Min)/(Top + Mid)")
plt.title("Range/(total mV) vs total mV February 1st Event Heatmap - All Events")

plt.colorbar(ratio_feb1[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/ratio_feb1.png")
plt.close()

#======================================================================================================================================
# CUTS
#======================================================================================================================================
ratio_14hr_cut_fig = plt.figure(figsize=(8, 6))

ratio_14hr_cut = plt.hist2d(
    df_14hr_cut[3],
    df_14hr_cut[4],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top + Mid + Bot (mV)")
plt.ylabel("(Max-Min)/(Top + Mid + Bot)")
plt.title("Range/(total mV) vs total mV 14 Hour Ground Test Event Heatmap - Anomalous Events")

plt.colorbar(ratio_14hr_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/ratio_14hr_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
ratio_flight_cut_fig = plt.figure(figsize=(8, 6))

ratio_flight_cut = plt.hist2d(
    df_flight_cut[3],
    df_flight_cut[4],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top + Mid + Bot (mV)")
plt.ylabel("(Max-Min)/(Top + Mid + Bot)")
plt.title("Range/(total mV) vs total mV Full Flight Event Heatmap - Anomalous Events")

plt.colorbar(ratio_flight_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/ratio_flight_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
ratio_flight_seg3_cut_fig = plt.figure(figsize=(8, 6))

ratio_flight_seg3_cut = plt.hist2d(
    df_flight_seg3_cut[3],
    df_flight_seg3_cut[4],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top + Mid + Bot (mV)")
plt.ylabel("(Max-Min)/(Top + Mid + Bot)")
plt.title("Range/(total mV) vs total mV High Altitude Flight Event Heatmap - Anomalous Events")

plt.colorbar(ratio_flight_seg3_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/ratio_flight_seg3_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
ratio_feb1_cut_fig = plt.figure(figsize=(8, 6))

ratio_feb1_cut = plt.hist2d(
    df_feb1_cut[0],
    df_feb1_cut[1],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Top + Mid (mV)")
plt.ylabel("(Max-Min)/(Top + Mid)")
plt.title("Range/(total mV) vs total mV February 1st Event Heatmap - Anomalous Events")

plt.colorbar(ratio_feb1_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/ratio_feb1_cut.png")
plt.close()


#======================================================================================================================================
#======================================================================================================================================
# STANDARD DEVIATION vs MEAN PLOTS
#======================================================================================================================================
#======================================================================================================================================
stdmean_14hr_fig = plt.figure(figsize=(8, 6))

stdmean_14hr = plt.hist2d(
    df_14hr["mean"],
    df_14hr["std"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mean (mV)")
plt.ylabel("Standard Deviation (mV)")
plt.title("Standard Deviation vs Mean 14 Hour Ground Test Event Heatmap - All Events")

plt.colorbar(stdmean_14hr[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/stdmean_14hr.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
stdmean_flight_fig = plt.figure(figsize=(8, 6))

stdmean_flight = plt.hist2d(
    df_flight["mean"],
    df_flight["std"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mean (mV)")
plt.ylabel("Standard Deviation (mV)")
plt.title("Standard Deviation vs Mean Full Flight Event Heatmap - All Events")

plt.colorbar(stdmean_flight[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/stdmean_flight.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
stdmean_flight_seg3_fig = plt.figure(figsize=(8, 6))

stdmean_flight_seg3 = plt.hist2d(
    df_flight_seg3["mean"],
    df_flight_seg3["std"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mean (mV)")
plt.ylabel("Standard Deviation (mV)")
plt.title("Standard Deviation vs Mean High Altitude Flight Event Heatmap - All Events")

plt.colorbar(stdmean_flight_seg3[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/stdmean_flight_seg3.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
stdmean_feb1_fig = plt.figure(figsize=(8, 6))

stdmean_feb1 = plt.hist2d(
    df_feb1["mean"],
    df_feb1["std"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mean (mV)")
plt.ylabel("Standard Deviation (mV)")
plt.title("Standard Deviation vs Mean February 1st Event Heatmap - All Events")

plt.colorbar(stdmean_feb1[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/stdmean_feb1.png")
plt.close()

#======================================================================================================================================
# CUTS
#======================================================================================================================================
stdmean_14hr_cut_fig = plt.figure(figsize=(8, 6))

stdmean_14hr_cut = plt.hist2d(
    df_14hr_cut["mean"],
    df_14hr_cut["std"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mean (mV)")
plt.ylabel("Standard Deviation (mV)")
plt.title("Standard Deviation vs Mean 14 Hour Ground Test Event Heatmap - Anomalous Events")

plt.colorbar(stdmean_14hr_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/stdmean_14hr_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
stdmean_flight_cut_fig = plt.figure(figsize=(8, 6))

stdmean_flight_cut = plt.hist2d(
    df_flight_cut["mean"],
    df_flight_cut["std"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mean (mV)")
plt.ylabel("Standard Deviation (mV)")
plt.title("Standard Deviation vs Mean Full Flight Event Heatmap - Anomalous Events")

plt.colorbar(stdmean_flight_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/stdmean_flight_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
stdmean_flight_seg3_cut_fig = plt.figure(figsize=(8, 6))

stdmean_flight_seg3_cut = plt.hist2d(
    df_flight_seg3_cut["mean"],
    df_flight_seg3_cut["std"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mean (mV)")
plt.ylabel("Standard Deviation (mV)")
plt.title("Standard Deviation vs Mean High Altitude Flight Event Heatmap - Anomalous Events")

plt.colorbar(stdmean_flight_seg3_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/stdmean_flight_seg3_cut.png")
plt.close()

#======================================================================================================================================
#======================================================================================================================================
stdmean_feb1_cut_fig = plt.figure(figsize=(8, 6))

stdmean_feb1_cut = plt.hist2d(
    df_feb1_cut["mean"],
    df_feb1_cut["std"],
    bins=100,
    cmap="viridis"
)

plt.xlabel("Mean (mV)")
plt.ylabel("Standard Deviation (mV)")
plt.title("Standard Deviation vs Mean February 1st Event Heatmap - Anomalous Events")

plt.colorbar(stdmean_feb1_cut[3], label="Event Count")
plt.tight_layout()
plt.savefig(f"{PLOTS_DIR}/stdmean_feb1_cut.png")
plt.close()

