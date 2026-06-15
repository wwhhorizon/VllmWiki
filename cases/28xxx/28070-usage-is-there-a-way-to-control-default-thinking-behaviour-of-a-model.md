# vllm-project/vllm#28070: [Usage]: Is there a way to control default thinking behaviour of a model?

| 字段 | 值 |
| --- | --- |
| Issue | [#28070](https://github.com/vllm-project/vllm/issues/28070) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is there a way to control default thinking behaviour of a model?

### Issue 正文摘录

### Your current environment Is there a way to control default thinking behaviour for models deployed through vllm. As per https://docs.vllm.ai/en/stable/features/reasoning_outputs.html, IBM Grantie 3.2 reasoning is disabled by default. Qwen3, GLM 4.6, Deepseek V3.1 all have reasoning enabled by default. It would be great if there is a way to control this from vllm. --override-generation-config allows user to override temperature and other params at deployment. But this does not work for reasoning. I have tried `docker run -d --runtime nvidia -e TRANSFORMERS_OFFLINE=1 -e DEBUG="true" -p 8000:8000 --ipc=host vllm/vllm-openai:v0.11.0 --reasoning-parser qwen3 --model Qwen/Qwen3-4B --override-generation-config '{"chat_template_kwargs": {"enable_thinking": false}}'` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: arams at deployment. But this does not work for reasoning. I have tried `docker run -d --runtime nvidia -e TRANSFORMERS_OFFLINE=1 -e DEBUG="true" -p 8000:8000 --ipc=host vllm/vllm-openai:v0.11.0 --reasoning-parser qwen3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Is there a way to control default thinking behaviour of a model? usage ### Your current environment Is there a way to control default thinking behaviour for models deployed through vllm. As per https://docs.vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: erride-generation-config '{"chat_template_kwargs": {"enable_thinking": false}}'` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
