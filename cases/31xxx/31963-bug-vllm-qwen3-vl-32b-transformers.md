# vllm-project/vllm#31963: [Bug]: vllm部署的Qwen3 VL 32B模型推理结果和transformers推理得到的结果不一致

| 字段 | 值 |
| --- | --- |
| Issue | [#31963](https://github.com/vllm-project/vllm/issues/31963) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm部署的Qwen3 VL 32B模型推理结果和transformers推理得到的结果不一致

### Issue 正文摘录

### Your current environment vllm离线版本和线上版本均部署了Qwen3 vl 32B微调后的模型，但是推理结果和transformers得到的结果不一样，经过排查，经过对话模版对齐后的prompt是完全一样的，tokenizer后的token_id也是完全一致的。不知道是不是vision encoder会有所差异？ vllm的版本是0.11.0，transformers的版本是 4.57.0。 vl任务是ocr，出现很多张图片的ocr结果中有一两个字符不一样，其中transformers基本都是对的，vllm离线和线上版本都是错的 ### 🐛 Describe the bug vllm离线版本和线上版本均部署了Qwen3 vl 32B微调后的模型，但是推理结果和transformers得到的结果不一样，经过排查，经过对话模版对齐后的prompt是完全一样的，tokenizer后的token_id也是完全一致的。不知道是不是vision encoder会有所差异？ vllm的版本是0.11.0，transformers的版本是 4.57.0。 vl任务是ocr，出现很多张图片的ocr结果中有一两个字符不一样，其中transformers基本都是对的，vllm离线和线上版本都是错的 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 是错的 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: vllm部署的Qwen3 VL 32B模型推理结果和transformers推理得到的结果不一致 bug;stale ### Your current environment vllm离线版本和线上版本均部署了Qwen3 vl 32B微调后的模型，但是推理结果和transformers得到的结果不一样，经过排查，经过对话模版对齐后的prompt是完全一样的，tokenizer后的token_id也是完全一致的。不知道是不...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm部署的Qwen3 VL 32B模型推理结果和transformers推理得到的结果不一致 bug;stale ### Your current environment vllm离线版本和线上版本均部署了Qwen3 vl 32B微调后的模型，但是推理结果和transformers得到的结果不一样，经过排查，经过对话模版对齐后的prompt是完全一样的，tokenizer后的token_id也是完全一致的。不知道是不...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
