# 📝 Publications 

## 🧬 AI for Science
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE J-BHI</div><img src='images/ptransips.png' alt="sy   m" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PTransIPs: Identification of phosphorylation sites enhanced by protein PLM embeddings](https://arxiv.org/pdf/2308.05115.pdf) \\
Ziyang Xu<sup>&dagger;</sup>, **Haitian Zhong**<sup>&dagger;</sup>, Bingrui He, Xueying Wang, Tianchi Lu

- **Work**: We present PTransIPs, **a new deep learning framework for the identification of phosphorylation sites** in host cells infected with SARS-CoV-2. It utilizes protein pre-trained language model (PLM) embeddings and transformer structure to make the final prediction, with transductive information maximization (TIM) loss to better evaluate the error. PTransIPs is also a universal framework for all peptide bioactivity tasks.

- **Performance**: After comparing PTransIPs with five existing phosphorylation site prediction tools, we notice it achieves **the best performance in all five model evaluation metrics (ACC, SEN, SPEC, MCC, AUC) for both S/T and Y sites**.

- **Impact**: We hope that PTransIPs will aid in deepening the understanding of SARS-CoV-2 phosphorylation sites and look forward to enhancing PTransIPs in the future to become a more powerful tool for the scientific community.

- **Codes**: [![](https://img.shields.io/github/stars/StatXzy7/PTransIPs?style=social&label=PTransIPs)](https://github.com/StatXzy7/PTransIPs)

</div>
</div>

## 📄 Manuscripts
``arXiv:2403.07350`` [ViKEB: A LVLM Knowledge Editing Benchmark](https://arxiv.org/pdf/2403.07350.pdf) \\
Han Huang<sup>&dagger;</sup>, **Haitian Zhong**<sup>&dagger;</sup>, Qiang Liu, Shu Wu, Liang Wang, Tieniu Tan

- **Abstract**: Currently, little research has been done on knowledge editing for Large Vision-Language Models (LVLMs). Editing LVLMs faces the challenge of effectively integrating diverse modalities (image and text) while ensuring coherent and contextually relevant modifications. An existing benchmark has three metrics (Reliability, Locality and Generality) to measure knowledge editing for LVLMs. However, the benchmark falls short in the quality of generated images used in evaluation and cannot assess whether models effectively utilize edited knowledge in relation to the associated content. We **adopt different data collection methods to construct a new benchmark, ViKEB, and extend new metric (Portability) for a comprehensive evaluation**. Leveraging a multimodal knowledge graph, our image data exhibits clear directionality towards entities. This directional aspect can be further utilized to extract entity-related knowledge and form editing data. We conducted experiments of different editing methods on five LVLMs, and thoroughly analyze how these methods impact the models. The results reveal strengths and deficiencies of these methods and, hopefully, provide insights into potential avenues for future research.

- **Codes**: Coming soon
