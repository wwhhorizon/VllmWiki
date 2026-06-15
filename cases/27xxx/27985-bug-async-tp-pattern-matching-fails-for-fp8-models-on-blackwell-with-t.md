# vllm-project/vllm#27985: [Bug]: Async TP pattern matching fails for fp8 models on Blackwell with the default Flashinfer fp8 gemm

| 字段 | 值 |
| --- | --- |
| Issue | [#27985](https://github.com/vllm-project/vllm/issues/27985) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Async TP pattern matching fails for fp8 models on Blackwell with the default Flashinfer fp8 gemm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` VLLM_DEBUG_DUMP_PATH=fx_graph_async_tp vllm bench latency --model nvidia/Llama-3.3-70B-Instruct-FP8 --output-len 2 --input-len 8192 --batch-size 1 --tensor-parallel-size 2 --load-format dummy --num_iters_warmup 1 --num_iters 2 --no-enable-prefix-caching --compilation-config '{"pass_config": {"enable_async_tp": true, "enable_sequence_parallelism": true} ,"custom_ops": ["+quant_fp8", "+rms_norm"],"cudagraph_mode": "FULL_DECODE_ONLY","splitting_ ops": []}' ``` In the fx graph dump, in files `./rank_0/__compiled_fn_1.post_grad.1.AsyncTPPass.before.0.py` and `./rank_0/__compiled_fn_1.post_grad.1.AsyncTPPass.after.0.py` it can be seen that no changes were applied. Example patterns where we should have Async TP apply: ``` # File: /usr/local/lib/python3.12/dist-packages/vllm/utils/flashinfer.py:425 in flashinfer_scaled_fp8_mm, code: b.unsqueeze(0), unsqueeze_9: "f8e4m3fn[1, 4096, 8192]" = torch.ops.aten.unsqueeze.default(arg10_1, 0); arg10_1 = None # File: /usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:676 in __call__, code: return self._opoverload(*args, **kwargs) bmm_fp8_1: "bf16[1, s72, 8192]" = torch.ops.vll...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Async TP pattern matching fails for fp8 models on Blackwell with the default Flashinfer fp8 gemm bug ### Your current environment ### 🐛 Describe the bug ``` VLLM_DEBUG_DUMP_PATH=fx_graph_async_tp vllm bench laten...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ","splitting_ ops": []}' ``` In the fx graph dump, in files `./rank_0/__compiled_fn_1.post_grad.1.AsyncTPPass.before.0.py` and `./rank_0/__compiled_fn_1.post_grad.1.AsyncTPPass.after.0.py` it can be seen that no changes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Async TP pattern matching fails for fp8 models on Blackwell with the default Flashinfer fp8 gemm bug ### Your current environment ### 🐛 Describe the bug ``` VLLM_DEBUG_DUMP_PATH=fx_graph_async_tp vllm bench laten...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Async TP pattern matching fails for fp8 models on Blackwell with the default Flashinfer fp8 gemm bug ### Your current environment ### 🐛 Describe the bug ``` VLLM_DEBUG_DUMP_PATH=fx_graph_async_tp vllm bench laten...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pty.memory_format([sym_size_int_160, 8192], dtype = torch.float8_e4m3fn, layout = torch.strided, device = device(type='cuda', index=0), pin_memory = False); sym_size_int_160 = None permute_default_158: "f8e4m3fn[(s72//2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
