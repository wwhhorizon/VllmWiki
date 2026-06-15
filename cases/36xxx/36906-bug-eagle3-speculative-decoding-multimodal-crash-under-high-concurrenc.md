# vllm-project/vllm#36906: [Bug]: EAGLE3 speculative decoding + multimodal crash under high concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#36906](https://github.com/vllm-project/vllm/issues/36906) |
| 状态 | open |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EAGLE3 speculative decoding + multimodal crash under high concurrency

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve` crashes when serving `lightonai/LightOnOCR-2-1B` with EAGLE3 speculative decoding and default async scheduling. Some info from debugging: - some request orders crash, some do not - concurrency `1` is stable - `--no-async-scheduling` avoided the crash in all tested cases so far - a dense batch of `old_scans` images crashes immediately on the first batch ### Minimal repro **Server** ```bash vllm serve lightonai/LightOnOCR-2-1B \ --port 8040 \ --no-enable-prefix-caching \ --mm-processor-cache-gb 0 \ --limit-mm-per-prompt '{"image": 1}' \ --gpu-memory-utilization 0.96 \ --speculative-config '{"model": "staghado/LightOnOCR-2-1B-speculator-eagle3-bug-report", "num_speculative_tokens": 3, "method": "eagle3"}' ``` **Client** Use 98 `old_scans` images from [`staghado/olmo-ocr`](https://huggingface.co/datasets/staghado/olmo-ocr) and send them concurrently to `/v1/chat/completions`: ```python import base64, json, urllib.request from concurrent.futures import ThreadPoolExecutor from pathlib import Path from huggingface_hub import snapshot_download url = "http://localhost:8040/v1/chat/completions" root = Path(snapshot_download("s...

## 现有链接修复摘要

#37092 [WIP][Bugfix] Clamp -1 async placeholders to fix CUDA assert in multimodal+EAGLE3 | #37629 [Bugfix] Fix EAGLE3+async crash: clear stale spec_token_ids for unscheduled requests

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: EAGLE3 speculative decoding + multimodal crash under high concurrency bug ### Your current environment ### 🐛 Describe the bug `vllm serve` crashes when serving `lightonai/LightOnOCR-2-1B` with EAGLE3 speculative...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: mo-ocr) and send them concurrently to `/v1/chat/completions`: ```python import base64, json, urllib.request from concurrent.futures import ThreadPoolExecutor from pathlib import Path from huggingface_hub import snapshot...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: EAGLE3 speculative decoding + multimodal crash under high concurrency bug ### Your current environment ### 🐛 Describe the bug `vllm serve` crashes when serving `lightonai/LightOnOCR-2-1B` with EAGLE3 speculative...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: . ### Error On `v0.17.1`, the server log shows: ```text RuntimeError: CUDA driver error: device-side assert triggered ... EngineCore encountered a fatal error. ... vllm.v1.engine.exceptions.EngineDeadError: EngineCore e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ed an issue. ``` The crash occurs in compiled model execution (Inductor/Triton), after which the API returns `500`. ### Likely cause The crash trace points to an out-of-bounds token ID reaching the **target model embedd...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37092](https://github.com/vllm-project/vllm/pull/37092) | closes_keyword | 0.95 | [WIP][Bugfix] Clamp -1 async placeholders to fix CUDA assert in multimodal+EAGLE3 | Fixes #36906. When async scheduling is used with EAGLE3 speculative decoding and multimodal models (e.g., `lightonai/LightOnOCR-2-1B`), `-1` placeholder token IDs can leak into em |
| [#37629](https://github.com/vllm-project/vllm/pull/37629) | closes_keyword | 0.95 | [Bugfix] Fix EAGLE3+async crash: clear stale spec_token_ids for unscheduled requests | Fixes #36906. EAGLE3 speculative decoding with async scheduling crashes under high concurrency: `CUDA error: device-side assert triggered` in `F.embedding()`. **Root cause**: In |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
