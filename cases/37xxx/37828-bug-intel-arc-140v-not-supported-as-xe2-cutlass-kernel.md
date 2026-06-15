# vllm-project/vllm#37828: [Bug]: Intel ARC 140v not supported as XE2 cutlass kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#37828](https://github.com/vllm-project/vllm/issues/37828) |
| 状态 | open |
| 标签 | bug;intel-gpu |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Intel ARC 140v not supported as XE2 cutlass kernel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I followed the official document, installed and ran vLLM on Ubuntu 24.04 via WSL2, with Intel arc 140v GPU integrated to Intel core ultra 7 268v. I encountered the error not recognizing Intel arc 140v as XE2 cutclass. It's worth mentioning that before "Deprecate ipex and switch to vllm-xpu-kernels for xpu platform" in Feb 2026, I was able to follow the tutorial here https://www.rogerngo.com/blog/accessible-ai-vllm-on-intel-arc to install and run vLLM. However, today I cannot find an old commit and follow the same steps to make it work. Error ``` (EngineCore pid=6844) ERROR 03-22 22:03:08 [core.py:1108] EngineCore failed to start. (EngineCore pid=6844) ERROR 03-22 22:03:08 [core.py:1108] Traceback (most recent call last): (EngineCore pid=6844) ERROR 03-22 22:03:08 [core.py:1108] File "/home/pteros/src/vllm/vllm/v1/engine/core.py", line 1082, in run_engine_core (EngineCore pid=6844) ERROR 03-22 22:03:08 [core.py:1108] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore pid=6844) ERROR 03-22 22:03:08 [core.py:1108] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=6844) ERROR 03-22 22:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug I followed the official document, installed and ran vLLM on Ubuntu 24.04 via WSL2, with Intel arc 140v GPU integrated to Intel core ultra 7 268v. I encountered the error n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _ (EngineCore pid=6844) ERROR 03-22 22:03:08 [core.py:1108] kv_cache_config = self._initialize_kv_caches(vllm_config) (EngineCore pid=6844) ERROR 03-22 22:03:08 [core.py:1108] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (En...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Intel ARC 140v not supported as XE2 cutlass kernel bug;intel-gpu ### Your current environment ### 🐛 Describe the bug I followed the official document, installed and ran vLLM on Ubuntu 24.04 via WSL2, with Intel a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: EL-SW-PRODUCTS.PUB | gpg --dearmor | sudo tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main"...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Core pid=6844) ERROR 03-22 22:03:08 [core.py:1108] self.model_runner.profile_run() (EngineCore pid=6844) ERROR 03-22 22:03:08 [core.py:1108] File "/home/pteros/src/vllm/vllm/v1/worker/gpu_model_runner.py", line 5520, in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
