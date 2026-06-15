# vllm-project/vllm#17614: [Bug]: Qwen 3 - Invalid Tool Call Response When Using Streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#17614](https://github.com/vllm-project/vllm/issues/17614) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen 3 - Invalid Tool Call Response When Using Streaming

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I try to call a simple function with a prompt like "what is issue 50306 about?", the API returns a function call with the last two numbers cut off (returns **503** instead of the whole number **50306**). However, if I turn streaming off, then the response contains the whole correct number **50306**. +What's interesting is that in the reasoning chain the number is correct even in the streaming version, so the model knows how to fill the function but in the final response the argument is incorrect... I'm using docker image `vllm/vllm-openai:v0.8.5` and I'm serving the model with this command: `--host 0.0.0.0 --port 8000 --served-model-name qwen-14b --model Qwen/Qwen3-14B-FP8 --gpu-memory-utilization 0.90 --max-model-len 16384 --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser hermes --max-num-seqs 2 --enable-prefix-caching --max-seq-len-to-capture 16384 --enable-reasoning --reasoning-parser deepseek_r1` I've tried the same request with the 30B MoE version and the result is the same. +I've also tried the same request with LM Studio (but with the MLX version) and it works correctly when using streaming. **Requ...

## 现有链接修复摘要

#20824 [Bugfix] Fix the bug in Hermes streaming parsing

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Qwen 3 - Invalid Tool Call Response When Using Streaming bug;stale ### Your current environment ### 🐛 Describe the bug When I try to call a simple function with a prompt like "what is issue 50306 about?", the API...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: that in the reasoning chain the number is correct even in the streaming version, so the model knows how to fill the function but in the final response the argument is incorrect... I'm using docker image `vllm/vllm-opena...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: 0.0.0.0 --port 8000 --served-model-name qwen-14b --model Qwen/Qwen3-14B-FP8 --gpu-memory-utilization 0.90 --max-model-len 16384 --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser hermes --max-num-seqs...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 3Z INFO 05-03 06:52:26 [__init__.py:239] Automatically detected platform cuda. 2025-05-03T13:52:29.527288566Z INFO 05-03 06:52:29 [api_server.py:1043] vLLM API server version 0.8.5 2025-05-03T13:52:29.527394415Z INFO 05...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen 3 - Invalid Tool Call Response When Using Streaming bug;stale ### Your current environment ### 🐛 Describe the bug When I try to call a simple function with a prompt like "what is issue 50306 about?", the API...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20824](https://github.com/vllm-project/vllm/pull/20824) | closes_keyword | 0.95 | [Bugfix] Fix the bug in Hermes streaming parsing | Fix the bug in Hermes streaming parsing Similar issues：[#17614](https://github.com/vllm-project/vllm/issues/17614) <details> <summary>The output of <code>python collect_env.py</co |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
