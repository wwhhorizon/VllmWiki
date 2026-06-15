# vllm-project/vllm#5186: [Bug]: vLLM api_server.py when using with prompt_token_ids causes error.

| 字段 | 值 |
| --- | --- |
| Issue | [#5186](https://github.com/vllm-project/vllm/issues/5186) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM api_server.py when using with prompt_token_ids causes error.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug `/generate` endpoint in `vllm.entrypoints.api_server.py` seems to support passing encoded tokens directly without tokenization but contains 2 bugs. 1st causes error making it useless, 2nd bug is not a bug maybe lack of implementation for returning token_ids. ## Bugs 1. When using the `prompt_token_ids` field in `/generate` api [last step](https://github.com/vllm-project/vllm/blob/8279078e218833b357f7c5076850e3688714d570/vllm/entrypoints/api_server.py#L77) of route tries to concatenate prompt field with generated text which raises error because `prompt` field is null when using `prompt_token_ids`. ```python # vllm/entrypoints/api_server.py @app.post("/generate") async def generate(request: Request) -> Response: ........................... hidden code ..................... prompt = final_output.prompt #[Bug] text_outputs = [prompt + output.text for output in final_output.outputs] ret = {"text": text_outputs} return JSONResponse(ret) ``` This can be avoided without any compatibility issues by checking if prompt is of type str or not ```python # vllm/entrypoints/api_server.py @app.pos...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: vLLM api_server.py when using with prompt_token_ids causes error. bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug `/generate` endpoint in `vllm.entrypoi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: trypoints/api_server.py#L77) field This could be simply fixed by introducing a new field in response, token_ids which could either always be populated or only if detokenize is False, the below code assumes the latter. `...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: prompt = final_output.prompt if isinstance(final_output.prompt,str) else "" # fix text_outputs = [prompt + output.text for output in final_output.outputs] ret = {"text": text_outputs} return JSONResponse(ret) ``` 2. The...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: outputs} return JSONResponse(ret) Both bug fixes have been tested by me while running Mistral 7b instruct v3, calling the `/generate` api and with above two fixes causes no issues and returns responses as intended.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
