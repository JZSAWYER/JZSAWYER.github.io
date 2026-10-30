# Turn 864

<!-- intern-agent.record.v2
{
  "activity": "completed",
  "code_end": "806542eb17f8d71907758fae272ff5ef9886564e",
  "code_start": "806542eb17f8d71907758fae272ff5ef9886564e",
  "completed_at": "2026-10-30T09:26:30.004Z",
  "conversation_id": "s_a80f891ea966452f",
  "evidence": [
    "Delivered file Haitian_Zhong_CV_ZH_Fields.html; SHA256 472cf559946020c96432ef8525c92a287c1f5b5e72d4eff7cd222499eb214004",
    "Codex observed turn/completed status completed",
    "Observed bound Codex transcript task_complete for turn 01a18c1f-a150-7290-b10a-c404b3da621a"
  ],
  "kind": "turn",
  "phase": "complete",
  "received_at": "2026-10-30T09:23:54.044Z",
  "revision": 14457,
  "schema": "intern-agent.record.v2",
  "source": "feishu",
  "sync": "synced",
  "task_id": null,
  "turn_id": "turn_864",
  "workspace": "homepage"
}
-->

## Request

> 项目链接：
> 论文题目：RC－GRPO： Reward－Conditioned Group Relative Policy Optimization for Multi－Turn Tool Calling Agents
> 论文作者：Haitian Zhong， Jixiu Zhai， Lei Song， Jiang Bian， Qiang Liu， Tieniu Tan
> 论文状态：投稿中；已公开 arXiv 预印本
> 项目描述：
> 1. 研究背景：面向长程多轮工具调用中的跨轮状态跟踪和连续函数执行问题。稀疏奖励下，同一 GRPO 采样组可能获得全部为 0 或全部为 1 的奖励，导致组内优势信号不足和更新停滞。
> 2. 方法设计：采用奖励条件轨迹微调（RCTP－FT），在混合质量轨迹上引入离散奖励目标 token，让模型学习按不同奖励条件生成轨迹；强化学习阶段在同一组内采样不同奖励 token，引导更有区分度的探索。
> 3. 评测与对照：在论文采用的 BFCLv4 多轮工具调用验证集上，对比 SFT、GRPO、RCTP 初始化及奖励条件化组合，分析奖励条件与初始化分别带来的效果。
> 4. 结果：Qwen2.5－7B－Instruct 采用 RCTP－FT＋RC－GRPO 达到 85.00％准确率；相同 RCTP 初始化的 GRPO 为 73.75％，提升 11.25 个百分点；SFT＋GRPO 为 48.75％。上述结果对应论文的实验设置与验证集口径。
> 相关技术：Python、PyTorch、SFT、GRPO、奖励条件策略、多轮工具调用、BFCLv4、消融实验。
> 导师：边江、宋磊
> 描述：
> 1. 参与 AI4AI at Scale 相关工作，利用其他模型蒸馏多步搜索轨迹，清洗并组织用于 SFT 与 GRPO 实验的训练数据。检查工具调用与工具返回的配对关系，以及最终答案与证据的一致性。
> 2. 结合问题级去重、按任务限额采样及长短轨迹配比，控制训练数据质量与任务分布，减少重复问题及单一轨迹长度对训练样本的影响。
> 3. 参与 AxisAgentic Harness 相关开发，在 256K 可见上下文预算内组织搜索、网页抽取和有状态 Python 工具，结合上下文压缩、网页分块抽取与工具错误恢复，支持长程搜索任务执行。
> 4. 通过上下文事件重放，基于模型实际可见历史导出 Swift 格式 SFT 数据，支持训练与推理上下文的一致性；结合轨迹重放和独立答案验证分析搜索失败。
> 5. 团队成果：XYZ－Aquila－mini 在 LiveBrowseComp 上的准确率为 48.7％，WideSearch Item F1 Max＠4 为 80.8。上述成绩为团队完整系统结果；个人参与内容为前述轨迹数据、训练实验与 Harness 相关工作。
> 项目链接：
> 
> 不知道为什么html项目链接无法识别

## Response

> 已发送修正版 HTML。上一版网址是普通文字，新版已改为“完整网址＋可点击超链接”，并统一链接字段的标点。
> 
> 所有项目链接均已本地核对；请用新文件重新上传飞书，实际识别结果仍需验证。

## Evidence

> Delivered file Haitian_Zhong_CV_ZH_Fields.html; SHA256 472cf559946020c96432ef8525c92a287c1f5b5e72d4eff7cd222499eb214004
> Codex observed turn/completed status completed
> Observed bound Codex transcript task_complete for turn 01a18c1f-a150-7290-b10a-c404b3da621a
