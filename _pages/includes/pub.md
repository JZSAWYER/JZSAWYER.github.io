# 📝 Publications 

## 💻 Large Language Models
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">``EMNLP 2025``</div><img src='images/react.png' alt="sy   m" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

 [**REACT**: **R**epresentation **E**xtraction **A**nd **C**ontrollable **T**uning to Overcome Overfitting in LLM Knowledge Editing](https://arxiv.org/pdf/2505.18933.pdf) \\
**Haitian Zhong**, Yuhuan Liu, Ziyang Xu, Guofan Liu, Qiang Liu, Shu Wu, Zhe Zhao, Liang Wang, Tieniu Tan

- **Abstract**: Large language model editing methods frequently suffer from overfitting, wherein factual updates can propagate beyond their intended scope, overemphasizing the edited target even when it's contextually inappropriate. To address this challenge, we introduce **REACT** (**R**epresentation **E**xtraction **A**nd **C**ontrollable **T**uning), a unified two-phase framework designed for precise and controllable knowledge editing. In the initial phase, we utilize tailored stimuli to extract latent factual representations and apply Principal Component Analysis with a simple learnbale linear transformation to compute a directional "belief shift" vector for each instance. In the second phase, we apply controllable perturbations to hidden states using the obtained vector with a magnitude scalar, gated by a pre-trained classifier that permits edits only when contextually necessary. Relevant experiments on EVOKE benchmarks demonstrate that **REACT** significantly reduces overfitting across nearly all evaluation metrics, and experiments on COUNTERFACT and MQuAKE shows that our method preserves balanced basic editing performance (reliability, locality, and generality) under diverse editing scenarios.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">``NeurIPS 2024``</div><img src='images/vlkeb.png' alt="sy   m" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

 [**VLKEB**: A Large **V**ision-**L**anguage Model **K**nowledge **E**diting **B**enchmark](https://arxiv.org/pdf/2403.07350.pdf) \\
Han Huang<sup>&dagger;</sup>, **Haitian Zhong**<sup>&dagger;</sup>, Qiang Liu, Shu Wu, Liang Wang, Tieniu Tan

- **Abstract**: Recently, knowledge editing on large language models (LLMs) has received considerable attention. Compared to this, editing Large Vision-Language Models (LVLMs) faces extra challenges from diverse data modalities and complicated model components, and data for LVLMs editing are limited. The existing LVLM editing benchmark, which comprises three metrics (Reliability, Locality, and Generality), falls short in the quality of synthesized evaluation images and cannot assess whether models apply edited knowledge in relevant content. Therefore, we employ more reliable data collection methods to construct a new Large **V**ision-**L**anguage Model **K**nowledge **E**diting **B**enchmark, **VLKEB**, and extend the Portability metric for more comprehensive evaluation. Leveraging a multi-modal knowledge graph, our image data are bound with knowledge entities. This can be further used to extract entity-related knowledge, which constitutes the base of editing data. We conduct experiments of different editing methods on five LVLMs, and thoroughly analyze how do they impact the models. The results reveal strengths and deficiencies of these methods and hopefully provide insights for future research.

- **Codes**: [![](https://img.shields.io/github/stars/VLKEB/VLKEB?style=social&label=VLKEB)](https://github.com/VLKEB/VLKEB)

- **Dataset**: [Kaggle](https://www.kaggle.com/datasets/hymanh/vlkeb-data); [huggingface](https://huggingface.co/datasets/HymanH/VLKEB-data).
</div>
</div>

## 🧬 AI for Science
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE J-BHI</div><img src='images/ptransips.png' alt="sy   m" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PTransIPs: Identification of phosphorylation sites enhanced by protein PLM embeddings](https://ieeexplore.ieee.org/abstract/document/10472595/) \\
Ziyang Xu<sup>&dagger;</sup>, **Haitian Zhong**<sup>&dagger;</sup>, Bingrui He, Xueying Wang, Tianchi Lu

- **Work**: We present PTransIPs, **a new deep learning framework for the identification of phosphorylation sites** in host cells infected with SARS-CoV-2. It utilizes protein pre-trained language model (PLM) embeddings and transformer structure to make the final prediction, with transductive information maximization (TIM) loss to better evaluate the error. PTransIPs is also a universal framework for all peptide bioactivity tasks.

- **Performance**: After comparing PTransIPs with five existing phosphorylation site prediction tools, we notice it achieves **the best performance in all five model evaluation metrics (ACC, SEN, SPEC, MCC, AUC) for both S/T and Y sites**.

- **Impact**: We hope that PTransIPs will aid in deepening the understanding of SARS-CoV-2 phosphorylation sites and look forward to enhancing PTransIPs in the future to become a more powerful tool for the scientific community.

- **Codes**: [![](https://img.shields.io/github/stars/StatXzy7/PTransIPs?style=social&label=PTransIPs)](https://github.com/StatXzy7/PTransIPs)

</div>
</div>

<!-- ## 📄 Manuscripts -->