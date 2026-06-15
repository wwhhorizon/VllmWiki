# vllm-project/vllm#34249: [Bug]: [Fp8] [MoE] 'FLASHINFER_CUTLASS' is auto-selected as MoE backend instead of 'DEEPGEMM' on hopper

| 字段 | 值 |
| --- | --- |
| Issue | [#34249](https://github.com/vllm-project/vllm/issues/34249) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: [Fp8] [MoE] 'FLASHINFER_CUTLASS' is auto-selected as MoE backend instead of 'DEEPGEMM' on hopper

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On H100 x 8 worker and using the latest vllm (here I am using `vllm==0.15.2rc1.dev152+g9608844f9`), launching a non-mla fp8 MoE model server prints the following log at the beginning: ## example vllm launch script Here I use Qwen3MoE checkpoint, but theoretically any non-mla fp8 MoE checkpoints would suffer similar error. ```shell vllm serve Qwen/Qwen3-235B-A22B-Instruct-2507-FP8 \ --gpu-utilization 0.95 \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --max-model-len 262144 \ --max-num-batched-tokens 16384 # set --max-num-batched-tokens to prove that flashinfer fp8 does not work over this token limit ``` ## FP8 MoE backend selection log ```log ... (Worker_TP0_EP0 pid=955) INFO 02-10 20:34:43 [fp8.py:329] Using FLASHINFER_CUTLASS Fp8 MoE backend out of potential backends: ['AITER', 'FLASHINFER_TRTLLM', 'FLASHINFER_CUTLASS', 'DEEPGEMM', 'BATCHED_DEEPGEMM', 'TRITON', 'BATCHED_TRITON', 'MARLIN']. ... ``` ## Error traceback for >16k input With the launch script above, the model server launches successfully and works well for short (<16k here, `--max-num-batched-tokens` is the threshold) inputs. But if a long request is sent, t...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: [Bug]: [Fp8] [MoE] 'FLASHINFER_CUTLASS' is auto-selected as MoE backend instead of 'DEEPGEMM' on hopper bug ### Your current environment ### 🐛 Describe the bug On H100 x 8 worker and using the latest vllm (here I am usi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: HINFER_CUTLASS' is auto-selected as MoE backend instead of 'DEEPGEMM' on hopper bug ### Your current environment ### 🐛 Describe the bug On H100 x 8 worker and using the latest vllm (here I am using `vllm==0.15.2rc1.dev1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d vice versa on blackwell), so it would be natural to apply the same principle and default the Fp8 MoE backend to `DEEPGEMM` on hopper / `FLASHINFER_CUTLASS` on blackwell. ### Before submitting a new issue... - [x] Make...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: [Fp8] [MoE] 'FLASHINFER_CUTLASS' is auto-selected as MoE backend instead of 'DEEPGEMM' on hopper bug ### Your current environment ### 🐛 Describe the bug On H100 x 8 worker and using the latest vllm (here I am usi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: or;quantization;triton build_error;crash;oom dtype;env_dependency;memory_layout #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generat...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 4_ep4 pid=959) error 02-10 19:36:29 [multiproc_executor.py:863] frame #4: at::detail::empty_generic(c10::arrayref<long>, c10::allocator*, c10::dispatchkeyset, c10::scalartype, std… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | 4_ep4 pid=959) error 02-10 19:36:29 [multiproc_executor.py:863] frame #6: at::detail::empty_cuda(c10::arrayref<long>, std::optional<c10::scalartype>, std::optional<c10::layout>, s… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 4_ep4 pid=959) error 02-10 19:36:29 [multiproc_executor.py:863] frame #7: at::native::empty_cuda(c10::arrayref<long>, std::optional<c10::scalartype>, std::optional<c10::layout>, s… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | 4_ep4 pid=959) error 02-10 19:36:29 [multiproc_executor.py:863] frame #12: at::_ops::empty_memory_format::call(c10::arrayref<c10::symint>, std::optional<c10::scalartype>, std::opt… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | 4_ep4 pid=959) error 02-10 19:36:29 [multiproc_executor.py:863] frame #16: <unknown function> + 0x78e302 (0x7fa5cd560302 in /opt/venv/lib/python3.12/site-packages/flashinfer_jit_c… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | 4_ep4 pid=959) error 02-10 19:36:29 [multiproc_executor.py:863] frame #20: <unknown function> + 0x54a8c (0x7fb0c4063a8c in /opt/venv/lib/python3.12/site-packages/tvm_ffi/core.abi3… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | 4_ep4 pid=959) error 02-10 19:36:29 [multiproc_executor.py:863] frame #21: pyobject_call + 0x6c (0x54afac in vllm::worker_tp4_ep4) (worker_tp4_ep4 pid=959) error 02-10 19:36:29 [m… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | 4_ep4 pid=959) error 02-10 19:36:29 [multiproc_executor.py:863] frame #27: pyobject_call + 0x115 (0x54b055 in vllm::worker_tp4_ep4) (worker_tp4_ep4 pid=959) error 02-10 19:36:29 [… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | 4_ep4 pid=959) error 02-10 19:36:29 [multiproc_executor.py:863] frame #29: _pyobject_call_prepend + 0x18a (0x54a73a in vllm::worker_tp4_ep4) (worker_tp4_ep4 pid=959) error 02-10 1… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | 4_ep4 pid=959) error 02-10 19:36:29 [multiproc_executor.py:863] frame #32: _pyeval_evalframedefault + 0xa89 (0x5d71d9 in vllm::worker_tp4_ep4) (worker_tp4_ep4 pid=959) error 02-10… |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | 4_ep4 pid=959) error 02-10 19:36:29 [multiproc_executor.py:863] frame #53: _pyobject_maketpcall + 0x75 (0x548e25 in vllm::worker_tp4_ep4) (worker_tp4_ep4 pid=959) error 02-10 19:3… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
