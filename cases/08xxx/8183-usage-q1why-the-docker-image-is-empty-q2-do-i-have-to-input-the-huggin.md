# vllm-project/vllm#8183: [Usage]: Q1why the docker image is empty? Q2 do I have to input the hugging face token? Q3 any python script to start vllm openai servering with codellama(llama2)?

| 字段 | 值 |
| --- | --- |
| Issue | [#8183](https://github.com/vllm-project/vllm/issues/8183) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Q1why the docker image is empty? Q2 do I have to input the hugging face token? Q3 any python script to start vllm openai servering with codellama(llama2)?

### Issue 正文摘录

### Your current environment the vllm-openai image on docker hub ### How would you like to use vllm I want to run inference of a [sqlcoder ](https://huggingface.co/defog/sqlcoder-7b-2). I don't know how to integrate it with vllm. and I want to run a script to start the openai servering not do it by docker run and some parameter. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: face token? Q3 any python script to start vllm openai servering with codellama(llama2)? usage;stale ### Your current environment the vllm-openai image on docker hub ### How would you like to use vllm I want to run infer...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: Q1why the docker image is empty? Q2 do I have to input the hugging face token? Q3 any python script to start vllm openai servering with codellama(llama2)? usage;stale ### Your current environment the vllm-opena...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: thon script to start vllm openai servering with codellama(llama2)? usage;stale ### Your current environment the vllm-openai image on docker hub ### How would you like to use vllm I want to run inference of a [sqlcoder ]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
