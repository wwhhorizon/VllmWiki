# vllm-project/vllm#8262: [Usage]: vllm Docker: OSError: Incorrect path_or_model_id

| 字段 | 值 |
| --- | --- |
| Issue | [#8262](https://github.com/vllm-project/vllm/issues/8262) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm Docker: OSError: Incorrect path_or_model_id

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [deepeek](https://modelscope.cn/models/deepseek-ai/DeepSeek-V2-Lite-Chat/files). I don't know how to integrate it with vllm. I want to deploy the fine-tuned [deepseek] (https://modelscope.cn/models/deepseek-ai/DeepSeek-V2-Lite-Chat/files) model using the docker image [vllm/vllm-openai:v0.6.0], but the container cannot run and an error occurs: OSError: Incorrect path_or_model_id: '/data1/models/deepseek'. Please provide either the path to a local folder or the repo_id of a model on the Hub. However, this model can be run in the python environment of vllm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: vllm Docker: OSError: Incorrect path_or_model_id usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [deepeek](ht...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: vllm Docker: OSError: Incorrect path_or_model_id usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [deepeek](ht...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
