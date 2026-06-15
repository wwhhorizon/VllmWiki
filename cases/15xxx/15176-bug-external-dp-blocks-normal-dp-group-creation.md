# vllm-project/vllm#15176: [Bug]: external_dp blocks normal DP group creation

| 字段 | 值 |
| --- | --- |
| Issue | [#15176](https://github.com/vllm-project/vllm/issues/15176) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: external_dp blocks normal DP group creation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/pull/14899 introduces error for normal DP. As https://github.com/vllm-project/vllm/blob/main/vllm/distributed/parallel_state.py#L904C35-L904C45 shown, "config.parallel_config.world_size" means `tp-size * pp-size` defined in config.py while world_size is size of all visible devices from "torch.distributed". As a result, as long as a regular DP size, it will enter this branch as unexpected, thereby preventing the establishment of DP group. Suppose replace "config.parallel_config.world_size" with "config.parallel_config.world_size_cross_dp" which matches the design of external_dp more. ```python if config.parallel_config.world_size_cross_dp != world_size: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: external_dp blocks normal DP group creation bug ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/pull/14899 introduces error for normal DP. As https://github.com/vllm-proje...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: llm/blob/main/vllm/distributed/parallel_state.py#L904C35-L904C45 shown, "config.parallel_config.world_size" means `tp-size * pp-size` defined in config.py while world_size is size of all visible devices from "torch.dist...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
