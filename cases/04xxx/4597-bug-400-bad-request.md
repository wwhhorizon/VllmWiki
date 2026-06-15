# vllm-project/vllm#4597: [Bug]: 400 Bad Request

| 字段 | 值 |
| --- | --- |
| Issue | [#4597](https://github.com/vllm-project/vllm/issues/4597) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 400 Bad Request

### Issue 正文摘录

### Your current environment 使用docker run --gpus all -v D:\docker\huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=****************" -d -p 8000:8000 --ipc=host --name vllm vllm/vllm-openai:latest --model nvidia/Llama3-ChatQA-1.5-8B --api-key vllm-abc123456 --gpu-memory-utilization 0.9部署成功了server端 客户端运行下面的代码报错： from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API server. openai_api_key = "vllm-abc123456" openai_api_base = "http://192.168.2.6:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) chat_response = client.chat.completions.create( model="nvidia/Llama3-ChatQA-1.5-8B", messages=[ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Tell me a joke."}, ], extra_body = { "guided_choice": ["positive", "negative"] } ).choices[0].message.content print("Chat response:", chat_response) 错误： D:\docker\vllm\venv\Scripts\python.exe D:\docker\vllm\llm_client.py Traceback (most recent call last): File "D:\docker\vllm\llm_client.py", line 14, in chat_response = client.chat.completions.create( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "D:\docker\vllm\venv\Lib\site-packages\openai\_utils\...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: stale ### Your current environment 使用docker run --gpus all -v D:\docker\huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=****************" -d -p 8000:8000 --ipc=host --name vllm vllm/vllm-openai:latest...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: 400 Bad Request bug;stale ### Your current environment 使用docker run --gpus all -v D:\docker\huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=****************" -d -p 8000:8000 --ipc=host --name v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: 400 Bad Request bug;stale ### Your current environment 使用docker run --gpus all -v D:\docker\huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=****************" -d -p 8000:8000 --ipc=host --name v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: *************" -d -p 8000:8000 --ipc=host --name vllm vllm/vllm-openai:latest --model nvidia/Llama3-ChatQA-1.5-8B --api-key vllm-abc123456 --gpu-memory-utilization 0.9部署成功了server端 客户端运行下面的代码报错： from openai import OpenAI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
