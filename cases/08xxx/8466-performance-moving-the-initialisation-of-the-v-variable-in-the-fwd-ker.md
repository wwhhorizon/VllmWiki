# vllm-project/vllm#8466: [Performance]: Moving the initialisation of the v variable in the _fwd_kernel() function has an effect on performance.

| 字段 | 值 |
| --- | --- |
| Issue | [#8466](https://github.com/vllm-project/vllm/issues/8466) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Moving the initialisation of the v variable in the _fwd_kernel() function has an effect on performance.

### Issue 正文摘录

### Proposal to improve performance I was trying to benchmark the performance of the _fwd_kernel() function which performs flash attention in `vllm/attention/ops/prefix_prefill.py`. While doing so I noticed that moving the initialisation of the v variable resulted in a consistent increase in performance. This is how the _fwd_kernel() function looks currently (shortened to the relevant parts) - ```python ... ... start_n = tl.multiple_of(start_n, BLOCK_N) # -- compute qk ---- k = tl.load(k_ptrs + (cur_batch_in_all_start_index + start_n) * stride_kbs, mask=dim_mask[:, None] & ((start_n + offs_n[None, :]) < cur_batch_query_len), other=0.0) qk = tl.zeros([BLOCK_M, BLOCK_N], dtype=tl.float32) qk += tl.dot(q, k) qk *= sm_scale ... ... # scale acc acc_scale = l_i / l_i_new * alpha acc = acc * acc_scale[:, None] # update acc v = tl.load(v_ptrs + (cur_batch_in_all_start_index + start_n) * stride_vbs, mask=dim_mask[None, :] & ((start_n + offs_n[:, None]) < cur_batch_query_len), other=0.0) ... ... ``` I just moved the initialisation of the v variable in the query against itself loop, just below the initialisation of k - ```python ... ... start_n = tl.multiple_of(start_n, BLOCK_N) # -- compute...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: so I do not quite understand why this is happening or if this is reproducible on other machines. If it is reproducible I would appreciate any explanation for this. As this function would be called several times during t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: tl.zeros([BLOCK_M, BLOCK_N], dtype=tl.float32) qk += tl.dot(q, k) qk *= sm_scale ... ... # scale acc acc_scale = l_i / l_i_new * alpha acc = acc * acc_scale[:, None] # update acc v = tl.load(v_ptrs + (cur_batch_in_all_s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ch_query_len), other=0.0) qk = tl.zeros([BLOCK_M, BLOCK_N], dtype=tl.float32) qk += tl.dot(q, k) qk *= sm_scale ... ... # scale acc acc_scale = l_i / l_i_new * alpha acc = acc * acc_scale[:, None] # update acc v = tl.lo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: relevant parts) - ```python ... ... start_n = tl.multiple_of(start_n, BLOCK_N) # -- compute qk ---- k = tl.load(k_ptrs + (cur_batch_in_all_start_index + start_n) * stride_kbs, mask=dim_mask[:, None] & ((start_n + offs_n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ronment (if you think it is necessary) ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
