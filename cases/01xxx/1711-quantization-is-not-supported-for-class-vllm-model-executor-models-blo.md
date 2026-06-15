# vllm-project/vllm#1711: Quantization is not supported for <class 'vllm.model_executor.models.bloom.BloomForCausalLM'>

| 字段 | 值 |
| --- | --- |
| Issue | [#1711](https://github.com/vllm-project/vllm/issues/1711) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Quantization is not supported for <class 'vllm.model_executor.models.bloom.BloomForCausalLM'>

### Issue 正文摘录

I'm trying to load my bloomz-3b-awq via vLLM but fail. Anyone know how to fix it? ``` /usr/local/lib/python3.10/dist-packages/pydantic/main.cpython-310-x86_64-linux-gnu.so in pydantic.main.BaseModel.__init__() ValidationError: 1 validation error for VLLM __root__ Quantization is not supported for . (type=value_error) ```

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Quantization is not supported for <class 'vllm.model_executor.models.bloom.BloomForCausalLM'> I'm trying to load my bloomz-3b-awq via vLLM but fail. Anyone know how to fix it? ``` /usr/local/lib/python3.10/dist-packages/
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Quantization is not supported for <class 'vllm.model_executor.models.bloom.BloomForCausalLM'> I'm trying to load my bloomz-3b-awq via vLLM but fail. Anyone know how to fix it? ``` /usr/local/lib/python3.10/dist-packages...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Quantization is not supported for <class 'vllm.model_executor.models.bloom.BloomForCausalLM'> I'm trying to load my bloomz-3b-awq via vLLM but fail. Anyone know how to fix it? ``` /usr/local/lib/python3.10/dist-packages...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
