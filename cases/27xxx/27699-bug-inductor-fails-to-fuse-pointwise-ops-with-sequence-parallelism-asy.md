# vllm-project/vllm#27699: [Bug]: Inductor fails to fuse pointwise ops with sequence parallelism + async TP

| 字段 | 值 |
| --- | --- |
| Issue | [#27699](https://github.com/vllm-project/vllm/issues/27699) |
| 状态 | open |
| 标签 | bug;torch.compile;keep-open |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Inductor fails to fuse pointwise ops with sequence parallelism + async TP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using sequence parallelism, we transform a sequence of `all_reduce -> rms_norm -> quant_fp8` into `reduce_scatter -> rms_norm -> quant_fp8 -> all_gather`. Async TP then fuses the 2 communication ops onto the GEMMs surrounding this pattern. Whether we're using SP or not, we expect the sequence of `rms_norm -> quant_fp8` to produce a single fused Triton kernel. That is the case without SP + Async TP but with those two passes, Inductor generates two separate kernels for some reason. This requires #27126. Repro command: ``` python examples/offline_inference/basic/generate.py --model redhatai/meta-llama-3.1-70B-Instruct-FP8 --tensor-parallel-size=4 --kv-cache-dtype=fp8 --no-enable-prefix-caching --gpu_memory_utilization=0.8 -O.pass_config='{"enable_async_tp":true,"enable_noop":true}' -O.use_inductor_graph_partition=True -O.cudagraph_mode=NONE --load-format=dummy ``` Inductor output code without SP + Async TP: ``` def partition_1(...): ... # Topologically Sorted Source Nodes: [view_7, unified_attention_with_output, to_10, reciprocal_2, mul_15, clamp_2, to_11, cutlass_scaled_mm_1], Original ATen: [aten.view, aten._to_copy, aten.rec...

## 现有链接修复摘要

#27126 [compile] Enable sequence parallelism matching w/o custom ops enabled

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: uence parallelism, we transform a sequence of `all_reduce -> rms_norm -> quant_fp8` into `reduce_scatter -> rms_norm -> quant_fp8 -> all_gather`. Async TP then fuses the 2 communication ops onto the GEMMs surrounding th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: epro command: ``` python examples/offline_inference/basic/generate.py --model redhatai/meta-llama-3.1-70B-Instruct-FP8 --tensor-parallel-size=4 --kv-cache-dtype=fp8 --no-enable-prefix-caching --gpu_memory_utilization=0....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ils to fuse pointwise ops with sequence parallelism + async TP bug;torch.compile;keep-open ### Your current environment ### 🐛 Describe the bug When using sequence parallelism, we transform a sequence of `all_reduce -> r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Inductor fails to fuse pointwise ops with sequence parallelism + async TP bug;torch.compile;keep-open ### Your current environment ### 🐛 Describe the bug When using sequence parallelism, we transform a sequence o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: expect the sequence of `rms_norm -> quant_fp8` to produce a single fused Triton kernel. That is the case without SP + Async TP but with those two passes, Inductor generates two separate kernels for some reason. This req...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27126](https://github.com/vllm-project/vllm/pull/27126) | mentioned | 0.45 | [compile] Enable sequence parallelism matching w/o custom ops enabled  | ductor generates two separate kernels for some reason. this requires #27126. repro command: ``` python examples/offline_inference/basic/generate.py --model redhatai/meta-llama-3.1… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
