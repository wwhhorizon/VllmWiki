# vllm-project/vllm#18942: [Bug]: AsyncLLM when DP > 1, device allocation bug

| 字段 | 值 |
| --- | --- |
| Issue | [#18942](https://github.com/vllm-project/vllm/issues/18942) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AsyncLLM when DP > 1, device allocation bug

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug enable DP > 1, TP = 1, but the UniProcExecutor can not correctly process the rank info, see [debug]. DP rank 0 and rank 1 are both rank 0, which is wrong. Outside UniProcExecutor , it is processed correctly. so maybe the initialization of UniProcExecutor should pass some info to init (for DP > 1 case), now the init function does not take any arguments. ![Image](https://github.com/user-attachments/assets/48f0b182-d745-488f-a7dc-d3559bfe7644) ![Image](https://github.com/user-attachments/assets/097af0f3-c00c-4766-a147-da76be4d608a) ![Image](https://github.com/user-attachments/assets/42aae792-2266-42a2-969b-6cb460bb48af) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory;speculative_decoding cuda;operator build_error env_dependency Your c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: AsyncLLM when DP > 1, device allocation bug bug;stale ### Your current environment ### 🐛 Describe the bug enable DP > 1, TP = 1, but the UniProcExecutor can not correctly process the rank info, see [debug]. DP ra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: af) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. development ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory;speculative_decoding cuda;operator build_error env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;scheduler_me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
