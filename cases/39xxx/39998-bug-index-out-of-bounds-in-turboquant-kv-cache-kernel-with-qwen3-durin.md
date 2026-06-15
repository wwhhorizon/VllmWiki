# vllm-project/vllm#39998: [Bug]: Index out of bounds in TurboQuant KV Cache kernel with Qwen3 during high-concurrency 32k context benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#39998](https://github.com/vllm-project/vllm/issues/39998) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;kernel |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Index out of bounds in TurboQuant KV Cache kernel with Qwen3 during high-concurrency 32k context benchmark

### Issue 正文摘录

### Your current environment code: vllm main 2026-04-16 gpu: 4090 cuda: 12.6 command: ``` VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \ vllm serve /model \ --port 8000 \ --tensor-parallel-size 1 \ --reasoning-parser qwen3 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --language-model-only \ --gpu-memory-utilization 0.7 \ --kv-cache-dtype=turboquant_4bit_nc \ --max-model-len 73728 \ --host 0.0.0.0 --port 8000 ``` ### 🐛 Describe the bug When running a performance benchmark on Qwen3-0.6B using TurboQuant 4-bit KV Cache (--kv-cache-dtype=turboquant_4bit_nc), the vLLM engine crashes during the prefill/decode phase. The crash occurs when handling 8 concurrent requests with a 32k input context length on an NVIDIA RTX 4090. The error trace points to an assertion failure in a compiled Torch Inductor kernel, indicating an out-of-bounds memory access. Error Logs ``` /root/.cache/vllm/torch_compile_cache/torch_aot_compile/.../inductor_cache/...py:53: unknown: block: [129,0,0], thread: [224,0,0] Assertion `index out of bounds: 0 <= tmp16 < 40960` failed. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the b...

## 现有链接修复摘要

#40073 Fix for Index out of bounds in TurboQuant KV Cache kernel with Qwen3 during high-concurrency 32k context benchmark | #40074 [Bugfix] Fix TurboQuant KV cache index-out-of-bounds in Triton decode kernel

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: k bug ### Your current environment code: vllm main 2026-04-16 gpu: 4090 cuda: 12.6 command: ``` VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \ vllm serve /model \ --port 8000 \ --tensor-parallel-size 1 \ --reasoning-parser qwen3 \ -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: --kv-cache-dtype=turboquant_4bit_nc), the vLLM engine crashes during the prefill/decode phase. The crash occurs when handling 8 concurrent requests with a 32k input context length on an NVIDIA RTX 4090. The error trace...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: an NVIDIA RTX 4090. The error trace points to an assertion failure in a compiled Torch Inductor kernel, indicating an out-of-bounds memory access. Error Logs ``` /root/.cache/vllm/torch_compile_cache/torch_aot_compile/....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Index out of bounds in TurboQuant KV Cache kernel with Qwen3 during high-concurrency 32k context benchmark bug ### Your current environment code: vllm main 2026-04-16 gpu: 4090 cuda: 12.6 command: ``` VLLM_ALLOW_...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: Index out of bounds in TurboQuant KV Cache kernel with Qwen3 during high-concurrency 32k context benchmark bug ### Your current environment code: vllm main 2026-04-16 gpu: 4090 cuda: 12.6 command: ``` VLLM_ALLOW_...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40073](https://github.com/vllm-project/vllm/pull/40073) | closes_keyword | 0.95 | Fix for Index out of bounds in TurboQuant KV Cache kernel with Qwen3 during high-concurrency 32k context benchmark | fixes issue [#39998](https://github.com/vllm-project/vllm/issues/39998) --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [x] |
| [#40074](https://github.com/vllm-project/vllm/pull/40074) | closes_keyword | 0.95 | [Bugfix] Fix TurboQuant KV cache index-out-of-bounds in Triton decode kernel | Fixes issue #39998 https://github.com/vllm-project/vllm/issues/39998 ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Descri |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
