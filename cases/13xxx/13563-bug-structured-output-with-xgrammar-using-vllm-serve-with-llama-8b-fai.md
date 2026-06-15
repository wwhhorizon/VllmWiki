# vllm-project/vllm#13563: [Bug]: structured output with xgrammar using vllm serve with llama-8b fails results in os error OSError: OSError: (...)/.cache/torch_extensions/py312_cu124/xgrammar/xgrammar.so: cannot open shared object file: No such file or directory

| 字段 | 值 |
| --- | --- |
| Issue | [#13563](https://github.com/vllm-project/vllm/issues/13563) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: structured output with xgrammar using vllm serve with llama-8b fails results in os error OSError: OSError: (...)/.cache/torch_extensions/py312_cu124/xgrammar/xgrammar.so: cannot open shared object file: No such file or directory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug hi - I get an error trying to generate structured prompts using xgrammar. The below works perfectly fine using outlines as engine, it only seems to be a problem when running xgrammar (default) Running 'vllm serve meta-llama/Llama-3.1-8B-Instruct' opens the server without any problems. When I try to run the below in python, I get the error from the server logs: ```OSError: OSError: *path-to-my-work-dir*/.cache/torch_extensions/py312_cu124/xgrammar/xgrammar.so: cannot open shared object file: No such file or directory``` ```python from pydantic import BaseModel from enum import Enum class Answer(BaseModel): reasoning: str answer: str json_schema = Answer.model_json_schema() from openai import OpenAI client = OpenAI( base_url="http://localhost:8000/v1", api_key="dummy", ) completion = client.chat.completions.create( model="meta-llama/Llama-3.1-8B-Instruct", messages=[ { "role": "user", "content": "What is the capital of France?", } ], extra_body={ "guided_json": json_schema, }, ) print(completion.choices[0].message.content) ``` I run it using a fresh virtual enviroment, with only vllm installed. The script used to produce this is al...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: hared object file: No such file or directory``` ```python from pydantic import BaseModel from enum import Enum class Answer(BaseModel): reasoning: str answer: str json_schema = Answer.model_json_schema() from openai imp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e one on the structured prompting tutorial. Adding ``` "guided_decoding_backend": "outlines", ``` to the ```extra_body``` argument makes it run perfectly fine. I've both tried reinstalling vllm from scratch but it is th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: me! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: structured output with xgrammar using vllm serve with llama-8b fails results in os error OSError: OSError: (...)/.cache/torch_extensions/py312_cu124/xgrammar/xgrammar.so: cannot open shared object file: No such f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rammar.so: cannot open shared object file: No such file or directory bug;stale ### Your current environment ### 🐛 Describe the bug hi - I get an error trying to generate structured prompts using xgrammar. The below work...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
