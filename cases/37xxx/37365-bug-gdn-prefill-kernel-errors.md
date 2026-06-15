# vllm-project/vllm#37365: [Bug]: gdn prefill kernel errors

| 字段 | 值 |
| --- | --- |
| Issue | [#37365](https://github.com/vllm-project/vllm/issues/37365) |
| 状态 | open |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gdn prefill kernel errors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug run ``` CUDA_VISIBLE_DEVICES=2,3 python -m vllm.entrypoints.openai.api_server --tensor-parallel-size 2 --model /data/models/Qwen3.5-27B --served-model-name Qwen3.5-27B --api-key xxx --reasoning-parser qwen3 --enable-prefix-caching --tool-call-parser qwen3_coder --enable-auto-tool-choice --gpu-memory-utilization 0.9 --max_model_len 262144 --port 8060 ``` flashinfer report some gdn prefill kernel errors, can not inference successfully ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#37507 [Bugfix] Fall back to Triton/FLA when system CUDA toolkit < 12.6 for GDN prefill kernel

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;sampling;triton build_e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ce --gpu-memory-utilization 0.9 --max_model_len 262144 --port 8060 ``` flashinfer report some gdn prefill kernel errors, can not inference successfully ### Before submitting a new issue... - [x] Make sure you already se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rs bug ### Your current environment ### 🐛 Describe the bug run ``` CUDA_VISIBLE_DEVICES=2,3 python -m vllm.entrypoints.openai.api_server --tensor-parallel-size 2 --model /data/models/Qwen3.5-27B --served-model-name Qwen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: python -m vllm.entrypoints.openai.api_server --tensor-parallel-size 2 --model /data/models/Qwen3.5-27B --served-model-name Qwen3.5-27B --api-key xxx --reasoning-parser qwen3 --enable-prefix-caching --tool-call-parser qw...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: gdn prefill kernel errors bug ### Your current environment ### 🐛 Describe the bug run ``` CUDA_VISIBLE_DEVICES=2,3 python -m vllm.entrypoints.openai.api_server --tensor-parallel-size 2 --model /data/models/Qwen3....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37507](https://github.com/vllm-project/vllm/pull/37507) | closes_keyword | 0.95 | [Bugfix] Fall back to Triton/FLA when system CUDA toolkit < 12.6 for GDN prefill kernel | Fix #37365 #35725 . When running Qwen3.5 on SM90 GPUs (H100/H20/H800) with a system CUDA toolkit older than 12.6, vLLM crashes at first inference with JIT compilation errors: ``` |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
