# vllm-project/vllm#9100: [Bug]: Try-catch conditions are incorrect to import correct  ROCm Flash Attention Backend in Draft Model

| 字段 | 值 |
| --- | --- |
| Issue | [#9100](https://github.com/vllm-project/vllm/issues/9100) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 | import_error;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Try-catch conditions are incorrect to import correct  ROCm Flash Attention Backend in Draft Model

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I found an issue running draft model speculative decoding on AMD platform, the issue arised from `vllm/spec_decode/draft_model_runner.py` ``` try: from vllm.attention.backends.flash_attn import FlashAttentionMetadata # this is throwing ImportError rather than ModuleNotFoundError except ModuleNotFoundError: # vllm_flash_attn is not installed, use the identical ROCm FA metadata from vllm.attention.backends.rocm_flash_attn import ( ROCmFlashAttentionMetadata as FlashAttentionMetadata) ``` Within the try-catch block `ImportError` is thrown rather than `ModuleNotFoundError` ``` File "/home/aac/apps/rocm611-0929/vllm-fix-spec-amd/vllm/engine/multiprocessing/engine.py", line 78, in __init__ self.engine = LLMEngine(*args, File "/home/aac/apps/rocm611-0929/vllm-fix-spec-amd/vllm/engine/llm_engine.py", line 335, in __init__ self.model_executor = executor_class( File "/home/aac/apps/rocm611-0929/vllm-fix-spec-amd/vllm/executor/distributed_gpu_executor.py", line 26, in __init__ super().__init__(*args, **kwargs) File "/home/aac/apps/rocm611-0929/vllm-fix-spec-amd/vllm/executor/executor_base.py", line 47, in...

## 现有链接修复摘要

#9101 [Bugfix] Fix try-catch conditions to import correct Flash Attention Backend in Draft Model

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Try-catch conditions are incorrect to import correct ROCm Flash Attention Backend in Draft Model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I found an issue runnin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Try-catch conditions are incorrect to import correct ROCm Flash Attention Backend in Draft Model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I found an issue runnin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Try-catch conditions are incorrect to import correct ROCm Flash Attention Backend in Draft Model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I found an issue runnin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: `` try: from vllm.attention.backends.flash_attn import FlashAttentionMetadata # this is throwing ImportError rather than ModuleNotFoundError except ModuleNotFoundError: # vllm_flash_attn is not installed, use the identi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ditions are incorrect to import correct ROCm Flash Attention Backend in Draft Model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I found an issue running draft model specul...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9101](https://github.com/vllm-project/vllm/pull/9101) | closes_keyword | 0.95 | [Bugfix] Fix try-catch conditions to import correct Flash Attention Backend in Draft Model | FIX #9100 (*link existing issues this PR will resolve*) Updated the try-catch block to import correct flash attention backend in `vllm/spec_decode/draft_model_runner.py` when ru |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
