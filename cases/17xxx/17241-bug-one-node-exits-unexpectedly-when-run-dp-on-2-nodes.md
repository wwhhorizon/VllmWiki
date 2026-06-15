# vllm-project/vllm#17241: [Bug]: One node exits unexpectedly when run DP on 2 nodes.

| 字段 | 值 |
| --- | --- |
| Issue | [#17241](https://github.com/vllm-project/vllm/issues/17241) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: One node exits unexpectedly when run DP on 2 nodes.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run vllm/examples/offline_inference/data_parallel.py on 2 nodes, change the model to Qwen1.5-MoE-A2.7B. Follow the Multi-node Usage. I change the dtype to "float32" because V100 is not support for "bp16". Master-node ouput: ``` INFO 11-21 08:53:08 [__init__.py:239] Automatically detected platform cuda. [ ] DP rank 0 needs to process 200 prompts INFO 11-21 08:53:09 [config.py:2696] Upcasting torch.bfloat16 to torch.float32. INFO 11-21 08:53:16 [config.py:600] This model supports multiple tasks: {'score', 'embed', 'generate', 'reward', 'classify'}. Defaulting to 'generate'. WARNING 11-21 08:53:16 [arg_utils.py:1708] Compute Capability ] DP rank 1 needs to process 200 prompts INFO 04-27 11:16:03 [config.py:2696] Upcasting torch.bfloat16 to torch.float32. INFO 04-27 11:16:11 [config.py:600] This model supports multiple tasks: {'generate', 'reward', 'embed', 'classify', 'score'}. Defaulting to 'generate'. WARNING 04-27 11:16:11 [arg_utils.py:1708] Compute Capability < 8.0 is not supported by the V1 Engine. Falling back to V0. INFO 04-27 11:16:11 [config.py:1600] Defaulting to use mp for distributed inference WARNING 04-27 11:16:11 [cu...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ne (v0.8.3) with config: model='/home/share/bz/model/Qwen1.5-MoE-A2.7B', speculative_config=None, tokenizer='/home/share/bz/model/Qwen1.5-MoE-A2.7B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, overri...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: he model to Qwen1.5-MoE-A2.7B. Follow the Multi-node Usage. I change the dtype to "float32" because V100 is not support for "bp16". Master-node ouput: ``` INFO 11-21 08:53:08 [__init__.py:239] Automatically detected pla...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[],"max_capture_size":0}, use_cached_outputs=False, WARNING 04-27 11:16:11 [multiproc_worker_utils.py:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: `` INFO 11-21 08:53:08 [__init__.py:239] Automatically detected platform cuda. [ ] DP rank 0 needs to process 200 prompts INFO 11-21 08:53:09 [config.py:2696] Upcasting torch.bfloat16 to torch.float32. INFO 11-21 08:53:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: vllm/examples/offline_inference/data_parallel.py on 2 nodes, change the model to Qwen1.5-MoE-A2.7B. Follow the Multi-node Usage. I change the dtype to "float32" because V100 is not support for "bp16". Master-node ouput:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
