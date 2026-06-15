# vllm-project/vllm#11411: Error in running 'python -m vllm.entrypoints.openai.api_server '

| 字段 | 值 |
| --- | --- |
| Issue | [#11411](https://github.com/vllm-project/vllm/issues/11411) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error in running 'python -m vllm.entrypoints.openai.api_server '

### Issue 正文摘录

### Your current environment ``` python -m vllm.entrypoints.openai.api_server \ --served-model-name Llama-3.1-8B-Instruct \ --model "/data/hf_models/Llama-3.1-8B-Instruct/" \ --tensor-parallel-size=4 \ --trust-remote-code ``` I want to deploy the llama model, ‘/data/hf_models/Llama-3.1-8B-Instruct/’ is the model path. However, when running this script, it will generate an error: ImportError: cannot import name 'build_regex_from_schema' from 'outlines.fsm.json_schema', and I cannot find build _regex _from _schema' in json_schema.py actually. **Enviroment: vllm=0.5.0.post1, outlines=0.1.11** How to solve this problem? ### How would you like to use vllm I want to run inference of a [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: environment ``` python -m vllm.entrypoints.openai.api_server \ --served-model-name Llama-3.1-8B-Instruct \ --model "/data/hf_models/Llama-3.1-8B-Instruct/" \ --tensor-parallel-size=4 \ --trust-remote-code ``` I want to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: odel path. However, when running this script, it will generate an error: ImportError: cannot import name 'build_regex_from_schema' from 'outlines.fsm.json_schema', and I cannot find build _regex _from _schema' in json_s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: mportError: cannot import name 'build_regex_from_schema' from 'outlines.fsm.json_schema', and I cannot find build _regex _from _schema' in json_schema.py actually. **Enviroment: vllm=0.5.0.post1, outlines=0.1.11** How t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Error in running 'python -m vllm.entrypoints.openai.api_server ' usage;stale ### Your current environment ``` python -m vllm.entrypoints.openai.api_server \ --served-model-name Llama-3.1-8B-Instruct \ --model "/data/hf_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
