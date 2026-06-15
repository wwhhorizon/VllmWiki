# vllm-project/vllm#23655: [Usage]: RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error?

| 字段 | 值 |
| --- | --- |
| Issue | [#23655](https://github.com/vllm-project/vllm/issues/23655) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error?

### Issue 正文摘录

I created an docker image in the WSL (Windows Subsystem for Linux) on PC A, with the **Dockerfile** as follows. However, **the following error occurred** when deploying it to the WSL on laptop PC B. （ps: it **works** when deploying it to the WSL on PC A. In the successfully running container, Python version is 3.10.12, torch version is 2.7.1, and vllm version is 0.10.1） ### Your current environment **PC A Environment** Operating System: Windows 11 Home Graphics Card: RTX 4070 SUPER GPU Driver Version: 572.60 Linux Version in WSL: 22.04 CUDA Version in WSL: 12.8 **PC B Environment** Operating System: Windows 11 Home Graphics Card: RTX 4060 Laptop GPU Driver Version: 580.97 Linux Version in WSL: 22.04 CUDA Version in WSL: 13.0 ## Dockerfile ``` FROM nvidia/cuda:12.4.0-devel-ubuntu22.04 ENV DEBIAN_FRONTEND=noninteractive ENV PYTHONUNBUFFERED=1 ENV CUDA_VISIBLE_DEVICES=0 WORKDIR /code RUN apt-get update && apt-get install -y \ python3 \ python3-pip \ python3-venv \ git \ curl \ wget \ build-essential \ && rm -rf /var/lib/apt/lists/* RUN ln -s /usr/bin/python3 /usr/bin/python # install UV RUN pip install uv ENV PATH="/root/.local/bin:$PATH" RUN uv --version RUN mkdir -p /models/Qwen RU...

## 现有链接修复摘要

#20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: umCudaDevices() that might have already set an error? usage I created an docker image in the WSL (Windows Subsystem for Linux) on PC A, with the **Dockerfile** as follows. However, **the following error occurred** when...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Usage]: RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? usage I created an docker image in the WSL (Window...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 0 pid=126) ERROR 08-26 13:24:12 [core.py:700] from vllm.v1.attention.backends.flash_attn import FlashAttentionMetadata (EngineCore_0 pid=126) ERROR 08-26 13:24:12 [core.py:700] File "/code/.venv/lib/python3.10/site-pack...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: odel-len 2048 --port 8080 --tensor-parallel-size 1 --trust-remote-code --dtype bfloat16 --served-model-name "Qwen2.5-0.5B-Instruct"\n\ ' > /start.sh && chmod +x /start.sh CMD ["/start.sh"] ``` ## Error ```text (EngineCo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ll uv ENV PATH="/root/.local/bin:$PATH" RUN uv --version RUN mkdir -p /models/Qwen RUN mkdir -p /code COPY ./code /code COPY ./models/Qwen/Qwen2___5-0___5B-Instruct /models/Qwen/Qwen2___5-0___5B-Instruct WORKDIR /code R...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | oject/vllm from past 7 days. All didn't trigger ROCm label ``` 1. #23655: [Usage]: RuntimeError: Unexpected error from cudaGetDeviceCo... [usage] 2. #23645: [Bug]: Qwen2.5-VL GPTQ |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23661: Should have ROCm label: NO (0 matches) #23655: Should have ROCm label: NO (0 matches) #23645: Should have ROCm label: NO (0 matches) #23641: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
