# vllm-project/vllm#80: Bug in LLaMA fast tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#80](https://github.com/vllm-project/vllm/issues/80) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Bug in LLaMA fast tokenizer

### Issue 正文摘录

In my environment, using the LLaMA fast tokenizer raises an error about protobuf: ``` File "/opt/conda/envs/dev/lib/python3.9/site-packages/transformers/convert_slow_tokenizer.py", line 445, in __init__ from .utils import sentencepiece_model_pb2 as model_pb2 File "/opt/conda/envs/dev/lib/python3.9/site-packages/transformers/utils/sentencepiece_model_pb2.py", line 91, in _descriptor.EnumValueDescriptor( File "/opt/conda/envs/dev/lib/python3.9/site-packages/google/protobuf/descriptor.py", line 796, in __new__ _message.Message._CheckCalledFromGeneratedFile() TypeError: Descriptors cannot not be created directly. If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0. If you cannot immediately regenerate your protos, some other possible workarounds are: 1. Downgrade the protobuf package to 3.20.x or lower. 2. Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python (but this will use pure-Python parsing and will be much slower). ``` While downgrading the protobuf version removed the error, it slowed down the initialization time by ~8x. * Initialization with fast tokenizer & protobuf==3.20.3 ``` real 4m18.476s user 3m52.706s sys...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ormers/convert_slow_tokenizer.py", line 445, in __init__ from .utils import sentencepiece_model_pb2 as model_pb2 File "/opt/conda/envs/dev/lib/python3.9/site-packages/transformers/utils/sentencepiece_model_pb2.py", line...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Bug in LLaMA fast tokenizer bug In my environment, using the LLaMA fast tokenizer raises an error about protobuf: ``` File "/opt/conda/envs/dev/lib/python3.9/site-packages/transformers/convert_slow_tokenizer.py", line 4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
