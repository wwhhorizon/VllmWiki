# vllm-project/vllm#730: can not run baichuan-13B  in v100

| 字段 | 值 |
| --- | --- |
| Issue | [#730](https://github.com/vllm-project/vllm/issues/730) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> can not run baichuan-13B  in v100

### Issue 正文摘录

hello when I run code as below: `from vllm import LLM llm = LLM(model='baichuan-inc/Baichuan-13B-Chat', trust_remote_code=True) # Name or path of your model output = llm.generate("Hello, my name is") print(output)` and error occur: **ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla V100-SXM2-32GB GPU has compute capability 7.0.** v100 can not run baichuan-13B-Chat in vllm?? could you help me?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e("Hello, my name is") print(output)` and error occur: **ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla V100-SXM2-32GB GPU has compute capability 7.0.** v100 can not r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: not run baichuan-13B in v100 hello when I run code as below: `from vllm import LLM llm = LLM(model='baichuan-inc/Baichuan-13B-Chat', trust_remote_code=True) # Name or path of your model output = llm.generate("Hello, my...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: occur: **ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla V100-SXM2-32GB GPU has compute capability 7.0.** v100 can not run baichuan-13B-Chat in vllm?? could you help me?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: in v100 hello when I run code as below: `from vllm import LLM llm = LLM(model='baichuan-inc/Baichuan-13B-Chat', trust_remote_code=True) # Name or path of your model output = llm.generate("Hello, my name is") print(outpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
