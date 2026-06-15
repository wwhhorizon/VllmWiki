# vllm-project/vllm#3063: [Bug] Models generate whitespace-only output when temperature is in range [1e-4, 1e-5], regardless of model type

| 字段 | 值 |
| --- | --- |
| Issue | [#3063](https://github.com/vllm-project/vllm/issues/3063) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Models generate whitespace-only output when temperature is in range [1e-4, 1e-5], regardless of model type

### Issue 正文摘录

Setting the temperature in a particular range causes vllm to generate whitespace-only outputs. Values above/below this range work correctly. I have seen this with facebook/opt-125m, fine-tuned mistral-7B models, codellama-13B, and several other models. It seems like this is an issue with vllm rather than the particular model: To reproduce: `python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m` Send request: ``` curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "facebook/opt-125m", "prompt": "San Francisco is a", "max_tokens": 7, "temperature": }' ``` With temperature: `1e-3`: Generates " great place to live. I" `1e-4`: Generates "\ \ \ \ \ \ \ " `1e-5`: Generates "\ \ \ \ \ \ \ " `1e-6`: Generates " great place to live. I"

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug] Models generate whitespace-only output when temperature is in range [1e-4, 1e-5], regardless of model type Setting the temperature in a particular range causes vllm to generate whitespace-only outputs. Values abov...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s like this is an issue with vllm rather than the particular model: To reproduce: `python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m` Send request: ``` curl http://localhost:8000/v1/completions \ -H...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: plication/json" \ -d '{ "model": "facebook/opt-125m", "prompt": "San Francisco is a", "max_tokens": 7, "temperature": }' ``` With temperature: `1e-3`: Generates " great place to live. I" `1e-4`: Generates "\ \ \ \ \ \ \...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n -m vllm.entrypoints.openai.api_server --model facebook/opt-125m` Send request: ``` curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "facebook/opt-125m", "prompt": "San F...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
