# vllm-project/vllm#6697: [Bug]:vllm backed with triton server is not working

| 字段 | 值 |
| --- | --- |
| Issue | [#6697](https://github.com/vllm-project/vllm/issues/6697) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | install |
| Operator 关键词 | attention;triton |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:vllm backed with triton server is not working

### Issue 正文摘录

### Your current environment ```text The output of `curl -X POST localhost:8000/v2/models/vllm_model/generate -d '{"text_input": "What is Triton Inference Server?", "parameters": {"stream": false, "temperature": 0}}' ``` ### 🐛 Describe the bug I have used below command to start the container: docker run --gpus all -it --net=host --rm -p 8001:8001 --shm-size=1G --ulimit memlock=-1 --ulimit stack=67108864 -v ${PWD}:/work -w /work nvcr.io/nvidia/tritonserver:24.06-vllm-python-py3 tritonserver --model-repository ./model_repository however when i am trying curl like below: $ curl -X POST localhost:8000/v2/models/vllm_model/generate -d '{"text_input": "What is Triton Inference Server?", "parameters": {"stream": false, "temperature": 0}}' This is the log i am seeing. here is the official doc i am following: https://github.com/triton-inference-server/vllm_backend 2024-07-23 19:39:35 I0723 14:09:35.070084 1 grpc_server.cc:2463] "Started GRPCInferenceService at 0.0.0.0:8001" 2024-07-23 19:39:35 I0723 14:09:35.070413 1 http_server.cc:4692] "Started HTTPService at 0.0.0.0:8000" 2024-07-23 19:39:35 I0723 14:09:35.119975 1 http_server.cc:362] "Started Metrics Service at 0.0.0.0:8002" 2024-07-23...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 🐛 Describe the bug I have used below command to start the container: docker run --gpus all -it --net=host --rm -p 8001:8001 --shm-size=1G --ulimit memlock=-1 --ulimit stack=67108864 -v ${PWD}:/work -w /work nvcr.io/nvid...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]:vllm backed with triton server is not working bug;stale ### Your current environment ```text The output of `curl -X POST localhost:8000/v2/models/vllm_model/generate -d '{"text_input": "What is Triton Inference Se...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: t_input": "What is Triton Inference Server?", "parameters": {"stream": false, "temperature": 0}}' ``` ### 🐛 Describe the bug I have used below command to start the container: docker run --gpus all -it --net=host --rm -p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]:vllm backed with triton server is not working bug;stale ### Your current environment ```text The output of `curl -X POST localhost:8000/v2/models/vllm_model/generate -d '{"text_input": "What is Triton Inference Se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rrent environment ```text The output of `curl -X POST localhost:8000/v2/models/vllm_model/generate -d '{"text_input": "What is Triton Inference Server?", "parameters": {"stream": false, "temperature": 0}}' ``` ### 🐛 Des...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
