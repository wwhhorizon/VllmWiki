# vllm-project/vllm#43967: [Bug]: KeyError: 'layers.0.mlp.gate_up_proj.g_idx'  of  GLM-OCR GPTQ Int8 in v0.21.1rc1

| 字段 | 值 |
| --- | --- |
| Issue | [#43967](https://github.com/vllm-project/vllm/issues/43967) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'layers.0.mlp.gate_up_proj.g_idx'  of  GLM-OCR GPTQ Int8 in v0.21.1rc1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Description Failed to load glm-ocr gptq quantization model vllm version: 0.21.1rc1.dev281+gaa2b56ffb # serve cmd Run `vllm serve ./GLM-OCR-w8g128 --served-model-name glm-ocr --tensor-parallel-size 1 --trust-remote-code --port 8888` # Model information https://huggingface.co/xiongjingwu/GLM-OCR-GPTQ-w8g128/tree/main # The error message ```text (EngineCore pid=1202) ERROR 05-29 07:53:57 [core.py:1165] EngineCore failed to start. (EngineCore pid=1202) ERROR 05-29 07:53:57 [core.py:1165] Traceback (most recent call last): (EngineCore pid=1202) ERROR 05-29 07:53:57 [core.py:1165] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1139, in run_engine_core (EngineCore pid=1202) ERROR 05-29 07:53:57 [core.py:1165] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore pid=1202) ERROR 05-29 07:53:57 [core.py:1165] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=1202) ERROR 05-29 07:53:57 [core.py:1165] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=1202) ERROR 05-29 07:53:57 [core.py:1165] return func(*...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: Describe the bug # Description Failed to load glm-ocr gptq quantization model vllm version: 0.21.1rc1.dev281+gaa2b56ffb # serve cmd Run `vllm serve ./GLM-OCR-w8g128 --served-model-name glm-ocr --tensor-parallel-size 1 -...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: QMarlinConfig` is executed during weight loading, the `config.modules_in_block_to_quantize` member is not split, causing it to return `UnquantizedLinearMethod`. `UnquantizedLinearMethod` only contains the weight paramet...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: bug # Description Failed to load glm-ocr gptq quantization model vllm version: 0.21.1rc1.dev281+gaa2b56ffb # serve cmd Run `vllm serve ./GLM-OCR-w8g128 --served-model-name glm-ocr --tensor-parallel-size 1 --trust-remote...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nt ### 🐛 Describe the bug # Description Failed to load glm-ocr gptq quantization model vllm version: 0.21.1rc1.dev281+gaa2b56ffb # serve cmd Run `vllm serve ./GLM-OCR-w8g128 --served-model-name glm-ocr --tensor-parallel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
