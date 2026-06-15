# vllm-project/vllm#15019: [Bug]: vllm 0.8.0 rc3 - Are we using the multimodal cache even if `disable_mm_preprocessor_cache=True`?

| 字段 | 值 |
| --- | --- |
| Issue | [#15019](https://github.com/vllm-project/vllm/issues/15019) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm 0.8.0 rc3 - Are we using the multimodal cache even if `disable_mm_preprocessor_cache=True`?

### Issue 正文摘录

### Your current environment vllm 0.8.0 rc3, cuda 12.4 ### 🐛 Describe the bug This might not be a bug but I set `disable_mm_preprocessor_cache=True` in a multimodal model I am testing and from the logs I saw ``` Encoder cache will be initialized with a budget of 9800 tokens, and profiled with 1 video items of the maximum feature size. ``` then I checked the code and I saw https://github.com/vllm-project/vllm/blob/d1695758b2f65fd314d1aee71ba2469ceba67a5b/vllm/v1/worker/gpu_model_runner.py#L861. should we clear the cache everytime if `disable_mm_preprocessor_cache=True` Feel free to close this bug report if everything is ok :) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: processor_cache=True`? bug ### Your current environment vllm 0.8.0 rc3, cuda 12.4 ### 🐛 Describe the bug This might not be a bug but I set `disable_mm_preprocessor_cache=True` in a multimodal model I am testing and from...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm 0.8.0 rc3 - Are we using the multimodal cache even if `disable_mm_preprocessor_cache=True`? bug ### Your current environment vllm 0.8.0 rc3, cuda 12.4 ### 🐛 Describe the bug This might not be a bug but I set...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ut I set `disable_mm_preprocessor_cache=True` in a multimodal model I am testing and from the logs I saw ``` Encoder cache will be initialized with a budget of 9800 tokens, and profiled with 1 video items of the maximum...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
