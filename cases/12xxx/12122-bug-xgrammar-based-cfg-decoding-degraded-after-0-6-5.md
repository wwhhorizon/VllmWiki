# vllm-project/vllm#12122: [Bug]: XGrammar-based CFG decoding degraded after 0.6.5

| 字段 | 值 |
| --- | --- |
| Issue | [#12122](https://github.com/vllm-project/vllm/issues/12122) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: XGrammar-based CFG decoding degraded after 0.6.5

### Issue 正文摘录

### Your current environment Tested in 3 environments with 8xH100: * `public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:61c1d499f07d3a50e3721a38f3f54a721f3eaf65` * CI version before v0.6.5 that contained XGrammars (v0.6.4.post2 did not contained XGrammars). * This image no longer exists. * `v0.6.5` * `v0.6.6.post1` ### Model Input Dumps ```python extra_body = { "guided_grammar": grammar, "guided_decoding_backend": "xgrammar", # optional } chat_completion = client.chat.completions.create( model=model, messages=messages, stream=True, temperature=0, max_tokens=1024, timeout=timeout, extra_body=extra_body, stream_options={"include_usage": True}, ) ``` ### 🐛 Describe the bug XGrammars guided decoding both for Time to first token (TTFT) and overall response time. I've tested 2 versions with a Llama3-70b: * A CI version before v0.6.5 that contained XGrammars (v0.6.4.post2 did not contained XGrammars). This is the exact image I was using: `public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:61c1d499f07d3a50e3721a38f3f54a721f3eaf65` * TTFT P50: ~0.6s * `v0.6.5` and `v0.6.6.post1`: * TTFT P50: ~4s Related [issue affecting Outlines](https://github.com/vllm-project/vllm/issues/12005) ### Before submitting a ne...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t Tested in 3 environments with 8xH100: * `public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:61c1d499f07d3a50e3721a38f3f54a721f3eaf65` * CI version before v0.6.5 that contained XGrammars (v0.6.4.post2 did not contained XGrammar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tput;stale ### Your current environment Tested in 3 environments with 8xH100: * `public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:61c1d499f07d3a50e3721a38f3f54a721f3eaf65` * CI version before v0.6.5 that contained XGrammars (v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mars). * This image no longer exists. * `v0.6.5` * `v0.6.6.post1` ### Model Input Dumps ```python extra_body = { "guided_grammar": grammar, "guided_decoding_backend": "xgrammar", # optional } chat_completion = client.ch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ython extra_body = { "guided_grammar": grammar, "guided_decoding_backend": "xgrammar", # optional } chat_completion = client.chat.completions.create( model=model, messages=messages, stream=True, temperature=0, max_token...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : XGrammar-based CFG decoding degraded after 0.6.5 bug;structured-output;stale ### Your current environment Tested in 3 environments with 8xH100: * `public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:61c1d499f07d3a50e3721a38f3f5...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
