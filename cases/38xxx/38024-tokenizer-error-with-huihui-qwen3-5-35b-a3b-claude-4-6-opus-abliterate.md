# vllm-project/vllm#38024: Tokenizer error with Huihui-Qwen3.5-35B-A3B-Claude-4.6-Opus-abliterated model - TokenizersBackend not found

| 字段 | 值 |
| --- | --- |
| Issue | [#38024](https://github.com/vllm-project/vllm/issues/38024) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Tokenizer error with Huihui-Qwen3.5-35B-A3B-Claude-4.6-Opus-abliterated model - TokenizersBackend not found

### Issue 正文摘录

## Issue Description When trying to run the model **Huihui-Qwen3.5-35B-A3B-Claude-4.6-Opus-abliterated** with vLLM, I encounter a tokenizer error. ## Model Information - **Model Name**: Huihui-Qwen3.5-35B-A3B-Claude-4.6-Opus-abliterated - **Model Architecture**: Qwen3_5MoeForConditionalGeneration (MoE) - **Parameters**: 35B total, 256 experts, 8 experts per token - **Quantization**: AWQ 4-bit - **Location**: /data/models/Huihui-Qwen3.5-35B-A3B-Claude-4.6-Opus-abliterated ## Error Message ``` ValueError: Tokenizer class TokenizersBackend does not exist or is not currently imported. ``` ## Environment - **vLLM Version**: 0.17.1 and nightly - **CUDA**: Available - **GPU**: 4x GPUs (tensor-parallel-size=4) - **Python**: 3.x ## Command Used ```bash sudo docker run -d --name vllm-huihui-qwen35-claude \ --runtime=nvidia \ -e CUDA_VISIBLE_DEVICES=4,5,6,7 \ -v /data:/data \ -p 8002:8000 \ --ipc=host \ vllm/vllm-openai:v0.17.1 \ python3 -m vllm.entrypoints.openai.api_server \ --model /data/models/Huihui-Qwen3.5-35B-A3B-Claude-4.6-Opus-abliterated \ --tensor-parallel-size 4 \ --max-model-len 100000 \ --gpu-memory-utilization 0.85 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_xml \ -...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: or: Tokenizer class TokenizersBackend does not exist or is not currently imported. ``` ## Environment - **vLLM Version**: 0.17.1 and nightly - **CUDA**: Available - **GPU**: 4x GPUs (tensor-parallel-size=4) - **Python**...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: (MoE) - **Parameters**: 35B total, 256 experts, 8 experts per token - **Quantization**: AWQ 4-bit - **Location**: /data/models/Huihui-Qwen3.5-35B-A3B-Claude-4.6-Opus-abliterated ## Error Message ``` ValueError: Tokenize...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Tokenizer error with Huihui-Qwen3.5-35B-A3B-Claude-4.6-Opus-abliterated model - TokenizersBackend not found ## Issue Description When trying to run the model **Huihui-Qwen3.5-35B-A3B-Claude-4.6-Opus-abliterated** with v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: del Name**: Huihui-Qwen3.5-35B-A3B-Claude-4.6-Opus-abliterated - **Model Architecture**: Qwen3_5MoeForConditionalGeneration (MoE) - **Parameters**: 35B total, 256 experts, 8 experts per token - **Quantization**: AWQ 4-b...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: 3.5-35B-A3B-Claude-4.6-Opus-abliterated - **Model Architecture**: Qwen3_5MoeForConditionalGeneration (MoE) - **Parameters**: 35B total, 256 experts, 8 experts per token - **Quantization**: AWQ 4-bit - **Location**: /dat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
