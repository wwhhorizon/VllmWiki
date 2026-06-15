# vllm-project/vllm#39872: [Bug]: [CI] Nightly Docker image CUDA `libcudart.so` mismatch regression (from `bcc2306`)

| 字段 | 值 |
| --- | --- |
| Issue | [#39872](https://github.com/vllm-project/vllm/issues/39872) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: [CI] Nightly Docker image CUDA `libcudart.so` mismatch regression (from `bcc2306`)

### Issue 正文摘录

Fixed by #39851 ### Your current environment ### 🐛 Describe the bug Works in `nightly-b075604da10a9e8ff23d23f63d5113d43f0e4208` and `cu130-nightly-b075604da10a9e8ff23d23f63d5113d43f0e4208`, but not `bcc2306cefa4179c548d3e638e7a22a88d281733`. vLLM is built for CUDA 13 when it is supposed to be built for CUDA 12, and vice versa. CUDA 12 `nightly-bcc2306cefa4179c548d3e638e7a22a88d281733` image: ``` (APIServer pid=1) INFO 04-15 06:22:41 [utils.py:299] (APIServer pid=1) INFO 04-15 06:22:41 [utils.py:299] █ █ █▄ ▄█ (APIServer pid=1) INFO 04-15 06:22:41 [utils.py:299] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.19.1rc1.dev296+gbcc2306ce (APIServer pid=1) INFO 04-15 06:22:41 [utils.py:299] █▄█▀ █ █ █ █ model zai-org/GLM-4.7-FP8 (APIServer pid=1) INFO 04-15 06:22:41 [utils.py:299] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=1) INFO 04-15 06:22:41 [utils.py:299] (APIServer pid=1) INFO 04-15 06:22:41 [utils.py:233] non-default args: {'api_server_count': 8, 'enable_auto_tool_choice': True, 'tool_call_parser': 'glm47', 'host': '0.0.0.0', 'port': 5000, 'model': 'zai-org/GLM-4.7-FP8', 'trust_remote_code': True, 'max_model_len': 202752, 'download_dir': '/workspace/.cache/huggingface/hub', 'reasoning_parser': 'glm45', 'gpu...

## 现有链接修复摘要

#39851 [CI][NIXL] Fix PD CI breakage: pin nixl-cu{12,13} versions

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: [CI] Nightly Docker image CUDA `libcudart.so` mismatch regression (from `bcc2306`) bug Fixed by #39851 ### Your current environment ### 🐛 Describe the bug Works in `nightly-b075604da10a9e8ff23d23f63d5113d43f0e420...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: er pid=1) INFO 04-15 06:22:41 [utils.py:299] █▄█▀ █ █ █ █ model zai-org/GLM-4.7-FP8 (APIServer pid=1) INFO 04-15 06:22:41 [utils.py:299] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=1) INFO 04-15 06:22:41 [utils.py:299] (APIServer...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 22:41 [utils.py:299] █▄█▀ █ █ █ █ model zai-org/GLM-4.7-FP8 (APIServer pid=1) INFO 04-15 06:22:41 [utils.py:299] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=1) INFO 04-15 06:22:41 [utils.py:299] (APIServer pid=1) INFO 04-15 06:22...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: [CI] Nightly Docker image CUDA `libcudart.so` mismatch regression (from `bcc2306`) bug Fixed by #39851 ### Your current environment ### 🐛 Describe the bug Works in `nightly-b075604da10a9e8ff23d23f63d5113d43f0e420...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 'gpu_memory_utilization': 0.925, 'enable_prefix_caching': True, 'offload_backend': 'uva', 'cpu_offload_gb': 384.0, 'max_num_batched_tokens': 8192, 'max_num_seqs': 32, 'enable_chunked_prefill': True} (APIServer pid=1) ER...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39851](https://github.com/vllm-project/vllm/pull/39851) | mentioned | 0.45 | [CI][NIXL] Fix PD CI breakage: pin nixl-cu{12,13} versions | age cuda `libcudart.so` mismatch regression (from `bcc2306`) fixed by #39851 ### your current environment <details> <summary>the output of <code>python collect_env.py</code></summ… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
