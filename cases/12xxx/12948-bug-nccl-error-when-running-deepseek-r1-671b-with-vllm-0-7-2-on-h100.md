# vllm-project/vllm#12948: [Bug]: NCCL Error When Running DeepSeek-R1 671B with vLLM 0.7.2 on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#12948](https://github.com/vllm-project/vllm/issues/12948) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: NCCL Error When Running DeepSeek-R1 671B with vLLM 0.7.2 on H100

### Issue 正文摘录

### Your current environment vllm serve /model/deepseek --port 8000 --dtype half --uvicorn-log-level info --tensor-parallel-size 8 --served-model-name deepseek --root-path /deepseek --trust-remote-code ### 🐛 Describe the bug [2.log](https://github.com/user-attachments/files/18717444/2.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: NCCL Error When Running DeepSeek-R1 671B with vLLM 0.7.2 on H100 bug;stale ### Your current environment vllm serve /model/deepseek --port 8000 --dtype half --uvicorn-log-level info --tensor-parallel-size 8 --serv...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ## Your current environment vllm serve /model/deepseek --port 8000 --dtype half --uvicorn-log-level info --tensor-parallel-size 8 --served-model-name deepseek --root-path /deepseek --trust-remote-code ### 🐛 Describe the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: LLM 0.7.2 on H100 bug;stale ### Your current environment vllm serve /model/deepseek --port 8000 --dtype half --uvicorn-log-level info --tensor-parallel-size 8 --served-model-name deepseek --root-path /deepseek --trust-r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g]: NCCL Error When Running DeepSeek-R1 671B with vLLM 0.7.2 on H100 bug;stale ### Your current environment vllm serve /model/deepseek --port 8000 --dtype half --uvicorn-log-level info --tensor-parallel-size 8 --served-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
