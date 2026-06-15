# vllm-project/vllm#13034: [Usage]: Multi lora inference support for llava v1.6

| 字段 | 值 |
| --- | --- |
| Issue | [#13034](https://github.com/vllm-project/vllm/issues/13034) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Multi lora inference support for llava v1.6

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I tried to run multi-lora inference on vllm for llava-hf/llava-v1.6-mistral-7b-hf. But i found it not supported according to the doc here https://docs.vllm.ai/en/latest/models/supported_models.html#list-of-multimodal-language-models. Is there any plan to support multi lora for more mllm in near future or any practical way to obtain it on llava-next? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: like to use vllm I tried to run multi-lora inference on vllm for llava-hf/llava-v1.6-mistral-7b-hf. But i found it not supported according to the doc here https://docs.vllm.ai/en/latest/models/supported_models.html#list...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: xt? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: und it not supported according to the doc here https://docs.vllm.ai/en/latest/models/supported_models.html#list-of-multimodal-language-models. Is there any plan to support multi lora for more mllm in near future or any...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
