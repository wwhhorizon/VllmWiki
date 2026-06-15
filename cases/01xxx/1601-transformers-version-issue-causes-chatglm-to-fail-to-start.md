# vllm-project/vllm#1601: Transformers version issue causes chatglm  to fail to start

| 字段 | 值 |
| --- | --- |
| Issue | [#1601](https://github.com/vllm-project/vllm/issues/1601) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Transformers version issue causes chatglm  to fail to start

### Issue 正文摘录

when the transformers>=4.33.2: File "/usr/local/lib/python3.8/dist-packages/transformers/models/auto/tokenization_auto.py", line 738, in from_pretrained return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs) File "/usr/local/lib/python3.8/dist-packages/transformers/tokenization_utils_base.py", line 2017, in from_pretrained return cls._from_pretrained( File "/usr/local/lib/python3.8/dist-packages/transformers/tokenization_utils_base.py", line 2249, in _from_pretrained tokenizer = cls(*init_inputs, **init_kwargs) File "/root/.cache/huggingface/modules/transformers_modules/chatglm2-tarotdice-v2/tokenization_chatglm.py", line 69, in __init__ super().__init__(padding_side=padding_side, **kwargs) File "/usr/local/lib/python3.8/dist-packages/transformers/tokenization_utils.py", line 367, in __init__ self._add_tokens( File "/usr/local/lib/python3.8/dist-packages/transformers/tokenization_utils.py", line 467, in _add_tokens current_vocab = self.get_vocab().copy() File "/root/.cache/huggingface/modules/transformers_modules/chatglm2-tarotdice-v2/tokenization_chatglm.py", line 108, in get_vocab vocab = {self._convert_id_to_token(i): i for i in range(self.voca...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rs>=4.33.2: File "/usr/local/lib/python3.8/dist-packages/transformers/models/auto/tokenization_auto.py", line 738, in from_pretrained return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Transformers version issue causes chatglm to fail to start when the transformers>=4.33.2: File "/usr/local/lib/python3.8/dist-packages/transformers/models/auto/tokenization_auto.py", line 738, in from_pretrained return...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
