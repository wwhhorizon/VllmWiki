# vllm-project/vllm#27440: [Bug]: Qwen3-VL-235B-NVFP4 DP+TP+EP config not working with FlashinferMoE

| 字段 | 值 |
| --- | --- |
| Issue | [#27440](https://github.com/vllm-project/vllm/issues/27440) |
| 状态 | closed |
| 标签 | bug;stale;nvidia |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-235B-NVFP4 DP+TP+EP config not working with FlashinferMoE

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to benchmark Qwen3-VL-235B-A22 with nvfp4 on different configurations, it appears that FlashinferExpert method's Allgather reads a wrong DP size, which lead to an assersion error. This error is **NVFP4 code path only** since it's pointing to flashinfer expert moe's AllGather communication setup. ``` (Worker_DP3_TP0_EP6 pid=11528) ERROR 10-23 04:29:35 [multiproc_executor.py:671] File "/usr/local/lib/python3.12/dist-packages/vllm/compilation/cuda_graph.py", line 121, in __call__ (Worker_DP3_TP0_EP6 pid=11528) ERROR 10-23 04:29:35 [multiproc_executor.py:671] return self.runnable(*args, **kwargs) (Worker_DP3_TP0_EP6 pid=11528) ERROR 10-23 04:29:35 [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_DP3_TP0_EP6 pid=11528) ERROR 10-23 04:29:35 [multiproc_executor.py:671] File "/usr/local/lib/python3.12/dist-packages/vllm/compilation/cuda_piecewise_backend.py", line 90, in __call__ (Worker_DP3_TP0_EP6 pid=11528) ERROR 10-23 04:29:35 [multiproc_executor.py:671] return self.compiled_graph_for_general_shape(*args) (Worker_DP3_TP0_EP6 pid=11528) ERROR 10-23 04:29:35 [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Qwen3-VL-235B-NVFP4 DP+TP+EP config not working with FlashinferMoE bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug When trying to benchmark Qwen3-VL-235B-A22 with nvfp4 on different configura...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: =11528) ERROR 10-23 04:29:35 [multiproc_executor.py:671] return self.compiled_graph_for_general_shape(*args) (Worker_DP3_TP0_EP6 pid=11528) ERROR 10-23 04:29:35 [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL-235B-NVFP4 DP+TP+EP config not working with FlashinferMoE bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug When trying to benchmark Qwen3-VL-235B-A22 with nvfp4 on different configura...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: Qwen3-VL-235B-NVFP4 DP+TP+EP config not working with FlashinferMoE bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug When trying to benchmark Qwen3-VL-235B-A22 with nvfp4 on different configura...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ### Your current environment ### 🐛 Describe the bug When trying to benchmark Qwen3-VL-235B-A22 with nvfp4 on different configurations, it appears that FlashinferExpert method's Allgather reads a wrong DP size, which lea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
