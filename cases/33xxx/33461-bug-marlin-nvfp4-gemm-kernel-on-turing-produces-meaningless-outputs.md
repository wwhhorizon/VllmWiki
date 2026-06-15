# vllm-project/vllm#33461: [Bug]: Marlin NVFP4 GEMM kernel on Turing produces meaningless outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#33461](https://github.com/vllm-project/vllm/issues/33461) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Marlin NVFP4 GEMM kernel on Turing produces meaningless outputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [#29901] Introduces marlin kernels for FP8 and NVFP4. However, when I tried loading NVFP4 checkpoints with marlin kernel on Turing device (RTX 2080Ti), model continuously outputs garbage outputs: ``` VLLM_NVFP4_GEMM_BACKEND=marlin vllm serve nvidia/Qwen3-14B-NVFP4 > curl http://localhost:8000/v1/chat/completions \ -X POST \ -H "Content-Type: application/json" \ -d '{ "model": "nvidia/Qwen3-14B-NVFP4", "messages": [ {"role": "user", "content": "Introduce yourself"} ], "temperature": 0.7, "max_tokens": 1000, "stream": true }' data: {"id":"chatcmpl-8bbcdb2d35bb72b2","object":"chat.completion.chunk","created":1769827901,"model":"nvidia/Qwen3-14B-NVFP4","choices":[{"index":0,"delta":{"role":"assistant","content":"","reasoning_content":null},"logprobs":null,"finish_reason":null}],"prompt_token_ids":null} data: {"id":"chatcmpl-8bbcdb2d35bb72b2","object":"chat.completion.chunk","created":1769827901,"model":"nvidia/Qwen3-14B-NVFP4","choices":[{"index":0,"delta":{"content":"!","reasoning_content":null},"logprobs":null,"finish_reason":null,"token_ids":null}]} data: {"id":"chatcmpl-8bbcdb2d35bb72b2","object":"chat.completion.chunk","created"...

## 现有链接修复摘要

#29901 [Kernel][Quantization][MoE] add marlin kernel support for turing (sm75) | #37135 [Bugfix] Fix FP16 overflow in NVFP4 Marlin kernel epilogue and forward input_global_scale on SM75

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Marlin NVFP4 GEMM kernel on Turing produces meaningless outputs bug;stale ### Your current environment ### 🐛 Describe the bug [#29901] Introduces marlin kernels for FP8 and NVFP4. However, when I tried loading NV...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: n I tried loading NVFP4 checkpoints with marlin kernel on Turing device (RTX 2080Ti), model continuously outputs garbage outputs: ``` VLLM_NVFP4_GEMM_BACKEND=marlin vllm serve nvidia/Qwen3-14B-NVFP4 > curl http://localh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;g...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 2080Ti), model continuously outputs garbage outputs: ``` VLLM_NVFP4_GEMM_BACKEND=marlin vllm serve nvidia/Qwen3-14B-NVFP4 > curl http://localhost:8000/v1/chat/completions \ -X POST \ -H "Content-Type: application/json"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ding NVFP4 checkpoints with marlin kernel on Turing device (RTX 2080Ti), model continuously outputs garbage outputs: ``` VLLM_NVFP4_GEMM_BACKEND=marlin vllm serve nvidia/Qwen3-14B-NVFP4 > curl http://localhost:8000/v1/c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29901](https://github.com/vllm-project/vllm/pull/29901) | mentioned | 0.45 | [Kernel][Quantization][MoE] add marlin kernel support for turing (sm75) | inductor_compile_threads=1 ``` </details> ### 🐛 describe the bug [#29901] introduces marlin kernels for fp8 and nvfp4. however, when i tried loading nvfp4 checkpoints with marlin… |
| [#37135](https://github.com/vllm-project/vllm/pull/37135) | closes_keyword | 0.95 | [Bugfix] Fix FP16 overflow in NVFP4 Marlin kernel epilogue and forward input_global_scale on SM75 | closes #33560 and #33461 **Relationship to PR #33972:** PR #33972 fixes the missing input scaling at the Python dispatch layer but does not touch the kernel. This PR includes the |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
