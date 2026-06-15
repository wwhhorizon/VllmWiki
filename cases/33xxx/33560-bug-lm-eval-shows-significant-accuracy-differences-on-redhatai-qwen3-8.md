# vllm-project/vllm#33560: [Bug]: lm-eval shows significant accuracy differences on RedHatAI/Qwen3-8B-NVFP4 model (Turing vs. Ampere)

| 字段 | 值 |
| --- | --- |
| Issue | [#33560](https://github.com/vllm-project/vllm/issues/33560) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: lm-eval shows significant accuracy differences on RedHatAI/Qwen3-8B-NVFP4 model (Turing vs. Ampere)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run follow lm-eval command on both Turing and Ampere: ```bash lm_eval --model vllm --model_args pretrained=RedHatAI/Qwen3-8B-NVFP4,tensor_parallel_size=2,gpu_memory_utilization=0.8,dtype=auto,attention_backend=FLASHINFER --trust_remote_code --tasks lambada_openai --batch_size auto --seed 42 ``` Completely different results were obtained, and the issue is reproducible with the provided files. The acc is 1 or 0.9998 (2x RTX2080Ti) and perplexity is NaN on Turing. And the acc is 0.6546 and perplexity is 4.5249 on Ampere. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#37135 [Bugfix] Fix FP16 overflow in NVFP4 Marlin kernel epilogue and forward input_global_scale on SM75

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ug]: lm-eval shows significant accuracy differences on RedHatAI/Qwen3-8B-NVFP4 model (Turing vs. Ampere) bug ### Your current environment ### 🐛 Describe the bug Run follow lm-eval command on both Turing and Ampere: ```b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ficant accuracy differences on RedHatAI/Qwen3-8B-NVFP4 model (Turing vs. Ampere) bug ### Your current environment ### 🐛 Describe the bug Run follow lm-eval command on both Turing and Ampere: ```bash lm_eval --model vllm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 4,tensor_parallel_size=2,gpu_memory_utilization=0.8,dtype=auto,attention_backend=FLASHINFER --trust_remote_code --tasks lambada_openai --batch_size auto --seed 42 ``` Completely different results were obtained, and the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ``` Completely different results were obtained, and the issue is reproducible with the provided files. The acc is 1 or 0.9998 (2x RTX2080Ti) and perplexity is NaN on Turing. And the acc is 0.6546 and perplexity is 4.524...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: lm-eval shows significant accuracy differences on RedHatAI/Qwen3-8B-NVFP4 model (Turing vs. Ampere) bug ### Your current environment ### 🐛 Describe the bug Run follow lm-eval command on both Turing and Ampere: ``...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37135](https://github.com/vllm-project/vllm/pull/37135) | closes_keyword | 0.95 | [Bugfix] Fix FP16 overflow in NVFP4 Marlin kernel epilogue and forward input_global_scale on SM75 | closes #33560 and #33461 **Relationship to PR #33972:** PR #33972 fixes the missing input scaling at the Python dispatch layer but does not touch the kernel. This PR includes the |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
