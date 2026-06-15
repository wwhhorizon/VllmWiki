# vllm-project/vllm#22444: [Bug]: Low GPU Utilization with Image Payloads for Qwen2-VL-2B-Instruct Embeddings

| 字段 | 值 |
| --- | --- |
| Issue | [#22444](https://github.com/vllm-project/vllm/issues/22444) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Low GPU Utilization with Image Payloads for Qwen2-VL-2B-Instruct Embeddings

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When generating embeddings with the `Qwen/Qwen2-VL-2B-Instruct` model, there is a significant performance issue when payloads contain images. - **With text-only payloads**, GPU utilization is stable at ~95% and throughput is high. - **With image+text payloads**, GPU utilization becomes low and unstable (fluctuating between 0-50%), leading to a drastic drop in throughput. This strongly suggests a bottleneck in how vLLM processes or batches image data for this multimodal model. ### ✅ To Reproduce The issue can be reproduced by comparing the performance of two scenarios: one with image payloads (which is slow) and one with text-only payloads (which is fast). #### Scenario 1: Image + Text Payloads (Problematic) 1. **Start the vLLM server with the following command:** ```bash vllm serve Qwen/Qwen2-VL-2B-Instruct --task embed --trust-remote-code --dtype auto --port 8000 --tensor-parallel-size 1 --gpu-memory-utilization 0.9 --max-model-len 512 --max-num-batched-tokens 231077 --max-num-seqs 256 --limit_mm_per_prompt='{"image": 1, "video":0}' --disable-log-requests --chat-template template_dse_qwen2_vl.jinja ``` 2. **Run the following Pyt...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Low GPU Utilization with Image Payloads for Qwen2-VL-2B-Instruct Embeddings bug;stale ### Your current environment ### 🐛 Describe the bug When generating embeddings with the `Qwen/Qwen2-VL-2B-Instruct` model, the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Utilization with Image Payloads for Qwen2-VL-2B-Instruct Embeddings bug;stale ### Your current environment ### 🐛 Describe the bug When generating embeddings with the `Qwen/Qwen2-VL-2B-Instruct` model, there is a signifi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: payloads:** *(This is the same client as before)* ```python import base64 from io import BytesIO from typing import List import string import random import numpy as np import time from tqdm import tqdm from vllm.multimo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: - **With text-only payloads**, GPU utilization is stable at ~95% and throughput is high. - **With image+text payloads**, GPU utilization becomes low and unstable (fluctuating between 0-50%), leading to a drastic drop in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: LLM processes or batches image data for this multimodal model. ### ✅ To Reproduce The issue can be reproduced by comparing the performance of two scenarios: one with image payloads (which is slow) and one with text-only...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
