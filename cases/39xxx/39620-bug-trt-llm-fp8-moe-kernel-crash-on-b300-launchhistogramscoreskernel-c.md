# vllm-project/vllm#39620: [Bug]: TRT-LLM FP8 MoE kernel crash on B300 - launchHistogramScoresKernel CUDA error

| 字段 | 值 |
| --- | --- |
| Issue | [#39620](https://github.com/vllm-project/vllm/issues/39620) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TRT-LLM FP8 MoE kernel crash on B300 - launchHistogramScoresKernel CUDA error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary Serving `Qwen/Qwen3.5-397B-A17B-FP8` on 8xB300 with `dp=8 --enable-expert-parallel` crashes during engine initialization with a CUDA error in the TRT-LLM fused MoE routing kernel (`launchHistogramScoresKernel`). ## Reproduction ```bash vllm serve Qwen/Qwen3.5-397B-A17B-FP8 \ --port 8000 -tp 1 -pp 1 -dp 8 \ --enable-expert-parallel \ --language-model-only \ --reasoning-parser qwen3 \ --stream-interval 100 ``` ## Error All DP workers crash during `determine_available_memory()` with: ``` RuntimeError: Error in function 'launchHistogramScoresKernel' at /workspace/csrc/fused_moe/trtllm_backend/routingRenormalize/launchHistogramScoresKernel.cu:95: Got CUDA error. See above for details. ``` Call chain: `trtllm_fp8_moe.py:_apply_block_scale` → `flashinfer.fused_moe.trtllm_fp8_block_scale_moe` → `launchHistogramScoresKernel` (CUDA error). [Full failure log](https://github.com/user-attachments/files/26658176/histogram_log.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/la...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: during engine initialization with a CUDA error in the TRT-LLM fused MoE routing kernel (`launchHistogramScoresKernel`). ## Reproduction ```bash vllm serve Qwen/Qwen3.5-397B-A17B-FP8 \ --port 8000 -tp 1 -pp 1 -dp 8 \ --e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: TRT-LLM FP8 MoE kernel crash on B300 - launchHistogramScoresKernel CUDA error bug ### Your current environment ### 🐛 Describe the bug ## Summary Serving `Qwen/Qwen3.5-397B-A17B-FP8` on 8xB300 with `dp=8 --enable-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: TRT-LLM FP8 MoE kernel crash on B300 - launchHistogramScoresKernel CUDA error bug ### Your current environment ### 🐛 Describe the bug ## Summary Serving `Qwen/Qwen3.5-397B-A17B-FP8` on 8xB300 with `dp=8 --enable-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Bug]: TRT-LLM FP8 MoE kernel crash on B300 - launchHistogramScoresKernel CUDA error bug ### Your current environment ### 🐛 Describe the bug ## Summary Serving `Qwen/Qwen3.5-397B-A17B-FP8` on 8xB300 with `dp=8 --enable-e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
