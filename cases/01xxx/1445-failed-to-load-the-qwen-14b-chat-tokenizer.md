# vllm-project/vllm#1445: Failed to load the Qwen-14b-chat tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#1445](https://github.com/vllm-project/vllm/issues/1445) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Failed to load the Qwen-14b-chat tokenizer

### Issue 正文摘录

from vllm import LLM llm = LLM(model='/root/.cache/huggingface/hub/models--Qwen--Qwen-14B-Chat/snapshots/63faec65d9eb7d31b6a177e0680563eb4043a1a1') # Name or path of your model output = llm.generate("Hello, my name is") print(output) The error message is as follows： Exception has occurred: RuntimeError Failed to load the tokenizer. If the tokenizer is a custom tokenizer not yet available in the HuggingFace transformers library, consider setting `trust_remote_code=True` in LLM or using the `--trust-remote-code` flag in the CLI. ValueError: Tokenizer class QWenTokenizer does not exist or is not currently imported. The above exception was the direct cause of the following exception: File "/home/czp/vllm-main/vllm/test.py", line 3, in llm = LLM(model='/root/.cache/huggingface/hub/models--Qwen--Qwen-14B-Chat/snapshots/63faec65d9eb7d31b6a177e0680563eb4043a1a1') # Name or path of your model RuntimeError: Failed to load the tokenizer. If the tokenizer is a custom tokenizer not yet available in the HuggingFace transformers library, consider setting `trust_remote_code=True` in LLM or using the `--trust-remote-code` flag in the CLI.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Failed to load the Qwen-14b-chat tokenizer from vllm import LLM llm = LLM(model='/root/.cache/huggingface/hub/models--Qwen--Qwen-14B-Chat/snapshots/63faec65d9eb7d31b6a177e0680563eb4043a1a1') # Name or path of your model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Failed to load the Qwen-14b-chat tokenizer from vllm import LLM llm = LLM(model='/root/.cache/huggingface/hub/models--Qwen--Qwen-14B-Chat/snapshots/63faec65d9eb7d31b6a177e0680563eb4043a1a1') # Name or path of your model...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rect cause of the following exception: File "/home/czp/vllm-main/vllm/test.py", line 3, in llm = LLM(model='/root/.cache/huggingface/hub/models--Qwen--Qwen-14B-Chat/snapshots/63faec65d9eb7d31b6a177e0680563eb4043a1a1') #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
