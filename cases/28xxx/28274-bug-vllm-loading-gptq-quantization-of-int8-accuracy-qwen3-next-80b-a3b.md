# vllm-project/vllm#28274: [Bug]: Vllm loading gptq quantization of int8 accuracy Qwen3-Next-80b-A3B model error KeyError: 'layers.0.mlp.experts.w2_weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#28274](https://github.com/vllm-project/vllm/issues/28274) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;moe;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Vllm loading gptq quantization of int8 accuracy Qwen3-Next-80b-A3B model error KeyError: 'layers.0.mlp.experts.w2_weight'

### Issue 正文摘录

### Your current environment > accelerate 1.10.1 aiofiles 24.1.0 aiohappyeyeballs 2.6.1 aiohttp 3.12.15 aiosignal 1.4.0 airportsdata 20250811 annotated-types 0.7.0 antlr4-python3-runtime 4.9.3 anyio 4.10.0 astor 0.8.1 asttokens 3.0.0 async-timeout 5.0.1 attrs 25.3.0 audioread 3.0.1 autopep8 2.3.2 av 14.2.0 bitsandbytes 0.48.0.dev0 blake3 1.0.5 cachetools 6.1.0 cbor2 5.7.0 certifi 2025.8.3 cffi 1.17.1 charset-normalizer 3.4.3 click 8.2.1 cloudpickle 3.1.1 comm 0.2.3 compressed-tensors 0.11.0 contourpy 1.3.2 cupy-cuda12x 13.5.1 cut-cross-entropy 25.1.1 cycler 0.12.1 datasets 3.6.0 debugpy 1.8.17 decorator 5.2.1 deepspeed 0.16.4 Deprecated 1.2.18 depyf 0.19.0 Device-SMI 0.5.1 diffusers 0.35.1 dill 0.3.8 diskcache 5.6.3 distro 1.9.0 dnspython 2.7.0 docstring_parser 0.17.0 einops 0.8.1 email_validator 2.2.0 et_xmlfile 2.0.0 exceptiongroup 1.3.0 executing 2.2.1 fastapi 0.116.1 fastapi-cli 0.0.8 fastapi-cloud-cli 0.1.5 fastrlock 0.8.3 ffmpeg 1.4 ffmpy 0.6.1 filelock 3.18.0 fire 0.7.0 flash_attn 2.8.1 fonttools 4.59.0 frozendict 2.4.6 frozenlist 1.7.0 fsspec 2025.3.0 gekko 1.3.0 gguf 0.17.1 googleapis-common-protos 1.70.0 GPTQModel 5.0.0+cu128torch2.8 gradio 5.31.0 gradio_client 1.10.1 gr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: [Bug]: Vllm loading gptq quantization of int8 accuracy Qwen3-Next-80b-A3B model error KeyError: 'layers.0.mlp.experts.w2_weight' bug;stale ### Your current environment > accelerate 1.10.1 aiofiles 24.1.0 aioha
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 1.10.1 groovy 0.1.2 grpcio 1.74.0 h11 0.16.0 hf_transfer 0.1.9 hf-xet 1.1.7 hjson
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 0.11.0 contourpy 1.3.2 cupy-cuda12x 13.5.1 cut-cross-entropy 25.1.1 cycler 0.12.1 datasets 3.6.0 debugpy
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Vllm loading gptq quantization of int8 accuracy Qwen3-Next-80b-A3B model error KeyError: 'layers.0.mlp.experts.w2_weight' bug;stale ### Your current environment > accelerate 1.10.1 aiofiles 24.
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: Vllm loading gptq quantization of int8 accuracy Qwen3-Next-80b-A3B model error KeyError: 'layers.0.mlp.experts.w2_weight' bug;stale ### Your current environment > accelerate 1.10.1 aiofiles 24.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
