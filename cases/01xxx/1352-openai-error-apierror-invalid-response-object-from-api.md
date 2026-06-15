# vllm-project/vllm#1352: openai.error.APIError: Invalid response object from API

| 字段 | 值 |
| --- | --- |
| Issue | [#1352](https://github.com/vllm-project/vllm/issues/1352) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> openai.error.APIError: Invalid response object from API

### Issue 正文摘录

Traceback (most recent call last): File "C:\Users\loong.conda\envs\nlp\lib\site-packages\openai\api_requestor.py", line 403, in handle_error_response error_data = resp["error"] KeyError: 'error' During handling of the above exception, another exception occurred: Traceback (most recent call last): File "D:\llm\NLP\aquila_openai_api_vllm.py", line 54, in test_embedding() File "D:\llm\NLP\aquila_openai_api_vllm.py", line 25, in test_embedding embedding = openai.Embedding.create(model =model,input="你好") File "C:\Users\loong.conda\envs\nlp\lib\site-packages\openai\api_resources\embedding.py", line 33, in create response = super().create(*args, **kwargs) File "C:\Users\loong.conda\envs\nlp\lib\site-packages\openai\api_resources\abstract\engine_api_resource.py", line 153, in create response, _, api_key = requestor.request( File "C:\Users\loong.conda\envs\nlp\lib\site-packages\openai\api_requestor.py", line 298, in request resp, got_stream = self._interpret_response(result, stream) File "C:\Users\loong.conda\envs\nlp\lib\site-packages\openai\api_requestor.py", line 707, in _interpret_response self._interpret_response_line( File "C:\Users\loong.conda\envs\nlp\lib\site-packages\openai\api_r...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm.py", line 25, in test_embedding embedding = openai.Embedding.create(model =model,input="你好") File "C:\Users\loong.conda\envs\nlp\lib\site-packages\openai\api_resources\embedding.py", line 33, in create response = s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: last): File "C:\Users\loong.conda\envs\nlp\lib\site-packages\openai\api_requestor.py", line 403, in handle_error_response error_data = resp["error"] KeyError: 'error' During handling of the above exception, another exce...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ent call last): File "D:\llm\NLP\aquila_openai_api_vllm.py", line 54, in test_embedding() File "D:\llm\NLP\aquila_openai_api_vllm.py", line 25, in test_embedding embedding = openai.Embedding.create(model =model,input="你...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
