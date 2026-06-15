# vllm-project/vllm#13234: [Performance]: Running llama-70b on 4 A100 40Gb

| 字段 | 值 |
| --- | --- |
| Issue | [#13234](https://github.com/vllm-project/vllm/issues/13234) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Running llama-70b on 4 A100 40Gb

### Issue 正文摘录

### Proposal to improve performance Hi, We are running Llama2-70b-Instruct on 4 A100 GPU 40Gb VRAM, It is running with tensor-parallelism across 4 GPU and dtype of float16 and prefix caching enabled. We didn’t touch the rest of the parameters. What we notice is that an average 1500 input tokens and about 50–100 output tokens in English, the average response time is about 7s. Is there any way to speed this up? Ideally we are looking for about 2s response times. Thank you ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: Running llama-70b on 4 A100 40Gb performance;stale ### Proposal to improve performance Hi, We are running Llama2-70b-Instruct on 4 A100 GPU 40Gb VRAM, It is running with tensor-parallelism across 4 GPU an...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 0 GPU 40Gb VRAM, It is running with tensor-parallelism across 4 GPU and dtype of float16 and prefix caching enabled. We didn’t touch the rest of the parameters. What we notice is that an average 1500 input tokens and ab...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ing for about 2s response times. Thank you ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The outp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: Running llama-70b on 4 A100 40Gb performance;stale ### Proposal to improve performance Hi, We are running Llama2-70b-Instruct on 4 A100 GPU 40Gb VRAM, It is running with tensor-parallelism across 4 GPU an...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Running llama-70b on 4 A100 40Gb performance;stale ### Proposal to improve performance Hi, We are running Llama2-70b-Instruct on 4 A100 GPU 40Gb VRAM, It is running with tensor-parallelism across 4 GPU an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
