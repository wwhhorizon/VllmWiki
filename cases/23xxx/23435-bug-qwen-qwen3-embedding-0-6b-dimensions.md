# vllm-project/vllm#23435: [Bug]: Qwen/Qwen3-Embedding-0.6B不支持修改dimensions？

| 字段 | 值 |
| --- | --- |
| Issue | [#23435](https://github.com/vllm-project/vllm/issues/23435) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen3-Embedding-0.6B不支持修改dimensions？

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` 通过vllm serve Qwen/Qwen3-Embedding-0.6B运行模型， client.embeddings.create( dimensions= 1024 ) 报如下错误 ``` ```python from openai import OpenAI # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" def main(): client = OpenAI( # defaults to os.environ.get("OPENAI_API_KEY") api_key=openai_api_key, base_url=openai_api_base, ) models = client.models.list() model = models.data[0].id responses = client.embeddings.create( input=[ "Hello my name is", "The best thing about vLLM is that it supports many different models", ], model=model, dimensions= 1024 ) # print(responses.data) for data in responses.data: print(data.embedding) # List of float of len 32 if __name__ == "__main__": main() ``` ``` raceback (most recent call last): File "/home/ps/echo/test.py", line 61, in main() File "/home/ps/echo/test.py", line 40, in main responses = client.embeddings.create( File "/home/ps/miniconda3/envs/myenv/lib/python3.10/site-packages/openai/resources/embeddings.py", line 132, in create return self._post( File "/home/ps/miniconda3/envs/myenv/lib/python3.10/site-packages/ope...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: create( dimensions= 1024 ) 报如下错误 ``` ```python from openai import OpenAI # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" def main():...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Qwen/Qwen3-Embedding-0.6B不支持修改dimensions？ bug;stale ### Your current environment ### 🐛 Describe the bug ``` 通过vllm serve Qwen/Qwen3-Embedding-0.6B运行模型， client.embeddings.create( dimensions= 1024 ) 报如下错误 ``` ```py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen/Qwen3-Embedding-0.6B不支持修改dimensions？ bug;stale ### Your current environment ### 🐛 Describe the bug ``` 通过vllm serve Qwen/Qwen3-Embedding-0.6B运行模型， client.embeddings.create( dimensions= 1024 ) 报如下错误
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
