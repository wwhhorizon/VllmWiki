# vllm-project/vllm#17609: [Bug]: content is null when use "chat_template_kwargs": {"enable_thinking": false} in the request.

| 字段 | 值 |
| --- | --- |
| Issue | [#17609](https://github.com/vllm-project/vllm/issues/17609) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: content is null when use "chat_template_kwargs": {"enable_thinking": false} in the request.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug start qwen3: ```shell docker run -itd --gpus '"device=4,5,6,7"' --shm-size=128g -e NCCL_DEBUG=INFO -e CUDA_LAUNCH_BLOCKING=1 -e NCCL_P2P_DISABLE=1 --name inference_model_2 -itd -p 8000:8000 -v /data/models:/models vllm/vllm-openai:v0.8.5 --model /models/Qwen3-30B-A3B-FP8/ --served-model-name helium --disable-log-requests --gpu-memory-utilization 0.9 --max-model-len 16384 --pipeline-parallel-size 1 --port 8000 --tensor-parallel-size 4 --enable-expert-parallel --enable-auto-tool-choice --tool-call-parser hermes --enable-reasoning --reasoning-parser deepseek_r1 ``` send request ```json { "messages": [ { "role": "system", "content": "你是人工智能助手." }, { "role": "user", "content": "常见的十字花科植物有哪些?" } ], "model": "helium", "max_tokens": 2048, "seed": 687590824, "stream": false, "temperature": 0.6, "chat_template_kwargs": {"enable_thinking": false} } ``` get the response: ``` { "id": "chatcmpl-17f8a28f909b464f91bd2855e5f1de37", "object": "chat.completion", "created": 1746261650, "model": "helium", "choices": [ { "index": 0, "message": { "role": "assistant", "reasoning_content": "十字花科（Brassicaceae，也称芸苔科）是一个包含许多重要蔬菜和经济作物的植物科。其最显著的特征是花朵有四片花瓣，呈十字...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ur current environment ### 🐛 Describe the bug start qwen3: ```shell docker run -itd --gpus '"device=4,5,6,7"' --shm-size=128g -e NCCL_DEBUG=INFO -e CUDA_LAUNCH_BLOCKING=1 -e NCCL_P2P_DISABLE=1 --name inference_model_2 -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ata/models:/models vllm/vllm-openai:v0.8.5 --model /models/Qwen3-30B-A3B-FP8/ --served-model-name helium --disable-log-requests --gpu-memory-utilization 0.9 --max-model-len 16384 --pipeline-parallel-size 1 --port 8000 -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: null when use "chat_template_kwargs": {"enable_thinking": false} in the request. bug;stale ### Your current environment ### 🐛 Describe the bug start qwen3: ```shell docker run -itd --gpus '"device=4,5,6,7"' --shm-size=1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: run -itd --gpus '"device=4,5,6,7"' --shm-size=128g -e NCCL_DEBUG=INFO -e CUDA_LAUNCH_BLOCKING=1 -e NCCL_P2P_DISABLE=1 --name inference_model_2 -itd -p 8000:8000 -v /data/models:/models vllm/vllm-openai:v0.8.5 --model /m...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: : content is null when use "chat_template_kwargs": {"enable_thinking": false} in the request. bug;stale ### Your current environment ### 🐛 Describe the bug start qwen3: ```shell docker run -itd --gpus '"device=4,5,6,7"'...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
