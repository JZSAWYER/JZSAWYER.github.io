<span class="anchor" id="-publications"></span>

# 📝 Publications

<sup>&dagger;</sup> Equal contribution.

<div class="publication-filters" role="group" aria-label="Filter publications" hidden>
  <button type="button" data-publication-filter="all" aria-pressed="true">All <span>7</span></button>
  <button type="button" data-publication-filter="post-training" aria-pressed="false">Post-training <span>4</span></button>
  <button type="button" data-publication-filter="knowledge-editing" aria-pressed="false">Knowledge Editing <span>3</span></button>
</div>
<span id="publication-status" class="visually-hidden" role="status" aria-live="polite"></span>

<div class="publication-group" data-publication-topic="post-training" markdown="1">

## Post-training

Agent post-training, tool use, harnesses, and reasoning evaluation.

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='images/rc-grpo.png' alt="Overview of reward-conditioned trajectory training and RC-GRPO rollouts" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**RC-GRPO**: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents](https://arxiv.org/abs/2602.03025) \\
**Haitian Zhong**, Jixiu Zhai, Lei Song, Jiang Bian, Qiang Liu, Tieniu Tan

- **Abstract**: Multi-turn tool-calling agents face sparse rewards, and GRPO updates can stall when rollouts within a group receive identical rewards. **RC-GRPO** first learns a reward-conditioned trajectory policy from mixed-quality examples, then varies reward tokens during RL to encourage informative exploration. We evaluate the approach on BFCLv4 multi-turn tool-calling tasks, studying both task performance and training dynamics.


</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Technical Report 2026</div><img src='images/ai4ai.png' alt="The bounded AI4AI development loop with an independent evaluation gate" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**AI4AI at Scale**: A Full-Pipeline System for Enhancing LLM Agentic Capabilities](https://xyz-lab.ai/blogs/ai4ai-at-scale/assets/bounded-exploration-ai4ai-system-optimization.pdf) \\
XYZ Agentic Team

- **Abstract**: This team report presents an agent-assisted development loop for deep search systems, spanning task construction, supervised post-training, runtime behavior, context management, and replay infrastructure. The released XYZ-Aquila systems are evaluated across seven search benchmarks. Reported scores describe the complete systems; they do not isolate the effect of an individual component or contributor.

- **Project**: [Technical blog and report](https://xyz-lab.ai/blogs/ai4ai-at-scale/).
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='images/harnesses.png' alt="Controlled evaluation of generated harnesses and repeated baseline executions" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**More Programs or More Rolls?** Separating Coverage from Specialization in LLM Harnesses](https://arxiv.org/abs/2609.35873) \\
Ziyang Xu, **Haitian Zhong**, Hao Zhou, Hao Qin, Chenhan Jin, Te Qi, Shengze Xu, Tieyong Zeng

- **Abstract**: Does generating different agent programs provide useful specialization beyond simply running the same program more often? We compare generated harnesses with repeated executions of identical baselines under matched inference budgets. The study separates answer coverage from repeatable task advantages and usable selection gains, showing why broader oracle coverage alone does not establish useful specialization.


</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Findings of ACL 2026</div><img src='images/morphobench.png' alt="MorphoBench adaptive reasoning benchmark and question transformation pipeline" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**MorphoBench**: A Benchmark with Difficulty Adaptive to Model Reasoning](https://aclanthology.org/2026.findings-acl.1171.pdf) \\
Xukai Wang<sup>&dagger;</sup>, Xuanbo Liu<sup>&dagger;</sup>, Mingrui Chen<sup>&dagger;</sup>, **Haitian Zhong**<sup>&dagger;</sup>, Xuanlin Yang<sup>&dagger;</sup>, Bohan Zeng<sup>&dagger;</sup>, Jinbo Hu, Hao Liang, Junbo Niu, Xuchen Li, Ruitao Wu, Ruichuan An, Yang Shi, Liu Liu, Xu-Yao Zhang, Qiang Liu, Zhouchen Lin, Wentao Zhang, Bin Dong

- **Abstract**: **MorphoBench** evaluates model reasoning with more than 1,300 multidisciplinary questions whose difficulty can evolve as models improve. It combines challenging source problems with reasoning-based question transformations and simulation-generated tasks. Adaptive difficulty and reasoning diagnostics help examine capabilities beyond performance on a fixed set of questions.

- **Codes and Data**: [GitHub](https://github.com/OpenDCAI/MorphoBench).


</div>
</div>

</div>

<div class="publication-group" data-publication-topic="knowledge-editing" markdown="1">

## Knowledge Editing

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='images/scan.png' alt="SCAN sparse circuit localization and targeted knowledge editing framework" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**SCAN**: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing](https://arxiv.org/abs/2603.15226) \\
Yuhuan Liu<sup>&dagger;</sup>, **Haitian Zhong**<sup>&dagger;</sup>, Xinyuan Xia, Qiang Liu, Shu Wu, Liang Wang

- **Abstract**: Repeated knowledge edits can disrupt previously stored facts and general model abilities. **SCAN** uses sparse transcoders and attribution graphs to locate fact-specific circuits and guide targeted editing. Experiments on multiple model families examine editing quality and retention of general capabilities, including MMLU and GSM8K, through sequences of up to 3,000 edits.


</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">``EMNLP 2025``</div><img src='images/react.png' alt="Overview of REACT knowledge editing" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

 [**REACT**: **R**epresentation **E**xtraction **A**nd **C**ontrollable **T**uning to Overcome Overfitting in LLM Knowledge Editing](https://arxiv.org/pdf/2505.18933.pdf) \\
**Haitian Zhong**, Yuhuan Liu, Ziyang Xu, Guofan Liu, Qiang Liu, Shu Wu, Zhe Zhao, Liang Wang, Tieniu Tan

- **Abstract**: Large language model editing methods frequently suffer from overfitting, wherein factual updates can propagate beyond their intended scope, overemphasizing the edited target even when it's contextually inappropriate. To address this challenge, we introduce **REACT** (**R**epresentation **E**xtraction **A**nd **C**ontrollable **T**uning), a unified two-phase framework designed for precise and controllable knowledge editing. In the initial phase, we utilize tailored stimuli to extract latent factual representations and apply Principal Component Analysis with a simple learnable linear transformation to compute a directional "belief shift" vector for each instance. In the second phase, we apply controllable perturbations to hidden states using the obtained vector with a magnitude scalar, gated by a pre-trained classifier that permits edits only when contextually necessary. Relevant experiments on EVOKE benchmarks demonstrate that **REACT** significantly reduces overfitting across nearly all evaluation metrics, and experiments on COUNTERFACT and MQuAKE show that our method preserves balanced basic editing performance (reliability, locality, and generality) under diverse editing scenarios.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">``NeurIPS 2024 D&B``</div><img src='images/vlkeb.png' alt="Overview of the VLKEB benchmark" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

 [**VLKEB**: A Large **V**ision-**L**anguage Model **K**nowledge **E**diting **B**enchmark](https://arxiv.org/pdf/2403.07350.pdf) \\
Han Huang<sup>&dagger;</sup>, **Haitian Zhong**<sup>&dagger;</sup>, Tao Yu, Qiang Liu, Shu Wu, Liang Wang, Tieniu Tan

- **Abstract**: Recently, knowledge editing on large language models (LLMs) has received considerable attention. Compared to this, editing Large Vision-Language Models (LVLMs) faces extra challenges from diverse data modalities and complicated model components, and data for LVLMs editing are limited. The existing LVLM editing benchmark, which comprises three metrics (Reliability, Locality, and Generality), falls short in the quality of synthesized evaluation images and cannot assess whether models apply edited knowledge in relevant content. Therefore, we employ more reliable data collection methods to construct a new Large **V**ision-**L**anguage Model **K**nowledge **E**diting **B**enchmark, **VLKEB**, and extend the Portability metric for more comprehensive evaluation. Leveraging a multi-modal knowledge graph, our image data are bound with knowledge entities. This can be further used to extract entity-related knowledge, which constitutes the base of editing data. We conduct experiments of different editing methods on five LVLMs, and thoroughly analyze how do they impact the models. The results reveal strengths and deficiencies of these methods and hopefully provide insights for future research.

- **Codes**: [![](https://img.shields.io/github/stars/VLKEB/VLKEB?style=social&label=VLKEB)](https://github.com/VLKEB/VLKEB)

- **Dataset**: [Kaggle](https://www.kaggle.com/datasets/hymanh/vlkeb-data); [huggingface](https://huggingface.co/datasets/HymanH/VLKEB-data).
</div>
</div>

</div>
