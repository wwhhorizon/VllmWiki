# vllm-project/vllm#10772: [Bug]: OpenAI compatible server with HuggingFaceTB/SmolVLM-Instruct resulting in 500 Internal Server error

| 字段 | 值 |
| --- | --- |
| Issue | [#10772](https://github.com/vllm-project/vllm/issues/10772) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenAI compatible server with HuggingFaceTB/SmolVLM-Instruct resulting in 500 Internal Server error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to run the HuggingFaceTB/SmolVLM-Instruct as openapi-compatible server. The server is coming up but when trying to use the api, it is giving a 500 Internal Server Error. Attaching the code snippet and error stack trace below. **Model** : https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct **Code**: ```import base64 from openai import OpenAI openai_api_key = "abc" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) # Function to encode the image def encode_image(image_path): with open(image_path, "rb") as image_file: return base64.b64encode(image_file.read()).decode('utf-8') # Path to your image image_path = "e44324b2c031f6.jpg" # Getting the base64 string base64_image = encode_image(image_path) # Single-image input inference image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg" try: chat_response = client.chat.completions.create( model="HuggingFaceTB/SmolVLM-Instruct", messages=[{ "role": "user", "content":...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: le "/home/rendernet/.conda/envs/vllm/lib/python3.10/site-packages/anyio/_backends/_asyncio.py", line 685, in __aexit__ raise BaseExceptionGroup( exceptiongroup.ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exce...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ** : https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct **Code**: ```import base64 from openai import OpenAI openai_api_key = "abc" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: OpenAI compatible server with HuggingFaceTB/SmolVLM-Instruct resulting in 500 Internal Server error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to run the Hu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: OpenAI compatible server with HuggingFaceTB/SmolVLM-Instruct resulting in 500 Internal Server error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to run the Hu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ath, "rb") as image_file: return base64.b64encode(image_file.read()).decode('utf-8') # Path to your image image_path = "e44324b2c031f6.jpg" # Getting the base64 string base64_image = encode_image(image_path) # Single-im...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
