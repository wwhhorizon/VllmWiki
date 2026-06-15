# vllm-project/vllm#34477: [Bug]: TVM_FFI_ICHECK(args->n_group != 0) << "n_group should not be zero for DeepSeekV3 routing"

| 字段 | 值 |
| --- | --- |
| Issue | [#34477](https://github.com/vllm-project/vllm/issues/34477) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TVM_FFI_ICHECK(args->n_group != 0) << "n_group should not be zero for DeepSeekV3 routing"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Currently on `GB200`, When I running `minimax/MiniMax-M2.1`, I encountered the following error. ```bash (Worker_TP2 pid=479523) ERROR 02-13 00:28:06 [multiproc_executor.py:863] File "/mnt/data/vllm/vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py", line 222, in flashinfer_fused_moe_blockscale_fp8 (Worker_TP2 pid=479523) ERROR 02-13 00:28:06 [multiproc_executor.py:863] return flashinfer_trtllm_fp8_block_scale_moe( (Worker_TP2 pid=479523) ERROR 02-13 00:28:06 [multiproc_executor.py:863] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP2 pid=479523) ERROR 02-13 00:28:06 [multiproc_executor.py:863] File "/mnt/data/vllm/vllm/utils/flashinfer.py", line 102, in wrapper (Worker_TP2 pid=479523) ERROR 02-13 00:28:06 [multiproc_executor.py:863] return impl(*args, **kwargs) (Worker_TP2 pid=479523) ERROR 02-13 00:28:06 [multiproc_executor.py:863] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP2 pid=479523) ERROR 02-13 00:28:06 [multiproc_executor.py:863] File "/mnt/data/vllm/.venv/lib/python3.12/site-packages/flashinfer/fused_moe/core.py", line 2335, in trtllm_fp8_block_scale_moe (Worker_TP2 pid=479523) ERROR 02-13 00:28:06 [multiproc_executor....

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Your current environment ### 🐛 Describe the bug Currently on `GB200`, When I running `minimax/MiniMax-M2.1`, I encountered the following error. ```bash (Worker_TP2 pid=479523) ERROR 02-13 00:28:06 [multiproc_executo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ICHECK(args->n_group != 0) << "n_group should not be zero for DeepSeekV3 routing" bug ### Your current environment ### 🐛 Describe the bug Currently on `GB200`, When I running `minimax/MiniMax-M2.1`, I encountered the fo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ed_moe/flashinfer_trtllm_moe.py", line 222, in flashinfer_fused_moe_blockscale_fp8 (Worker_TP2 pid=479523) ERROR 02-13 00:28:06 [multiproc_executor.py:863] return flashinfer_trtllm_fp8_block_scale_moe( (Worker_TP2 pid=4...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ICHECK(args->n_group != 0) << "n_group should not be zero for DeepSeekV3 routing" bug ### Your current environment ### 🐛 Describe the bug Currently on `GB200`, When I running `minimax/MiniMax-M2.1`, I encountered the fo...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pid=479523) ERROR 02-13 00:28:06 [multiproc_executor.py:863] ``` ## Reproduced Snippet ```bash vllm serve minimax/MiniMax-M2.1 \ --tensor-parallel-size 4 \ --tool-call-parser minimax_m2 \ --reasoning-parser minimax_m2_a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
