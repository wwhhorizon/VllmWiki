# vllm-project/vllm#112: [Performance]: SmoothQuant quantization is too slow

| 字段 | 值 |
| --- | --- |
| Issue | [#112](https://github.com/vllm-project/llm-compressor/issues/112) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: SmoothQuant quantization is too slow

### Issue 正文摘录

### Proposal to improve performance I am using SmoothQuant to quantize Llama2-7b, but each sample takes 1 hour. Is this speed normal, and are there any ways to improve it? ![image](https://github.com/user-attachments/assets/a11b9d1b-63b5-4c9c-8d41-25f647096d50) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: SmoothQuant quantization is too slow ### Proposal to improve performance I am using SmoothQuant to quantize Llama2-7b, but each sample takes 1 hour. Is this speed normal, and are there any ways to improve...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: /assets/a11b9d1b-63b5-4c9c-8d41-25f647096d50) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Performance]: SmoothQuant quantization is too slow ### Proposal to improve performance I am using SmoothQuant to quantize Llama2-7b, but each sample takes 1 hour. Is this speed normal, and are there any ways to improve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ### Proposal to improve performance I am using SmoothQuant to quantize Llama2-7b, but each sample takes 1 hour. Is this speed normal, and are there any ways to improve it? ![image](https://github.com/user-attachments/as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
