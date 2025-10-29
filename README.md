

<p align="center">
  <img src="/assets/naip_hr.png" alt="NAIP Logo" width="30%" style="border: 4px solid #231815; border-radius: 12px; padding: 5px;">
</p>

# Framework for Newborn Article Impact Prediction & Quality Estimation.

<p align="center">
&nbsp;&nbsp;📊 <a href="https://huggingface.co/ssocean/NAIP">NAIP-v1-weights</a>&nbsp;&nbsp | &nbsp;&nbsp;📈 <a href="https://huggingface.co/ssocean/NAIPv2">NAIP-v2-weights</a>&nbsp;&nbsp | &nbsp;&nbsp;🤗 <a href="https://huggingface.co/spaces/ssocean/Newborn_Article_Impact_Predict">Hugging Face Demo</a>&nbsp;&nbsp 
<br>
&nbsp;&nbsp; 📑 <a href="https://sway.cloud.microsoft/KOH09sPR21Ubojbc">v1 Homepage</a> &nbsp;&nbsp; | &nbsp;&nbsp;📑 <a href="https://sway.cloud.microsoft/Pr42npP80MfPhvj8">v2 Homepage</a>
</p>


## Overview 

The NAIP series leverages large language models (LLMs) to efficiently assess the potential impact and quality of research articles through analysis of their intrinsic content. NAIP-v1 focuses on regressing a field- and time-normalized score (TNCSIsp) as a quantitative indicator of scientific impact, while NAIP-v2 aims to model human preferences in the peer-review process by learning from pairwise review data.

<p align="center">
  <img src="/assets/typo.png" alt="NAIP Framework Overview" width="100%">
</p>


| Version | Input              | Output                  | Model Weights                                                               | Homepage                                                                 | Paper                                                                     |
|---------|--------------------|-------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------|
| v1      | Title & Abstract   | Impact Estimation (0–1) | [Link](https://huggingface.co/ssocean/NAIP)                                 | [Link](https://sway.cloud.microsoft/KOH09sPR21Ubojbc)                    | [AAAI 2025](https://ojs.aaai.org/index.php/AAAI/article/view/32106/34261) |
| v2      | Title & Abstract   | Quality Estimation      | [Link](https://huggingface.co/ssocean/NAIPv2)                               | [Link](https://sway.cloud.microsoft/Pr42npP80MfPhvj8)                    | [arXiv](https://arxiv.org/abs/2509.25179)                                 |

[//]: # (This repository contains the official implementation for the paper [**"From Words to Worth: Newborn Article Impact Prediction with LLM"**]&#40;https://sway.cloud.microsoft/KOH09sPR21Ubojbc&#41;. The tool is designed to PEFT the LLMs for the prediction of the future impact.)



## 🚀 **Update Log**
- **250930 – Introducing NAIPv2: extending the series with an emphasis on quality estimation.**
- **241210 - The paper has now been accepted by AAAI 2025!**
- **241204 - Huggingface Spaces Support🥰** 
  - We've set up an online demo on Hugging Face Spaces—now you can easily give it a try without writing a single line of code!
- **241126 - V1.0**  We’re thrilled to announce the end of Early Access and the official release of V1.0! ✨
  - The codebase is now more organized and easier to navigate! 🧹  
  - Updated and streamlined README with detailed instructions for setup and usage. 💡
  - Decoupling the dataset, more LoRa adapters weight download links, and more! 🔄  
  - Known Issues: The functionality for building the NAID dataset has not been tested on other machines, which may lead to potential issues. We plan to replace this function with a more powerful framefowk in our [another codebase](https://github.com/ssocean/PyBiblion).
- **240808 - Eerly Access**   
  - We have released the Early Access version of our code！


## Quick Deployment (for most researchers)
First, pull the repo and type following commands in the console:
```
git clone https://github.com/ssocean/NAIP.git
cd NAIP
pip install -r requirements.txt
```
- To try **v1**, please use `demo_v1.py`.  
- To try **v2**, please use `demo_v2.py`.  
- You may need to download the corresponding model weights.  
- When providing the **title** and **abstract**, please avoid line breaks, LaTeX symbols, or other special formatting.  

## How to Reproduce
### NAIPv1 
Prepare `train.sh` bash file like below to fine-tune NAIPv1:
```
DATA_PATH="NAIP/v1_resource/NAIDv1/NAID_train_extrainfo.csv"
TEST_DATA_PATH="NAIP/v1_resource/NAIDv1/NAID_test_extrainfo.csv"

OMP_NUM_THREADS=1 accelerate launch NAIP/v1_resource/v1_finetune.py \
    --total_epochs 5 \
    --learning_rate 1e-4 \
    --data_path $DATA_PATH \
    --test_data_path $TEST_DATA_PATH \
    --runs_dir official_runs/LLAMA3 \
    --checkpoint  path_to_huggingface_LLaMA3
```

Similar to fine-tuning, prepare `test.sh` as below:
```
python NAIP/v1_resource/v1_test.py \
 --data_path NAIP/NAID/NAID_test_extrainfo.csv \
 --weight_dir path_to_runs_dir
```
Then, type `sh test.sh`.


### NAIPv2
Check `NAIP/v2_resource/shell/fine-tune.sh` and modify depend on your situation.


## 🛠️ Free Support for Academic Use

To ensure that research comparisons with **NAIP** are carried out under consistent and reproducible conditions, we provide **free technical assistance** for researchers who may encounter challenges in environment setup or code reproduction.  

You may send a `.jsonl` file containing the **"title"** and **"abstract"** fields, and we will return the corresponding prediction results.  

The `jsonl` file template is provided in `./assets/free_inference_template.jsonl`

- In urgent cases, results can usually be provided **within one day**.  
- This support is intended solely to facilitate rigorous and reproducible evaluation within the research community and is not available for commercial use or requests.

- 📩 Contact: [oceanytech@gmail.com] 


## 📚 Citation
If you find this work useful, please cite:

```bibtex
@article{Zhao2024NAIP,
  title={From Words to Worth: Newborn Article Impact Prediction with LLM},
  author={Penghai Zhao and Qinghua Xing and Kairan Dou and Jinyu Tian and Ying Tai and Jian Yang and Ming-Ming Cheng and Xiang Li},
  journal={ArXiv},
  year={2024},
  volume={abs/2408.03934},
  url={https://api.semanticscholar.org/CorpusID:271744831}
}
```

