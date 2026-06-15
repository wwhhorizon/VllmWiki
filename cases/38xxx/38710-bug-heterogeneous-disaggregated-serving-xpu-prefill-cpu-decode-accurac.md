# vllm-project/vllm#38710: [Bug]: heterogeneous disaggregated serving XPU (Prefill) + CPU (Decode) accuracy issue

| 字段 | 值 |
| --- | --- |
| Issue | [#38710](https://github.com/vllm-project/vllm/issues/38710) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: heterogeneous disaggregated serving XPU (Prefill) + CPU (Decode) accuracy issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I started one Prefill instance on XPU, and one Decode instance on Xeon CPU, with the toy proxy server handling these two instances. After sending a request to the proxy, the flow seems work, and the kv transfer is ok but the output seems incorrect. Steps to reproduce: * Prefill+proxy ```bash export VLLM_LOGGING_LEVEL=debug export HF_ENDPOINT=https://hf-mirror.com export UCX_TLS=tcp export model_name=Qwen/Qwen3-0.6B export tp_size=1 export ZE_AFFINITY_MASK=4 # PREFILL VLLM_USE_V1=1 \ VLLM_NIXL_SIDE_CHANNEL_HOST=0.0.0.0 \ VLLM_NIXL_SIDE_CHANNEL_PORT=5577 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ vllm serve $model_name \ -tp $tp_size \ --host 0.0.0.0 \ --port 8100 \ --seed 42 \ --enforce-eager \ --dtype float16 \ --gpu-memory-utilization 0.8 \ --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_device":"cpu","kv_connector_extra_config":{"enforce_handshake_compat": false},"enable_permute_local_kv":"True"}' \ --max-model-len 9216 \ --max_num_batched_tokens 2048 \ --block-size 64 \ --no-enable-prefix-caching \ & # PROXY python3 /workspace/vllm/tests/v1/kv_connector/nixl_i...

## 现有链接修复摘要

#38935 [PD][HeteroArch]Fix accuracy issue with CPU_ATTN as Decoder and Flash_ATTN as prefiller

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ndex":0, "message":{"role":"assistant", "content":"```\nfrom collections import defaultdict\n\ndef main():\n # Create a defaultdict with a specific key-value pair\n d = defaultdict(lambda: 0", "refusal":null,"annotation...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: produce: * Prefill+proxy ```bash export VLLM_LOGGING_LEVEL=debug export HF_ENDPOINT=https://hf-mirror.com export UCX_TLS=tcp export model_name=Qwen/Qwen3-0.6B export tp_size=1 export ZE_AFFINITY_MASK=4 # PREFILL VLLM_US...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: heterogeneous disaggregated serving XPU (Prefill) + CPU (Decode) accuracy issue bug ### Your current environment ### 🐛 Describe the bug I started one Prefill instance on XPU, and one Decode instance on Xeon CPU,...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: [Bug]: heterogeneous disaggregated serving XPU (Prefill) + CPU (Decode) accuracy issue bug ### Your current environment ### 🐛 Describe the bug I started one Prefill instance on XPU, and one Decode instance on Xeon CPU,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: kv_transfer_params":null ``` The answer for hetero disaggregated case mismatch with the aggregated one, and incorrect. Any thoughts are welcome! ### Before submitting a new issue... - [x] Make sure you already searched...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38935](https://github.com/vllm-project/vllm/pull/38935) | closes_keyword | 0.95 | [PD][HeteroArch]Fix accuracy issue with CPU_ATTN as Decoder and Flash_ATTN as prefiller | Fix the error reported in #38710 When using CPU as decoder to work with Hetero Arch Platform (CUDA, Intel GPU, Intel Gaudi ...) as prefiller, there is an accuracy issue due to |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
