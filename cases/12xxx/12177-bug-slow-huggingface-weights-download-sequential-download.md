# vllm-project/vllm#12177: [Bug]: Slow huggingface weights download. Sequential download

| 字段 | 值 |
| --- | --- |
| Issue | [#12177](https://github.com/vllm-project/vllm/issues/12177) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Slow huggingface weights download. Sequential download

### Issue 正文摘录

### Your current environment None ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using the latest vllm docker and I noticed the model download is happening sequentially. It used to download 8 files in parallel but now it looks like it is downloading one file at time. ``` INFO 01-17 13:17:16 weight_utils.py:251] Using model weights format ['*.safetensors'] model-00001-of-00006.safetensors: 100%|███████████████████████▉| 4.93G/4.93G [00:25<00:00, 194MB/s] model-00002-of-00006.safetensors: 100%|███████████████████████▉| 4.95G/4.95G [00:24<00:00, 201MB/s] model-00003-of-00006.safetensors: 100%|███████████████████████▉| 4.90G/4.90G [00:26<00:00, 184MB/s] model-00004-of-00006.safetensors: 100%|███████████████████████▉| 4.77G/4.77G [00:25<00:00, 187MB/s] ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Slow huggingface weights download. Sequential download bug;stale ### Your current environment None ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using the latest vllm docker and I noticed the mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Dumps _No response_ ### 🐛 Describe the bug I'm using the latest vllm docker and I noticed the model download is happening sequentially. It used to download 8 files in parallel but now it looks like it is downloading one...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Slow huggingface weights download. Sequential download bug;stale ### Your current environment None ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using the latest vllm docker and I noticed the mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: odel Input Dumps _No response_ ### 🐛 Describe the bug I'm using the latest vllm docker and I noticed the model download is happening sequentially. It used to download 8 files in parallel but now it looks like it is down...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
