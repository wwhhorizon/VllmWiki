# vllm-project/vllm#20612: [Bug]: Specifying a huggingface id to "path" in lora module only partially works

| 字段 | 值 |
| --- | --- |
| Issue | [#20612](https://github.com/vllm-project/vllm/issues/20612) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Specifying a huggingface id to "path" in lora module only partially works

### Issue 正文摘录

### Your current environment The mistake is obvious from the source code. ### 🐛 Describe the bug When you provide a hugggingface id of a lora adapter to the `path` field of `vllm serve --lora-modules` argument, it successfully downloads and loads the adapter. This is consistent with huggingface behavior https://huggingface.co/docs/peft/v0.16.0/en/package_reference/peft_model#peft.PeftModel.from_pretrained.model_id : the path and the model id are interchangeable. However, upon query, it tries to find `[path]/adapter_config.json` and fails because `[path]` is a huggingface id. Worse, this FileNotFoundError is completely hidden and reported as 500 Internal Server Error! This bug was discovered by #20610 , which should be separately merged in as a general QoL saver. The correct way is to detect this and convert it into `snapshot_path = huggingface_hub.snapshot_download(path)`. There are several files that directly mentions such a path, including https://github.com/vllm-project/vllm/blob/main/vllm/lora/peft_helper.py#L99 . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [docume...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Specifying a huggingface id to "path" in lora module only partially works bug;stale ### Your current environment The mistake is obvious from the source code. ### 🐛 Describe the bug When you provide a hugggingface...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Specifying a huggingface id to "path" in lora module only partially works bug;stale ### Your current environment The mistake is obvious from the source code. ### 🐛 Describe the bug When you provide a hugggingface...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 9 . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: fying a huggingface id to "path" in lora module only partially works bug;stale ### Your current environment The mistake is obvious from the source code. ### 🐛 Describe the bug When you provide a hugggingface id of a lor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
