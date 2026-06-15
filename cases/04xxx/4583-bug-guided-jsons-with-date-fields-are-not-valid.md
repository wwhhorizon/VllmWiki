# vllm-project/vllm#4583: [Bug]: guided jsons with date fields are not valid

| 字段 | 值 |
| --- | --- |
| Issue | [#4583](https://github.com/vllm-project/vllm/issues/4583) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: guided jsons with date fields are not valid

### Issue 正文摘录

### Your current environment I host llama3-8B-instruct model in a docker image using the base image vllm/vllm-openai:0.4.1 openai version: 1.6.1 (example script below) ### 🐛 Describe the bug # description When we prompt the model to produce a json with the guided_json parameter set and including a date field, we get an invalid json response. This is also not dependent on the specific model. We got the same error with mixtral models. # code ``` from openai import OpenAI model_name = "/docker_share/models/llama3_8b_instruct" num_prompt_tokens = 1000 base_url = "http://model-url" api_key = "EMPTY" client = OpenAI(base_url=base_url, api_key=api_key) def call_vllm(prompt, guided_json=None): if guided_json: extra_body = { "guided_json": guided_json } messages = [{"role": "user", "content": prompt}] chat_completion = client.chat.completions.create( model=model_name, messages=messages, extra_body=extra_body, seed=42, max_tokens=num_prompt_tokens, temperature=0 ) return chat_completion.choices[0].message.content guided_json = """{ "additionalProperties": false, "properties": { "DocumentDate": {"anyOf": [{"format": "date", "type": "string"}, {"type": "null"}], "description": "Document date"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: stale ### Your current environment I host llama3-8B-instruct model in a docker image using the base image vllm/vllm-openai:0.4.1 openai version: 1.6.1 (example script below) ### 🐛 Describe the bug # description When we...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: date fields are not valid bug;stale ### Your current environment I host llama3-8B-instruct model in a docker image using the base image vllm/vllm-openai:0.4.1 openai version: 1.6.1 (example script below) ### 🐛 Describe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: es[0].message.content guided_json = """{ "additionalProperties": false, "properties": { "DocumentDate": {"anyOf": [{"format": "date", "type": "string"}, {"type": "null"}], "description": "Document date", "title": "Docum...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: guided jsons with date fields are not valid bug;stale ### Your current environment I host llama3-8B-instruct model in a docker image using the base image vllm/vllm-openai:0.4.1 openai version: 1.6.1 (example scri...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
