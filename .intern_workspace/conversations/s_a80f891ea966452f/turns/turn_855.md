# Turn 855

<!-- intern-agent.record.v2
{
  "activity": "completed",
  "code_end": "6ea47ba70d50baa20f0394f95c0d729c806bd924",
  "code_start": "fa8d4693ac741cae7e3d256ddfe6914c76a43aaa",
  "completed_at": "2026-10-30T08:42:53.416Z",
  "conversation_id": "s_a80f891ea966452f",
  "evidence": [
    "1 files attached in upload order to this unchanged message.",
    "Downloaded attachment Haitian_Zhong_PostTraining_ZH_Draft.pdf; SHA256 ec2171240ba6df7b0f0cf1f981dff999e9947c236080b7dfc8b2f8d92c659979",
    "Codex observed turn/completed status completed",
    "Observed bound Codex transcript task_complete for turn 01a18beb-5693-7ca3-8cdf-f02bb7494551"
  ],
  "kind": "turn",
  "phase": "complete",
  "received_at": "2026-10-30T08:26:51.999Z",
  "revision": 14363,
  "schema": "intern-agent.record.v2",
  "source": "feishu",
  "sync": "synced",
  "task_id": null,
  "turn_id": "turn_855",
  "workspace": "homepage"
}
-->

## Request

> referring to my homepage and my uploaded resume, generate a comprehensive chinese version of personal cv so that it can be parsed to fit into this kind of recruitment of internship: 
> - 
> 申请信息
> 内推码
> 4QJJ8JY
> 意向城市
> 最多可选 3 个城市
> 附件简历
> 将你的简历拖拽至此处
> 支持格式：PDF、DOC、DOCX、PPT、PPTX、PNG、JPG、JPEG、HTML
> 基础信息
> 请填写基本信息
> 姓名
> 仲海天
> 手机号码
> +86 159-9629-5520
> 邮箱
> haitian.zhong@cripac.ia.ac.cn haitian.zhong@cripac.ia.ac.cn
> 教育经历
> 请填写教育经历
> 学校
> 兰州大学
> 学历
> 专业
> 数学与应用数学
> 起止时间
> 无准确的毕业时间可填写预计毕业时间
> 学校
> 中国科学院自动化研究所
> 学历
> 专业
> 模式识别与智能系统
> 起止时间
> 无准确的毕业时间可填写预计毕业时间
> 学校
> 北京中关村学院
> 学历
> 专业
> 请输入
> 起止时间
> 无准确的毕业时间可填写预计毕业时间
> 添加
> 工作经历
> 没有工作经历
> 实习经历
> 请填写实习经历
> 公司
> XYZ AI Lab
> 职位
> 大模型算法实习生
> 起止时间
> 描述
> Agentic RL Group 研究助理； 导师：边江、宋磊
> 利用其他模型蒸馏并清洗多步搜索轨迹，开展 SFT＋GRPO 实验；检查工具调用／返回配对及答案－证据一致性，结合问题级去重、按任务限额采样与长短轨迹配比控制数据质量。
> AxisAgentic Harness 在 256K 可见上下文预算内结合搜索／网页抽取／有状态 Python、上下文压缩、网页分块抽取与工具错误恢复；通过上下文事件重放，基于模型可见历史导出 Swift 格式 SFT 数据， 支持训练与推理上下文一致性；结合轨迹重放与独立答案验证分析搜索失败。
> 我们的模型 XYZ－Aquila－mini：LiveBrowseComp 准确率 48.7％；WideSearch Item F1 Max＠4 80.8。
> 公司
> 微软亚洲研究院
> 职位
> 研究助理
> 起止时间
> 描述
> Machine Learning Group实习生，导师：边江、宋磊
> 公司
> 微软亚洲研究院
> 职位
> 实习
> 起止时间
> 描述
> Social Computing Group 实习生，LLM 安全；导师：谢幸
> 添加
> 项目经历
> 请填写项目经历
> 项目名称
> rc-grpo:多轮工具调用的奖励条件强化学习
> 项目角色
> 请输入
> 起止时间
> 项目链接
> 请输入
> 项目描述
> Haitian Zhong， Jixiu Zhai， Lei Song， …， Tieniu Tan  投稿中；arXiv：2602.03025
> • 面向 长程多轮工具调用（跨轮状态跟踪与连续函数执行）开展后训练，以 奖励条件轨迹微调（RCTP－FT）＋ token 条件化
> GRPO 缓解稀疏奖励下的优势消失。
> • 在 BFCLv4 multi－turn split（Berkeley Function Calling Leaderboard v4）上，Qwen2.5－7B－Instruct 达 85.00％；较同 RCTP 初始化 GRPO（73.75％）提升 11.25 个百分点，SFT＋GRPO 为 48.75％。
> 项目名称
> morphobench:推理难度自适应的跨学科评测基准
> 项目角色
> 请输入
> 起止时间
> 项目链接
> 请输入
> 项目描述
> Xukai Wang＊， Xuanbo Liu＊， Mingrui Chen＊， Haitian Zhong＊， …， Bin Dong  ACL Findings 2026
> • 共建 1，300＋ 道跨学科推理题，以推理链关键语句、提示／干扰和仿真生成自适应调节难度；用 LLM－as－judge 诊断逐步正确性与推理质量。［代码］。
> 项目名称
> scan:基于稀疏知识回路的终身知识编辑
> 项目角色
> 请输入
> 起止时间
> 项目链接
> 请输入
> 项目描述
> Yuhuan Liu＊， Haitian Zhong＊， Xinyuan Xia， …， Liang Wang  投稿中；arXiv：2603.15226
> • 以 Sparse Transcoder 与归因图 定位事实相关稀疏回路并定向编辑；评测扩展至 3，000 次连续编辑，检验 MMLU／GSM8K 通用能力保持，缓解累积编辑引发的遗忘与模型崩溃。
> 项目名称
> react:缓解大模型知识编辑过拟合
> 项目角色
> 请输入
> 起止时间
> 项目链接
> 请输入
> 项目描述
> Haitian Zhong， Yuhuan Liu， Ziyang Xu， …， Tieniu Tan  EMNLP 2025
> • 以 PCA／线性映射 ＋ 分类器门控 实现可控表征编辑；Llama－3.1－8B 在 COUNTERFACT／MQuAKE 上 四指标均值 81.86 vs。
> 58.54（单向量消融，按表重算）；另评测 EVOKE。
> 项目名称
> vlkeb:视觉语言大模型知识编辑基准
> 项目角色
> 请输入
> 起止时间
> 项目链接
> 请输入
> 项目描述
> Han Huang＊， Haitian Zhong＊， Tao Yu， …， Tieniu Tan  NeurIPS 2024 D＆B
> • 基于多模态知识图谱构建 8，174 个编辑样本、18，434 张图像 的基准，扩展 Portability 评测，在 5 个 LVLM 上比较单次与连续
> 编辑。［代码］。
>     更新日期：2026 年 10 月 30 日
> 添加
> 作品
> 添加
> 获奖
> 请填写获奖记录
> 奖项名称
> 甘肃省优秀毕业生
> 获奖时间
> 2024
> 描述
> 请输入
> 奖项名称
> 全国大学生数学竞赛二等奖
> 获奖时间
> YYYY
> 描述
> 全国大学生数学竞赛二等奖; 丘成桐大学生数学竞赛两项优胜奖、全国大学生英语竞赛全国一等奖。
> 奖项名称
> 全国大学生英语竞赛全国一等奖
> 获奖时间
> YYYY
> 描述
> 全国大学生数学竞赛二等奖; 丘成桐大学生数学竞赛两项优胜奖、全国大学生英语竞赛全国一等奖。
> 奖项名称
> 兰州大学出彩毕业生
> 获奖时间
> YYYY
> 描述
> 请输入
> 添加
> 语言能力
> 请填写语言能力
> 语言
> 精通程度
> 添加
> 社交账号
> you should place them not directly into these, but into more details(not required to fit into one page this time), and make sure its listed in these way, and make sure like a project should have 项目名称
> 项目角色
> 请输入
> 起止时间
> 项目链接
> 请输入
> 项目描述
> all these items, not just in the previous simple way, this cv is just for parsing so include detail, be clear, no need to be beautiful or follow any format or style or pattern

## Response

> 请补充希望写入简历的意向城市（最多3个）、最早到岗时间、每周可实习天数和预计实习时长；暂未确定的项目我会保留为“待补充”。
> 
> 已发送 **PDF（10页）、HTML 和 TXT**，可直接上传 PDF 或 HTML。
> 
> 内容包含3段高等教育、4段实习／科研经历、9个项目和13项获奖／荣誉。每个项目均完整列出：**项目名称、项目角色、起止时间、项目链接、项目描述**。
> 
> 已填写北京、每周5天、实习6个月，未列到岗时间。缺少依据的项目月份等标为“待补充”。PDF、HTML 的全文提取校验均通过。
> 
> DOCX 被导出检查误判拦截，原因是 Word 标准的 `.rels` 文件被识别为私有路径，因此改发了 HTML。

## Evidence

> 1 files attached in upload order to this unchanged message.
> Downloaded attachment Haitian_Zhong_PostTraining_ZH_Draft.pdf; SHA256 ec2171240ba6df7b0f0cf1f981dff999e9947c236080b7dfc8b2f8d92c659979
> Codex observed turn/completed status completed
> Observed bound Codex transcript task_complete for turn 01a18beb-5693-7ca3-8cdf-f02bb7494551
