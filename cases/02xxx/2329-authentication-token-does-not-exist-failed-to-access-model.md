# vllm-project/vllm#2329: Authentication token does not exist, failed to access model

| 字段 | 值 |
| --- | --- |
| Issue | [#2329](https://github.com/vllm-project/vllm/issues/2329) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Authentication token does not exist, failed to access model

### Issue 正文摘录

when i run the command bellow: ``` import os os.environ['VLLM_USE_MODELSCOPE']='True' from vllm import LLM, SamplingParams llm = LLM(model="/data/share/rwq/Qwen-7B-Chat", revision="v1.1.8", trust_remote_code=True) ``` which I load the model from local, it runs error as following: ``` 2024-01-03 17:58:31,460 - modelscope - ERROR - Authentication token does not exist, failed to access model /data/share/rwq/Qwen-7B-Chat which may not exist or may be private. Please login first. --------------------------------------------------------------------------- HTTPError Traceback (most recent call last) File ~/work/conda/envs/qwen/lib/python3.10/site-packages/modelscope/hub/errors.py:91, in handle_http_response(response, logger, cookies, model_id) 90 try: ---> 91 response.raise_for_status() 92 except HTTPError as error: ``` how to solve it ?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Authentication token does not exist, failed to access model when i run the command bellow: ``` import os os.environ['VLLM_USE_MODELSCOPE']='True' from vllm import LLM, SamplingParams llm = LLM(model="/data/share/rwq/Qwe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oes not exist, failed to access model when i run the command bellow: ``` import os os.environ['VLLM_USE_MODELSCOPE']='True' from vllm import LLM, SamplingParams llm = LLM(model="/data/share/rwq/Qwen-7B-Chat", revision="...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
