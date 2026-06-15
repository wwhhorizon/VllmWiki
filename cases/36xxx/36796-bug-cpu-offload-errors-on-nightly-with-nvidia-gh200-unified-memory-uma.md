# vllm-project/vllm#36796: [Bug]: CPU offload errors on nightly with NVIDIA GH200 Unified Memory (UMA)

| 字段 | 值 |
| --- | --- |
| Issue | [#36796](https://github.com/vllm-project/vllm/issues/36796) |
| 状态 | open |
| 标签 | bug;torch.compile |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU offload errors on nightly with NVIDIA GH200 Unified Memory (UMA)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Version: `nightly-76c6e6da08dbe73c2ee0d92dabe01786b44845d2` **Scenario 1:** Without `PYTORCH_ALLOC_CONF="expandable_segments:True"`, vLLM just OOMs, so it is required. ```bash PYTORCH_ALLOC_CONF="expandable_segments:True" VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY=1 VLLM_WEIGHT_OFFLOADING_DISABLE_UVA=1 python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --model zai-org/GLM-4.7-FP8 --tensor-parallel-size 1 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 32 --gpu-memory-utilization 0.75 --max-model-len 202752 --enable-auto-tool-choice --tool-call-parser glm47 --reasoning-parser glm45 --cpu-offload-gb 360 ``` ``` (EngineCore_DP0 pid=372) torch._dynamo.exc.Unsupported: Failed to trace builtin operator (EngineCore_DP0 pid=372) Explanation: Dynamo does not know how to trace builtin operator `setattr` with argument types ['OrderedDict', 'str', 'OrderedDict'] (has_kwargs False) (EngineCore_DP0 pid=372) Hint: Avoid calling builtin `setattr` with argument types ['OrderedDict', 'str', 'OrderedDict']. Consider using an equivalent alternat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: fload errors on nightly with NVIDIA GH200 Unified Memory (UMA) bug;torch.compile ### Your current environment ### 🐛 Describe the bug Version: `nightly-76c6e6da08dbe73c2ee0d92dabe01786b44845d2` **Scenario 1:** Without `P...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: i.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --model zai-org/GLM-4.7-FP8 --tensor-parallel-size 1 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-nu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: LM-4.7-FP8 --tensor-parallel-size 1 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 32 --gpu-memory-utilization 0.75 --max-model-len 202752 --enable-auto-tool-choice --tool-call-parse...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --download-dir /workspace/.cache/huggingface/hub --model zai-org/GLM-4.7-FP8 --tensor-parallel-size 1 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 32 --gpu-memory-utilization 0.75...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: with argument types ['OrderedDict', 'str', 'OrderedDict'] (has_kwargs False) (EngineCore_DP0 pid=372) Hint: Avoid calling builtin `setattr` with argument types ['OrderedDict', 'str', 'OrderedDict']. Consider using an eq...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
