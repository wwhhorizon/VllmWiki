# vllm-project/vllm#11705: [Bug]: Extremely slow inference speed when deploying with vLLM on 16 H100 GPUs according to instructions on DeepSeekV3

| 字段 | 值 |
| --- | --- |
| Issue | [#11705](https://github.com/vllm-project/vllm/issues/11705) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Extremely slow inference speed when deploying with vLLM on 16 H100 GPUs according to instructions on DeepSeekV3

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm deploying the model using the following command: ``` vllm serve local_deepseekv3_path --trust-remote-code --tensor-parallel-size 8 --pipeline-parallel-size 2 --model-max-len 16384 --served-model-name deepseek-v3 deepseek ``` I'm using the official Ray example, and NCCL is enabled. After launching the model with the above command, the inference speed is extremely slow. The inference speed is almost 5 times slower than an unquantized Qwen-72B model. INFO: 10.39.129.93:36766 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 01-02 16:16:48 async_llm_engine.py:211] Added request chatcmpl-bc1d5239d4c743aabedf1249038b99da. INFO 01-02 16:16:56 metrics.py:467] Avg prompt throughput: 1.9 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%. INFO 01-02 16:17:02 metrics.py:467] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 2.9 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%.INFO 01-02 16:17:07 metrics.py:467] Avg prompt th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: len 16384 --served-model-name deepseek-v3 deepseek ``` I'm using the official Ray example, and NCCL is enabled. After launching the model with the above command, the inference speed is extremely slow. The inference spee...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Extremely slow inference speed when deploying with vLLM on 16 H100 GPUs according to instructions on DeepSeekV3 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nstructions on DeepSeekV3 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm deploying the model using the following command: ``` vllm serve local_deepseekv3_path --tru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ng with vLLM on 16 H100 GPUs according to instructions on DeepSeekV3 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm deploying the model using the following command:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: d4c743aabedf1249038b99da. INFO 01-02 16:16:56 metrics.py:467] Avg prompt throughput: 1.9 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
