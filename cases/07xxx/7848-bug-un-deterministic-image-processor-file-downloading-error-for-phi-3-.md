# vllm-project/vllm#7848: [Bug]: un-deterministic image processor file downloading error for phi-3 vision

| 字段 | 值 |
| --- | --- |
| Issue | [#7848](https://github.com/vllm-project/vllm/issues/7848) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: un-deterministic image processor file downloading error for phi-3 vision

### Issue 正文摘录

### Your current environment vllm == 0.5.5. ### 🐛 Describe the bug when we deploy the `microsoft/Phi-3.5-vision-instruct`, it will randomly hit this issue. ``` [1;36m(VllmWorkerProcess pid=2195)[0;0m ERROR 08-25 08:03:14 multiproc_worker_utils.py:226] FileNotFoundError: [Errno 2] No such file or directory: '/root/.cache/huggingface/hub/models--microsoft--Phi-3.5-vision-instruct/snapshots/c68f85286eac3fb376a17068e820e738a89c194a/processing_phi3_v.py' ``` the problem might be caused by this https://github.com/vllm-project/vllm/blob/80162c44b1d1e59a2c10f65b6adb9b0407439b1f/vllm/multimodal/image.py#L16 for multi gpus environment that head one hasn't yet finished downloading. is it better to put it where AutoTokenizer is run? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 6] FileNotFoundError: [Errno 2] No such file or directory: '/root/.cache/huggingface/hub/models--microsoft--Phi-3.5-vision-instruct/snapshots/c68f85286eac3fb376a17068e820e738a89c194a/processing_phi3_v.py' ``` the proble...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: un-deterministic image processor file downloading error for phi-3 vision bug;stale ### Your current environment vllm == 0.5.5. ### 🐛 Describe the bug when we deploy the `microsoft/Phi-3.5-vision-instruct`, it wil...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: un-deterministic image processor file downloading error for phi-3 vision bug;stale ### Your current environment vllm == 0.5.5. ### 🐛 Describe the bug when we deploy the `microsoft/Phi-3.5-vision-instruct`, it wil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: un? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eterministic image processor file downloading error for phi-3 vision bug;stale ### Your current environment vllm == 0.5.5. ### 🐛 Describe the bug when we deploy the `microsoft/Phi-3.5-vision-instruct`, it will randomly...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
