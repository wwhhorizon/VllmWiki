# vllm-project/vllm#28451: [Bug]: AMD Radeon pro W6800 + gpt-oss crash

| 字段 | 值 |
| --- | --- |
| Issue | [#28451](https://github.com/vllm-project/vllm/issues/28451) |
| 状态 | closed |
| 标签 | bug;feature request;rocm;gpt-oss |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;crash;import_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AMD Radeon pro W6800 + gpt-oss crash

### Issue 正文摘录

### Your current environment Environment: Docker compose container using image `rocm/vllm-dev:nightly` (as well as latest, and others - tried many) GPU: AMD Radeon Pro W6800 32GB VRam Details: Running `vllm serve openai/gpt-oss-20b` crashes, Added details of the crash in the bug description ### 🐛 Describe the bug Crash: ``` root@vllm-amd:/app# export VLLM_LOGGING_LEVEL=DEBUG root@vllm-amd:/app# vllm serve openai/gpt-oss-20b DEBUG 11-11 07:12:45 [plugins/__init__.py:32] No plugins for group vllm.platform_plugins found. DEBUG 11-11 07:12:45 [platforms/__init__.py:36] Checking if TPU platform is available. DEBUG 11-11 07:12:45 [platforms/__init__.py:55] TPU platform is not available because: No module named 'libtpu' DEBUG 11-11 07:12:45 [platforms/__init__.py:61] Checking if CUDA platform is available. DEBUG 11-11 07:12:45 [platforms/__init__.py:88] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBUG 11-11 07:12:45 [platforms/__init__.py:105] CUDA platform is not available because: NVML Shared Library Not Found DEBUG 11-11 07:12:45 [platforms/__init__.py:112] Checking if ROCm platform is available. DEBUG 11-11 07:12:45 [platforms/__init__.py:120] Confir...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ;feature request;rocm;gpt-oss ### Your current environment Environment: Docker compose container using image `rocm/vllm-dev:nightly` (as well as latest, and others - tried many) GPU: AMD Radeon Pro W6800 32GB VRam Detai...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: AMD Radeon pro W6800 + gpt-oss crash bug;feature request;rocm;gpt-oss ### Your current environment Environment: Docker compose container using image `rocm/vllm-dev:nightly` (as well as latest, and others - tried...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: AMD Radeon pro W6800 + gpt-oss crash bug;feature request;rocm;gpt-oss ### Your current environment Environment: Docker compose container using image `rocm/vllm-dev:nightly` (as well as latest, and others - tried...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: AMD Radeon pro W6800 + gpt-oss crash bug;feature request;rocm;gpt-oss ### Your current environment Environment: Docker compose container using image `rocm/vllm-dev:nightly` (as well as latest, and others - tried...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
