# vllm-project/vllm#25036: [Bug]: Service Crashes Upon Any Request When Using OpenReasoning-Nemotron-32B After Switching to V1

| 字段 | 值 |
| --- | --- |
| Issue | [#25036](https://github.com/vllm-project/vllm/issues/25036) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Service Crashes Upon Any Request When Using OpenReasoning-Nemotron-32B After Switching to V1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deploying with Docker using the OpenReasoning-Nemotron-32B model, the service crashes and exits immediately after processing any request once the container is fully started. This issue may be related to flexattention. Adding the environment variable `-e 'VLLM_USE_V1=0'` prevents the crash (though it introduces [another bug](https://github.com/vllm-project/vllm/issues/21292)). ### Startup command: ```bash docker run --runtime nvidia --gpus '"device=0,1,2,3,4,5,6,7"' -v cache/huggingface:/root/.cache/huggingface -e 'VLLM_USE_FLASHINFER_SAMPLER=0' -p 8000:8000 --ipc=host -d vllm/vllm-openai:v0.10.2 --enable-auto-tool-choice --tool-call-parser hermes --model nvidia/OpenReasoning-Nemotron-32B --max-model-len 32768 --enforce-eager -tp 8 ``` ### Sample code: Just use [https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client.py) ### Error message: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom rig...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug When deploying with Docker using the OpenReasoning-Nemotron-32B model, the service crashes and exits immediately after processing any request once the container is fully s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Service Crashes Upon Any Request When Using OpenReasoning-Nemotron-32B After Switching to V1 bug;stale ### Your current environment ### 🐛 Describe the bug When deploying with Docker using the OpenReasoning-Nemotr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 2,3,4,5,6,7"' -v cache/huggingface:/root/.cache/huggingface -e 'VLLM_USE_FLASHINFER_SAMPLER=0' -p 8000:8000 --ipc=host -d vllm/vllm-openai:v0.10.2 --enable-auto-tool-choice --tool-call-parser hermes --model nvidia/OpenR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the bug When deploying with Docker using the OpenReasoning-Nemotron-32B model, the service crashes and exits immediately after processing any request once the container is fully started. This issue may be related to fle...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
