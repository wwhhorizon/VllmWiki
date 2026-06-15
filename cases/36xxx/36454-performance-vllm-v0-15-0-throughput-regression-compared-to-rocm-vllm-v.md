# vllm-project/vllm#36454: [Performance]: vLLM v0.15.0 throughput regression compared to ROCm vLLM v0.14.0

| 字段 | 值 |
| --- | --- |
| Issue | [#36454](https://github.com/vllm-project/vllm/issues/36454) |
| 状态 | closed |
| 标签 | performance;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: vLLM v0.15.0 throughput regression compared to ROCm vLLM v0.14.0

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Performance observations were conducted for vLLM [**v0.15.0**](https://hub.docker.com/r/vllm/vllm-openai-rocm/tags) in comparison with the ROCm forked vLLM [**v0.14.0**](https://hub.docker.com/r/rocm/vllm) (now deprecated). Testing was executed on a server equipped with **8× AMD Instinct MI300X GPUs**. Benchmarking was performed using the **vLLM bench** utility across **eight Docker-based vLLM serving instances** of the model Qwen3-30B-A3B-Thinking-2507. Traffic distribution across the serving instances was handled through nginx load balancing. The command executed is shown below: ` HF_HOME=/mnt/models HUGGINGFACE_HUB_CACHE=/mnt/models/hub TRANSFORMERS_CACHE=/mnt/models/hub vllm bench serve --backend vllm --model Qwen/Qwen3-30B-A3B-Thinking-2507 --tokenizer /mnt/models/hub/models--Qwen--Qwen3-30B-A3B-Thinking-2507/snapshots/144afc2f379b542fdd4e85a1fcd5e1f79112d95d --host localhost --port 8000 --endpoint /v1/completions --dataset-name sharegpt --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --output-len 128 --num-prompts 4096 --max-concurrency 4096 2>&1 | tee "$LOG"` Benchmark results...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ch** utility across **eight Docker-based vLLM serving instances** of the model Qwen3-30B-A3B-Thinking-2507. Traffic distribution across the serving instances was handled through nginx load balancing. The command execute...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Performance]: vLLM v0.15.0 throughput regression compared to ROCm vLLM v0.14.0 performance;rocm ### Proposal to improve performance _No response_ ### Report of performance regression Performance observations were condu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: vLLM v0.15.0 throughput regression compared to ROCm vLLM v0.14.0 performance;rocm ### Proposal to improve performance _No response_ ### Report of performance regression Performance observations were condu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rformance observations were conducted for vLLM [**v0.15.0**](https://hub.docker.com/r/vllm/vllm-openai-rocm/tags) in comparison with the ROCm forked vLLM [**v0.14.0**](https://hub.docker.com/r/rocm/vllm) (now deprecated...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: =/mnt/models/hub TRANSFORMERS_CACHE=/mnt/models/hub vllm bench serve --backend vllm --model Qwen/Qwen3-30B-A3B-Thinking-2507 --tokenizer /mnt/models/hub/models--Qwen--Qwen3-30B-A3B-Thinking-2507/snapshots/144afc2f379b54...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
