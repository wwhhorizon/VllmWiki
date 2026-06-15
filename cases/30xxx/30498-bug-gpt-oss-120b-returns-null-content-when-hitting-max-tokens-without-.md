# vllm-project/vllm#30498: [Bug]: GPT-OSS-120B returns null content when hitting max_tokens without --enforce-eager

| 字段 | 值 |
| --- | --- |
| Issue | [#30498](https://github.com/vllm-project/vllm/issues/30498) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic;slowdown |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS-120B returns null content when hitting max_tokens without --enforce-eager

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running GPT-OSS-120B without the --enforce-eager flag, the model returns content: null when responses hit max_tokens, despite successfully generating tokens server-side and returning HTTP 200 OK. **Key characteristics:** - Non-deterministic initially: First 1-2 requests may succeed, then subsequent requests fail - Becomes deterministic: After warm-up, fails consistently (100% failure rate) - Silent failure: No errors thrown, just null content with 200 OK status - Server-side generation succeeds: Logs show ~120-150 tokens/s throughput and 200 OK - Client-side receives nothing: content: null, reasoning_content: "" **Minimal reproduction code:** ```python import requests # Run this 3-5 times - first may work, then consistently fails response = requests.post( 'http://localhost:8000/v1/chat/completions', json={ 'model': '/models/gpt-oss-120b', 'messages': [ {'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': '''Analyze this complex distributed system architecture with microservices for API gateway, authentication, user management, content processing, search, analytics, notifications, caching...

## 现有链接修复摘要

#30650 [Bugfix] CustomAR + TritonAttn[AMPERE] + FULL_CG - gpt-oss

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t: null, reasoning_content: "" **Minimal reproduction code:** ```python import requests # Run this 3-5 times - first may work, then consistently fails response = requests.post( 'http://localhost:8000/v1/chat/completions...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: returns null content when hitting max_tokens without --enforce-eager bug;stale ### Your current environment ### 🐛 Describe the bug When running GPT-OSS-120B without the --enforce-eager flag, the model returns content: n...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: kens server-side and returning HTTP 200 OK. **Key characteristics:** - Non-deterministic initially: First 1-2 requests may succeed, then subsequent requests fail - Becomes deterministic: After warm-up, fails consistentl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: {'role': 'user', 'content': '''Analyze this complex distributed system architecture with microservices for API gateway, authentication, user management, content processing, search, analytics, notifications, caching, mes...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GPT-OSS-120B returns null content when hitting max_tokens without --enforce-eager bug;stale ### Your current environment ### 🐛 Describe the bug When running GPT-OSS-120B without the --enforce-eager flag, the mode...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30650](https://github.com/vllm-project/vllm/pull/30650) | mentioned | 0.6 | [Bugfix] CustomAR + TritonAttn[AMPERE] + FULL_CG - gpt-oss | d as expected. Before this change, the the python requests loop from #30498 always hung by the 2nd or 3rd request. After this change, it continues to work for multiple subsequent… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
