# vllm-project/vllm#324: GPTBigCodeForCasualLM support doesn't work

| 字段 | 值 |
| --- | --- |
| Issue | [#324](https://github.com/vllm-project/vllm/issues/324) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPTBigCodeForCasualLM support doesn't work

### Issue 正文摘录

I tried to use vllm on my finetuned model from starcoder, but its seems not supported from the official package (?) In the README.md is said to be supported. ``` ValueError Traceback (most recent call last) [ ](https://localhost:8080/#) in () 2 3 prompts = ["Helloworld in python"] #You can put several prompts in this list ----> 4 llm = LLM(model="Safurai/Safurai-001") # Load the model 5 outputs = llm.generate(prompts) # Trigger inference 5 frames [/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader.py](https://localhost:8080/#) in _get_model_architecture(config) 25 if arch in _MODEL_REGISTRY: 26 return _MODEL_REGISTRY[arch] ---> 27 raise ValueError( 28 f"Model architectures {architectures} are not supported for now. " 29 f"Supported architectures: {list(_MODEL_REGISTRY.keys())}" ValueError: Model architectures ['GPTBigCodeForCausalLM'] are not supported for now. Supported architectures: ['GPT2LMHeadModel', 'GPTNeoXForCausalLM', 'LlamaForCausalLM', 'OPTForCausalLM'] ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: CodeForCasualLM support doesn't work I tried to use vllm on my finetuned model from starcoder, but its seems not supported from the official package (?) In the README.md is said to be supported. ``` ValueError Traceback...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: finetuned model from starcoder, but its seems not supported from the official package (?) In the README.md is said to be supported. ``` ValueError Traceback (most recent call last) [ ](https://localhost:8080/#) in () 2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /model_executor/model_loader.py](https://localhost:8080/#) in _get_model_architecture(config) 25 if arch in _MODEL_REGISTRY: 26 return _MODEL_REGISTRY[arch] ---> 27 raise ValueError( 28 f"Model architectures {architectu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
