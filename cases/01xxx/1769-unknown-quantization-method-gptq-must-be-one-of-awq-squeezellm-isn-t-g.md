# vllm-project/vllm#1769: Unknown quantization method: gptq. Must be one of ['awq', 'squeezellm'].Isn’t gptq already supported?

| 字段 | 值 |
| --- | --- |
| Issue | [#1769](https://github.com/vllm-project/vllm/issues/1769) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Unknown quantization method: gptq. Must be one of ['awq', 'squeezellm'].Isn’t gptq already supported?

### Issue 正文摘录

My code like this: ``` llm = LLM(model="/home/llm/QWenData/Qwen-14B-Chat-Int4", revision="v1.1.8", trust_remote_code=True,quantization="gptq") ``` I notice this url :https://github.com/vllm-project/vllm/pull/916 showing qptq already merge in master. I already install git source code for the newest code.but I got this: ``` Unknown quantization method: gptq. Must be one of ['awq', 'squeezellm'] ``` So what should I do to use the gptq model?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Unknown quantization method: gptq. Must be one of ['awq', 'squeezellm'].Isn’t gptq already supported? My code like this: ``` llm = LLM(model="/home/llm/QWenData/Qwen-14B-Chat-Int4", revision="v1.1.8", trust_remote_code=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: eezellm'].Isn’t gptq already supported? My code like this: ``` llm = LLM(model="/home/llm/QWenData/Qwen-14B-Chat-Int4", revision="v1.1.8", trust_remote_code=True,quantization="gptq") ``` I notice this url :https://githu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: m-project/vllm/pull/916 showing qptq already merge in master. I already install git source code for the newest code.but I got this: ``` Unknown quantization method: gptq. Must be one of ['awq', 'squeezellm'] ``` So what...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
