# vllm-project/vllm#12391: [Usage]: use vllm to serve gguf model with cpu only

| 字段 | 值 |
| --- | --- |
| Issue | [#12391](https://github.com/vllm-project/vllm/issues/12391) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: use vllm to serve gguf model with cpu only

### Issue 正文摘录

### Your current environment I was trying to use vllm like this: ```bash vllm serve /opt/llm/dpsk/DeepSeek-R1-Distill-Qwen-1.5B-Q8_0.gguf --quantization gguf --device cpu --tokenizer ./DeepSeek-R1-Distill-Qwen-1.5B ``` and got this error: ```text File "/opt/miniconda3/envs/locallm/lib/python3.12/site-packages/vllm/platforms/interface.py", line 165, in is_async_output_supported raise NotImplementedError NotImplementedError ``` Don't know if it is possible to use vllm to serve gguf model with CPU only. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. need help. thanks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: y. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. need help. thanks. ### Before submitting a new issue... - [x] Make sure you...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: use vllm to serve gguf model with cpu only usage ### Your current environment I was trying to use vllm like this: ```bash vllm serve /opt/llm/dpsk/DeepSeek-R1-Distill-Qwen-1.5B-Q8_0.gguf --quantization gguf --d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: `bash vllm serve /opt/llm/dpsk/DeepSeek-R1-Distill-Qwen-1.5B-Q8_0.gguf --quantization gguf --device cpu --tokenizer ./DeepSeek-R1-Distill-Qwen-1.5B ``` and got this error: ```text File "/opt/miniconda3/envs/locallm/lib/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
