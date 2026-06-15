# vllm-project/vllm#1813: Install vLLM with CUDA 11.8 run api_server failed

| 字段 | 值 |
| --- | --- |
| Issue | [#1813](https://github.com/vllm-project/vllm/issues/1813) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Install vLLM with CUDA 11.8 run api_server failed

### Issue 正文摘录

install vLLM with CUDA 11.8 by running: # Install vLLM with CUDA 11.8. # Replace `cp310` with your Python version (e.g., `cp38`, `cp39`, `cp311`). pip install https://github.com/vllm-project/vllm/releases/download/v0.2.2/vllm-0.2.2+cu118-cp310-cp310-manylinux1_x86_64.whl # Re-install PyTorch with CUDA 11.8. pip uninstall torch -y pip install torch --upgrade --index-url https://download.pytorch.org/whl/cu118 pip list: Package Version ------------------------- ------------ aiosignal 1.3.1 anyio 3.7.1 argcomplete 3.1.6 attrs 23.1.0 certifi 2023.11.17 charset-normalizer 3.3.2 click 8.1.7 einops 0.7.0 exceptiongroup 1.2.0 fastapi 0.104.1 filelock 3.13.1 frozenlist 1.4.0 fsspec 2023.10.0 h11 0.14.0 httptools 0.6.1 huggingface-hub 0.19.4 idna 3.6 Jinja2 3.1.2 jsonschema 4.20.0 jsonschema-specifications 2023.11.1 MarkupSafe 2.1.3 mpmath 1.3.0 msgpack 1.0.7 networkx 3.2.1 ninja 1.11.1.1 numpy 1.26.2 nvidia-cublas-cu12 12.1.3.1 nvidia-cuda-cupti-cu12 12.1.105 nvidia-cuda-nvrtc-cu12 12.1.105 nvidia-cuda-runtime-cu12 12.1.105 nvidia-cudnn-cu12 8.9.2.26 nvidia-cufft-cu12 11.0.2.54 nvidia-curand-cu12 10.3.2.106 nvidia-cusolver-cu12 11.4.5.107 nvidia-cusparse-cu12 12.1.0.106 nvidia-nccl-cu12 2.1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Install vLLM with CUDA 11.8 run api_server failed install vLLM with CUDA 11.8 by running: # Install vLLM with CUDA 11.8. # Replace `cp310` with your Python version (e.g., `cp38`, `cp39`, `cp311`). pip install https://git
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 23.10.0 h11 0.14.0 httptools 0.6.1 huggingface-hub 0.19.4 idna 3.6 Jinja2 3.1.2 jsonschema 4.20.0 jsonschema-specifications 2023.11.1 MarkupSafe 2.1.3 mpmath
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 1.8" \ --trust-remote-code WARNING 11-28 21:04:20 config.py:140] awq quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 11-28 21:04:20 llm_engine.py:72] Initializing an LLM...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: +cu118 tqdm 4.66.1 transformers 4.35.2 triton 2.1.0 typing_extensions 4.8.0 tzdata 2023.3 urllib3 2.1.0 userpath 1.9.1 uvicorn 0.24.0.post1 uvloop
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Install vLLM with CUDA 11.8 run api_server failed install vLLM with CUDA 11.8 by running: # Install vLLM with CUDA 11.8. # Replace `cp310` with your Python version (e.g., `cp38`, `cp39`, `cp311`). pip install https://gi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
