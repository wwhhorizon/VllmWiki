# vllm-project/vllm#31625: [Feature][ROCm][AITER]: Speculative Decoding Accuracy Issue with VLLM_ATTENTION_BACKEND=ROCM_AITER_FA

| 字段 | 值 |
| --- | --- |
| Issue | [#31625](https://github.com/vllm-project/vllm/issues/31625) |
| 状态 | closed |
| 标签 | bug;feature request;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature][ROCm][AITER]: Speculative Decoding Accuracy Issue with VLLM_ATTENTION_BACKEND=ROCM_AITER_FA

### Issue 正文摘录

### Your current environment `rocm/vllm-dev:nightly` ### 🐛 Describe the bug ## Problem Description When running speculative decoding using `VLLM_ATTENTION_BACKEND=ROCM_AITER_FA`, the model produces extremely poor accuracy results on GSM8K benchmark. ### Command Used ```bash VLLM_USE_V1=1 \ VLLM_ROCM_USE_AITER=1 \ SAFETENSORS_FAST_GPU=1 \ VLLM_DISABLE_COMPILE_CACHE=1 \ VLLM_ATTENTION_BACKEND=ROCM_AITER_FA \ vllm serve meta-llama/Llama-3.3-70B-Instruct \ -tp 4 \ --speculative-config '{"model": "yuhuili/EAGLE3-LLaMA3.3-Instruct-70B", "num_speculative_tokens": 3, "method":"eagle3", "draft_tensor_parallel_size":1}' ``` ### Initial Benchmark Results |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.0478|± |0.0059| | | |strict-match | 5|exact_match|↑ |0.0334|± |0.0049| ## Approach Taken Upon investigation, we identified that CUDA graph support for `UNIFORM_BATCH` was needed to properly support `query_len > 1` for speculative decoding. The attention backend needs to handle decode, prefill, and extend tokens accordingly to enable speculative decoding for the ROC...

## 现有链接修复摘要

#32084 [ROCm][Bugfix] Fix AITER speculative decoding accuracy issue

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: USE_V1=1 \ VLLM_ROCM_USE_AITER=1 \ SAFETENSORS_FAST_GPU=1 \ VLLM_DISABLE_COMPILE_CACHE=1 \ VLLM_ATTENTION_BACKEND=ROCM_AITER_FA \ vllm serve meta-llama/Llama-3.3-70B-Instruct \ -tp 4 \ --speculative-config '{"model": "y...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Feature][ROCm][AITER]: Speculative Decoding Accuracy Issue with VLLM_ATTENTION_BACKEND=ROCM_AITER_FA bug;feature request;rocm ### Your current environment `rocm/vllm-dev:nightly` ### 🐛 Describe the bug ## Problem Descr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Feature][ROCm][AITER]: Speculative Decoding Accuracy Issue with VLLM_ATTENTION_BACKEND=ROCM_AITER_FA bug;feature request;rocm ### Your current environment `rocm/vllm-dev:nightly` ### 🐛 Describe the bug ## Problem Descr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g speculative decoding using `VLLM_ATTENTION_BACKEND=ROCM_AITER_FA`, the model produces extremely poor accuracy results on GSM8K benchmark. ### Command Used ```bash VLLM_USE_V1=1 \ VLLM_ROCM_USE_AITER=1 \ SAFETENSORS_FA...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Feature][ROCm][AITER]: Speculative Decoding Accuracy Issue with VLLM_ATTENTION_BACKEND=ROCM_AITER_FA bug;feature request;rocm ### Your current environment `rocm/vllm-dev:nightly` ### 🐛 Describe the bug ## Problem Descr...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32084](https://github.com/vllm-project/vllm/pull/32084) | closes_keyword | 0.95 | [ROCm][Bugfix] Fix AITER speculative decoding accuracy issue | Fixes #31625 🤖 Generated with [Claude Code](https://claude.ai/code) --- > [!NOTE] > Improves decode handling on ROCm AITER FA to correctly process speculative (multi-token) quer |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
