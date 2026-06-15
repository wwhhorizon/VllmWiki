# vllm-project/vllm#30830: [Bug]: accuracy issue on MoE online fp8 quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#30830](https://github.com/vllm-project/vllm/issues/30830) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: accuracy issue on MoE online fp8 quantization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` python3 examples/offline_inference/basic/generate.py --model Qwen/Qwen3-30B-A3B --enforce-eager --quantization fp8 -tp=2 ``` output: ``` Processed prompts: 100%|██████████████████| 4/4 [00:00<00:00, 5.85it/s, est. speed input: 32.20 toks/s, output: 93.66 toks/s] -------------------------------------------------- Prompt: 'Hello, my name is' Generated text: " Alex and I'm trying to and\nI have, so,\n10" -------------------------------------------------- Prompt: 'The president of the United States is' Generated text: ' the. The United States has. The United States. The United States. The' -------------------------------------------------- Prompt: 'The capital of France is' Generated text: ' the city is the capital of the state. Is the\nThe\n\nthe\n\n' -------------------------------------------------- Prompt: 'The future of AI is' Generated text: '\n\nWhat will be the\n\nThe\n\nThe\n\nThe\n\nThe\n\nThe\n\n' ``` Per debugged, this is caused by `patched_weight_loader`: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/fp8.py#L1350 ### Before submitting a new issue... - [x] Make sure you already...

## 现有链接修复摘要

#30831 [XPU] fix broken fp8 online quantization for XPU platform

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: --------------- Prompt: 'The capital of France is' Generated text: ' the city is the capital of the state. Is the\nThe\n\nthe\n\n' -------------------------------------------------- Prompt: 'The future of AI is' Generat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: accuracy issue on MoE online fp8 quantization bug ### Your current environment ### 🐛 Describe the bug ``` python3 examples/offline_inference/basic/generate.py --model Qwen/Qwen3-30B-A3B --enforce-eager --quantiza...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 350 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ribe the bug ``` python3 examples/offline_inference/basic/generate.py --model Qwen/Qwen3-30B-A3B --enforce-eager --quantization fp8 -tp=2 ``` output: ``` Processed prompts: 100%|██████████████████| 4/4 [00:00<00:00, 5.8...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: accuracy issue on MoE online fp8 quantization bug ### Your current environment ### 🐛 Describe the bug ``` python3 examples/offline_inference/basic/generate.py --model Qwen/Qwen3-30B-A3B --enforce-eager --quantiza...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30831](https://github.com/vllm-project/vllm/pull/30831) | mentioned | 0.6 | [XPU] fix broken fp8 online quantization for XPU platform | ing quantization feature. Since streaming quantization has acc issue (#30830), here we just provide a quick fix for the broken without supporting this feature. We will enable it o… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
