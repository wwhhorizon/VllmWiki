# vllm-project/vllm#348: 'MPTConfig' object has no attribute 'num_attention_heads'

| 字段 | 值 |
| --- | --- |
| Issue | [#348](https://github.com/vllm-project/vllm/issues/348) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 'MPTConfig' object has no attribute 'num_attention_heads'

### Issue 正文摘录

Hi there, Thanks a lot for a great project. It really helps. I have come across an issue while trying "mosaicml/mpt-7b", which is advertised to be supported at: # https://vllm.readthedocs.io/en/latest/models/supported_models.html ``` from vllm import LLM, SamplingParams # https://vllm.readthedocs.io/en/latest/models/supported_models.html llm = LLM(model="mosaicml/mpt-7b") ``` ``` Downloading (…)lve/main/config.json: 100% 1.23k/1.23k [00:00 in [/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py](https://localhost:8080/#) in __init__(self, model, tensor_parallel_size, dtype, seed, **kwargs) 53 **kwargs, 54 ) ---> 55 self.llm_engine = LLMEngine.from_engine_args(engine_args) 56 self.request_counter = Counter() 57 4 frames [/usr/local/lib/python3.10/dist-packages/transformers/configuration_utils.py](https://localhost:8080/#) in __getattribute__(self, key) 259 if key != "attribute_map" and key in super().__getattribute__("attribute_map"): 260 key = super().__getattribute__("attribute_map")[key] --> 261 return super().__getattribute__(key) 262 263 def __init__(self, **kwargs): AttributeError: 'MPTConfig' object has no attribute 'num_attention_heads' ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 'MPTConfig' object has no attribute 'num_attention_heads' Hi there, Thanks a lot for a great project. It really helps. I have come across an issue while trying "mosaicml/mpt-7b", which is advertised to be supported at:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: llm.readthedocs.io/en/latest/models/supported_models.html ``` from vllm import LLM, SamplingParams # https://vllm.readthedocs.io/en/latest/models/supported_models.html llm = LLM(model="mosaicml/mpt-7b") ``` ``` Download...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: https://localhost:8080/#) in __init__(self, model, tensor_parallel_size, dtype, seed, **kwargs) 53 **kwargs, 54 ) ---> 55 self.llm_engine = LLMEngine.from_engine_args(engine_args) 56 self.request_counter = Counter() 57...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lm_engine = LLMEngine.from_engine_args(engine_args) 56 self.request_counter = Counter() 57 4 frames [/usr/local/lib/python3.10/dist-packages/transformers/configuration_utils.py](https://localhost:8080/#) in __getattribu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ch is advertised to be supported at: # https://vllm.readthedocs.io/en/latest/models/supported_models.html ``` from vllm import LLM, SamplingParams # https://vllm.readthedocs.io/en/latest/models/supported_models.html llm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
