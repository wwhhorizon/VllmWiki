# vllm-project/vllm#7645: [Usage]: The results of the model depend on the number of GPUs.

| 字段 | 值 |
| --- | --- |
| Issue | [#7645](https://github.com/vllm-project/vllm/issues/7645) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: The results of the model depend on the number of GPUs.

### Issue 正文摘录

### Your current environment **package version** - vllm: 0.2.6 - python: 3.9 **Phenomenon** - The output of the same model is different when using only one gpu and two. - the same environment - the same arguments ### How would you like to use vllm I would like to get the same result even if the number of gpu is used differently when referring using vLLM. The code I used is as follows. ```python payload = json.dumps({ "model_name": model_name, "prompt": output_ex['model_input'], "max_tokens": 1024, "stream": False, "top_p": 0.9, "temperature": 0.01, "presence_penalty": 1.0, "stop_token_ids": [2], "best_of": 1 }) headers = { 'Content-Type': 'application/json' } response = requests.request("POST", url, headers=headers, data=payload) ``` - when using only one gpu - output: "" (=empty) - when using twon gpu - output: "No answer found." Has anyone experienced a phenomenon like me where the output comes out differently depending on the number of gpu loading the model?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: The results of the model depend on the number of GPUs. usage;stale ### Your current environment **package version** - vllm: 0.2.6 - python: 3.9 **Phenomenon** - The output of the same model is different when us...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the number of GPUs. usage;stale ### Your current environment **package version** - vllm: 0.2.6 - python: 3.9 **Phenomenon** - The output of the same model is different when using only one gpu and two. - the same environ...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "prompt": output_ex['model_input'], "max_tokens": 1024, "stream": False, "top_p": 0.9, "temperature": 0.01, "presence_penalty": 1.0, "stop_token_ids": [2], "best_of": 1 }) headers = { 'Content-Type': 'application/json'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: The results of the model depend on the number of GPUs. usage;stale ### Your current environment **package version** - vllm: 0.2.6 - python: 3.9 **Phenomenon** - The output of the same model is different when us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
