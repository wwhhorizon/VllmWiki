# vllm-project/vllm#15577: [Bug]: guided_json not working correctly with (quantized) mistral-small model

| 字段 | 值 |
| --- | --- |
| Issue | [#15577](https://github.com/vllm-project/vllm/issues/15577) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: guided_json not working correctly with (quantized) mistral-small model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am providing `guided_json` schema in my request, but the output is not a valid json. Here is my setup: ```docker-compose.yml services: vllm: image: vllm/vllm-openai:v0.8.2 env_file: - .env shm_size: 12gb ports: - 8000:8000 command: --model stelterlab/Mistral-Small-24B-Instruct-2501-AWQ --tokenizer mistralai/Mistral-Small-24B-Instruct-2501 --tokenizer-mode mistral --tool-call-parser mistral --enable-auto-tool-choice --max-model-len 4096 --dtype half --guided-decoding-backend xgrammar ``` and here is my client script: ```main.py from openai import Client from pydantic import BaseModel client = Client(api_key="dummy", base_url="http://localhost:8000/v1") class CarDescription(BaseModel): brand: str model: str json_schema = CarDescription.model_json_schema() completion = client.chat.completions.create( model="stelterlab/Mistral-Small-24B-Instruct-2501-AWQ", messages=[ { "role": "user", "content": "Generate a JSON with the brand, model and car_type of the most iconic car from the 90's", } ], extra_body={"guided_json": json_schema}, ) print(completion.choices[0].message.content) ``` The output is: ``` { "br o" : "Ford" , "model" : "Mu...

## 现有链接修复摘要

#43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: in my request, but the output is not a valid json. Here is my setup: ```docker-compose.yml services: vllm: image: vllm/vllm-openai:v0.8.2 env_file: - .env shm_size: 12gb ports: - 8000:8000 command: --model stelterlab/Mi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: guided_json not working correctly with (quantized) mistral-small model bug;structured-output;stale ### Your current environment ### 🐛 Describe the bug I am providing `guided_json` schema in my request, but the ou...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ing correctly with (quantized) mistral-small model bug;structured-output;stale ### Your current environment ### 🐛 Describe the bug I am providing `guided_json` schema in my request, but the output is not a valid json. H...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ble-auto-tool-choice --max-model-len 4096 --dtype half --guided-decoding-backend xgrammar ``` and here is my client script: ```main.py from openai import Client from pydantic import BaseModel client = Client(api_key="du...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: guided_json not working correctly with (quantized) mistral-small model bug;structured-output;stale ### Your current environment ### 🐛 Describe the bug I am providing `guided_json` schema in my request, but the ou...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15577">#15577</a> by <a href="https://github.com/tiangolo"><code>@​tiangolo</code></a>.</li> <li>🍱 Update sponsors:… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15577">#15577</a> by <a href="https://github.com/tiangolo"><code>@​tiangolo</code></a>.</li> <li>🍱 Update sponsors:… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
