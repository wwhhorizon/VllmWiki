# vllm-project/vllm#26067: [Bug]: DSR1 + DEP8 on B200 fails with TensorRT-LLM latency and throughput kernels.

| 字段 | 值 |
| --- | --- |
| Issue | [#26067](https://github.com/vllm-project/vllm/issues/26067) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;gemm;kernel;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DSR1 + DEP8 on B200 fails with TensorRT-LLM latency and throughput kernels.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` (EngineCore_DP6 pid=243188) result = self.fn(*self.args, **self.kwargs) (EngineCore_DP6 pid=243188) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP6 pid=243188) File "/workspace/scratch-pmaj-1/gh-pm-vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response (EngineCore_DP6 pid=243188) raise RuntimeError( (EngineCore_DP6 pid=243188) RuntimeError: Worker failed with error 'Error occurred when running GEMM! (numBatches: 32, GemmMNK: 65536 4096 7168, Kernel: bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_cga1x1x1_16dp256b_TN_transOut_noShflA_dsFp8_s chedP4x2x2x3_bN_ldgsts_clmp_dynBatch_sm100f)', please check the stack trace above for the root cause (EngineCore_DP7 pid=243189) Process EngineCore_DP7: (EngineCore_DP7 pid=243189) Traceback (most recent call last): (EngineCore_DP7 pid=243189) File "/usr/lib/python3.12/multiprocess ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: DSR1 + DEP8 on B200 fails with TensorRT-LLM latency and throughput kernels. bug;stale ### Your current environment ### 🐛 Describe the bug ``` (EngineCore_DP6 pid=243188) result = self.fn(*self.args, **self.kwargs)
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support cuda;gemm;kernel;triton build_error;crash;slowdown env_depen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: DSR1 + DEP8 on B200 fails with TensorRT-LLM latency and throughput kernels. bug;stale ### Your current environment ### 🐛 Describe the bug ``` (EngineCore_DP6 pid=243188) result = self.fn(*self.args, **self.kwargs)
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_cga1x1x1_16dp256b_TN_transOut_noShflA_dsFp8_s chedP4x2x2x3_bN_ldgsts_clmp_dynBatch_sm100f)', please check the stack trace above for the root cause (EngineCore_DP7 pid=243189) Proc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: frontend_api;gemm_linear;hardware_porting;model_support cuda;gemm;kernel;triton build_error;crash;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
