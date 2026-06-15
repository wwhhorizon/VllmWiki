# vllm-project/vllm#37546: [Bug]: CPU backend crashes with `TypeError: 'function' object is not subscriptable` on first   inference request

| 字段 | 值 |
| --- | --- |
| Issue | [#37546](https://github.com/vllm-project/vllm/issues/37546) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CPU backend crashes with `TypeError: 'function' object is not subscriptable` on first   inference request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Environment - **vLLM version:** 0.17.1 - **Python:** 3.12 - **PyTorch:** - **Device:** CPU (`device_config=cpu`) - **Model:** `Qwen3_5ForConditionalGeneration` (Qwen3.5-VL-0.8B) - **OS:** Linux (Kubernetes pod, no GPU) ### Description When running vLLM with the CPU backend, the engine crashes on the **first inference request** with: ### Steps to Reproduce ```bash python3 -m vllm.entrypoints.openai.api_server \ --model /path/to/qwen3.5-vl \ --dtype half \ --enforce-eager \ --no-enable-prefix-caching Then send any completion request: curl -X POST http://localhost:8080/v1/completions \ -H "Content-Type: application/json" \ -d '{"model": "my-model", "prompt": "hello", "max_tokens": 16}' Actual Behavior (EngineCore_DP0) ERROR [core.py:1102] File ".../vllm/v1/worker/gpu_model_runner.py", line 978, in _update_states (EngineCore_DP0) ERROR [core.py:1102] self._zero_block_ids(scheduler_output.new_block_ids_to_zero) (EngineCore_DP0) ERROR [core.py:1102] File ".../vllm/v1/worker/gpu_model_runner.py", line 940, in _zero_block_ids (EngineCore_DP0) ERROR [core.py:1102] self._kv_block_zeroer.zero_block_ids(block_ids) (EngineCore_DP0) ERROR...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: CPU backend crashes with `TypeError: 'function' object is not subscriptable` on first inference request bug;cpu ### Your current environment ### 🐛 Describe the bug ### Environment - **vLLM version:** 0.17.1 - **P
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 17.1 - **Python:** 3.12 - **PyTorch:** - **Device:** CPU (`device_config=cpu`) - **Model:** `Qwen3_5ForConditionalGeneration` (Qwen3.5-VL-0.8B) - **OS:** Linux (Kubernetes pod, no GPU) ### Description When running vLLM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rent environment ### 🐛 Describe the bug ### Environment - **vLLM version:** 0.17.1 - **Python:** 3.12 - **PyTorch:** - **Device:** CPU (`device_config=cpu`) - **Model:** `Qwen3_5ForConditionalGeneration` (Qwen3.5-VL-0.8...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: t is not subscriptable Expected Behavior CPU backend should handle KV cache block zeroing without calling a Triton GPU kernel. Root Cause Analysis Two issues combine to cause this: 1. CPUModelRunner inherits _zero_block...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: `TypeError: 'function' object is not subscriptable` on first inference request bug;cpu ### Your current environment ### 🐛 Describe the bug ### Environment - **vLLM version:** 0.17.1 - **Python:** 3.12 - **PyTorch:** - *...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
