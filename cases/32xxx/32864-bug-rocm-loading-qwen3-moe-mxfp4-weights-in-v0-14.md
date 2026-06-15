# vllm-project/vllm#32864: [Bug] [ROCm]: Loading Qwen3-MoE-MXFP4 Weights in v0.14.

| 字段 | 值 |
| --- | --- |
| Issue | [#32864](https://github.com/vllm-project/vllm/issues/32864) |
| 状态 | open |
| 标签 | bug;rocm;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [ROCm]: Loading Qwen3-MoE-MXFP4 Weights in v0.14.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have quantized `Qwen/Qwen3-VL-235B-A22B-Instruct` to `mxfp4` using the following script ``` # # Copyright (C) 2023, Advanced Micro Devices, Inc. All rights reserved. # SPDX-License-Identifier: MIT # # from transformers import AutoModelForCausalLM, AutoTokenizer, AutoProcessor from transformers import Qwen3VLMoeForConditionalGeneration, AutoTokenizer, AutoProcessor from quark.torch import ModelQuantizer, export_safetensors from quark.torch.quantization import OCP_MXFP4Spec from quark.torch.quantization.config.config import QLayerConfig, QConfig # Load the original floating-point model # ckpt_path = "Qwen/Qwen3-30B-A3B-Instruct-2507" ckpt_path = "Qwen/Qwen3-VL-235B-A22B-Instruct" # model = AutoModelForCausalLM.from_pretrained(ckpt_path, device_map="auto", trust_remote_code=True) model = Qwen3VLMoeForConditionalGeneration.from_pretrained(ckpt_path, device_map="auto", trust_remote_code=True) model.eval() tokenizer = AutoTokenizer.from_pretrained(ckpt_path) tokenizer_processor = AutoProcessor.from_pretrained(ckpt_path) # Set the quantization configuration W_MXFP4_A_DYN_MXFP4_CONFIG = QLayerConfig( input_tensors=OCP_MXFP4Spec(ch_axis...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug] [ROCm]: Loading Qwen3-MoE-MXFP4 Weights in v0.14. bug;rocm;stale ### Your current environment ### 🐛 Describe the bug I have quantized `Qwen/Qwen3-VL-235B-A22B-Instruct` to `mxfp4` using the following script ``` #...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug] [ROCm]: Loading Qwen3-MoE-MXFP4 Weights in v0.14. bug;rocm;stale ### Your current environment ### 🐛 Describe the bug I have quantized `Qwen/Qwen3-VL-235B-A22B-Instruct` to `mxfp4` using the following script ``` #...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: l rights reserved. # SPDX-License-Identifier: MIT # # from transformers import AutoModelForCausalLM, AutoTokenizer, AutoProcessor from transformers import Qwen3VLMoeForConditionalGeneration, AutoTokenizer, AutoProcessor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: me/model/Qwen3-VL-235B-A22B-Instruct-MXFP4 VLLM_USE_V1=1 VLLM_ROCM_USE_AITER=1 \ VLLM_ROCM_SHUFFLE_KV_CACHE_LAYOUT=1 \ vllm serve $MODEL \ --tensor-parallel-size 8 \ --max-num-batched-tokens 32768 \ --disable-log-reques...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug] [ROCm]: Loading Qwen3-MoE-MXFP4 Weights in v0.14. bug;rocm;stale ### Your current environment ### 🐛 Describe the bug I have quantized `Qwen/Qwen3-VL-235B-A22B-Instruct` to `mxfp4` using the following script ``` # #

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
