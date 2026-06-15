# vllm-project/vllm#42593: [Bug]: --enable-return-routed-experts crashes with AttributeError on non-MoE models after full model load (missing architecture compatibility check)

| 字段 | 值 |
| --- | --- |
| Issue | [#42593](https://github.com/vllm-project/vllm/issues/42593) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --enable-return-routed-experts crashes with AttributeError on non-MoE models after full model load (missing architecture compatibility check)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving a dense (non-MoE) model such as `Meta-Llama-3.1-8B-Instruct` with `--enable-return-routed-experts`, the CLI and config validation both accept the flag without complaint, but the server crashes deep into KV cache initialization with an `AttributeError` because `LlamaConfig` has no `num_experts_per_tok` attribute. This is a missing validation bug: `--enable-return-routed-experts` is a MoE-only feature, but there is no early check to verify that the loaded model architecture actually has routed experts before attempting to initialize the `RoutedExpertsCapturer`. The crash occurs after the full model has been loaded (~15 GiB, ~4 seconds) and torch.compile has completed, wasting significant GPU resources before failing with an unhelpful internal error. Note: `--enable-expert-parallel` (`-ep`) has an equivalent check in pydantic that correctly rejects non-MoE models at config time with a clear message. `--enable-return-routed-experts` has no such guard. ## Steps to Reproduce ```bash vllm serve \ --host 127.0.0.1 \ --port 19354 \ --enable-return-routed-experts ``` ``` (vllm) root@lizhiyuan-ubuntu-01:~# /root/anaconda3/envs/...

## 现有链接修复摘要

#42858 [Bugfix] Validate --enable-return-routed-experts requires a MoE model (fixes #42593) | #42867 config: reject --enable-return-routed-experts for non-MoE models at startup

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: urs after the full model has been loaded (~15 GiB, ~4 seconds) and torch.compile has completed, wasting significant GPU resources before failing with an unhelpful internal error. Note: `--enable-expert-parallel` (`-ep`)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ]: --enable-return-routed-experts crashes with AttributeError on non-MoE models after full model load (missing architecture compatibility check) bug ### Your current environment ### 🐛 Describe the bug When serving a den...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: --enable-return-routed-experts crashes with AttributeError on non-MoE models after full model load (missing architecture compatibility check) bug ### Your current environment ### 🐛 Describe the bug When serving a...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42858](https://github.com/vllm-project/vllm/pull/42858) | closes_keyword | 0.95 | [Bugfix] Validate --enable-return-routed-experts requires a MoE model (fixes #42593) | Closes #42593. |
| [#42867](https://github.com/vllm-project/vllm/pull/42867) | closes_keyword | 0.95 | config: reject --enable-return-routed-experts for non-MoE models at startup | Fixes #42593 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
