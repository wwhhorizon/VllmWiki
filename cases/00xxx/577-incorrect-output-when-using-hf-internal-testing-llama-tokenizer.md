# vllm-project/vllm#577: Incorrect output when using hf-internal-testing/llama-tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#577](https://github.com/vllm-project/vllm/issues/577) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Incorrect output when using hf-internal-testing/llama-tokenizer

### Issue 正文摘录

When using 'hf-internal-testing/llama-tokenizer': ``` python -m vllm.entrypoints.api_server \ --model openlm-research/open_llama_13b \ --tokenizer hf-internal-testing/llama-tokenizer \ --tensor-parallel-size 1 --port 9990 ``` Output: ``` $> curl http://localhost:9990/generate -d '{ "prompt": "San Francisco is a", "use_beam_search": true, "n": 2, "temperature": 0 }' $> {"text": ["San Francisco is a\u0440\u0430\u043d\n Pur Francisco is a\u0440\u0430\u043d and t forivoion impro\u8d8aion \u044e\u0433\u043e", "San Francisco is aong\u8d8a\u1f7aor togg is a\u0440\u0430\u043d an d t|\\\u8d8a \u044e\u0433\u043eion impro\u7532"]} debug $ curl http://localhost ``` When using original tokenizer, although it is very slow on initialization, the results seemed to be correct: ``` python -m vllm.entrypoints.api_server \ --model openlm-research/open_llama_13b \ --tensor-parallel-size 1 \ --port 9990 ``` Output: ``` $> curl http://localhost :9990/generate -d '{ "prompt": "San Francisco is a", "use_beam_search": true, "n": 2, "temperature": 0 }' ``` $> {"text": ["San Francisco is acity of has a lot to offer. It is a city that is has a", "San Francisco is abeautiful that is known for its diversity, an...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Incorrect output when using hf-internal-testing/llama-tokenizer bug When using 'hf-internal-testing/llama-tokenizer': ``` python -m vllm.entrypoints.api_server \ --model openlm-research/open_llama_13b \ --tokenizer hf-i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: put: ``` $> curl http://localhost:9990/generate -d '{ "prompt": "San Francisco is a", "use_beam_search": true, "n": 2, "temperature": 0 }' $> {"text": ["San Francisco is a\u0440\u0430\u043d\n Pur Francisco is a\u0440\u0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: python -m vllm.entrypoints.api_server \ --model openlm-research/open_llama_13b \ --tokenizer hf-internal-testing/llama-tokenizer \ --tensor-parallel-size 1 --port 9990 ``` Output: ``` $> curl http://localhost:9990/gener...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Incorrect output when using hf-internal-testing/llama-tokenizer bug When using 'hf-internal-testing/llama-tokenizer': ``` python -m vllm.entrypoints.api_server \ --model openlm-research/open_llama_13b \ --tokenizer hf-i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
