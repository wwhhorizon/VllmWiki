# vllm-project/vllm#19495: [Bug]: Latest Mistral Model requires v11 from mistral_common

| 字段 | 值 |
| --- | --- |
| Issue | [#19495](https://github.com/vllm-project/vllm/issues/19495) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Latest Mistral Model requires v11 from mistral_common

### Issue 正文摘录

### Your current environment vLLM latest commit as of time of post: commit `943ffa57032d62c21610e9cebffbdbe6c5c886ca` ### 🐛 Describe the bug Latest mistral reasoning models, ie: `mistralai/Magistral-Small-2506` requires v11 from mistral_common, which needs version `mistral_common>=1.6.0`. Otherwise the following error occurs when loading the model in vLLM: ```python File "/usr/local/lib/python3.12/dist-packages/vllm/transformers_utils/tokenizer.py", line 222, in get_tokenizer tokenizer = MistralTokenizer.from_pretrained(str(tokenizer_name), ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/transformers_utils/tokenizers/mistral.py", line 241, in from_pretrained mistral_tokenizer = PublicMistralTokenizer.from_file(tokenizer_file) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/mistral_common/tokens/tokenizers/mistral.py", line 184, in from_file tokenizer = Tekkenizer.from_file(tokenizer_filename) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/mistral_common/tokens/tokenizers/tekken.py", line 151, in from_file raise ValueError( ValueError: Unkn...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cribe the bug Latest mistral reasoning models, ie: `mistralai/Magistral-Small-2506` requires v11 from mistral_common, which needs version `mistral_common>=1.6.0`. Otherwise the following error occurs when loading the mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Latest Mistral Model requires v11 from mistral_common bug ### Your current environment vLLM latest commit as of time of post: commit `943ffa57032d62c21610e9cebffbdbe6c5c886ca` ### 🐛 Describe the bug Latest mistra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: alai/Magistral-Small-2506` requires v11 from mistral_common, which needs version `mistral_common>=1.6.0`. Otherwise the following error occurs when loading the model in vLLM: ```python File "/usr/local/lib/python3.12/di...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Latest Mistral Model requires v11 from mistral_common bug ### Your current environment vLLM latest commit as of time of post: commit `943ffa57032d62c21610e9cebffbdbe6c5c886ca` ### 🐛 Describe the bug Latest mistra...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
