# vllm-project/vllm#11077: [Bug]: multilora w/ async engine is limited can only be queried by first `--max-loras` number of models

| 字段 | 值 |
| --- | --- |
| Issue | [#11077](https://github.com/vllm-project/vllm/issues/11077) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: multilora w/ async engine is limited can only be queried by first `--max-loras` number of models

### Issue 正文摘录

### Your current environment ### Model Input Dumps [inference_error.zip](https://github.com/user-attachments/files/18087311/inference_error.zip) ### 🐛 Describe the bug I've been trying to test out the multi lora feature of vllm using the async engine (currently pulling the latest openai vllm server docker `0.6.4.post1`). I notice that no matter what I set `--max-cpu-loras` to and how many loras I specify under `--lora-modules`, it seems like only the first `--max-loras` number of loras are query-able, not just in the same batch (ie what this param is supposed to do according to the documentation), but at all. This error does not occur with the non-async llm engine. This means that if I start the server with this config (NOTE: `--max-loras 1`) ``` sudo docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model meta-llama/Meta-Llama-3.1-8B-Instruct --served-model-name base --enable-lora --num-scheduler-steps 8 --max-loras 1 --max-cpu-loras 4096 --max-lora-rank 32 --lora-modules model0=lora/llama3-8b-lora-adapter-0 model1=lora/llama3-8b-lora-ad...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: using the async engine (currently pulling the latest openai vllm server docker `0.6.4.post1`). I notice that no matter what I set `--max-cpu-loras` to and how many loras I specify under `--lora-modules`, it seems like o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: c engine is limited can only be queried by first `--max-loras` number of models bug;stale ### Your current environment ### Model Input Dumps [inference_error.zip](https://github.com/user-attachments/files/18087311/infer...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: limited can only be queried by first `--max-loras` number of models bug;stale ### Your current environment ### Model Input Dumps [inference_error.zip](https://github.com/user-attachments/files/18087311/inference_error.z...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: . ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
