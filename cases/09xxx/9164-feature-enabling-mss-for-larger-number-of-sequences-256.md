# vllm-project/vllm#9164: [Feature]: Enabling MSS for larger number of sequences (>256)

| 字段 | 值 |
| --- | --- |
| Issue | [#9164](https://github.com/vllm-project/vllm/issues/9164) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 | memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Enabling MSS for larger number of sequences (>256)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In the advance_step.cu, there is a constraint on the number of sequences based on the number of available GPU threads and block_tables stride. ``` // TODO(will): support arbitrary block_tables stride if ((blocks * threads) / block_tables.stride(0) < num_queries) { TORCH_CHECK(false, ``` This prevents supporting larger batch sizes for which we have enabled cuda graphs recently, which hit perf significantly on H100/200 machines with models like llama70B. Would also like to help and @youkaichao please kindly connect us to Will. Thank you. ### Alternatives Change the kernel to support larger sequence size ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: the number of sequences based on the number of available GPU threads and block_tables stride. ``` // TODO(will): support arbitrary block_tables stride if ((blocks * threads) / block_tables.stride(0) < num_queries) { TOR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ` This prevents supporting larger batch sizes for which we have enabled cuda graphs recently, which hit perf significantly on H100/200 machines with models like llama70B. Would also like to help and @youkaichao please k...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: graphs recently, which hit perf significantly on H100/200 machines with models like llama70B. Would also like to help and @youkaichao please kindly connect us to Will. Thank you. ### Alternatives Change the kernel to su...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Enabling MSS for larger number of sequences (>256) feature request;stale ### 🚀 The feature, motivation and pitch In the advance_step.cu, there is a constraint on the number of sequences based on the number of...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance frontend_api cuda;kernel memory_layout;shape 🚀 The feature, motivation an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
