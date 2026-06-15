# vllm-project/vllm#34954: [Bug]: Triton Error [CUDA]: out of memory when received query

| 字段 | 值 |
| --- | --- |
| Issue | [#34954](https://github.com/vllm-project/vllm/issues/34954) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton Error [CUDA]: out of memory when received query

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug My server has 8 H100 GPUs. And I lauched vllm server with 4 GPUs for qwen3-next-fp8 model by the script below ``` export CUDA_VISIBLE_DEVICES=0,3,6,7 vllm serve models/qwen3-next-fp8 \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.9 \ --api-key kmh \ --max-model-len 8192 \ --max-num-batched-tokens 8192 \ --port $2 \ --enable-expert-parallel \ --quantization fp8 ``` The server started successfully. When I request for response, it gives me error messages below even though my request has less than 100 tokens. Can anyone help? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#36384 Fix/fla triton autotune oom 34954

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits cuda;fp8;moe;operator;quant...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: er has 8 H100 GPUs. And I lauched vllm server with 4 GPUs for qwen3-next-fp8 model by the script below ``` export CUDA_VISIBLE_DEVICES=0,3,6,7 vllm serve models/qwen3-next-fp8 \ --tensor-parallel-size 4 \ --gpu-memory-u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Triton Error [CUDA]: out of memory when received query bug ### Your current environment ### 🐛 Describe the bug My server has 8 H100 GPUs. And I lauched vllm server with 4 GPUs for qwen3-next-fp8 model by the scri...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 8192 \ --max-num-batched-tokens 8192 \ --port $2 \ --enable-expert-parallel \ --quantization fp8 ``` The server started successfully. When I request for response, it gives me error messages below even though my request...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ug My server has 8 H100 GPUs. And I lauched vllm server with 4 GPUs for qwen3-next-fp8 model by the script below ``` export CUDA_VISIBLE_DEVICES=0,3,6,7 vllm serve models/qwen3-next-fp8 \ --tensor-parallel-size 4 \ --gp...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36384](https://github.com/vllm-project/vllm/pull/36384) | closes_keyword | 0.95 | Fix/fla triton autotune oom 34954 | Fixes #34954 Qwen3-Next / Qwen3.5 models use Flash Linear Attention (FLA) with Triton kernels that are decorated with @triton.autotune. When these kernels are invoked for the firs |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
