# vllm-project/vllm#42385: [Bug]: MooncakeConnector startup failure triggers secondary `AttributeError` during cleanup (`async_zmq_ctx`)

| 字段 | 值 |
| --- | --- |
| Issue | [#42385](https://github.com/vllm-project/vllm/issues/42385) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MooncakeConnector startup failure triggers secondary `AttributeError` during cleanup (`async_zmq_ctx`)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When `MooncakeConnector` is enabled and Mooncake engine import is unavailable, vLLM correctly raises: `RuntimeError: Mooncake is not available` But then object cleanup triggers a second exception: `AttributeError: 'MooncakeConnectorWorker' object has no attribute 'async_zmq_ctx'` This secondary exception is misleading and obscures the root cause. ```bash # 1) Ensure this import fails in the repro environment: python3 -c "import mooncake.engine" # 2) Start vLLM with MooncakeConnector: vllm serve Qwen/Qwen3-Omni-30B-A3B-Instruct \ --port 8010 \ --kv-transfer-config '{"kv_connector":"MooncakeConnector","kv_role":"kv_producer"}' \ 2>&1 | tee repro.log ``` Expected error sequence in `repro.log`: 1. `RuntimeError: Mooncake is not available` 2. `AttributeError: 'MooncakeConnectorWorker' object has no attribute 'async_zmq_ctx'` ## Observed Traceback (key part) ```text RuntimeError: Mooncake is not available Exception ignored in: AttributeError: 'MooncakeConnectorWorker' object has no attribute 'async_zmq_ctx' ``` ## Why this is a vLLM bug In `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`: - `MooncakeConnect...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: escribe the bug When `MooncakeConnector` is enabled and Mooncake engine import is unavailable, vLLM correctly raises: `RuntimeError: Mooncake is not available` But then object cleanup triggers a second exception: `Attri...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ort mooncake.engine" # 2) Start vLLM with MooncakeConnector: vllm serve Qwen/Qwen3-Omni-30B-A3B-Instruct \ --port 8010 \ --kv-transfer-config '{"kv_connector":"MooncakeConnector","kv_role":"kv_producer"}' \ 2>&1 | tee r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ot complete. ## Additional Context Installing `mooncake-transfer-engine-cuda13==0.3.10.post2` allows startup to pass this specific failure path, but we observed a separate data-integrity/accuracy issue under PD load (`d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ss this specific failure path, but we observed a separate data-integrity/accuracy issue under PD load (`dst != src_post` in byte-hash probes). That is filed separately to avoid conflating root causes. [repro_vllm_moonca...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
