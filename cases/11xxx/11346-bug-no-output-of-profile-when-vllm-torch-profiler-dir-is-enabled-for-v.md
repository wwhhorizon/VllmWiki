# vllm-project/vllm#11346: [Bug]: no output of profile when VLLM_TORCH_PROFILER_DIR is enabled for vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#11346](https://github.com/vllm-project/vllm/issues/11346) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: no output of profile when VLLM_TORCH_PROFILER_DIR is enabled for vllm serve

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I start a vlllm server with ``` VLLM_RPC_TIMEOUT=1800000 VLLM_TORCH_PROFILER_DIR=***/MLinference/language/llama2-70b/vllm_profile_output vllm serve ${CHECKPOINT_PATH} --tensor-parallel-size 4 2>&1 | tee vllm_serve_profile_opt-13b_log.log & ``` then use scripts from MLinference/language/llama2-70b/main.py to feed request to the server. After the scripts is finished I cannot see any output of profile in the given folder. But I can see from the vllm_serve_profile_opt-13b_log.log that the torch profiler is enabled. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: is enabled for vllm serve bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I start a vlllm server with ``` VLLM_RPC_TIMEOUT=1800000 VLLM_TORCH_PROFILER_DIR=***/MLinferenc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ut of profile when VLLM_TORCH_PROFILER_DIR is enabled for vllm serve bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I start a vlllm server with ``` VLLM_RPC_TIMEOUT=180...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: no output of profile when VLLM_TORCH_PROFILER_DIR is enabled for vllm serve bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I start a vlllm server with ``` VLLM_R...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
