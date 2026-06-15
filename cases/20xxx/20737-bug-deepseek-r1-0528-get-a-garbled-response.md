# vllm-project/vllm#20737: [Bug]: deepseek-r1-0528  get a garbled response

| 字段 | 值 |
| --- | --- |
| Issue | [#20737](https://github.com/vllm-project/vllm/issues/20737) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deepseek-r1-0528  get a garbled response

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use docker to deploy the model with vllm docker image==0.8.5 ` docker run --runtime nvidia -e VLLM_USE_V1=1 -e VLLM_ATTENTION_BACKEND=FLASHMLA --gpus all -v /data/llm-models/DeepSeek-R1-0528:/data/llm-models/DeepSeek-R1-0528 -p 8000:8000 --ipc=host vllm/vllm-openai:v0.8.5 --model /data/llm-models/DeepSeek-R1-0528 --served-model-name deepseek-r1 --enable-prefix-caching --max-model-len 131072 --gpu-memory-utilization 0.95 --tensor-parallel-size 8 --block-size 64 --enable-chunked-prefill --enable-expert-parallel --enable-reasoning --reasoning-parser deepseek_r1 ` When I use this model for long text inputs like meeting summaries, the model occasionally generates corrupted output and enters an infinite generation loop. When I used the same model from other service providers, I didn't encounter this issue with identical inputs. Could you suggest a solution to help resolve this issue? That would be extremely helpful. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which ca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: bug;stale ### Your current environment ### 🐛 Describe the bug I use docker to deploy the model with vllm docker image==0.8.5 ` docker run --runtime nvidia -e VLLM_USE_V1=1 -e VLLM_ATTENTION_BACKEND=FLASHMLA --gpus all -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: deepseek-r1-0528 get a garbled response bug;stale ### Your current environment ### 🐛 Describe the bug I use docker to deploy the model with vllm docker image==0.8.5 ` docker run --runtime nvidia -e VLLM_USE_V1=1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 0.8.5 ` docker run --runtime nvidia -e VLLM_USE_V1=1 -e VLLM_ATTENTION_BACKEND=FLASHMLA --gpus all -v /data/llm-models/DeepSeek-R1-0528:/data/llm-models/DeepSeek-R1-0528 -p 8000:8000 --ipc=host vllm/vllm-openai:v0.8.5 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ul. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: del-len 131072 --gpu-memory-utilization 0.95 --tensor-parallel-size 8 --block-size 64 --enable-chunked-prefill --enable-expert-parallel --enable-reasoning --reasoning-parser deepseek_r1 ` When I use this model for long...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
