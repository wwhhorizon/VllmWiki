# vllm-project/vllm#31679: [Bug]: Qwen3-VL-8B crashes on latest nightly with --async-scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#31679](https://github.com/vllm-project/vllm/issues/31679) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;quantization;sampling |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-8B crashes on latest nightly with --async-scheduling

### Issue 正文摘录

### Summary Running **Qwen/Qwen3-VL-8B-Instruct-FP8** on the **latest nightly vLLM OpenAI docker image** consistently crashes under load when **`--async-scheduling` is enabled**. Disabling async scheduling makes the issue disappear. This appears closely related to the previously fixed **async multimodal CPU tensor race condition** (PR #31373), but the crash is still reproducible on a newer nightly (`0.14.0rc1.dev221+g97a01308e`). --- ### Environment **Host OS** * Debian GNU/Linux (bare metal / VM) **GPU** * 2 × NVIDIA GeForce RTX 5060 Ti (16 GB each) * Driver: `590.44.01` * CUDA: `13.1` **nvidia-smi** ``` Driver Version: 590.44.01 CUDA Version: 13.1 GPU: RTX 5060 Ti (16GB) ×4 ``` **Docker images** ``` vllm/vllm-openai:nightly (ID: 31e08c7f6d05) ``` **vLLM version (nightly)** ``` vLLM API server version: 0.14.0rc1.dev221+g97a01308e ``` --- ### Model * `Qwen/Qwen3-VL-8B-Instruct-FP8` * Multimodal (image enabled, video disabled) --- ### Launch Command ```bash docker run -d --security-opt apparmor=unconfined \ --name qwen3vl-8b-fp8 \ --restart unless-stopped \ --gpus '"device=1,2"' \ -p 9003:9000 \ -v /mnt/aidisk/cache:/root/.cache \ -e VLLM_SLEEP_WHEN_IDLE=1 \ -e HF_HUB_OFFLINE=1 \ v...

## 现有链接修复摘要

#31841 [Bugfix] Fix race condition in async-scheduling for vlm model

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: Qwen3-VL-8B crashes on latest nightly with --async-scheduling bug ### Summary Running **Qwen/Qwen3-VL-8B-Instruct-FP8** on the **latest nightly vLLM OpenAI docker image** consistently crashes under load when **`-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: After a period of sustained traffic (multiple concurrent chat/completion requests): * Worker processes exit: ``` Parent process exited, terminating worker ``` * Engine crashes: ``` EngineCore_DP0 died unexpectedly vllm....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: [Bug]: Qwen3-VL-8B crashes on latest nightly with --async-scheduling bug ### Summary Running **Qwen/Qwen3-VL-8B-Instruct-FP8** on the **latest nightly vLLM OpenAI docker image** consistently crashes under load when **`-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ng **Qwen/Qwen3-VL-8B-Instruct-FP8** on the **latest nightly vLLM OpenAI docker image** consistently crashes under load when **`--async-scheduling` is enabled**. Disabling async scheduling makes the issue disappear. Thi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: --async-scheduling bug ### Summary Running **Qwen/Qwen3-VL-8B-Instruct-FP8** on the **latest nightly vLLM OpenAI docker image** consistently crashes under load when **`--async-scheduling` is enabled**. Disabling async s...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31841](https://github.com/vllm-project/vllm/pull/31841) | closes_keyword | 0.95 | [Bugfix] Fix race condition in async-scheduling for vlm model | Fixes #31679 The issue occurs because when `--async-scheduling` is enabled, the previous iteration's async copy may still be reading from the CPU `is_mm_embed` buffer while the cu |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
