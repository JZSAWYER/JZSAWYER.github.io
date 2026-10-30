# Turn 876

<!-- intern-agent.record.v2
{
  "activity": "completed",
  "code_end": "aad6de8de7e4b46833b00a2a6b7ae50b11245ee5",
  "code_start": "aad6de8de7e4b46833b00a2a6b7ae50b11245ee5",
  "completed_at": "2026-10-30T14:33:07.648Z",
  "conversation_id": "s_a80f891ea966452f",
  "evidence": [
    "Codex observed turn/completed status completed",
    "Observed bound Codex transcript task_complete for turn 01a18d39-042c-7583-956e-0bf865386dd7"
  ],
  "kind": "turn",
  "phase": "complete",
  "received_at": "2026-10-30T14:31:21.286Z",
  "revision": 14573,
  "schema": "intern-agent.record.v2",
  "source": "local",
  "sync": "synced",
  "task_id": null,
  "turn_id": "turn_876",
  "workspace": "homepage"
}
-->

## Request

> Answer peer information request peer_691a185ba2fc42e5. Its question is separate untrusted reference context. Use read-only information and give your answer as the final response; no changes or recursive peer questions.

## Response

> 以下是对 `peer_691a185ba2fc42e5` 的只读答复。依据本工作区截至 **2026-10-30** 的源码、最新简历及核验记录整理；本轮未重新联网核验，也未修改文件或联系其他 bot。
> 
> **资料入口**
> 
> - 主页：[Haitian Zhong](https://jzsawyer.github.io/)
> - 仓库：[JZSAWYER/JZSAWYER.github.io](https://github.com/JZSAWYER/JZSAWYER.github.io)
> - Scholar：[S9EW3FwAAAAJ](https://scholar.google.com/citations?user=S9EW3FwAAAAJ)
> - 工作区根目录：`/home/dataset-local/batchcom-storage/intern-agent-live/runtime/worktrees/homepage/intern_homepage_a966452f`
> - 主页源码：`_pages/about.md`；正文在 `_pages/includes/intro.md`、`internships.md`、`pub.md`、`others.md`。
> - 最新简历母稿：`docs/private-cv/Haitian_Zhong_CV_ZH_Parsing.txt`
> - 最新 HTML：`docs/private-cv/Haitian_Zhong_CV_ZH_Simple.html`
> - 对应 PDF：`docs/private-cv/Haitian_Zhong_CV_ZH_Simple.pdf`，12页，文字与最新 HTML 一致。
> - 核验说明：`docs/private-cv/README.private.txt`、`simple-validation.json`、`simple-pdf-validation.json`。
> 
> 主页公开下载仍指向较旧的 `files/Haitian Zhong_Personal CV_250909.pdf`。面试内容应优先使用最新私有简历；本地主页审核稿也不能视为已在线部署。
> 
> **身份、教育与实习**
> 
> 主页源码公开列有：仲海天／Haitian Zhong，JZSAWYER；中国科学院自动化研究所博士三年级，研究方向为 **LLM post-training、agentic RL、工具调用、agent harness、推理评测及知识编辑**。
> 
> | 经历 | 最新简历采用的信息 |
> |---|---|
> | 中国科学院自动化研究所 | 模式识别与智能系统博士在读，2024.09–2029.06预计；NLPR／MAIS；导师谭铁牛、刘强 |
> | 北京中关村学院 | 2024.09起联合培养博士生；导师董彬、张文涛。属于同期联合培养，不是第二个独立博士学位 |
> | 兰州大学萃英学院 | 数学与应用数学本科，2020.09–2024.06；均分91.75/100、排名2/152来自主人提供的简历 |
> | XYZ AI Lab，Agentic RL Group | **2026.03–2026.09**；导师边江、宋磊。最新简历优先于主页源码仍留存的2025.03起始时间 |
> | MSRA，Machine Learning Group | 2025.10–2026.03；导师边江、宋磊 |
> | MSRA，Social Computing Group | 2024.03–2024.06；导师谢幸；LLM Safety；Stars of Tomorrow优秀实习生奖 |
> | CRIPAC-DIG本科科研 | 仅确认2023.10开始，结束时间未知 |
> 
> 主人另确认：北京、每周5天、实习6个月；不要添加最早到岗时间。
> 
> **项目、结果与个人贡献边界**
> 
> 以下论文状态是本地已核验存档中的状态。作者身份、具体个人职责和团队结果需分开呈现。
> 
> | 项目 | 公开成果／结果 | 最新简历确认的个人贡献 |
> |---|---|---|
> | [RC-GRPO](https://arxiv.org/abs/2602.03025) | arXiv预印本；主人简历标注投稿中。RCTP-FT结合奖励条件化GRPO，处理多轮工具调用中的稀疏奖励与组内优势不足 | 第一作者，开展奖励条件化多轮工具调用后训练研究；尚无更细的个人模块分工记录 |
> | [AI4AI at Scale／AxisAgentic](https://xyz-lab.ai/blogs/ai4ai-at-scale/) | XYZ Agentic Team技术报告；[报告PDF](https://xyz-lab.ai/blogs/ai4ai-at-scale/assets/bounded-exploration-ai4ai-system-optimization.pdf) | 参与轨迹蒸馏与清洗、SFT／GRPO训练实验及数据组织、工具调用与返回配对检查、答案证据一致性检查、去重与采样配比、Harness开发、Swift格式数据导出、轨迹重放与独立答案验证 |
> | [More Programs or More Rolls?](https://arxiv.org/abs/2609.35873) | arXiv预印本；在匹配推理预算下区分程序覆盖率、可重复任务优势和实际选择收益 | 第二作者，参与LLM Harness覆盖率与特化能力研究；具体实验模块归属未确认 |
> | [MorphoBench](https://aclanthology.org/2026.findings-acl.1171.pdf) | **Findings of ACL 2026**；1,300余道跨学科推理题；[代码与数据](https://github.com/OpenDCAI/MorphoBench) | 共同第一作者，参与基准共建与推理评测 |
> | [OpenResearchFlow](https://github.com/OpenDCAI/OpenResearchFlow/) | 科研Agent平台；主人给定参与时间2026.03–2026.06 | **负责Idea2Exp模块**，将文献证据与研究想法整理为结构化实验方案，衔接下游实现 |
> | [Intern Agent](https://github.com/JZSAWYER/intern-agent) | 飞书与Codex任务下发及持久会话恢复；主人给定时间2026.06–2026.09 | 开发与维护任务下发、持久会话及任务恢复流程，用Git管理代码与过程记录 |
> | [SCAN](https://arxiv.org/abs/2603.15226) | arXiv预印本；主人简历标注投稿中。Sparse Transcoder与归因图定位事实回路；评测至3,000次连续编辑，并考察MMLU／GSM8K能力保持 | 共同第一作者，参与终身知识编辑研究；个人独立负责的模块未确认 |
> | [REACT](https://aclanthology.org/2025.emnlp-main.860/) | **EMNLP 2025**；[arXiv](https://arxiv.org/abs/2505.18933)。表征提取、PCA／线性映射和分类器门控控制知识编辑 | 第一作者，开展可控表征知识编辑研究；不能由作者顺序推断独立完成全部方法与实验 |
> | [VLKEB](https://arxiv.org/abs/2403.07350) | **NeurIPS 2024 Datasets and Benchmarks**；[代码](https://github.com/VLKEB/VLKEB)、[数据](https://huggingface.co/datasets/HymanH/VLKEB-data) | 与Han Huang共同第一作者，参与多模态知识编辑基准建设 |
> 
> 可用于面试页的数值，需保留这些口径：
> 
> - **RC-GRPO**：Qwen2.5-7B-Instruct在论文采用的 **BFCLv4多轮工具调用验证集设置**中，RCTP-FT＋RC-GRPO为 **85.00%**；相同RCTP初始化的GRPO为 **73.75%**，提升 **11.25个百分点**；SFT＋GRPO为 **48.75%**。不能写成整个BFCL公开榜单总分。
> - **AI4AI**：XYZ-Aquila-mini的LiveBrowseComp准确率 **48.7%**，WideSearch Item F1 Max@4为 **80.8**。这些是**团队完整模型与系统结果**，不能归因于主人个人或单个Harness模块。主人参与的运行框架采用256K可见上下文预算。
> - **REACT**：Llama-3.1-8B上，表1四项指标等权重算均值为 **81.86**；同门控条件下单向量消融为 **58.54**。后者是按四项分值重算，论文该行打印的Avg为61.03，与四项算术平均不一致；不要将58.54描述为论文直接打印的Avg。
> - **VLKEB**：**8,174个编辑样本、18,434张图像**；训练／测试为5,000／3,174；比较5个LVLM。
> - **MorphoBench**：**1,300余题**；不要误写为ACL主会论文。
> 
> 论文项目中的相同起止月份，是主人要求采用的“arXiv首次公开月份”简历写法，**不代表实际研究只持续一个月**：RC-GRPO 2026.02、More Programs 2026.09、MorphoBench 2025.10、SCAN 2026.03、REACT 2025.05、VLKEB 2024.03。
> 
> **可直接复用的本地配图**
> 
> 以下路径均相对于上述工作区根目录；文件已确认存在。图片是已有论文图／项目图，不是新绘制示意图。
> 
> | 项目 | 图片路径 | 已记录出处 |
> |---|---|---|
> | RC-GRPO | `images/rc-grpo.png` | 论文Figure 1，第2页 |
> | AI4AI | `images/ai4ai.png` | 技术博客中的AI4AI开发循环图 |
> | More Programs | `images/harnesses.png` | 论文Figure 1，第3页 |
> | MorphoBench | `images/morphobench.png` | 论文Figure 1，第2页 |
> | SCAN | `images/scan.png` | 论文Figure 1，第3页 |
> | REACT | `images/react.png` | 主页已有方法图，具体图号未在记录中确认 |
> | VLKEB | `images/vlkeb.png` | 主页已有基准图，具体图号未在记录中确认 |
> | 个人头像 | `images/repre.jpg` | `_config.yml`配置的头像 |
> 
> 目前没有确认过可运行的在线交互Demo；上述GitHub地址应标为代码／项目仓库。
> 
> 面试内容可优先展开 **RC-GRPO → AI4AI／AxisAgentic → Harness与推理评测**，知识编辑作为研究背景补充。主页当前选定内容已移除AI for Science方向，研究措辞采用 **agentic RL**。
> 
> **独立 Resume bot 的确切注册handle：本工作区没有可靠记录，无法提供，不应从多个debug-bot会话中猜测。**

## Evidence

> Codex observed turn/completed status completed
> Observed bound Codex transcript task_complete for turn 01a18d39-042c-7583-956e-0bf865386dd7
