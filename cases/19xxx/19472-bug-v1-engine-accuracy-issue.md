# vllm-project/vllm#19472: [Bug]: v1 engine accuracy issue

| 字段 | 值 |
| --- | --- |
| Issue | [#19472](https://github.com/vllm-project/vllm/issues/19472) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v1 engine accuracy issue

### Issue 正文摘录

### Your current environment 4 * A100 vllm 0.9.0.1 torch 2.6 cuda 12.6 ### 🐛 Describe the bug ``` python3 -m vllm.entrypoints.openai.api_server --served-model-name model --model /root/Qwen3-235B-A22B-AWQ/ --tensor-parallel-size 4 --port 8000 --trust-remote-code --dtype half --max-num-seqs 256 --max-model-len 16384 --gpu-memory-utilization 0.9 ``` If I request the api with many threads (e.g. 256 threads), the initial output appears normal, but after generating several dozen tokens, it begins to produce meaningless and repetitive content. For example ``` 2021-08-06 15:22:38 1. 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2022-01-01 2...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: g]: v1 engine accuracy issue bug;stale ### Your current environment 4 * A100 vllm 0.9.0.1 torch 2.6 cuda 12.6 ### 🐛 Describe the bug ``` python3 -m vllm.entrypoints.openai.api_server --served-model-name model --model /r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: v1 engine accuracy issue bug;stale ### Your current environment 4 * A100 vllm 0.9.0.1 torch 2.6 cuda 12.6 ### 🐛 Describe the bug ``` python3 -m vllm.entrypoints.openai.api_server --served-model-name model --model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 35B-A22B-AWQ/ --tensor-parallel-size 4 --port 8000 --trust-remote-code --dtype half --max-num-seqs 256 --max-model-len 16384 --gpu-memory-utilization 0.9 ``` If I request the api with many threads (e.g. 256 threads), th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ribe the bug ``` python3 -m vllm.entrypoints.openai.api_server --served-model-name model --model /root/Qwen3-235B-A22B-AWQ/ --tensor-parallel-size 4 --port 8000 --trust-remote-code --dtype half --max-num-seqs 256 --max-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: v1 engine accuracy issue bug;stale ### Your current environment 4 * A100 vllm 0.9.0.1 torch 2.6 cuda 12.6 ### 🐛 Describe the bug ``` python3 -m vllm.entrypoints.openai.api_server --served-model-name model --model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
