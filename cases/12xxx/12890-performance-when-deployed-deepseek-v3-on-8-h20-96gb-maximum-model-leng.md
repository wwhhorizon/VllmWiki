# vllm-project/vllm#12890: [Performance]: When deployed DeepSeek-V3 on 8*H20(96GB), maximum model length only reaches 6500 using vllm, but with sglang can achieve 163840.

| 字段 | 值 |
| --- | --- |
| Issue | [#12890](https://github.com/vllm-project/vllm/issues/12890) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: When deployed DeepSeek-V3 on 8*H20(96GB), maximum model length only reaches 6500 using vllm, but with sglang can achieve 163840.

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance vllm command `python3 -m vllm.entrypoints.openai.api_server --model ${model_path} --port 8108 --max-model-len 6500 --gpu-memory-utilization 0.98 --tensor-parallel-size 8 --trust-remote-code --quantization fp8` sglang command `python3 -m sglang.launch_server --model-path ${model_path} --tp 8 --trust-remote-code --mem-fraction-static 0.9 --host 0.0.0.0 --port 50050 --served-model-name atom` ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -memory-utilization 0.98 --tensor-parallel-size 8 --trust-remote-code --quantization fp8` sglang command `python3 -m sglang.launch_server --model-path ${model_path} --tp 8 --trust-remote-code --mem-fraction-static 0.9 -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance vllm command `python3 -m vllm.entrypoints.openai.api_server --model ${model_path} --port...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: When deployed DeepSeek-V3 on 8*H20(96GB), maximum model length only reaches 6500 using vllm, but with sglang can achieve 163840. performance;stale ### Proposal to improve performance _No response_ ### Rep...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: reaches 6500 using vllm, but with sglang can achieve 163840. performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
