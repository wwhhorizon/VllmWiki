# vllm-project/vllm#40769: [Bug]: dbo not support spec decode

| 字段 | 值 |
| --- | --- |
| Issue | [#40769](https://github.com/vllm-project/vllm/issues/40769) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: dbo not support spec decode

### Issue 正文摘录

### Your current environment https://github.com/vllm-project/vllm/blob/56bdf85e10b807be13225f659f2593051306c77d/vllm/v1/worker/gpu_ubatch_wrapper.py#L260-L276 Latest main ### 🐛 Describe the bug `--enable-dbo` is incompatible with any speculative decoding method which collects auxiliary hidden states from the target model. During profile_run, the ubatch wrapper crashes in `torch.cat` because the model's per-ubatch output is a tuple rather than a single Tensor. ### Root cause In vllm `/v1/worker/gpu_ubatch_wrapper.py`, `_run_ubatches` assumes each ubatch's model_output is a single Tensor and concatenates the two ubatches directly: ``` results: list[tuple[int, torch.Tensor]] = [] ... ... sorted_results = [value for position, value in sorted(results)] result = torch.cat(sorted_results, dim=0) # <-- crashes return result ``` When EAGLE3 is enabled, the target model's forward returns a tuple, because the auxiliary hidden states are required to feed the EAGLE3 drafter. `torch.cat` then fails with: ``` TypeError: expected Tensor as element 0 in argument 0, but got tuple ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: dbo not support spec decode bug ### Your current environment https://github.com/vllm-project/vllm/blob/56bdf85e10b807be13225f659f2593051306c77d/vllm/v1/worker/gpu_ubatch_wrapper.py#L260-L276 Latest main ### 🐛 Des...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 225f659f2593051306c77d/vllm/v1/worker/gpu_ubatch_wrapper.py#L260-L276 Latest main ### 🐛 Describe the bug `--enable-dbo` is incompatible with any speculative decoding method which collects auxiliary hidden states from th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e decoding method which collects auxiliary hidden states from the target model. During profile_run, the ubatch wrapper crashes in `torch.cat` because the model's per-ubatch output is a tuple rather than a single Tensor....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
