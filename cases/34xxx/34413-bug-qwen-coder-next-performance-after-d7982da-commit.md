# vllm-project/vllm#34413: [Bug]: Qwen coder next performance after d7982da commit.

| 字段 | 值 |
| --- | --- |
| Issue | [#34413](https://github.com/vllm-project/vllm/issues/34413) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen coder next performance after d7982da commit.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug All qwen3 models i have now are broken after the following commit. https://github.com/vllm-project/vllm/commit/d7982daff5334b9465b29fa943a1954c064ab226 The model is loading but the speed is about 1 tps against 60tps on previous commit on my two sparks. this is the only noticable change i've found in log ```text Using default MoE config. Performance might be sub-optimal! Config file not found at /usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/configs/E=512,N=256,device_name=NVIDIA_GB10,dtype=fp8_w8a8,block_shape=[128,128].json ``` I was trying to use benchmark_moe for the model and I've got only 3-4 batches for 8+ hours done. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#34507 [Bugfix] Fix fused MoE int32 overflow in stride*offset without perf regression

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen coder next performance after d7982da commit. bug ### Your current environment ### 🐛 Describe the bug All qwen3 models i have now are broken after the following commit. https://github.com/vllm-project/vllm/co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: A_GB10,dtype=fp8_w8a8,block_shape=[128,128].json ``` I was trying to use benchmark_moe for the model and I've got only 3-4 batches for 8+ hours done. ### Before submitting a new issue... - [x] Make sure you already sear...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: el_executor/layers/fused_moe/configs/E=512,N=256,device_name=NVIDIA_GB10,dtype=fp8_w8a8,block_shape=[128,128].json ``` I was trying to use benchmark_moe for the model and I've got only 3-4 batches for 8+ hours done. ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34507](https://github.com/vllm-project/vllm/pull/34507) | closes_keyword | 0.95 | [Bugfix] Fix fused MoE int32 overflow in stride*offset without perf regression | Fixes #34413 PR #34279 annotated all stride parameters as tl.int64 to fix an int32 overflow crash, but this caused ~60x perf regression on small GPUs (e.g. NVIDIA GB10) due to reg |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
