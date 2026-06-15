# vllm-project/vllm#41955: [Bug]: Mixed INT4/INT8 GPTQ MoE models crash on initialization (AssertionError in fused_marlin_moe)

| 字段 | 值 |
| --- | --- |
| Issue | [#41955](https://github.com/vllm-project/vllm/issues/41955) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mixed INT4/INT8 GPTQ MoE models crash on initialization (AssertionError in fused_marlin_moe)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run a mixed-precision GPTQ model (INT4 / INT8) with a Mixture of Experts architecture (GLM-4 MoE). On recent vLLM commits, the server crashes immediately upon loading weights because the dispatcher forces INT8 MoE layers into the MarlinExperts fused kernel. The MarlinExperts kernel strictly asserts for 4-bit or FP8 weights. Because some of my expert layers are quantized to standard INT8 (int8_w8a16), the assertion trips. The server crashes with `AssertionError: Supports only {mxfp,nvfp,int}4_w4a16 or fp8_w8a16` start: ``` vllm serve QuantTrio/GLM-4.7-GPTQ-Int4-Int8Mix \ --gpu-memory-utilization 0.95 --max-model-len 202752 --port 8000 \ --max-num-seqs 16 --max-num-batched-tokens 512 \ -tp 8 -pp 2 --enable-expert-parallel \ --scheduling-policy priority \ --tool-call-parser glm47 --reasoning-parser glm45 --enable-auto-tool-choice \ --served-model-name GLM --distributed-executor-backend ray ``` Relevant part of log: ``` (APIServer) Resolved architecture: Glm4MoeForCausalLM (APIServer) The model is convertible to gptq_marlin during runtime. Using gptq_marlin kernel. (EngineCore pid=586017) ERROR 05-03 18:53:34 [core.py:...

## 现有链接修复摘要

#42022 [Bugfix] Route INT8 GPTQ MoE to WNA16 fallback

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Mixed INT4/INT8 GPTQ MoE models crash on initialization (AssertionError in fused_marlin_moe) bug ### Your current environment ### 🐛 Describe the bug I am trying to run a mixed-precision GPTQ model (INT4 / INT8) w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: commits, the server crashes immediately upon loading weights because the dispatcher forces INT8 MoE layers into the MarlinExperts fused kernel. The MarlinExperts kernel strictly asserts for 4-bit or FP8 weights. Because...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nt environment ### 🐛 Describe the bug I am trying to run a mixed-precision GPTQ model (INT4 / INT8) with a Mixture of Experts architecture (GLM-4 MoE). On recent vLLM commits, the server crashes immediately upon loading...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: run a mixed-precision GPTQ model (INT4 / INT8) with a Mixture of Experts architecture (GLM-4 MoE). On recent vLLM commits, the server crashes immediately upon loading weights because the dispatcher forces INT8 MoE layer...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Mixed INT4/INT8 GPTQ MoE models crash on initialization (AssertionError in fused_marlin_moe) bug ### Your current environment ### 🐛 Describe the bug I am trying to run a mixed-precision GPTQ model (INT4 / INT8) w...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42022](https://github.com/vllm-project/vllm/pull/42022) | closes_keyword | 0.95 | [Bugfix] Route INT8 GPTQ MoE to WNA16 fallback | Fixes #41955 ## Test Plan ```bash pytest tests/quantization/test_gptq_int8_moe_fallback.py -v ``` Six test cases covering: - Base INT8 config falls back to `MoeWNA16Method` - Ba |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
