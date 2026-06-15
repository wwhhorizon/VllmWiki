# vllm-project/vllm#30153: [BUG] vLLM NIXL Side Channel Defaults to Localhost - Breaks Disaggregated Kubernetes Deployments

| 字段 | 值 |
| --- | --- |
| Issue | [#30153](https://github.com/vllm-project/vllm/issues/30153) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cache |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [BUG] vLLM NIXL Side Channel Defaults to Localhost - Breaks Disaggregated Kubernetes Deployments

### Issue 正文摘录

# [BUG] vLLM NIXL Side Channel Defaults to Localhost - Breaks Disaggregated Kubernetes Deployments ## Summary vLLM's NIXL connector defaults the side channel host to `localhost`, preventing cross-pod communication in Kubernetes disaggregated deployments. This causes 120-second KV cache transfer timeouts and inference failures. ## Environment - **vLLM Version**: 0.11.0 - **NIXL Version**: 0.7.1 - **Platform**: Kubernetes (AWS EKS + Hyperpod) - **Instance Type**: ml.p5.48xlarge (H100 GPUs with EFA) - **Backend**: LIBFABRIC with EFA RDMA - **Python**: 3.12 ## Problem Description ### Root Cause In `dynamo/vllm/nixl_connector.py` (or vLLM core NIXL integration): ```python def __init__(self, ...): # Hardcoded default to localhost side_channel_host = os.getenv('VLLM_NIXL_SIDE_CHANNEL_HOST', 'localhost') side_channel_port = os.getenv('VLLM_NIXL_SIDE_CHANNEL_PORT', '5557') # NIXL binds to this address and advertises it to other workers self.side_channel_endpoint = f"{side_channel_host}:{side_channel_port}" ``` ### Failure Flow 1. **Prefill worker (Pod A)** starts with side channel bound to `localhost:5557` 2. **Service discovery** (NATS/ETCD) advertises endpoint as `localhost:5557` 3. **De...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ache transfer timeouts and inference failures. ## Environment - **vLLM Version**: 0.11.0 - **NIXL Version**: 0.7.1 - **Platform**: Kubernetes (AWS EKS + Hyperpod) - **Instance Type**: ml.p5.48xlarge (H100 GPUs with EFA)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: **: Kubernetes (AWS EKS + Hyperpod) - **Instance Type**: ml.p5.48xlarge (H100 GPUs with EFA) - **Backend**: LIBFABRIC with EFA RDMA - **Python**: 3.12 ## Problem Description ### Root Cause In `dynamo/vllm/nixl_connector...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: me: vllm command: ["python3", "-m", "dynamo.vllm"] args: - --model=Qwen/Qwen3-0.6B - --is-prefill-worker - --kv-transfer-config={"kv_connector": "NixlConnector", "kv_role": "kv_both"} # Note: No VLLM_NIXL_SIDE_CHANNEL_H...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: = f"{side_channel_host}:{side_channel_port}" ``` ### Failure Flow 1. **Prefill worker (Pod A)** starts with side channel bound to `localhost:5557` 2. **Service discovery** (NATS/ETCD) advertises endpoint as `localhost:5...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ``` ## Symptoms ### Logs **Prefill Worker**: ``` Releasing expired KV blocks for request which were retrieved by 0 decode worker(s) within 120 seconds ``` **Decode Worker**: ``` (No errors - silently fails to connect to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
