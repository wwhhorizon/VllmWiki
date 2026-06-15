# vllm-project/vllm#22043: [Usage]: Provide a valid Hugging Face repository ID

| 字段 | 值 |
| --- | --- |
| Issue | [#22043](https://github.com/vllm-project/vllm/issues/22043) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Provide a valid Hugging Face repository ID

### Issue 正文摘录

### Your current environment Hi, I am getting error below after I try to download my fine-tune model > ValidationError Traceback (most recent call last) [/tmp/ipython-input-16585914.py](https://localhost:8080/#) in () ----> 1 llm = LLM(model="orkungedik/recruitment-docs-7b-extractor") 4 frames [/usr/local/lib/python3.11/dist-packages/pydantic/_internal/_dataclasses.py](https://localhost:8080/#) in __init__(__dataclass_self__, *args, **kwargs) 121 __tracebackhide__ = True 122 s = __dataclass_self__ --> 123 s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s) 124 125 __init__.__qualname__ = f'{cls.__qualname__}.__init__' ValidationError: 1 validation error for ModelConfig Value error, Invalid repository ID or local directory specified: 'orkungedik/recruitment-docs-7b-extractor'. Please verify the following requirements: 1. Provide a valid Hugging Face repository ID. 2. Specify a local directory that contains a recognized configuration file. - For Hugging Face models: ensure the presence of a 'config.json'. - For Mistral models: ensure the presence of a 'params.json'. 3. For GGUF: pass the local path of the GGUF checkpoint. Loading GGUF from a remote re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r ModelConfig Value error, Invalid repository ID or local directory specified: 'orkungedik/recruitment-docs-7b-extractor'. Please verify the following requirements: 1. Provide a valid Hugging Face repository ID. 2. Spec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ment Hi, I am getting error below after I try to download my fine-tune model > ValidationError Traceback (most recent call last) [/tmp/ipython-input-16585914.py](https://localhost:8080/#) in () ----> 1 llm = LLM(model="...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: d. [type=value_error, input_value=ArgsKwargs((), {'model': ...attention_dtype': None}), input_type=ArgsKwargs] For further information visit https://errors.pydantic.dev/2.11/v/value_error Please find the source code bel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
