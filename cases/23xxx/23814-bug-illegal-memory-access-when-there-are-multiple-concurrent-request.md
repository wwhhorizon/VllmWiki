# vllm-project/vllm#23814: [Bug]: illegal memory access when there are multiple concurrent request

| 字段 | 值 |
| --- | --- |
| Issue | [#23814](https://github.com/vllm-project/vllm/issues/23814) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 38; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: illegal memory access when there are multiple concurrent request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have deploy the vLLM with Qwen3 model in docker with below files Dockerfile ```Dockerfile FROM vllm/vllm-openai:latest COPY . . RUN pip install -r requirements.txt ``` docker-compose.yaml ```yaml services: vllm-openai: # image: vllm/vllm-openai:v0.9.2 build: . ports: - "8000:8000" deploy: resources: reservations: devices: - capabilities: [gpu] command: > --model Qwen/Qwen3-30B-A3B-Instruct-2507 --host 0.0.0.0 --port 8000 --swap-space 2 --tensor-parallel-size 8 --pipeline-parallel-size 2 --gpu-memory-utilization 0.85 --enable-auto-tool-choice --tool-call-parser xlam --middleware middlewares.tracing.phoenix_middleware environment: - HUGGING_FACE_HUB_TOKEN= ${HUGGING_FACE_HUB_TOKEN} - VLLM_LOGGING_LEVEL=ERROR - PHOENIX_API_KEY=${PHOENIX_API_KEY} - CUDA_LAUNCH_BLOCKING=1 runtime: nvidia volumes: - ~/.cache/huggingface:/root/.cache/huggingface - ./middlewares:/vllm-workspace/middlewares gpus: all ipc: host shm_size: 64g ``` The deployment was functioning correctly under normal conditions, but in production, when handling multiple concurrent requests from different applications, it consistently triggers an illegal memory access error...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag | #40376 [Perf] Enable FlashInfer top-k/top-p sampler by default

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: illegal memory access when there are multiple concurrent request bug;stale ### Your current environment ### 🐛 Describe the bug I have deploy the vLLM with Qwen3 model in docker with below files Dockerfile ```Dock...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ### 🐛 Describe the bug I have deploy the vLLM with Qwen3 model in docker with below files Dockerfile ```Dockerfile FROM vllm/vllm-openai:latest COPY . . RUN pip install -r requirements.txt ``` docker-compose.yaml ```yam...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rent environment ### 🐛 Describe the bug I have deploy the vLLM with Qwen3 model in docker with below files Dockerfile ```Dockerfile FROM vllm/vllm-openai:latest COPY . . RUN pip install -r requirements.txt ``` docker-co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=2, disable_custom_al...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | ream":"stderr","time":"2025-08-28t08:07:36.019111256z"} {"log":"frame #4: c10d::tcpstore::check(std::vector\u003cstd::__cxx11::basic_string\u003cchar, std::char_traits\u003cchar\u… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | ream":"stderr","time":"2025-08-28t08:07:36.019118858z"} {"log":"frame #6: \u003cunknown function\u003e + 0xdc253 (0x7fb89adb3253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)\n","s… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | ream":"stderr","time":"2025-08-28t08:07:36.019122101z"} {"log":"frame #7: \u003cunknown function\u003e + 0x94ac3 (0x7fb915a59ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)\n","stream… |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23816: Should have ROCm label: NO (0 matches) #23814: Should have ROCm label: NO (0 matches) #23813: Should have ROCm label: NO (0 matches) #23805: Should hav |
| [#40376](https://github.com/vllm-project/vllm/pull/40376) | mentioned | 0.6 | [Perf] Enable FlashInfer top-k/top-p sampler by default | ug]: illegal memory access when there are multiple concurrent request #23814](https://github.com/vllm-project/vllm/issues/23814) * [[Bug][v0.11.0]: gpt-oss-120b generates with no… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
