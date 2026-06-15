# vllm-project/vllm#37672: [Bug]: Prefetch CPU offload OOMs; `VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY` must be implemented

| 字段 | 值 |
| --- | --- |
| Issue | [#37672](https://github.com/vllm-project/vllm/issues/37672) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefetch CPU offload OOMs; `VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY` must be implemented

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Environment: GH200 Command: `python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --model zai-org/GLM-4.7-FP8 --api-server-count 8 --tensor-parallel-size 1 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 32 --gpu-memory-utilization 0.75 --max-model-len 202752 --enable-auto-tool-choice --tool-call-parser glm47 --reasoning-parser glm45 --offload-backend prefetch --offload-group-size 1 --offload-num-in-group 1 --offload-prefetch-step 1` OOM (at 474 GiB, maximum of a GH200) occurs in GLM-4.7-FP8 (https://huggingface.co/zai-org/GLM-4.7-FP8, Model weight = 362 GB = 338 GiB) in the same way described in https://github.com/vllm-project/vllm/pull/32993. And looking at the code, there are no references of `VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY` present in `vllm/model_executor/offloader/prefetch.py` or `vllm/model_executor/offloader/prefetch_ops.py` CC @wzhao18 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation pa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --download-dir /workspace/.cache/huggingface/hub --model zai-org/GLM-4.7-FP8 --api-server-count 8 --tensor-parallel-size 1 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 32 --gpu-mem...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -tool-choice --tool-call-parser glm47 --reasoning-parser glm45 --offload-backend prefetch --offload-group-size 1 --offload-num-in-group 1 --offload-prefetch-step 1` OOM (at 474 GiB, maximum of a GH200) occurs in GLM-4.7...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 18 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: Prefetch CPU offload OOMs; `VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY` must be implemented bug ### Your current environment ### 🐛 Describe the bug Environment: GH200 Command: `python3 -m vllm.entrypoints.openai.a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
