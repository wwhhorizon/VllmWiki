# vllm-project/vllm#19733: [Bug]: Fails to load llmcompressor GPTQ Qwen2.5-VL model

| 字段 | 值 |
| --- | --- |
| Issue | [#19733](https://github.com/vllm-project/vllm/issues/19733) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fails to load llmcompressor GPTQ Qwen2.5-VL model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM crashes on start when loading Qwen2.5-VL 7B compressed with llmcompressor using the example configuration. The example configuration was obtained here: [https://github.com/vllm-project/llm-compressor/blob/main/examples/multimodal_vision/qwen_2_5_vl_example.py](https://github.com/vllm-project/llm-compressor/blob/main/examples/multimodal_vision/qwen_2_5_vl_example.py). To avoid any library mismatch issue of any kind, I created 2 venv, one for the quantization and the other for inference (vLLM) (Python 3.10.12, Ubuntu 22.04.5 LTS) # Quantization process ```bash python3 -m venv venv source venv/bin/activate pip install llmcompressor==0.5.1 qwen_vl_utils torchvision python3 qwen_2_5_vl_example.py ``` I have uploaded the resulting model there: [https://huggingface.co/NM-dev/Qwen2.5-VL-7B-Instruct-W4A16-G128](https://huggingface.co/NM-dev/Qwen2.5-VL-7B-Instruct-W4A16-G128) if you want to try it yourself. # vLLM ## Installation ```bash python3 -m venv venv source venv/bin/activate pip install vllm==0.9.1 ``` ## Starting the online inference server Either specifying the quantization ```bash python3 -m vllm.entrypoints.openai.api_serv...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Fails to load llmcompressor GPTQ Qwen2.5-VL model bug ### Your current environment ### 🐛 Describe the bug vLLM crashes on start when loading Qwen2.5-VL 7B compressed with llmcompressor using the example configura...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: zation process ```bash python3 -m venv venv source venv/bin/activate pip install llmcompressor==0.5.1 qwen_vl_utils torchvision python3 qwen_2_5_vl_example.py ``` I have uploaded the resulting model there: [https://hugg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: mples/multimodal_vision/qwen_2_5_vl_example.py). To avoid any library mismatch issue of any kind, I created 2 venv, one for the quantization and the other for inference (vLLM) (Python 3.10.12, Ubuntu 22.04.5 LTS) # Quan...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: id any library mismatch issue of any kind, I created 2 venv, one for the quantization and the other for inference (vLLM) (Python 3.10.12, Ubuntu 22.04.5 LTS) # Quantization process ```bash python3 -m venv venv source ve...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;mismatch;nan_inf;slowdown dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
