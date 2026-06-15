# vllm-project/vllm#5677: [Usage]:  Use quantization=gptq_marlin for faster inference

| 字段 | 值 |
| --- | --- |
| Issue | [#5677](https://github.com/vllm-project/vllm/issues/5677) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  Use quantization=gptq_marlin for faster inference

### Issue 正文摘录

### Your current environment Docker image tag: **vllm/vllm-openai:v0.5.0.post1** ### How would you like to use vllm In fact, I am not sure whether this is a bug or a usage inquiry. When vLLM startup, I can see a line of log says that: ```text INFO 06-19 06:04:52 gptq_marlin.py:137] Detected that the model can run with gptq_marlin, however you specified quantization=gptq explicitly, so forcing gptq. Use quantization=gptq_marlin for faster inference ``` So, I modified my startup command, to specify the `quantization=gptq_marlin` argument. However, vLLM raised an error: ```text ValueError: Quantization method specified in the model config (gptq) does not match the quantization method specified in the `quantization` argument (gptq_marlin). ``` Am I set the argument correctly?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ion=gptq_marlin for faster inference usage ### Your current environment Docker image tag: **vllm/vllm-openai:v0.5.0.post1** ### How would you like to use vllm In fact, I am not sure whether this is a bug or a usage inqu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: that: ```text INFO 06-19 06:04:52 gptq_marlin.py:137] Detected that the model can run with gptq_marlin, however you specified quantization=gptq explicitly, so forcing gptq. Use quantization=gptq_marlin for faster infere...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Usage]: Use quantization=gptq_marlin for faster inference usage ### Your current environment Docker image tag: **vllm/vllm-openai:v0.5.0.post1** ### How would you like to use vllm In fact, I am not sure whether this is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
