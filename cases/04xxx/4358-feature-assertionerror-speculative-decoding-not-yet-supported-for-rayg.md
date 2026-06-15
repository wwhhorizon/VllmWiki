# vllm-project/vllm#4358: [Feature]: AssertionError: Speculative decoding not yet supported for RayGPU backend.

| 字段 | 值 |
| --- | --- |
| Issue | [#4358](https://github.com/vllm-project/vllm/issues/4358) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: AssertionError: Speculative decoding not yet supported for RayGPU backend.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, Do you guys have any workaround for the `Speculative decoding not yet supported for RayGPU backend.` error or idea when the RayGPU backend will support speculative decoding? I run vllm server with the following command: ``` python3 -u -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --model casperhansen/mixtral-instruct-awq \ --tensor-parallel-size 4 \ --enforce-eager \ --quantization awq \ --gpu-memory-utilization 0.96 \ --kv-cache-dtype fp8 \ --speculative-model mistralai/Mistral-7B-Instruct-v0.2 \ --num-speculative-tokens 3 \ --use-v2-block-manager \ --num-lookahead-slots 5 ``` However, I got `AssertionError: Speculative decoding not yet supported for RayGPU backend.` ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: wq \ --tensor-parallel-size 4 \ --enforce-eager \ --quantization awq \ --gpu-memory-utilization 0.96 \ --kv-cache-dtype fp8 \ --speculative-model mistralai/Mistral-7B-Instruct-v0.2 \ --num-speculative-tokens 3 \ --use-v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: AssertionError: Speculative decoding not yet supported for RayGPU backend. feature request;stale ### 🚀 The feature, motivation and pitch Hi, Do you guys have any workaround for the `Speculative decoding not y...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: l-7B-Instruct-v0.2 \ --num-speculative-tokens 3 \ --use-v2-block-manager \ --num-lookahead-slots 5 ``` However, I got `AssertionError: Speculative decoding not yet supported for RayGPU backend.` ### Alternatives _No res...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ture]: AssertionError: Speculative decoding not yet supported for RayGPU backend. feature request;stale ### 🚀 The feature, motivation and pitch Hi, Do you guys have any workaround for the `Speculative decoding not yet s...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: --quantization awq \ --gpu-memory-utilization 0.96 \ --kv-cache-dtype fp8 \ --speculative-model mistralai/Mistral-7B-Instruct-v0.2 \ --num-speculative-tokens 3 \ --use-v2-block-manager \ --num-lookahead-slots 5 ``` Howe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
