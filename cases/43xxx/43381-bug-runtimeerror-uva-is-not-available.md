# vllm-project/vllm#43381: [Bug]: RuntimeError: UVA is not available

| 字段 | 值 |
| --- | --- |
| Issue | [#43381](https://github.com/vllm-project/vllm/issues/43381) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: UVA is not available

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug running ```bash vllm serve Qwen/Qwen3-0.6B --gpu-memory-utilization 0.8 ``` on wsl2, but got `RuntimeError: UVA is not available`, the detailed message is ``` WARNING 05-22 10:02:30 [config.py:70] Support for Transformers v4 is deprecated. The Transformers v4 codepath will become unmaintained in vLLM v0.22.0 and will be removed in vLLM v0.24.0. Please upgrade to Transformers v5: pip install --upgrade transformers WARNING 05-22 10:02:31 [interface.py:729] Using 'pin_memory=False' as WSL is detected. This may slow down the performance. (APIServer pid=17649) INFO 05-22 10:02:31 [utils.py:344] (APIServer pid=17649) INFO 05-22 10:02:31 [utils.py:344] █ █ █▄ ▄█ (APIServer pid=17649) INFO 05-22 10:02:31 [utils.py:344] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.20.2rc1.dev562+g1c78f76c2.d20260521 (APIServer pid=17649) INFO 05-22 10:02:31 [utils.py:344] █▄█▀ █ █ █ █ model /home/malone/.cache/huggingface/hub/models--Qwen--Qwen3-0.6B/snapshots/c1899de289a04d12100db370d81485cdf75e47ca/ (APIServer pid=17649) INFO 05-22 10:02:31 [utils.py:344] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=17649) INFO 05-22 10:02:31 [utils.py:344] (APIServer pid=17649) INFO 05-22 10:02:3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: will be removed in vLLM v0.24.0. Please upgrade to Transformers v5: pip install --upgrade transformers WARNING 05-22 10:02:31 [interface.py:729] Using 'pin_memory=False' as WSL is detected. This may slow down the perfor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: l_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=False, quantization=None, quantization_config=None, enforce_eager=False, enable_return_routed_experts=Fal...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rrent environment ### 🐛 Describe the bug running ```bash vllm serve Qwen/Qwen3-0.6B --gpu-memory-utilization 0.8 ``` on wsl2, but got `RuntimeError: UVA is not available`, the detailed message is ``` WARNING 05-22 10:02...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: --Qwen--Qwen3-0.6B/snapshots/c1899de289a04d12100db370d81485cdf75e47ca/', speculative_config=None, tokenizer='/home/malone/.cache/huggingface/hub/models--Qwen--Qwen3-0.6B/snapshots/c1899de289a04d12100db370d81485cdf75e47c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
