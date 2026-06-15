# vllm-project/vllm#27450: [Bug]: deepseek-ocr model running error when use VLLM_USE_MODELSCOPE is true

| 字段 | 值 |
| --- | --- |
| Issue | [#27450](https://github.com/vllm-project/vllm/issues/27450) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: deepseek-ocr model running error when use VLLM_USE_MODELSCOPE is true

### Issue 正文摘录

### Your current environment Because i from MODELSCOPE download model, but process from huggingface get file. ```text (EngineCore_DP0 pid=483687) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=483687) File "/root/code/vllm/vllm/multimodal/profiling.py", line 121, in get_dummy_processor_inputs (EngineCore_DP0 pid=483687) dummy_text = self.get_dummy_text(mm_counts) (EngineCore_DP0 pid=483687) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=483687) File "/root/code/vllm/vllm/model_executor/models/deepseek_ocr.py", line 233, in get_dummy_text (EngineCore_DP0 pid=483687) processor = self.info.get_hf_processor() (EngineCore_DP0 pid=483687) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=483687) File "/root/code/vllm/vllm/model_executor/models/deepseek_ocr.py", line 185, in get_hf_processor (EngineCore_DP0 pid=483687) return self.ctx.get_hf_processor(DeepseekOCRProcessor, **kwargs) (EngineCore_DP0 pid=483687) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=483687) File "/root/code/vllm/vllm/multimodal/processing.py", line 998, in get_hf_processor (EngineCore_DP0 pid=483687) return cached_processor_from_config( (EngineCore_DP0 pid=483687) ^^^^^^^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: deepseek-ocr model running error when use VLLM_USE_MODELSCOPE is true bug ### Your current environment Because i from MODELSCOPE download model, but process from huggingface get file. ```text (EngineCore_DP0 pid=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: cessor_config.json file ``` ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from vllm.model_executor.models.deepseek_ocr import NGramPerReqLogitsProcessor from PIL import Image import os os.environ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ^^^^ (EngineCore_DP0 pid=483687) File "/root/code/vllm/vllm/multimodal/profiling.py", line 121, in get_dummy_processor_inputs (EngineCore_DP0 pid=483687) dummy_text = self.get_dummy_text(mm_counts) (EngineCore_DP0 pid=4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: = LLM( model="deepseek-ai/DeepSeek-OCR", enable_prefix_caching=False, mm_processor_cache_gb=0, logits_processors=[NGramPerReqLogitsProcessor] ) # Prepare batched input with your image file image_1 = Image.open("target/l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
