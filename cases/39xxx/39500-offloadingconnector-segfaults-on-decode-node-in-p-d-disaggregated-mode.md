# vllm-project/vllm#39500: OffloadingConnector segfaults on decode node in P/D disaggregated mode with MultiConnector + NixlConnector

| 字段 | 值 |
| --- | --- |
| Issue | [#39500](https://github.com/vllm-project/vllm/issues/39500) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | crash;nondeterministic |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> OffloadingConnector segfaults on decode node in P/D disaggregated mode with MultiConnector + NixlConnector

### Issue 正文摘录

## Disclaimer - I will keep iterating on this issue as it's not very replicable right now due to sheer size and non-determinism, opening now to see if anyone has any clue from the top of their head ## Title OffloadingConnector segfaults on decode node in P/D disaggregated mode with MultiConnector + NixlConnector ## Bug ### Environment - **vLLM version**: v0.19.0 - **Model**: `zai-org/GLM-5-FP8` (MoE, FP8, expert parallel) - **Hardware**: 8x H200 per node, 4 nodes (2 prefill, 2 decode) - **Setup**: P/D disaggregated with `MultiConnector` wrapping `NixlConnector` + `OffloadingConnector` ### Configuration ```json { "kv_connector": "MultiConnector", "kv_role": "kv_both", "kv_connector_extra_config": { "connectors": [ {"kv_connector": "NixlConnector", "kv_role": "kv_both", "kv_connector_extra_config": {"num_threads": 1}}, {"kv_connector": "OffloadingConnector", "kv_role": "kv_both", "kv_connector_extra_config": {"cpu_bytes_to_use": 128000000000}} ] } } ``` Additional flags: - `data_parallel_size=16`, `data_parallel_size_local=8`, `data_parallel_hybrid_lb=True` - `enable_expert_parallel=True`, `all2all_backend=deepep_low_latency` - `compilation_config: {"cudagraph_mode": "FULL_DECODE_ON...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: OffloadingConnector segfaults on decode node in P/D disaggregated mode with MultiConnector + NixlConnector ## Disclaimer - I will keep iterating on this issue as it's not very replicable right now due to sheer size and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ### Environment - **vLLM version**: v0.19.0 - **Model**: `zai-org/GLM-5-FP8` (MoE, FP8, expert parallel) - **Hardware**: 8x H200 per node, 4 nodes (2 prefill, 2 decode) - **Setup**: P/D disaggregated with `MultiConnecto...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: _runner.py", line 3858, in execute_model logits_indices, spec_decode_metadata = self._prepare_inputs( File "vllm/v1/worker/gpu_model_runner.py", line 1958, in _prepare_inputs self.num_accepted_tokens.gpu.fill_(1) torch....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: allel;model_support;moe;quantization;scheduler_memory cuda;fp8;moe crash;nondeterministic dtype;env_dependency;memory_layout Disclaimer
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: de with MultiConnector + NixlConnector ## Bug ### Environment - **vLLM version**: v0.19.0 - **Model**: `zai-org/GLM-5-FP8` (MoE, FP8, expert parallel) - **Hardware**: 8x H200 per node, 4 nodes (2 prefill, 2 decode) - **...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
