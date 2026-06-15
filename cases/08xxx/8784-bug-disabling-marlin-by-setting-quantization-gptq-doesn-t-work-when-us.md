# vllm-project/vllm#8784: [Bug]: Disabling Marlin by setting --quantization gptq doesn't work when using a draft model

| 字段 | 值 |
| --- | --- |
| Issue | [#8784](https://github.com/vllm-project/vllm/issues/8784) |
| 状态 | closed |
| 标签 | bug;speculative-decoding;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Disabling Marlin by setting --quantization gptq doesn't work when using a draft model

### Issue 正文摘录

### Your current environment . ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems that setting --quantization gptq only disables the marlin for the main model. Maybe this can be fixed by adding a --quantization-draft-model setting or forcing the draft model to gptq when main model is forced. ``` INFO 09-24 15:46:11 gptq_marlin.py:112] Detected that the model can run with gptq_marlin, **however you specified quantization=gptq explicitly, so forcing gptq. Use quantization=gptq_marlin for faster inference** WARNING 09-24 15:46:11 config.py:335] gptq quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 09-24 15:46:11 config.py:904] Defaulting to use mp for distributed inference **INFO 09-24 15:46:11 gptq_marlin.py:108] The model is convertible to gptq_marlin during runtime. Using gptq_marlin kernel.** ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: isabling Marlin by setting --quantization gptq doesn't work when using a draft model bug;speculative-decoding;stale ### Your current environment . ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems that...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ng Marlin by setting --quantization gptq doesn't work when using a draft model bug;speculative-decoding;stale ### Your current environment . ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems that setti...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e this can be fixed by adding a --quantization-draft-model setting or forcing the draft model to gptq when main model is forced. ``` INFO 09-24 15:46:11 gptq_marlin.py:112] Detected that the model can run with gptq_marl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Disabling Marlin by setting --quantization gptq doesn't work when using a draft model bug;speculative-decoding;stale ### Your current environment . ### Model Input Dumps _No response_ ### 🐛 Describe the bug It se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
