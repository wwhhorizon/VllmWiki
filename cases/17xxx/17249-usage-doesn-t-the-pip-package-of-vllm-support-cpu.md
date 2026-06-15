# vllm-project/vllm#17249: [Usage]: Doesn't the pip package of vllm support CPU?

| 字段 | 值 |
| --- | --- |
| Issue | [#17249](https://github.com/vllm-project/vllm/issues/17249) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Doesn't the pip package of vllm support CPU?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` device_config = DeviceConfig(device=self.device) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/xxx/myenv/lib/python3.11/site-packages/vllm/config.py", line 1091, in __init__ raise RuntimeError("Failed to infer device type") RuntimeError: Failed to infer device type $ pip list | grep vllm vllm 0.6.3.post1 ### How would you like to use vllm My device is not recognized as a cpu device ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ice ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nvironment ```text The output of `python collect_env.py` ``` device_config = DeviceConfig(device=self.device) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/xxx/myenv/lib/python3.11/site-packages/vllm/config.py", line 1091, in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
