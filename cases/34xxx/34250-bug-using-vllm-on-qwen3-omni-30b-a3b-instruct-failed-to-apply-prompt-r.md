# vllm-project/vllm#34250: [Bug]: using vllm on Qwen3-Omni-30B-A3B-Instruct: Failed to apply prompt replacement for mm_items['audio'][0].

| 字段 | 值 |
| --- | --- |
| Issue | [#34250](https://github.com/vllm-project/vllm/issues/34250) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: using vllm on Qwen3-Omni-30B-A3B-Instruct: Failed to apply prompt replacement for mm_items['audio'][0].

### Issue 正文摘录

### Your current environment ### Environment Information Linux Python 3.10.0 Cuda 12.8 accelerate==1.12.0 aiohappyeyeballs==2.6.1 aiohttp==3.13.3 aiosignal==1.4.0 annotated-doc==0.0.4 annotated-types==0.7.0 anthropic==0.71.0 anyio==4.12.1 apache-tvm-ffi==0.1.8.post2 astor==0.8.1 async-timeout==5.0.1 attrs==25.4.0 audioread==3.1.0 av==16.1.0 blake3==1.0.8 cachetools==7.0.0 cbor2==5.8.0 certifi==2026.1.4 cffi==2.0.0 charset-normalizer==3.4.4 click==8.3.1 cloudpickle==3.1.2 compressed-tensors==0.12.2 cryptography==46.0.4 cuda-bindings==13.1.1 cuda-pathfinder==1.3.3 cuda-python==13.1.1 cupy-cuda12x==13.6.0 decorator==5.2.1 depyf==0.20.0 dill==0.4.1 diskcache==5.6.3 distro==1.9.0 dnspython==2.8.0 docstring_parser==0.17.0 einops==0.8.2 email-validator==2.3.0 exceptiongroup==1.3.1 fastapi==0.128.1 fastapi-cli==0.0.20 fastapi-cloud-cli==0.11.0 fastar==0.8.0 fastrlock==0.8.3 filelock==3.20.3 flash_attn==2.8.3 flashinfer-python==0.5.3 frozenlist==1.8.0 fsspec==2026.1.0 gguf==0.17.1 h11==0.16.0 hf-xet==1.2.0 httpcore==1.0.9 httptools==0.7.1 httpx==0.28.1 httpx-sse==0.4.3 huggingface_hub==0.36.1 idna==3.11 ijson==3.4.0.post0 ImageIO==2.37.2 imageio-ffmpeg==0.6.0 interegular==0.3.3 Jinja2==3.1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: mespath==1.1.0 joblib==1.5.3 jq==1.10.0 jsonschema==4.26.0 jsonschema-specifications==2025.9.1 lark==1.2.2 lazy_loader==0.4 librosa==0.11.0 llguidance==1.3.0 llvmlite==0.44.0 lm-format-enforcer==0.11.3 loguru==0.7.3 mar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: using vllm on Qwen3-Omni-30B-A3B-Instruct: Failed to apply prompt replacement for mm_items['audio'][0]. bug;stale ### Your current environment ### Environment Information Linux Python 3.10.0 Cuda 12.8 accelerate=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 0.11.0 fastar==0.8.0 fastrlock==0.8.3 filelock==3.20.3 flash_attn==2.8.3 flashinfer-python==0.5.3 frozenlist==1.8.0 fsspec==2026.1.0 gguf==0.17.1 h11==0.16.0 hf-xet==1.2.0 httpcore==1.0.9 httptools==0.7.1 httpx==0.28.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: struct: Failed to apply prompt replacement for mm_items['audio'][0]. bug;stale ### Your current environment ### Environment Information Linux Python 3.10.0 Cuda 12.8 accelerate==1.12.0 aiohappyeyeballs==2.6.1 aiohttp==3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: .upper() return clean_text[:1].upper() if clean_text else "N/A" def evaluate_answer(model_answer, correct_answer): if not model_answer: return False return model_answer.strip().upper() == correct_answer.strip().upper()...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
