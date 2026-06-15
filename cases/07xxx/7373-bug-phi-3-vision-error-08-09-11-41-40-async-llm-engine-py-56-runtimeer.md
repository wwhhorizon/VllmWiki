# vllm-project/vllm#7373: [Bug]: Phi-3-vision: ERROR 08-09 11:41:40 async_llm_engine.py:56] RuntimeError: stack expects each tensor to be equal size, but got [1933, 4096] at entry 0 and [2509, 4096] at entry 1

| 字段 | 值 |
| --- | --- |
| Issue | [#7373](https://github.com/vllm-project/vllm/issues/7373) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;sampling_logits |
| 子分类 | install |
| Operator 关键词 | moe;sampling;triton |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Phi-3-vision: ERROR 08-09 11:41:40 async_llm_engine.py:56] RuntimeError: stack expects each tensor to be equal size, but got [1933, 4096] at entry 0 and [2509, 4096] at entry 1

### Issue 正文摘录

### Your current environment docker latest for 0.5.3 ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=1"' \ --shm-size=10.24gb \ -p 5063:5063 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -e VLLM_NCCL_SO_PATH=/usr/local/lib/python3.10/dist-packages/nvidia/nccl/lib/libnccl.so.2 \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name phi3vision \ vllm/vllm-openai:latest \ --port=5063 \ --host=0.0.0.0 \ --model=microsoft/Phi-3-vision-128k-instruct \ --tensor-parallel-size=1 \ --seed 1234 \ --trust-remote-code \ --max-model-len=131072 \ --max-num-batched-tokens 131072 \ --max-num-seqs=17 \ --max-log-len=100 \ --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_server.phi3vision.txt ``` ### 🐛 Describe the bug Was using phi-3 for 2 weeks without issue, many images etc. Unsure exactly what caused it, but this is the failure. Clearly image processing issue. ``` 08-09 11:41:40 async_llm_engine.py:173] Added request chat-3379ed24...

## 现有链接修复摘要

#7392 [Bugfix] Fix phi3v batch inference when images have different aspect ratio

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ING_FACE_HUB_TOKEN \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name phi3vision \ vllm/vllm-openai:latest \ --port=5063 \ --host=0.0.0....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: at entry 0 and [2509, 4096] at entry 1 bug ### Your current environment docker latest for 0.5.3 ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=1"' \ --shm-siz...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: t chat-fcbb9c8388104f9ca63b7ecd29b89b43: prompt: ' \nYou are h2oGPTe, an expert question-answering AI system created by H2O.ai. \n , error_callback= >) handle: , error_callback= >)> ``` development ci_build;distributed_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name phi3vision \ vllm/vllm-openai:latest \ --port=5063 \ --host=0.0.0.0 \ --model=microsoft/Phi-3-vision...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ge processing issue. ``` 08-09 11:41:40 async_llm_engine.py:173] Added request chat-3379ed24490d4f398fc0db684039f72e. WARNING 08-09 11:41:40 chat_utils.py:146] 'image_url.detail' is currently not supported and will be i...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7392](https://github.com/vllm-project/vllm/pull/7392) | closes_keyword | 0.95 | [Bugfix] Fix phi3v batch inference when images have different aspect ratio | FIX #7373 (*link existing issues this PR will resolve*) - Previous PR #6621 broke the batch inference when images have different aspect ratio. - This PR fixes the batch inferenc |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
