# vllm-project/vllm#2254: Can not modify the assistance message using post.request with openai_api

| 字段 | 值 |
| --- | --- |
| Issue | [#2254](https://github.com/vllm-project/vllm/issues/2254) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can not modify the assistance message using post.request with openai_api

### Issue 正文摘录

Hello, I am trying to modify the assistant message through the post_url_request as follow: prompt_generate_sentence = f"Generate a new sentence different than the following sentences {sentences} that .........." response_generate_sentence= post_http_request2(prompt_generate_sentence,' ',api_url, 700) and the post_http_request2: def post_http_request2(prompt: str, assistant_msg :str, api_url: str, max_t: int) -> requests.Response: # Model Specsification system_prompt = "You are a linguist who can understand the semantic roles and can provide a rating on the semantic fit of predicate-arguments for a specific semantic role, given the predicate, the argument and the semantic role." temp = 0.0 top_p = 0.95 pload = { "model":"codellama/CodeLlama-13b-Instruct-hf", "messages":[ {"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}, {"role": "assistant", "content": assistant_msg} ], "temperature": temp, "top_p": top_p, "max_tokens": max_t, } response = requests.post(api_url, json=pload) return response the response I got as follow: using System; using System.Collections.Generic; using System.Linq; using System.Text; using System.Threading.Tasks; namespace _01.Co...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: str, max_t: int) -> requests.Response: # Model Specsification system_prompt = "You are a linguist who can understand the semantic roles and can provide a rating on the semantic fit of predicate-arguments for a specific...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: can provide a rating on the semantic fit of predicate-arguments for a specific semantic role, given the predicate, the argument and the semantic role." temp = 0.0 top_p = 0.95 pload = { "model":"codellama/CodeLlama-13b-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Can not modify the assistance message using post.request with openai_api Hello, I am trying to modify the assistant message through the post_url_request as follow: prompt_generate_sentence = f"Generate a new sentence di...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
