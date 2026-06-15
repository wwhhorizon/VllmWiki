# vllm-project/vllm#43523: NIXL KV transfer crash with asymmetric TP (prefill TP=4, decode TP=1) — vLLM 0.1.dev1+g2b51d23f6, NIXL 0.8.0

| 字段 | 值 |
| --- | --- |
| Issue | [#43523](https://github.com/vllm-project/vllm/issues/43523) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | crash;mismatch;nondeterministic |
| 根因提示 | dtype;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> NIXL KV transfer crash with asymmetric TP (prefill TP=4, decode TP=1) — vLLM 0.1.dev1+g2b51d23f6, NIXL 0.8.0

### Issue 正文摘录

## Bug: NIXL KeyError in block_size_ratio_from_engine_id with asymmetric TP ### Description When running PD disaggregation with **asymmetric TP** (prefill TP=4, decode TP=1), the decode pod crashes with a `KeyError` in `nixl_connector.py` during KV transfer. The decode engine can't find the prefill engine's block size in its `remote_block_size` map. The crash happens on the first request that completes prefill and attempts KV handoff to decode. All decode pods crash, leaving only prefill pods running. ### Reproduction - **Model**: RedHatAI/Meta-Llama-3.1-70B-Instruct-FP8-dynamic (dense, NOT MoE) - **Architecture**: PD disaggregation (separate prefill and decode LWS) - **Prefill**: 3 pods × TP=4 (12 GPUs) - **Decode**: 4 pods × TP=1 (4 GPUs) - **GPU**: NVIDIA H200 141GB - **KV Connector**: NixlConnector, kv_role=kv_both - **max_model_len**: 2205 - **Workload**: 100 concurrent users, ISL=2000, OSL=100 Symmetric TP configurations (TP=1/TP=1, TP=2/TP=2, TP=4/TP=4) work fine. The crash only occurs when `prefill_tp > decode_tp`. ### Error ``` File "/opt/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 2671, in execute_model return self.kv_connector_no_forward( File "/opt/vllm-sourc...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: NIXL KV transfer crash with asymmetric TP (prefill TP=4, decode TP=1) — vLLM 0.1.dev1+g2b51d23f6, NIXL 0.8.0 ## Bug: NIXL KeyError in block_size_ratio_from_engine_id with asymmetric TP ### Description When running PD di...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: andshake either fails silently or the registration is rejected due to TP mismatch, leaving `remote_block_size` empty for that engine ID. When `get_finished()` tries to compute `block_size_ratio_from_engine_id()` for a c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ng. ### Reproduction - **Model**: RedHatAI/Meta-Llama-3.1-70B-Instruct-FP8-dynamic (dense, NOT MoE) - **Architecture**: PD disaggregation (separate prefill and decode LWS) - **Prefill**: 3 pods × TP=4 (12 GPUs) - **Deco...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: *: RedHatAI/Meta-Llama-3.1-70B-Instruct-FP8-dynamic (dense, NOT MoE) - **Architecture**: PD disaggregation (separate prefill and decode LWS) - **Prefill**: 3 pods × TP=4 (12 GPUs) - **Decode**: 4 pods × TP=1 (4 GPUs) -...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: de TP=1) — vLLM 0.1.dev1+g2b51d23f6, NIXL 0.8.0 ## Bug: NIXL KeyError in block_size_ratio_from_engine_id with asymmetric TP ### Description When running PD disaggregation with **asymmetric TP** (prefill TP=4, decode TP=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
