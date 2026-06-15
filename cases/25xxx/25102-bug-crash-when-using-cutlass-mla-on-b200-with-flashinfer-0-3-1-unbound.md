# vllm-project/vllm#25102: [Bug]: Crash when using CUTLASS_MLA on B200 with flashinfer 0.3.1: `UnboundLocalError: cannot access local variable 'returned_lse' where it is not associated with a value`

| 字段 | 值 |
| --- | --- |
| Issue | [#25102](https://github.com/vllm-project/vllm/issues/25102) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash when using CUTLASS_MLA on B200 with flashinfer 0.3.1: `UnboundLocalError: cannot access local variable 'returned_lse' where it is not associated with a value`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running a DP=8 DeepSeek 1p1d config on main with this [configuration](https://github.com/smarterclayton/ig-load/blob/flashinfer/config/deploy_base_deepseek_r1_ep_pd.yaml#L79) I encounter a stack trace on the decode worker after the NIXL transfer completes from cutlass. ``` (EngineCore_DP0 pid=948) DEBUG 09-17 17:43:05 [distributed/.../v1/nixl_connector.py:630] NIXL handshake: add agent took: 0.14727665903046727 (EngineCore_DP0 pid=948) INFO 09-17 17:43:06 [distributed/eplb/eplb_state.py:390] EPLB step: avg_tokens=0.00, max_tokens=0, balancedness=0.0000 (EngineCore_DP0 pid=948) DEBUG 09-17 17:43:06 [v1/core/sched/scheduler.py:346] cmpl-4b261d56-940f-11f0-8834-f626bb89024b-0 is still in WAITING_FOR_REMOTE_KVS state. (EngineCore_DP0 pid=948) DEBUG 09-17 17:43:06 [distributed/.../v1/nixl_connector.py:1144] Remote agent 848c5216-c1fa-48a2-bc07-a64aba9aa04a_dp0 available, calling _read_blocks for req cmpl-4b261d56-940f-11f0-8834-f626bb89024b-0 [1758145386.070144] [vllm-deepseek-r1-ep-pd-0:948 :0] mpool.c:281 UCX DEBUG mpool ucp_requests: allocated chunk 0x120e18d74 of 41044 bytes with 128 elements [1758145386.070538] [vllm-deepsee...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: cal variable 'returned_lse' where it is not associated with a value` bug;stale ### Your current environment ### 🐛 Describe the bug When running a DP=8 DeepSeek 1p1d config on main with this [configuration](https://githu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: Crash when using CUTLASS_MLA on B200 with flashinfer 0.3.1: `UnboundLocalError: cannot access local variable 'returned_lse' where it is not associated with a value` bug;stale ### Your current environment ### 🐛 De...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: alError: cannot access local variable 'returned_lse' where it is not associated with a value` bug;stale ### Your current environment ### 🐛 Describe the bug When running a DP=8 DeepSeek 1p1d config on main with this [con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Crash when using CUTLASS_MLA on B200 with flashinfer 0.3.1: `UnboundLocalError: cannot access local variable 'returned_lse' where it is not associated with a value` bug;stale ### Your current environment ### 🐛 De...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
