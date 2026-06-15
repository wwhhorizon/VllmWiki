# vllm-project/vllm#30969: [Bug]: SmolLM3-3B FP8 Fails to Load [`compressed-tensors` and `transformers-impl` compatibility issue]

| 字段 | 值 |
| --- | --- |
| Issue | [#30969](https://github.com/vllm-project/vllm/issues/30969) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: SmolLM3-3B FP8 Fails to Load [`compressed-tensors` and `transformers-impl` compatibility issue]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM v0.11.1 fails to load SmolLM3-3B FP8 quantized models with llm-compressor using compressed-tensors. Same models work on v0.11.0. Tested with: - [huggingface.co/RedHatAI/SmolLM3-3B-FP8-dynamic](https://huggingface.co/RedHatAI/SmolLM3-3B-FP8-dynamic) - Manually quantized fine tuned [SmolLM3-3B](https://huggingface.co/HuggingFaceTB/SmolLM3-3B) using llmcompressor==0.7 (compressed-tensors==0.12.2) in FP8-dynamic - Manually quantized fine tuned [SmolLM3-3B(https://huggingface.co/HuggingFaceTB/SmolLM3-3B) using llmcompressor==0.8.1 (compressed-tensors==0.12.2) in FP8-dynamic All fail on v0.11.1. All work on v0.11.0. Error occurs during model loading in find_matched_target function. The error is: "Unable to find matching target for model.layers.0.self_attn.q_proj in the compressed-tensors config" Complete error ``` + exec python3 -m vllm.entrypoints.openai.api_server --model RedHatAI/SmolLM3-3B-FP8-dynamic --port 8000 --trust-remote-code --max-model-len 5000 [APIServer pid=1] INFO 12-12 05:05:29 [api_server.py:1772] vLLM API server version 0.11.1 [APIServer pid=1] INFO 12-12 05:05:29 [utils.py:253] non-default args: {'model': 'RedH...

## 现有链接修复摘要

#26501 [CI/Build] upgrade compressed-tensors to 0.12.2 to address LGPLv3

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: PIServer pid=1] INFO 12-12 05:05:29 [api_server.py:1772] vLLM API server version 0.11.1 [APIServer pid=1] INFO 12-12 05:05:29 [utils.py:253] non-default args: {'model': 'RedHatAI/SmolLM3-3B-FP8-dynamic', 'trust_remote_c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: SmolLM3-3B FP8 Fails to Load [`compressed-tensors` and `transformers-impl` compatibility issue] bug;help wanted;good first issue ### Your current environment ### 🐛 Describe the bug vLLM v0.11.1 fails to load Smol...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: SmolLM3-3B FP8 Fails to Load [`compressed-tensors` and `transformers-impl` compatibility issue] bug;help wanted;good first issue ### Your current environment ### 🐛 Describe the bug vLLM v0.11.1 fails to load Smol...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 🐛 Describe the bug vLLM v0.11.1 fails to load SmolLM3-3B FP8 quantized models with llm-compressor using compressed-tensors. Same models work on v0.11.0. Tested with: - [huggingface.co/RedHatAI/SmolLM3-3B-FP8-dynamic](ht...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: (s): {} ``` This is a dense transformer model (SmolLM3ForCausalLM), not MoE. Docker command to reproduce: `docker run --runtime nvidia --gpus all -p 8000:8000 vllm/vllm-openai:v0.11.1 --model RedHatAI/SmolLM3-3B-FP8-dyn...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26501](https://github.com/vllm-project/vllm/pull/26501) | mentioned | 0.45 | [CI/Build] upgrade compressed-tensors to 0.12.2 to address LGPLv3 | namic --trust-remote-code --max-model-len 5000` suspected cause: [pr #26501 upgraded compressed-tensors from 0.11.0 to 0.12.2.](https://github.com/vllm-project/vllm/pull/26501) th… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
