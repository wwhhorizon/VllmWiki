# vllm-project/vllm#43326: [Bug]: Gemma4 26B-A4B fails because GELU_TANH is unsupported in CPU fused MoE path

| 字段 | 值 |
| --- | --- |
| Issue | [#43326](https://github.com/vllm-project/vllm/issues/43326) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;moe;operator;sampling |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4 26B-A4B fails because GELU_TANH is unsupported in CPU fused MoE path

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `google/gemma-4-26B-A4B-it` fails on the vLLM CPU backend because the CPU fused MoE path does not support `MoEActivation.GELU_TANH`. The model loads successfully, but engine initialization fails during warmup in the CPU fused MoE path with: ```text AssertionError: MoEActivation.GELU_TANH is not supported. ``` Minimal reproduction: ```bash VLLM_TARGET_DEVICE=cpu \ vllm bench throughput \ --model google/gemma-4-26B-A4B-it \ --dataset-name sonnet \ --dataset-path vllm_source/benchmarks/sonnet.txt \ --num-prompts 1 \ --max-model-len 2048 \ --override-generation-config '{"temperature": "0.0", "top_p": "1.0"}' ``` Expected behavior: ```text vLLM CPU engine should initialize and run the benchmark for google/gemma-4-26B-A4B-it. ``` Actual behavior: ```text Engine initialization fails because GELU_TANH is not supported in the CPU fused MoE activation mapping. ``` Relevant traceback: Relevant traceback: ```text torch._dynamo.exc.Unsupported: Observed exception Developer debug context: raised exception AssertionError([ConstantVariable(str: 'MoEActivation.GELU_TANH is not supported.')]) from user code: File ".../vllm/model_executor/models/ge...

## 现有链接修复摘要

#43344 [Bugfix] Add GELU_TANH activation support to CPU fused MoE

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: Gemma4 26B-A4B fails because GELU_TANH is unsupported in CPU fused MoE path bug ### Your current environment ### 🐛 Describe the bug `google/gemma-4-26B-A4B-it` fails on the vLLM CPU backend because the CPU fused...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n answer lots of frequently asked questions. correctness activation_norm;ci_build;hardware_porting;model_support;moe;sampling_logits;speculative_decoding activation;cuda;moe;operator;sampling build_error;crash;nan_inf;s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma4 26B-A4B fails because GELU_TANH is unsupported in CPU fused MoE path bug ### Your current environment ### 🐛 Describe the bug `google/gemma-4-26B-A4B-it` fails on the vLLM CPU backend because the CPU fused...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ``` Minimal reproduction: ```bash VLLM_TARGET_DEVICE=cpu \ vllm bench throughput \ --model google/gemma-4-26B-A4B-it \ --dataset-name sonnet \ --dataset-path vllm_source/benchmarks/sonnet.txt \ --num-prompts 1 \ --max-m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: self.runner.forward( File ".../vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py", line 354, in apply_monolithic return self.cpu_fused_moe( File ".../vllm/model_executor/layers/fused_moe/cpu_fused_moe...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43344](https://github.com/vllm-project/vllm/pull/43344) | closes_keyword | 0.95 | [Bugfix] Add GELU_TANH activation support to CPU fused MoE | Fixes #43326 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
