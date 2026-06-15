# vllm-project/vllm#13847: [Doc]: guided grammar example lack parameter guided_decoding_backend

| 字段 | 值 |
| --- | --- |
| Issue | [#13847](https://github.com/vllm-project/vllm/issues/13847) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: guided grammar example lack parameter guided_decoding_backend

### Issue 正文摘录

### 📚 The doc issue vllm-0.7.3, outlines 0.2.1 Hey! Thank you for amazing vLLM. I found one issue and several strange things related to example of structured outputs docs. At example in docs and on Github we can see following: ``` -- Guided decoding by Grammar ... extra_body={"guided_grammar": simplified_sql_grammar}, ) ``` №1 >>> If we are not specifying guided_decoding_backend then there is no guidance. Let's run and see it. But also mind the throughput in log, we'll get back to it. > INFO 02-25 23:26:51 logger.py:39] Received request chatcmpl-3c0bff06209b42ec9f5be974471be7d9: prompt: ' system\nВы — помощник, способный генерировать PL/pgSQL-функции и проверять их синтаксис. \n user\nСгенерируй функцию на PL/pgSQL, которая возвращает сумму чисел от 1 до 100. \n assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=5120, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, gu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: guided_grammar": simplified_sql_grammar}, ) ``` №1 >>> If we are not specifying guided_decoding_backend then there is no guidance. Let's run and see it. But also mind the throughput in log, we'll get back to it. > INFO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ded grammar example lack parameter guided_decoding_backend documentation;stale ### 📚 The doc issue vllm-0.7.3, outlines 0.2.1 Hey! Thank you for amazing vLLM. I found one issue and several strange things related to exam...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ckend then there is no guidance. Let's run and see it. But also mind the throughput in log, we'll get back to it. > INFO 02-25 23:26:51 logger.py:39] Received request chatcmpl-3c0bff06209b42ec9f5be974471be7d9: prompt: '...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Doc]: guided grammar example lack parameter guided_decoding_backend documentation;stale ### 📚 The doc issue vllm-0.7.3, outlines 0.2.1 Hey! Thank you for amazing vLLM. I found one issue and several strange things relat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /home/abalagaev/Programs/vllm_env/lib/python3.12/site-packages/outlines/fsm/guide.py:110: **UserWarning: Outlines' public *community-contributed* CFG structured generation is experimental. Please review https://dottxt-a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
