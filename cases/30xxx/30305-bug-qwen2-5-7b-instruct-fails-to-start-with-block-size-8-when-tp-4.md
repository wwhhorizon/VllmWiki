# vllm-project/vllm#30305: [Bug]: Qwen2.5-7B-Instruct fails to start with block_size=8 when TP=4

| 字段 | 值 |
| --- | --- |
| Issue | [#30305](https://github.com/vllm-project/vllm/issues/30305) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-7B-Instruct fails to start with block_size=8 when TP=4

### Issue 正文摘录

### Your current environment 8 * H800 **Startup command used**: ```bash VLLM_LOGGING_LEVEL=DEBUG CUDA_VISIBLE_DEVICES=0,1,2,3 numactl --cpunodebind=0 --membind=0 \ .venv/bin/python -m vllm.entrypoints.openai.api_server \ --model /work/models/Qwen2.5-7B-Instruct \ --port 8010 \ --tensor-parallel-size 4 \ --block-size 8 \ --no-enable-prefix-caching \ --kv-transfer-config '{"kv_connector":"MooncakeConnector","kv_role":"kv_producer"}' ``` ### 🐛 Describe the bug A clear and concise description of what the bug is. When launching vLLM with Qwen2.5-7B-Instruct using `tensor-parallel-size=4` and `block-size=8`, the engine fails to initialize. The worker process exits and the API server raises a `RuntimeError` indicating "No common block size for 8.". ```python # Startup command that reproduces the problem VLLM_LOGGING_LEVEL=DEBUG CUDA_VISIBLE_DEVICES=0,1,2,3 numactl --cpunodebind=0 --membind=0 \ .venv/bin/python -m vllm.entrypoints.openai.api_server \ --model /work/models/Qwen2.5-7B-Instruct \ --port 8010 \ --tensor-parallel-size 4 \ --block-size 8 \ --no-enable-prefix-caching \ --kv-transfer-config '{"kv_connector":"MooncakeConnector","kv_role":"kv_producer"}' ``` ``` [0;36m(EngineCore_DP...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 8 * H800 **Startup command used**: ```bash VLLM_LOGGING_LEVEL=DEBUG CUDA_VISIBLE_DEVICES=0,1,2,3 numactl --cpunodebind=0 --membind=0 \ .venv/bin/python -m vllm.entrypoints.openai.api_server \ --model /work/models/Qwen2....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen2.5-7B-Instruct fails to start with block_size=8 when TP=4 bug;stale ### Your current environment 8 * H800 **Startup command used**: ```bash VLLM_LOGGING_LEVEL=DEBUG CUDA_VISIBLE_DEVICES=0,1,2,3 numactl --cpu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: Qwen2.5-7B-Instruct fails to start with block_size=8 when TP=4 bug;stale ### Your current environment 8 * H800 **Startup command used**: ```bash VLLM_LOGGING_LEVEL=DEBUG CUDA_VISIBLE_DEVICES=0,1,2,3 numactl --cpu...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: icating "No common block size for 8.". ```python # Startup command that reproduces the problem VLLM_LOGGING_LEVEL=DEBUG CUDA_VISIBLE_DEVICES=0,1,2,3 numactl --cpunodebind=0 --membind=0 \ .venv/bin/python -m vllm.entrypo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r","kv_role":"kv_producer"}' ``` ### 🐛 Describe the bug A clear and concise description of what the bug is. When launching vLLM with Qwen2.5-7B-Instruct using `tensor-parallel-size=4` and `block-size=8`, the engine fail...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
