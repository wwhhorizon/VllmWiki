# vllm-project/vllm#36279: [Bug]: --cpu-offload-gb fails with AssertionError on Windows (v0.16.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#36279](https://github.com/vllm-project/vllm/issues/36279) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;quantization;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: --cpu-offload-gb fails with AssertionError on Windows (v0.16.0)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The `--cpu-offload-gb` flag fails with an `AssertionError` during initialization on Windows (community build v0.16.0). This makes it impossible to run VRAM-constrained models (like Voxtral Mini 4B at ~8.4 GiB) effectively on 12GB GPUs. Without CPU offload, the model fills nearly all VRAM, leaving only ~400 tokens of KV cache (~0.82 GiB). With working CPU offload, even 1-2 GiB offloaded would increase KV cache to ~1120+ tokens and make the model reliable. ### Steps to Reproduce 1. Windows 11 with NVIDIA RTX 3060 (12GB VRAM) 2. Install vllm-windows v0.16.0 (community build from [SystemPanic/vllm-windows](https://github.com/SystemPanic/vllm-windows)) 3. Run: ```bash vllm serve D:/STT/vllm/models/voxtral-mini-4b \ --host 0.0.0.0 --port 8000 \ --gpu-memory-utilization 0.91 \ --enforce-eager \ --max-model-len 1024 \ --cpu-offload-gb 2 ``` 4. Observe `AssertionError` during startup ### Expected Behavior vLLM offloads 2 GiB of model weights to system RAM, freeing ~2 GiB of VRAM for KV cache. The server starts and serves requests normally. ### Actual Behavior Startup fails with `AssertionError`. Removing `--cpu-offload-gb` allows startup...

## 现有链接修复摘要

#18298 [Don't merge] Debug failing quantization test with input batch move

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ils with an `AssertionError` during initialization on Windows (community build v0.16.0). This makes it impossible to run VRAM-constrained models (like Voxtral Mini 4B at ~8.4 GiB) effectively on 12GB GPUs. Without CPU o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e model reliable. ### Steps to Reproduce 1. Windows 11 with NVIDIA RTX 3060 (12GB VRAM) 2. Install vllm-windows v0.16.0 (community build from [SystemPanic/vllm-windows](https://github.com/SystemPanic/vllm-windows)) 3. R...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: --cpu-offload-gb fails with AssertionError on Windows (v0.16.0) bug ### Your current environment ### 🐛 Describe the bug The `--cpu-offload-gb` flag fails with an `AssertionError` during initialization on Windows...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nity build v0.16.0). This makes it impossible to run VRAM-constrained models (like Voxtral Mini 4B at ~8.4 GiB) effectively on 12GB GPUs. Without CPU offload, the model fills nearly all VRAM, leaving only ~400 tokens of...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: orting;model_support;multimodal_vlm;quantization cache;cuda;quantization;triton build_error;nan_inf env_dependency #18298 [Don't merge] Debug failing quantization test with input batch move Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18298](https://github.com/vllm-project/vllm/pull/18298) | mentioned | 0.45 | [Don't merge] Debug failing quantization test with input batch move | maintainer said this is a core vllm issue, not windows-specific) - #18298 (quantization + cpu offload producing wrong outputs) - #10267 (unified memory support, closed) - #17611 ( |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
