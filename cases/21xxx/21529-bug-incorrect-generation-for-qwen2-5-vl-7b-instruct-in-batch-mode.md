# vllm-project/vllm#21529: [Bug]: Incorrect Generation for Qwen2.5-VL-7B-Instruct in Batch Mode

| 字段 | 值 |
| --- | --- |
| Issue | [#21529](https://github.com/vllm-project/vllm/issues/21529) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect Generation for Qwen2.5-VL-7B-Instruct in Batch Mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There is a bug with the `Qwen/Qwen2.5-VL-7B-Instruct` model when running inference in batch mode with vLLM. I have created a minimal example that demonstrates the issue. When prompts are processed sequentially, the model's output is correct and as expected. However, when the exact same prompts are run as a batch, the generation for the longer prompt becomes completely different and faulty, often resulting in repetitive or nonsensical text. The generation for the shorter prompt in the same batch remains correct. The issue seems to be specific to batch processing of prompts with varying lengths. It is quite reproducible on my end, although it may occasionally require a second run to appear. **Minimal Reproducible Example** The following Python script, `vllm_qwen_2.5_bug.py`, first runs two prompts sequentially (which works) and then runs them in a batch (which fails for the longer prompt). ```python #!/usr/bin/env python3 # /// script # requires-python = ">=3.10" # dependencies = [ # "vllm==0.9.2", # ] # /// from vllm import LLM, SamplingParams llm = LLM(model="Qwen/Qwen2.5-VL-7B-Instruct") conversations = [ [ { "role": "user", "co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rter prompt in the same batch remains correct. The issue seems to be specific to batch processing of prompts with varying lengths. It is quite reproducible on my end, although it may occasionally require a second run to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Incorrect Generation for Qwen2.5-VL-7B-Instruct in Batch Mode bug;stale ### Your current environment ### 🐛 Describe the bug There is a bug with the `Qwen/Qwen2.5-VL-7B-Instruct` model when running inference in ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: A40 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: pecific to batch processing of prompts with varying lengths. It is quite reproducible on my end, although it may occasionally require a second run to appear. **Minimal Reproducible Example** The following Python script,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: _parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;mismatch;nan_inf;slowdown...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
