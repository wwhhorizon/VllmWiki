# vllm-project/vllm#36771: [Bug]: LMCache does not work with vLLM 0.17.0 (Qwen3Next)

| 字段 | 值 |
| --- | --- |
| Issue | [#36771](https://github.com/vllm-project/vllm/issues/36771) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LMCache does not work with vLLM 0.17.0 (Qwen3Next)

### Issue 正文摘录

### Your current environment - vLLM version: 0.17.0 - LMCache: latest nightly-2026-03-10 & vllm/vllm-openai:v0.17.0 - Model: Qwen3-Coder-Next-FP8 - Python: 3.12 - Deployment: Kubernetes - Load format: runai_streamer ### 🐛 Describe the bug We encountered two different problems when trying to use LMCache with vLLM 0.17.0. Case 1 — vllm/vllm-openai:v0.17.0 image Using the original vllm/vllm-openai:v0.17.0 image with LMCache enabled fails for all tested models (GLM, Qwen-Coder, etc.). LMCache initialization starts but crashes with a binary import error: ``` ImportError: /usr/local/lib/python3.12/dist-packages/lmcache/c_ops.cpython-312-x86_64-linux-gnu.so: undefined symbol: _ZN3c104cuda29c10_cuda_check_implementationEiPKcS2_ib ``` Relevant log snippet: ``` Creating v1 connector with name: LMCacheConnectorV1 Initializing latest dev LMCache connector ImportError: lmcache/c_ops.cpython-312-x86_64-linux-gnu.so: undefined symbol: _ZN3c104cuda29c10_cuda_check_implementationEiPKcS2_ib ``` Case 2 — lmcache/vllm-openai image Using the lmcache/vllm-openai image: GLM-4.7-Flash works with LMCache Qwen3-Coder-Next fails during startup. The server crashes with: ``` ValueError: Hybrid KV cache manage...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: LMCache does not work with vLLM 0.17.0 (Qwen3Next) bug ### Your current environment - vLLM version: 0.17.0 - LMCache: latest nightly-2026-03-10 & vllm/vllm-openai:v0.17.0 - Model: Qwen3-Coder-Next-FP8 - Python: 3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rk with vLLM 0.17.0 (Qwen3Next) bug ### Your current environment - vLLM version: 0.17.0 - LMCache: latest nightly-2026-03-10 & vllm/vllm-openai:v0.17.0 - Model: Qwen3-Coder-Next-FP8 - Python: 3.12 - Deployment: Kubernet...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lmcache/c_ops.cpython-312-x86_64-linux-gnu.so: undefined symbol: _ZN3c104cuda29c10_cuda_check_implementationEiPKcS2_ib ``` Relevant log snippet: ``` Creating v1 connector with name: LMCacheConnectorV1 Initializing lates...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nightly-2026-03-10 & vllm/vllm-openai:v0.17.0 - Model: Qwen3-Coder-Next-FP8 - Python: 3.12 - Deployment: Kubernetes - Load format: runai_streamer ### 🐛 Describe the bug We encountered two different problems when trying...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t fails during startup. The server crashes with: ``` ValueError: Hybrid KV cache manager is disabled but failed to convert the KV cache specs to one unified type. ``` This happens when LMCache is enabled via: ``` --kv-t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
