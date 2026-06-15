# vllm-project/vllm#26788: [Bug]: compressed tensors moe (nvfp4) consume an unusually large amount of vram

| 字段 | 值 |
| --- | --- |
| Issue | [#26788](https://github.com/vllm-project/vllm/issues/26788) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: compressed tensors moe (nvfp4) consume an unusually large amount of vram

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug * Merged #26669 ``` VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve RedHatAI/Qwen3-30B-A3B-NVFP4 ``` ``` (EngineCore_DP0 pid=6016) INFO 10-14 08:10:58 [default_loader.py:267] Loading weights took 7.45 seconds (EngineCore_DP0 pid=6016) INFO 10-14 08:10:59 [gpu_model_runner.py:2653] Model loading took 25.9087 GiB and 8.627268 seconds (EngineCore_DP0 pid=6016) INFO 10-14 08:11:08 [backends.py:548] Using cache directory: /root/.cache/vllm/torch_compile_cache/00507ceb63/rank_0_0/backbone for vLLM's torch.compile (EngineCore_DP0 pid=6016) INFO 10-14 08:11:08 [backends.py:559] Dynamo bytecode transform time: 8.67 s (EngineCore_DP0 pid=6016) INFO 10-14 08:11:13 [backends.py:197] Cache the graph for dynamic shape for later use (EngineCore_DP0 pid=6016) INFO 10-14 08:11:59 [backends.py:218] Compiling a graph for dynamic shape takes 5.96 s (EngineCore_DP0 pid=6016) INFO 10-14 08:17:26 [monitor.py:34] torch.compile takes 9.64 s in total ``` It takes 25.9087 GiB here, about 9 GiB larger than expected. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 8:11:08 [backends.py:548] Using cache directory: /root/.cache/vllm/torch_compile_cache/00507ceb63/rank_0_0/backbone for vLLM's torch.compile (EngineCore_DP0 pid=6016) INFO 10-14 08:11:08 [backends.py:559] Dynamo bytecod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: t environment ### 🐛 Describe the bug * Merged #26669 ``` VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve RedHatAI/Qwen3-30B-A3B-NVFP4 ``` ``` (EngineCore_DP0 pid=6016) INFO 10-14 08:10:58 [default_loader.py:267] Loading weight...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: compressed tensors moe (nvfp4) consume an unusually large amount of vram bug ### Your current environment ### 🐛 Describe the bug * Merged #26669 ``` VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve RedHatAI/Qwen3-30B-A3B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: * Merged #26669 ``` VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve RedHatAI/Qwen3-30B-A3B-NVFP4 ``` ``` (EngineCore_DP0 pid=6016) INFO 10-14 08:10:58 [default_loader.py:267] Loading weights took 7.45 seconds (EngineCore_DP0 p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
