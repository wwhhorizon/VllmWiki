# vllm-project/vllm#2825: GBNF throws a tensor error

| 字段 | 值 |
| --- | --- |
| Issue | [#2825](https://github.com/vllm-project/vllm/issues/2825) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GBNF throws a tensor error

### Issue 正文摘录

No matter what I do and which GBNF format I use I can't get it work. I have even tried the included json.gbnf and asked the model to provide a sample json file, nothing happens but in the console the following errors are displayed: ``` Traceback (most recent call last): File "/home/xxx/apps/text-generation-webui/modules/callbacks.py", line 61, in gentask ret = self.mfunc(callback=_callback, *args, **self.kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/xxx/apps/text-generation-webui/modules/text_generation.py", line 390, in generate_with_callback shared.model.generate(**kwargs) File "/home/xxx/apps/text-generation-webui/installer_files/env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/home/xxx/apps/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/generation/utils.py", line 1525, in generate return self.sample( ^^^^^^^^^^^^ File "/home/xxx/apps/text-generation-webui/installer_files/env/lib/python3.11/site-packages/transformers/generation/utils.py", line 2635, in sample next_token_scores = logits_processor(input_ids, next_toke...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: GBNF throws a tensor error No matter what I do and which GBNF format I use I can't get it work. I have even tried the included json.gbnf and asked the model to provide a sample json file, nothing happens but in the cons...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed.model.generate(**kwargs) File "/home/xxx/apps/text-generation-webui/installer_files/env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: d tensor [1, 32256] at index ``` I am using DeepSeeker model for this test, loading it as a transformer model.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
