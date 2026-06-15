# vllm-project/vllm#14176: [Feature]: deepseek-r1-w8a8

| 字段 | 值 |
| --- | --- |
| Issue | [#14176](https://github.com/vllm-project/vllm/issues/14176) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: deepseek-r1-w8a8

### Issue 正文摘录

### 🚀 The feature, motivation and pitch At present, DeepSeek-R1-W8A8 is released by Huawei, but its quantization method, vLLM, does not support it for the time being. May I ask if there are any plans to support it? Its application scenarios are still very extensive. [DeepSeek-R1-模型库-ModelZoo-昇腾社区](https://www.hiascend.com/software/modelzoo/models/detail/68457b8a51324310aad9a0f55c3e56e3) In addition, there is one here as well: https://huggingface.co/meituan/DeepSeek-R1-Block-INT8 https://huggingface.co/meituan/DeepSeek-R1-Channel-INT8 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: it? Its application scenarios are still very extensive. [DeepSeek-R1-模型库-ModelZoo-昇腾社区](https://www.hiascend.com/software/modelzoo/models/detail/68457b8a51324310aad9a0f55c3e56e3) In addition, there is one here as well:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: deepseek-r1-w8a8 feature request;stale ### 🚀 The feature, motivation and pitch At present, DeepSeek-R1-W8A8 is released by Huawei, but its quantization method, vLLM, does not support it for the time being. Ma...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: n and pitch At present, DeepSeek-R1-W8A8 is released by Huawei, but its quantization method, vLLM, does not support it for the time being. May I ask if there are any plans to support it? Its application scenarios are st...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: n, there is one here as well: https://huggingface.co/meituan/DeepSeek-R1-Block-INT8 https://huggingface.co/meituan/DeepSeek-R1-Channel-INT8 ### Alternatives _No response_ ### Additional context _No response_ ### Before...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
